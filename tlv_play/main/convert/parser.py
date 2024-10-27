from python_helpers.ph_constants import PhConstants
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_util import PhUtil

from tlv_play.main.convert import converter
from tlv_play.main.helper.metadata import MetaData
from tlv_play.main.tlv.tlv_handler import TlvHandler
from tlv_play.main.tlv.tlv_parser import TlvParser


def process_all_data_types(data, meta_data=None, info_data=None):
    """

    :param meta_data:
    :param data:
    :return:
    """
    """
    Individual
    """
    converter.set_defaults_for_printing(data)
    if meta_data is None:
        meta_data = MetaData(input_data_org=data.input_data)
    data.set_auto_generated_remarks_if_needed()
    PhUtil.print_heading(data.get_remarks_as_str(), heading_level=2)
    converter.set_defaults(data, meta_data)
    if not data.input_data:
        raise ValueError(PhExceptionHelper(msg_key=PhConstants.MISSING_INPUT_DATA))
    tlv_handler_result = TlvHandler(input_data=data.input_data, non_tlv_neighbor=data.non_tlv_neighbor,
                                    info_data=info_data).process_data()
    meta_data.parsed_data = TlvParser(tlv_handler_result=tlv_handler_result).get_printable_tlv(data.length_in_decimal,
                                                                                               data.value_in_ascii,
                                                                                               data.one_liner)
    converter.print_data(data=data, meta_data=meta_data, info_data=info_data)
