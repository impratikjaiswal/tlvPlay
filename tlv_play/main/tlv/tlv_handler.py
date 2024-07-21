import binascii
from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from tlv_play.main.tlv.tlv import Tlv

# if b5 b4 b3 b2 b1 are set, then see subsequent bytes
tag_mask_first_byte_subsequent_bytes = 0x1F
# if b8 is set, Another byte follows
tag_mask_subsequent_bytes = 0x80
len_mask_additional_bytes = 0x0F
invalid_tags_list = [[0x00]]


class TlvHandler:
    def __init__(self, input_data, non_tlv_neighbor):
        self.input_data_list = []
        self.non_tlv_neighbor = non_tlv_neighbor
        if isinstance(input_data, str):
            input_data = PhUtil.trim_and_kill_all_white_spaces(input_data)
            input_data = PhUtil.decode_to_hex_if_base64(input_data)
            input_data = binascii.unhexlify(input_data)
            self.input_data_list = list(input_data)

    def __process_tlv(self, data_list, level, initial_offset):
        """

        :return:
        """
        offset = initial_offset
        """
        TAG: coded on one or two bytes
        """
        data_len = len(data_list)
        if data_len < 2:
            return None, -1  # Minimum Tag Len is needed
        # Debug
        # print(
        #     f'level: {level}; initial_offset: {initial_offset}; data_list: {PhUtil.to_hex_string(data_list, PhConstants.FORMAT_HEX_STRING_AS_PACK)}')
        tag_list = [data_list[offset]]
        if tag_list[0] & tag_mask_first_byte_subsequent_bytes == tag_mask_first_byte_subsequent_bytes:
            offset += 1
            tag_list.append(data_list[offset])
            while data_list[offset] & tag_mask_subsequent_bytes == tag_mask_subsequent_bytes:
                offset += 1
                if offset >= data_len:
                    return None, -1  # Tag is not available
                tag_list.append(data_list[offset])
        # check for invalid Tags
        for invalid_tag in invalid_tags_list:
            if invalid_tag == tag_list:
                return None, -1  # Invalid Tag Found
        """
        LEN: consists of one or more consecutive bytes
        """
        offset += 1
        len_offset = 0
        if data_len <= offset:
            return None, -1  # Len is not available
        len_list = [data_list[offset]]
        if data_list[offset] & tag_mask_subsequent_bytes == tag_mask_subsequent_bytes:
            len_additional_bytes = data_list[offset] & len_mask_additional_bytes
            if data_len <= offset + len_mask_additional_bytes:
                return None, -1  # Mentioned Len is not available
            if len_additional_bytes == 0:
                return None, -1  # Not Multi Length, e.g.: F0
            while len_offset < len_additional_bytes:
                offset += 1
                len_offset += 1
                len_list.append(data_list[offset])
            len_offset = 0
            len_dec = PhUtil.hex_str_to_dec(
                PhUtil.to_hex_string(len_list[len_offset + 1: len_offset + 1 + len_additional_bytes],
                                     PhConstants.FORMAT_HEX_STRING_AS_PACK))
        else:
            len_dec = len_list[len_offset]
        """
        Value
        """
        offset += 1
        if data_len < offset + len_dec:
            return None, -1  # Value is not available
        value_list = data_list[offset:offset + len_dec]
        offset += len_dec
        return Tlv(tag_list, len_list, value_list, len_dec, level), offset

    def process_data(self, input_data_list=None, level=0, non_tlv_neighbor=None):
        if input_data_list is None:
            input_data_list = self.input_data_list
        if non_tlv_neighbor is None:
            non_tlv_neighbor = self.non_tlv_neighbor
        offset = 0
        tlv_data = []
        non_tlv_data = []
        sub_tlv_obj_temp = []
        while offset < len(input_data_list):
            tlv_obj, temp_offset = self.__process_tlv(input_data_list, level, offset)
            if tlv_obj is None:
                break
            offset = temp_offset
            if len(tlv_obj.value_list) > 2:  # Possible nested TLV, parse it & store result in temp list
                sub_tlv_data_temp = (self.process_data(tlv_obj.value_list, level=level + 1, non_tlv_neighbor=False)
                                     .get(PhKeys.RESULT_PROCESSED, None))
                # Always returned a list
                if isinstance(sub_tlv_data_temp[0], Tlv):  # Nested TLV Suspected, & Found
                    tlv_obj.value_list = sub_tlv_data_temp.copy()
                    sub_tlv_obj_temp.append(tlv_obj)
                else:
                    sub_tlv_obj_temp.append(tlv_obj)  # Nested TLV Suspected, but Not Found
            else:  # No Nested TLV
                # TODO: ESIM-1475: Actually this should be concat_tlv_obj_temp, For Concatenated TLV Handling
                sub_tlv_obj_temp.append(tlv_obj)
        count_sub_tlv_obj_temp = len(sub_tlv_obj_temp)
        # Check if at least one TLV is found
        if count_sub_tlv_obj_temp > 0:
            # Check if neighbourhood is perfect or not
            neighbour_tantrum = True if tlv_obj is None else False
            if neighbour_tantrum:
                # non TLV data
                non_tlv_data = input_data_list[offset:]
                if non_tlv_neighbor is False:
                    # no need to handle non_tlv_neighbor
                    return {PhKeys.RESULT_PROCESSED: input_data_list}
                tlv_obj = sub_tlv_obj_temp[-1]
            for item in sub_tlv_obj_temp:
                if isinstance(item, list):
                    tlv_obj.value_list = item
                else:  # instance of tlv
                    if item.level == tlv_obj.level:
                        # print('Same Level')
                        tlv_data.append(item)
                    else:
                        # print('Parent')
                        tlv_obj.value_list = item
                        tlv_data.append(tlv_obj)
            result = {PhKeys.RESULT_PROCESSED: tlv_data}
            if non_tlv_data:
                result.update({PhKeys.RESULT_UNPROCESSED: non_tlv_data})
            return result
        else:
            # No TLV Found
            return {PhKeys.RESULT_PROCESSED: input_data_list}
