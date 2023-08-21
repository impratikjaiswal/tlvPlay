from python_helpers.ph_util import PhUtil

from tlv_play.main.convert import converter
from tlv_play.main.helper.metadata import MetaData
from tlv_play.main.tlv.tlv_handler import TlvHandler
from tlv_play.main.tlv.tlv_parser import TlvParser


def parse_or_update_any_data(data, meta_data=None):
    """

    :param meta_data:
    :param data:
    :return:
    """
    converter.set_defaults_for_printing(data)
    if meta_data is None:
        meta_data = MetaData(raw_data_org=data.raw_data)
    data.set_auto_generated_remarks_if_needed()
    PhUtil.print_heading(data.get_remarks_as_str(), heading_level=2)
    converter.set_defaults(data, meta_data)
    tlv_obj = TlvHandler(data.raw_data).process_data()
    meta_data.parsed_data = TlvParser(tlv_obj).get_printable_tlv(data.length_in_decimal, data.value_in_ascii,
                                                                 data.one_liner)
    converter.print_data(data, meta_data)
