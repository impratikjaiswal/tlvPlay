import io
import unittest.mock

from src.main.tlv.tlv_handler import TlvHandler
from src.main.tlv.tlv_parser import TlvParser
import test_tlv_data

STR_TEST_OBJ = 'test_obj :'


class test_obj_tlv:
    def __init__(self, input_data, expected_op, expected_op_print, test_name='', length_in_decimal=None,
                 value_in_ascii=None, one_liner=None):
        length_in_decimal = True if length_in_decimal is None else length_in_decimal
        value_in_ascii = True if value_in_ascii is None else value_in_ascii
        one_liner = False if one_liner is None else one_liner
        self.input_data = input_data
        self.expected_op = expected_op
        self.expected_op_print = expected_op_print
        self.test_name = test_name
        self.length_in_decimal = length_in_decimal
        self.value_in_ascii = value_in_ascii
        self.one_liner = one_liner


class test_tlv(unittest.TestCase):
    test_obj_pool = [
        test_obj_tlv(input_data=test_tlv_data.STR_INP_SINGLE_NON_NESTED_TLV,
                     expected_op=test_tlv_data.LIST_OP_SINGLE_NON_NESTED_TLV,
                     expected_op_print=test_tlv_data.STR_OP_SINGLE_NON_NESTED_TLV,
                     test_name='Single Non-Nested TLV'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_MULTIPLE_NON_NESTED_TLV,
                     expected_op=test_tlv_data.LIST_OP_MULTIPLE_NON_NESTED_TLV,
                     expected_op_print=test_tlv_data.STR_OP_MULTIPLE_NON_NESTED_TLV,
                     test_name='Multiple Non-Nested TLV'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_SINGLE_POSSIBLE_NESTED_TLV,
                     expected_op=test_tlv_data.LIST_OP_SINGLE_POSSIBLE_NESTED_TLV,
                     expected_op_print=test_tlv_data.STR_OP_SINGLE_POSSIBLE_NESTED_TLV,
                     test_name='Single Possible Nested TLV'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_THREE_BYTES_TAG_NO_LENGTH,
                     expected_op=test_tlv_data.LIST_OP_THREE_BYTES_TAG_NO_LENGTH,
                     expected_op_print=test_tlv_data.STR_OP_THREE_BYTES_TAG_NO_LENGTH,
                     test_name='Three Bytes Tag, No Length'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_FOUR_BYTES_TAG_NO_LENGTH,
                     expected_op=test_tlv_data.LIST_OP_FOUR_BYTES_TAG_NO_LENGTH,
                     expected_op_print=test_tlv_data.STR_OP_FOUR_BYTES_TAG_NO_LENGTH,
                     test_name='Four Bytes Tag, No Length'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_THREE_BYTES_TAG_0_LENGTH,
                     expected_op=test_tlv_data.LIST_OP_THREE_BYTES_TAG_0_LENGTH,
                     expected_op_print=test_tlv_data.STR_OP_THREE_BYTES_TAG_0_LENGTH,
                     test_name='Three Bytes Tag, 0 Length'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_FOUR_BYTES_TAG_0_LENGTH,
                     expected_op=test_tlv_data.LIST_OP_FOUR_BYTES_TAG_0_LENGTH,
                     expected_op_print=test_tlv_data.STR_OP_FOUR_BYTES_TAG_0_LENGTH,
                     test_name='Four Bytes Tag, 0 Length'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_MULTIPLE_NON_NESTED_AND_SINGLE_NESTED_TLV,
                     expected_op=test_tlv_data.LIST_OP_MULTIPLE_NON_NESTED_AND_SINGLE_NESTED_TLV,
                     expected_op_print=test_tlv_data.STR_OP_MULTIPLE_NON_NESTED_AND_SINGLE_NESTED_TLV,
                     test_name='Multiple Non Nested & Single Nested TLV'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_MULTIPLE_NON_NESTED_AND_MULTIPLE_NESTED_TLV,
                     expected_op=test_tlv_data.LIST_OP_MULTIPLE_NON_NESTED_AND_MULTIPLE_NESTED_TLV,
                     expected_op_print=test_tlv_data.STR_OP_MULTIPLE_NON_NESTED_AND_MULTIPLE_NESTED_TLV,
                     test_name='Multiple Non Nested & Multiple Nested TLV'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_SINGLE_NESTED_TLV_WITH_1_LEN,
                     expected_op=test_tlv_data.LIST_OP_SINGLE_NESTED_TLV_WITH_1_LEN,
                     expected_op_print=test_tlv_data.STR_OP_SINGLE_NESTED_TLV_WITH_1_LEN,
                     test_name='Single Nested TLV with 1 len'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_SINGLE_NESTED_TLV_WITH_2_LEN,
                     expected_op=test_tlv_data.LIST_OP_SINGLE_NESTED_TLV_WITH_2_LEN,
                     expected_op_print=test_tlv_data.STR_OP_SINGLE_NESTED_TLV_WITH_2_LEN,
                     test_name='Single Nested TLV with 2 len'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_SINGLE_NESTED_TLV_POSSIBLE_SUB_NESTED,
                     expected_op=test_tlv_data.LIST_OP_SINGLE_NESTED_TLV_POSSIBLE_SUB_NESTED,
                     expected_op_print=test_tlv_data.STR_OP_SINGLE_NESTED_TLV_POSSIBLE_SUB_NESTED,
                     test_name='Single Nested TLV, Possible Sub Nested'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_MULTIPLE_SUB_NESTED_TLV,
                     expected_op=test_tlv_data.LIST_OP_MULTIPLE_SUB_NESTED_TLV,
                     expected_op_print=test_tlv_data.STR_OP_MULTIPLE_SUB_NESTED_TLV,
                     test_name='Multiple Sub Nested TLV'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_MULTIPLE_SUB_NESTED_TLV_POSSIBLE_GRAND_SUB_NESTED,
                     expected_op=test_tlv_data.LIST_OP_MULTIPLE_SUB_NESTED_TLV_POSSIBLE_GRAND_SUB_NESTED,
                     expected_op_print=test_tlv_data.STR_OP_MULTIPLE_SUB_NESTED_TLV_POSSIBLE_GRAND_SUB_NESTED,
                     test_name='Multiple Sub Nested TLV, Possible Grand Sub Nested'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_MULTI_BYTE_TAG_FAKE_SUB_NESTED,
                     expected_op=test_tlv_data.LIST_OP_MULTI_BYTE_TAG_FAKE_SUB_NESTED,
                     expected_op_print=test_tlv_data.STR_OP_MULTI_BYTE_TAG_FAKE_SUB_NESTED,
                     test_name='Multi Byte Tag, Fake Sub Nested'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_MULTI_BYTE_TAG_FAKE_SUB_NESTED_ALONG_WITH_SIBLINGS_TLV,
                     expected_op=test_tlv_data.LIST_OP_MULTI_BYTE_TAG_FAKE_SUB_NESTED_ALONG_WITH_SIBLINGS_TLV,
                     expected_op_print=test_tlv_data.STR_OP_MULTI_BYTE_TAG_FAKE_SUB_NESTED_ALONG_WITH_SIBLINGS_TLV,
                     test_name='Multi Byte Tag, Fake Sub Nested, along with Siblings TLV'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_FAKE_MULTIBYTE_TAG_IN_NESTED_TLV,
                     expected_op=test_tlv_data.LIST_OP_FAKE_MULTIBYTE_TAG_IN_NESTED_TLV,
                     expected_op_print=test_tlv_data.STR_OP_FAKE_MULTIBYTE_TAG_IN_NESTED_TLV,
                     test_name='Fake MultiByte Tag in Nested TLV'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_FAKE_MULTIBYTE_LENGTH_IN_NESTED_TLV,
                     expected_op=test_tlv_data.LIST_OP_FAKE_MULTIBYTE_LENGTH_IN_NESTED_TLV,
                     expected_op_print=test_tlv_data.STR_OP_FAKE_MULTIBYTE_LENGTH_IN_NESTED_TLV,
                     test_name='Fake MultiByte Length in Nested TLV'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_NESTED_TLVS_WITH_ASCII_DATA,
                     expected_op=test_tlv_data.LIST_OP_NESTED_TLVS_WITH_ASCII_DATA,
                     expected_op_print=test_tlv_data.STR_OP_NESTED_TLVS_WITH_ASCII_DATA,
                     test_name='Nested TLVs with ascii data; value_in_ascii=True',
                     value_in_ascii=True),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_NESTED_TLVS_WITH_ASCII_DATA,
                     expected_op=test_tlv_data.LIST_OP_NESTED_TLVS_WITH_ASCII_DATA,
                     expected_op_print=test_tlv_data.STR_OP_NESTED_TLVS_WITH_ASCII_DATA_VALUE_IN_ASCII_IS_FALSE,
                     test_name='Nested TLVs with ascii data; value_in_ascii=False',
                     value_in_ascii=False),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_NESTED_TLV_MULTI_BYTE_LEN_81,
                     expected_op=test_tlv_data.LIST_OP_NESTED_TLV_MULTI_BYTE_LEN_81,
                     expected_op_print=test_tlv_data.STR_OP_NESTED_TLV_MULTI_BYTE_LEN_81,
                     test_name='Nested TLV, Multi Byte Len 81; length_in_decimal=True',
                     length_in_decimal=True),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_NESTED_TLV_MULTI_BYTE_LEN_81,
                     expected_op=test_tlv_data.LIST_OP_NESTED_TLV_MULTI_BYTE_LEN_81,
                     expected_op_print=test_tlv_data.STR_OP_NESTED_TLV_MULTI_BYTE_LEN_81_LENGTH_IN_DECIMAL_IS_FALSE,
                     test_name='Nested TLV, Multi Byte Len 81; length_in_decimal=False',
                     length_in_decimal=False),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_NESTED_TLV_MULTI_BYTE_LEN_82,
                     expected_op=test_tlv_data.LIST_OP_NESTED_TLV_MULTI_BYTE_LEN_82,
                     expected_op_print=test_tlv_data.STR_OP_NESTED_TLV_MULTI_BYTE_LEN_82,
                     test_name='Nested TLV, Multi Byte Len 82'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_SINGLE_NON_NESTED_TLV_DATA_FF,
                     expected_op=test_tlv_data.LIST_OP_SINGLE_NON_NESTED_TLV_DATA_FF,
                     expected_op_print=test_tlv_data.STR_OP_SINGLE_NON_NESTED_TLV_DATA_FF,
                     test_name='Single Non-Nested TLV, Data is FF'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_SINGLE_NON_NESTED_TLV_DATA_FF_BULK,
                     expected_op=test_tlv_data.LIST_OP_SINGLE_NON_NESTED_TLV_DATA_FF_BULK,
                     expected_op_print=test_tlv_data.STR_OP_SINGLE_NON_NESTED_TLV_DATA_FF_BULK,
                     test_name='Single Non-Nested TLV, Data is FF Bulk'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_EMV_TLVS,
                     expected_op=test_tlv_data.LIST_OP_EMV_TLVS,
                     expected_op_print=test_tlv_data.STR_OP_EMV_TLVS,
                     test_name='EMV TLVs'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_EMV_TLVS,
                     expected_op=test_tlv_data.LIST_OP_EMV_TLVS,
                     expected_op_print=test_tlv_data.STR_OP_EMV_TLVS_ONE_LINER_PLAIN,
                     test_name='EMV TLVs One Liner; one_liner=True',
                     length_in_decimal=False,
                     value_in_ascii=False,
                     one_liner=True),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_EMV_TLVS,
                     expected_op=test_tlv_data.LIST_OP_EMV_TLVS,
                     expected_op_print=test_tlv_data.STR_OP_EMV_TLVS_ONE_LINER_IS_FALSE,
                     test_name='EMV TLVs One Liner; one_liner=False',
                     length_in_decimal=False,
                     value_in_ascii=False,
                     one_liner=False),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_RSP_TLVS,
                     expected_op=test_tlv_data.LIST_OP_RSP_TLVS,
                     expected_op_print=test_tlv_data.STR_OP_RSP_TLVS,
                     test_name='RSP TLVs'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_RSP_TLVS,
                     expected_op=test_tlv_data.LIST_OP_RSP_TLVS,
                     expected_op_print=test_tlv_data.STR_OP_RSP_TLVS_ONE_LINER_PLAIN,
                     test_name='RSP TLVs One Liner',
                     length_in_decimal=False,
                     value_in_ascii=False,
                     one_liner=True),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_AID_00_TAG,
                     expected_op=test_tlv_data.LIST_OP_AID_00_TAG,
                     expected_op_print=test_tlv_data.STR_OP_AID_00_TAG,
                     test_name='AID, 00 Tag'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_AID_01_TAG,
                     expected_op=test_tlv_data.LIST_OP_AID_01_TAG,
                     expected_op_print=test_tlv_data.STR_OP_AID_01_TAG,
                     test_name='AID, 01 Tag'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_RESTRICT_CHILD_MAPPING,
                     expected_op=test_tlv_data.LIST_OP_RESTRICT_CHILD_MAPPING,
                     expected_op_print=test_tlv_data.STR_OP_RESTRICT_CHILD_MAPPING,
                     test_name='Restrict Child Mapping'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_RESTRICT_TWO_BYTE_TAG,
                     expected_op=test_tlv_data.LIST_OP_RESTRICT_TWO_BYTE_TAG,
                     expected_op_print=test_tlv_data.STR_OP_RESTRICT_TWO_BYTE_TAG,
                     test_name='Restrict Two Byte Tag'),

        test_obj_tlv(input_data=test_tlv_data.STR_INP_PROFILE_1,
                     expected_op=test_tlv_data.LIST_OP_PROFILE_1,
                     expected_op_print=test_tlv_data.STR_OP_PROFILE_1,
                     test_name='Profile 1'),
    ]

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, test_obj, mock_stdout):
        expected_op_print = test_obj.expected_op_print[1:] if test_obj.expected_op_print[
                                                                  0] == '\n' else test_obj.expected_op_print
        TlvParser(TlvHandler(test_obj.input_data).process_data()).print_tlv(
            length_in_decimal=test_obj.length_in_decimal,
            value_in_ascii=test_obj.value_in_ascii,
            one_liner=test_obj.one_liner)
        self.assertEqual(mock_stdout.getvalue(), expected_op_print)

    def test_tlv_data(self):
        """
        :return:
        """
        self.maxDiff = None
        for count, test_obj in enumerate(test_tlv.test_obj_pool, start=1):
            with self.subTest(STR_TEST_OBJ + (test_obj.test_name if test_obj.test_name else str(count))):
                self.assertEqual(TlvHandler(test_obj.input_data).process_data(), test_obj.expected_op)

    def test_tlv_print(self):
        """

        :return:
        """
        self.maxDiff = None
        for count, test_obj in enumerate(test_tlv.test_obj_pool, start=1):
            with self.subTest(STR_TEST_OBJ + (test_obj.test_name if test_obj.test_name else str(count))):
                self.assert_stdout(test_obj)


if __name__ == '__main__':
    unittest.main()
