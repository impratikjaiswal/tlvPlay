from src.main.data_type.data_type_master import DataTypeMaster
from src.main.helper.tlv_data import TlvData


class UserData(DataTypeMaster):

    def set_one_liner(self):
        one_liner = None
        super().set_one_liner(one_liner)

    def set_value_in_ascii(self):
        value_in_ascii = None
        super().set_value_in_ascii(value_in_ascii)

    def set_length_in_decimal(self):
        length_in_decimal = None
        super().set_length_in_decimal(length_in_decimal)

    def set_remarks_list(self):
        remarks_list = None
        super().set_remarks_list(remarks_list)

    def set_data_pool(self):
        data_pool = [
            #
            TlvData(
                remarks_list='Simple TLV',
                raw_data='86020102',
            ),
        ]
        super().set_data_pool(data_pool)
