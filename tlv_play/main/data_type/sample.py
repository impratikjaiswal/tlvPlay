from collections import OrderedDict

from python_helpers.ph_util import PhUtil

from tlv_play.main.data_type.data_type_master import DataTypeMaster
from tlv_play.main.helper.data import Data


# Data has to be declared in global, so that it can be used by other classes

class Sample(DataTypeMaster):

    def get_sample_data_pool_for_web(self):
        if not self.data_pool:
            self.set_data_pool()
        sample_data_dic = OrderedDict()
        for data in self.data_pool:
            remarks = data.remarks
            remarks = PhUtil.to_list(remarks, all_str=True, trim_data=True)
            if len(remarks) < 1:
                raise ValueError("Remarks should not be empty")
            key, data.data_group = PhUtil.generate_key_and_data_group(remarks)
            if key in sample_data_dic:
                raise ValueError(f'Duplicate Sample Remarks: {key}')
            sample_data_dic.update({key: super().to_dic(data)})
        return sample_data_dic

    def __init__(self):
        super().__init__()

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

    def set_output_path(self):
        output_path = None
        super().set_output_path(output_path)

    def set_output_file_name_keyword(self):
        output_file_name_keyword = None
        super().set_output_file_name_keyword(output_file_name_keyword)

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
        data_pool = [
            #
            Data(
                remarks='Simple TLV',
                input_data='86020102',
            ),
            #
            Data(
                remarks='Multiple Simple TLVs; Neighbors',
                input_data='81020105820106830209AB',
            ),
            #
            Data(
                remarks='Multiple Simple TLVs; Neighbors; Non TLV Neighbors; non_tlv_neighbor=True',
                input_data='81020105820106830209AB6A88',
                non_tlv_neighbor=True,
            ),
            #
            Data(
                remarks='Simple TLV; Multi Byte Tag',
                input_data='BF3E125A1089049032123451234512345678901235',
            ),
            #
            Data(
                remarks='Nested BER TLV; length_in_decimal=True',
                input_data='064B21220D2048656C6C6F2C204275792031204742204461746120666F7220302E3520555344210F0D0D41726520596F7520537572653F151431107777772E66616365626F6F6B2E636F6D0500',
                length_in_decimal=True,
            ),
            #
            Data(
                remarks='BER TLV; length_in_decimal=False',
                input_data='064B21220D2048656C6C6F2C204275792031204742204461746120666F7220302E3520555344210F0D0D41726520596F7520537572653F151431107777772E66616365626F6F6B2E636F6D0500',
                length_in_decimal=False,
            ),
            #
            Data(
                remarks='Nested BER TLV; value_in_ascii=True',
                input_data='064B21220D2048656C6C6F2C204275792031204742204461746120666F7220302E3520555344210F0D0D41726520596F7520537572653F151431107777772E66616365626F6F6B2E636F6D0500',
                value_in_ascii=True,
            ),
            #
            Data(
                remarks='BER TLV; value_in_ascii=False',
                input_data='064B21220D2048656C6C6F2C204275792031204742204461746120666F7220302E3520555344210F0D0D41726520596F7520537572653F151431107777772E66616365626F6F6B2E636F6D0500',
                value_in_ascii=False,
            ),
            #
            Data(
                remarks='Nested BER TLV; one_liner=True',
                input_data='064B21220D2048656C6C6F2C204275792031204742204461746120666F7220302E3520555344210F0D0D41726520596F7520537572653F151431107777772E66616365626F6F6B2E636F6D0500',
                one_liner=True,
            ),
            #
            Data(
                remarks='Nested BER TLV; one_liner=False',
                input_data='064B21220D2048656C6C6F2C204275792031204742204461746120666F7220302E3520555344210F0D0D41726520596F7520537572653F151431107777772E66616365626F6F6B2E636F6D0500',
                one_liner=False,
            ),
            #
            Data(
                remarks='Nested BER TLV; Base64',
                input_data='vyUzWgqYkgkBIUNlhwn1kQlTUCBOYW1lIDGSGk9wZXJhdGlvbmFsIFByb2ZpbGUgTmFtZSAx',
            ),
            #
            Data(
                remarks='Nested BER TLV; Complex; ESIM Profile; length_in_decimal=True; value_in_ascii=True; one_liner=True',
                input_data='A042800102810101821447534D412050726F66696C65205061636B616765830A8929901012345678905FA506810084008B00A610060667810F010201060667810F010204B08201F8A0058000810101810667810F010201A207A105C60301020AA305A1038B010FA40C830A989209012143658709F5A527A109820442210026800198831A61184F10A0000000871002FF33FF01890000010050045553494DA682019EA10A8204422100258002022B831B8001019000800102A406830101950108800158A40683010A95010882010A8316800101A40683010195010880015AA40683010A95010882010F830B80015BA40683010A95010882011A830A800101900080015A970082011B8316800103A406830101950108800158A40683010A95010882010F8316800111A40683010195010880014AA40683010A95010882010F8321800103A406830101950108800158A40683010A950108840132A4068301019501088201048321800101A406830101950108800102A406830181950108800158A40683010A950108820104831B800101900080011AA406830101950108800140A40683010A95010882010A8310800101900080015AA40683010A95010882011583158001019000800118A40683010A95010880014297008201108310800101A40683010195010880015A97008201158316800113A406830101950108800148A40683010A95010882010F830B80015EA40683010A95010882011A83258001019000800102A010A406830101950108A406830102950108800158A40683010A950108A33FA0058000810102A13630118001018108303030303030303082020099300D800102810831323334353637383012800200818108393239343536373882020088A244A0058000810103A13BA0393013800101810831323334FFFFFFFF8201018301063010800102810830303030FFFFFFFF820102301080010A810835363738FFFFFFFF830101B381C3A0058000810104810667810F010204A21DA11B83027FF18410A0000000871002FF33FF018900000100C60301810AA30B8309082999181132547698A406A104C7022F06A80F830D0A2E148CE73204000000000000AB45A10D82044221003483026F428001688334534D53433120FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF1FFFFFFFFFFFFFFFFFFFFFFFF07916427417900F4FFFFFFFFFFFFFFAD1383110247534D41206555494343FFFFFFFFFFFFAE03830100B20483020040B606830419F1FF01A225A0058000810105A11CA01A301880020081810839323338FFFFFFFF82020081830101840122A43AA0058000810106A131A12F8001018101018210000102030405060708090A0B0C0D0E0F83100102030405060708090A0B0C0D0E0F008603010203A681BBA0058000810107A1444F07A00000015153504F08A0000001515350414F08A000000151000000820382DC0083010FC90A810280008201F08701F0EA11800F0100000100000002011203B2010000A26C302295013882010183010130173015800180861066778899AABBCCDD1122334455EEFF103022950134820102830101301730158001808610112233445566778899AABBCCDDEEFF1030229501C882010383010130173015800180861099AABBCCDDEEFF101122334455667788A681C0A0058000810108A1494F07A00000015153504F08A0000001515350414F10A00000055910100102736456616C7565820380800083010FC907810280008201F0EA11800F01000001000000020112036C756500A26C30229501388201018301013017301580018086101122334455667788112233445566778830229501348201028301013017301580018086101122334455667788112233445566778830229501C882010383010130173015800180861011223344556677881122334455667788A720A00381010B4F09A00000055910100001A0050403B00000810112040100040100A740A00381010C4F09A00000055910100002A0050403B00020810112040100040100301E8010A0000000871002FF33FF018900000100810402000100820402000100AA07A0058000810163',
                length_in_decimal=True,
                value_in_ascii=True,
                one_liner=True,
            ),
            #
        ]
        super().set_data_pool(data_pool)
