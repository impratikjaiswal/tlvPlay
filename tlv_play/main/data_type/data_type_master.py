from tlv_play.main.convert.parser import parse_or_update_any_data_safe
from tlv_play.main.helper.tlv_data import TlvData


class DataTypeMaster(object):
    def __init__(self):
        self.one_liner = None
        self.value_in_ascii = None
        self.length_in_decimal = None
        self.remarks_list = None
        self.data_pool = []

    def set_one_liner(self, one_liner):
        self.one_liner = one_liner

    def set_value_in_ascii(self, value_in_ascii):
        self.value_in_ascii = value_in_ascii

    def set_length_in_decimal(self, length_in_decimal):
        self.length_in_decimal = length_in_decimal

    def set_remarks_list(self, remarks_list):
        self.remarks_list = remarks_list

    def set_data_pool(self, data_pool):
        self.data_pool = data_pool

    def parse(self, error_handling_mode):
        """

        :param error_handling_mode:
        :return:
        """
        for data in self.data_pool:
            if isinstance(data, TlvData):
                data.length_in_decimal = data.length_in_decimal if data.length_in_decimal is not None else self.length_in_decimal
                data.value_in_ascii = data.value_in_ascii if data.value_in_ascii is not None else self.value_in_ascii
                data.one_liner = data.one_liner if data.one_liner is not None else self.one_liner
                data.remarks_list = data.remarks_list if data.remarks_list is not None else self.remarks_list
            else:
                data = TlvData(
                    raw_data=data,
                    length_in_decimal=self.length_in_decimal,
                    value_in_ascii=self.value_in_ascii,
                    one_liner=self.one_liner,
                    remarks_list=self.remarks_list,
                )
            parse_or_update_any_data_safe(data, error_handling_mode)
