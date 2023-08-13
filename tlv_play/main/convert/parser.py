import traceback

from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_util import PhUtil

from tlv_play.main.convert import converter
from tlv_play.main.tlv.tlv_handler import TlvHandler
from tlv_play.main.tlv.tlv_parser import TlvParser


def parse_or_update_any_data_safe(data, error_handling_mode):
    try:
        parse_or_update_any_data(data)
    except Exception as e:
        print(f'Exception Occurred {e}')
        traceback.print_exc()
        if error_handling_mode == PhErrorHandlingModes.STOP_ON_ERROR:
            raise


def parse_or_update_any_data(data):
    """

    :param data:
    :return:
    """
    converter.set_defaults(data)
    PhUtil.print_heading(data.get_remarks_as_str(), heading_level=3)
    tlv_obj = TlvHandler(data.raw_data).process_data()
    TlvParser(tlv_obj).print_tlv(data.length_in_decimal, data.value_in_ascii, data.one_liner)
