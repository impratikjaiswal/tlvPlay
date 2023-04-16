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
            #
            TlvData(
                remarks_list='Test TLV',
                raw_data="""
                9F4005FF80F0F001
91102263BCC1C2D9C4420013
9F0206000000012345
9F0306000000004000
9F26088E19ED4BCA5C670A
82025C00
5F340102
9F3602000A
9F0702FF00
9F080208C1
9F09021001
8A025931
9F3403A40002
9F270180
9F1E0853455249414C3132
9F0D05F040008800
9F0E05FCF8FCF8F0
9F0F05FCF8FCF8F0
5F28020840
9F390100
9F1A020840
9F350122
95050000048000
5F2A020840
9B024800
9F2103123456
9C0100
9F370400BC614E
4F07A0000000031010
9F0607A0000000031010
9F7C0412345678
8407A0000000031010
9F1006010A03600000
9F5B052000000000
9F4104000001B3
910A2263BCC1C2D9C4420013
710A0102030405060708090A
720A0102030405060708090A
                """,
                one_liner=False,
            ),
        ]
        super().set_data_pool(data_pool)
