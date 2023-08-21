from python_helpers.ph_constants import PhConstants
from python_helpers.ph_util import PhUtil

from tlv_play.main.tlv.tlv import Tlv
from tlv_play.main.tlv.tlv_print import TlvPrint


class TlvParser:
    def __init__(self, tlv_objs):
        self.tlv_obj = tlv_objs

    def get_printable_tlv(self, length_in_decimal=None, value_in_ascii=None, one_liner=None, print_also=False):
        result = self.parse_tlv(length_in_decimal=length_in_decimal, value_in_ascii=value_in_ascii, one_liner=one_liner)
        if print_also:
            print(result)
        return result

    def parse_tlv(self, tlv_obj=None, level=0, length_in_decimal=None, value_in_ascii=None, one_liner=None):
        if tlv_obj is None:
            tlv_obj = self.tlv_obj
        parsed_data = ''
        if isinstance(tlv_obj, list):  # List of Multiple Objects
            if isinstance(tlv_obj[0], Tlv):
                for tlv in tlv_obj:
                    parsed_data_temp = self._parse_tlv(tlv, level=level, length_in_decimal=length_in_decimal,
                                                       value_in_ascii=value_in_ascii,
                                                       one_liner=one_liner)
                    parsed_data = TlvPrint.SEP_CONCAT_TLVS.join(filter(None, [parsed_data, parsed_data_temp]))
                return parsed_data
            if isinstance(tlv_obj[0], int):
                return PhUtil.to_hex_string(tlv_obj, PhConstants.FORMAT_HEX_STRING_AS_PACK)
        else:  # Single Object
            return self._parse_tlv(tlv_obj, level=level, length_in_decimal=length_in_decimal,
                                   value_in_ascii=value_in_ascii, one_liner=one_liner)

    def _parse_tlv(self, tlv, level, length_in_decimal, value_in_ascii, one_liner):
        if isinstance(tlv, list):
            return self.parse_tlv(tlv, level=level + 1, length_in_decimal=length_in_decimal,
                                  value_in_ascii=value_in_ascii, one_liner=one_liner)
        if not isinstance(tlv, Tlv):
            return ''
        tlv_print = TlvPrint(tlv, level, length_in_decimal, value_in_ascii, one_liner)
        if len(tlv.value_list) > 0 and isinstance(tlv.value_list[0], Tlv):  # Single or Multiple SUB TLV
            parsed_data = f'{tlv_print.get_tl_as_str()}'
            for item in tlv.value_list:
                parsed_data = TlvPrint.SEP_SUB_TLVS.join(
                    filter(None, [parsed_data, self.parse_tlv(item, level=level + 1,
                                                              length_in_decimal=length_in_decimal,
                                                              value_in_ascii=value_in_ascii,
                                                              one_liner=one_liner)]))
            return parsed_data
        else:
            return tlv_print.get_tlv_as_str()
