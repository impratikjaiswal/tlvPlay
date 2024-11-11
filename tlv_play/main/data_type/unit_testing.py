from tlv_play.main.data_type.data_type_master import DataTypeMaster
from tlv_play.main.helper.data import Data


class UnitTesting(DataTypeMaster):

    def set_print_input(self):
        print_input = None
        super().set_print_input(print_input)

    def set_print_output(self):
        print_output = None
        super().set_print_output(print_output)

    def set_print_info(self):
        print_info = None
        super().set_print_info(print_info)

    def set_quiet_mode(self):
        quite_mode = None
        super().set_quiet_mode(quite_mode)

    def set_remarks(self):
        remarks = None
        super().set_remarks(remarks)

    def set_encoding(self):
        encoding = None
        super().set_encoding(encoding)

    def set_encoding_errors(self):
        encoding_errors = None
        super().set_encoding_errors(encoding_errors)

    def set_archive_output(self):
        archive_output = None
        super().set_archive_output(archive_output)

    def set_archive_output_format(self):
        archive_output_format = None
        super().set_archive_output_format(archive_output_format)

    def set_length_in_decimal(self):
        length_in_decimal = None
        super().set_length_in_decimal(length_in_decimal)

    def set_value_in_ascii(self):
        value_in_ascii = None
        super().set_value_in_ascii(value_in_ascii)

    def set_one_liner(self):
        one_liner = None
        super().set_one_liner(one_liner)

    def set_non_tlv_neighbor(self):
        non_tlv_neighbor = None
        super().set_non_tlv_neighbor(non_tlv_neighbor)

    def set_data_pool(self):
        data_pool_positive = [
            #
            Data(
                remarks='BER TLV; Multiple Simple TLV as Children',
                input_data='D00D8103010500820281829902090A'
            ),
            #
            Data(
                remarks='Simple TLV; length_in_decimal=True',
                input_data='86020102',
                length_in_decimal=True,
            ),
            #
            Data(
                remarks='Simple TLV; length_in_decimal=False',
                input_data='86020102',
                length_in_decimal=False,
            ),
            #
            Data(
                remarks='BER TLV; Multiple Simple TLV as Children; one_liner=True',
                input_data='D00D 8103010500 82028182 9902090A',
                one_liner=True
            ),
            #
            Data(
                remarks='BER TLV; Multiple Simple TLV as Children; one_liner=False',
                input_data='D00D 8103010500 82028182 9902090A',
                one_liner=False
            ),
            #
            Data(
                remarks='Simple TLV with ASCII Characters; value_in_ascii=True',
                input_data='50 04 5553494D',
                value_in_ascii=True,
            ),
            #
            Data(
                remarks='Simple TLV with ASCII Characters; value_in_ascii=False',
                input_data='50 04 5553494D',
                value_in_ascii=False,
            ),
            #
            Data(
                remarks='List',
                input_data=['50 04 5553494D', 'D00D 8103010500 82028182 9902090A', '86020102',
                            'D00D8103010500820281829902090A'],
            ),
            #
            Data(
                remarks='Test TLV',
                input_data="""
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
            #
            Data(
                remarks='Nested BER TLV; length_in_decimal=True; value_in_ascii=True; one_liner=True',
                input_data='064B21220D2048656C6C6F2C204275792031204742204461746120666F7220302E3520555344210F0D0D41726520596F7520537572653F151431107777772E66616365626F6F6B2E636F6D0500',
                length_in_decimal=True,
                value_in_ascii=True,
                one_liner=True,
            ),
            #
            Data(
                remarks='Multiple Simple TLVs; Neighbors; Non TLV Neighbors',
                input_data='810201020102',
            ),
            #
            Data(
                remarks='Multiple Simple TLVs; Neighbors; Non TLV Neighbors',
                input_data='81020102810201020102',
            ),
            #
            Data(
                remarks='Non TLV',
                input_data='0102',
            ),
            #
        ]
        data_pool_negative = [
            #
            Data(
                remarks_list='Kwargs; remarks_list',
                input_data='86020102',
            ),
            #
            Data(
                remarks='Kwargs; raw_data',
                raw_data='86020102',
            ),
            #
            Data(
                remarks='Kwargs; future',
                input_data='86020102',
                future='AmenityPj.in',
            ),
            #
            Data(
                remarks='Empty Data',
                input_data='',
            ),
            #
            Data(
                remarks='Garbage Hex Data',
                input_data='124',
            ),
        ]
        super().set_data_pool(data_pool_positive + data_pool_negative)
