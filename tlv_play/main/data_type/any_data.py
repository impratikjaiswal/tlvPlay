from tlv_play.main.data_type.data_type_master import DataTypeMaster
from tlv_play.main.helper.tlv_data import TlvData


class AnyData(DataTypeMaster):

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
                remarks_list='Parallel Simple TLV',
                raw_data='81020105 820106 830209AB',
            ),
            #
            TlvData(
                remarks_list='BER TLV; Multiple Simple TLV as Children',
                raw_data='D00D 8103010500 82028182 9902090A'
            ),
            #
            TlvData(
                remarks_list='Simple TLV; length_in_decimal=True',
                raw_data='86020102',
                length_in_decimal=True,
            ),
            #
            TlvData(
                remarks_list='Simple TLV; length_in_decimal=False',
                raw_data='86020102',
                length_in_decimal=False,
            ),
            #
            TlvData(
                remarks_list='BER TLV; Multiple Simple TLV as Children; one_liner=True',
                raw_data='D00D 8103010500 82028182 9902090A',
                one_liner=True
            ),
            #
            TlvData(
                remarks_list='BER TLV; Multiple Simple TLV as Children; one_liner=False',
                raw_data='D00D 8103010500 82028182 9902090A',
                one_liner=False
            ),
            #
            TlvData(
                remarks_list='Simple TLV with ASCII Characters; value_in_ascii=True',
                raw_data='50 04 5553494D',
                value_in_ascii=True,
            ),
            #
            TlvData(
                remarks_list='Simple TLV with ASCII Characters; value_in_ascii=False',
                raw_data='50 04 5553494D',
                value_in_ascii=False,
            ),
            #
            TlvData(
                remarks_list='BER TLV; Ber TLV as Children; with Ascii characters; value_in_ascii=True',
                raw_data='064B21220D2048656C6C6F2C204275792031204742204461746120666F7220302E3520555344210F0D0D41726520596F7520537572653F151431107777772E66616365626F6F6B2E636F6D0500',
                value_in_ascii=True,
            ),
            #
            TlvData(
                remarks_list='BER TLV; Ber TLV as Children; with Ascii characters; value_in_ascii=False',
                raw_data='064B21220D2048656C6C6F2C204275792031204742204461746120666F7220302E3520555344210F0D0D41726520596F7520537572653F151431107777772E66616365626F6F6B2E636F6D0500',
                value_in_ascii=False,
            ),
            #
            TlvData(
                remarks_list='Multi Byte Tag; EID',
                raw_data='BF3E 12 5A 10 89049032123451234512345678901235'
            ),
            #
            TlvData(
                remarks_list='Complex Nested Ber TLVz; ESIM Profile',
                raw_data='A042800102810101821447534D412050726F66696C65205061636B616765830A8929901012345678905FA506810084008B00A610060667810F010201060667810F010204B08201F8A0058000810101810667810F010201A207A105C60301020AA305A1038B010FA40C830A989209012143658709F5A527A109820442210026800198831A61184F10A0000000871002FF33FF01890000010050045553494DA682019EA10A8204422100258002022B831B8001019000800102A406830101950108800158A40683010A95010882010A8316800101A40683010195010880015AA40683010A95010882010F830B80015BA40683010A95010882011A830A800101900080015A970082011B8316800103A406830101950108800158A40683010A95010882010F8316800111A40683010195010880014AA40683010A95010882010F8321800103A406830101950108800158A40683010A950108840132A4068301019501088201048321800101A406830101950108800102A406830181950108800158A40683010A950108820104831B800101900080011AA406830101950108800140A40683010A95010882010A8310800101900080015AA40683010A95010882011583158001019000800118A40683010A95010880014297008201108310800101A40683010195010880015A97008201158316800113A406830101950108800148A40683010A95010882010F830B80015EA40683010A95010882011A83258001019000800102A010A406830101950108A406830102950108800158A40683010A950108A33FA0058000810102A13630118001018108303030303030303082020099300D800102810831323334353637383012800200818108393239343536373882020088A244A0058000810103A13BA0393013800101810831323334FFFFFFFF8201018301063010800102810830303030FFFFFFFF820102301080010A810835363738FFFFFFFF830101B381C3A0058000810104810667810F010204A21DA11B83027FF18410A0000000871002FF33FF018900000100C60301810AA30B8309082999181132547698A406A104C7022F06A80F830D0A2E148CE73204000000000000AB45A10D82044221003483026F428001688334534D53433120FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF1FFFFFFFFFFFFFFFFFFFFFFFF07916427417900F4FFFFFFFFFFFFFFAD1383110247534D41206555494343FFFFFFFFFFFFAE03830100B20483020040B606830419F1FF01A225A0058000810105A11CA01A301880020081810839323338FFFFFFFF82020081830101840122A43AA0058000810106A131A12F8001018101018210000102030405060708090A0B0C0D0E0F83100102030405060708090A0B0C0D0E0F008603010203A681BBA0058000810107A1444F07A00000015153504F08A0000001515350414F08A000000151000000820382DC0083010FC90A810280008201F08701F0EA11800F0100000100000002011203B2010000A26C302295013882010183010130173015800180861066778899AABBCCDD1122334455EEFF103022950134820102830101301730158001808610112233445566778899AABBCCDDEEFF1030229501C882010383010130173015800180861099AABBCCDDEEFF101122334455667788A681C0A0058000810108A1494F07A00000015153504F08A0000001515350414F10A00000055910100102736456616C7565820380800083010FC907810280008201F0EA11800F01000001000000020112036C756500A26C30229501388201018301013017301580018086101122334455667788112233445566778830229501348201028301013017301580018086101122334455667788112233445566778830229501C882010383010130173015800180861011223344556677881122334455667788A720A00381010B4F09A00000055910100001A0050403B00000810112040100040100A740A00381010C4F09A00000055910100002A0050403B00020810112040100040100301E8010A0000000871002FF33FF018900000100810402000100820402000100AA07A0058000810163'
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
