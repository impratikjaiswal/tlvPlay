import copy

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_exception_helper import PhExceptionHelper

from tlv_play.main.tlv.tlv_handler import TlvHandler
from tlv_play.main.tlv.tlv_parser import TlvParser


def handle_tlv(input_data, length_in_decimal, value_in_ascii, one_liner, non_tlv_neighbor, info_data):
    """

    :param input_data:
    :param length_in_decimal:
    :param value_in_ascii:
    :param one_liner:
    :param non_tlv_neighbor:
    :param info_data:
    :return:
    """
    tlv_handler_result = TlvHandler(input_data=input_data, non_tlv_neighbor=non_tlv_neighbor,
                                    info_data=info_data).process_data()
    output_data = TlvParser(tlv_handler_result=tlv_handler_result).get_printable_tlv(length_in_decimal, value_in_ascii,
                                                                                     one_liner)
    return output_data


def process_data(data, meta_data, info_data, flip_output=False):
    """

    :param data:
    :param meta_data:
    :param info_data:
    :param flip_output:
    :return:
    """
    input_data = data.input_data
    # input_File_path = meta_data.input_data_org if meta_data.input_mode_key == PhKeys.INPUT_FILE else None
    # input_format = data.input_format
    # output_format = data.output_format
    # if flip_output is True:
    #     input_data = meta_data.parsed_data
    #     input_format = data.output_format
    #     output_format = data.input_format
    # parse_only = True
    # asn1_element = data.asn1_element
    if not data.input_data:
        raise ValueError(PhExceptionHelper(msg_key=PhConstants.MISSING_INPUT_DATA))
    res = handle_tlv(input_data=input_data, length_in_decimal=data.length_in_decimal,
                      value_in_ascii=data.value_in_ascii, one_liner=data.one_liner,
                      non_tlv_neighbor=data.non_tlv_neighbor, info_data=info_data)
    if flip_output is True:
        meta_data.re_parsed_data = res
    else:
        meta_data.parsed_data = res
