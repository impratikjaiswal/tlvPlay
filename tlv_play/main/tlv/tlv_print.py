from python_helpers.ph_constants import PhConstants
from python_helpers.ph_util import PhUtil


class TlvPrint:
    SPACE = '  '
    SPACE_ONE_LINER = ' '
    SPACE_TL = ' '
    SEP_TL_V = '\n'
    SEP_TL_V_ONE_LINER = ''
    SEP_CONCAT_TLVS = '\n'
    SEP_SUB_TLVS = '\n'

    def __init__(self, tlv_obj, level, length_in_decimal=None, value_in_ascii=None, one_liner=None):
        self.tlv_obj = tlv_obj
        self.level = level
        self.length_in_decimal = length_in_decimal
        self.value_in_ascii = value_in_ascii
        self.one_liner = one_liner

    def get_tl_as_str(self):
        return (f'{TlvPrint.SPACE * self.level}'
                f'{PhUtil.to_hex_string(self.tlv_obj.tag_list, PhConstants.FORMAT_HEX_STRING_AS_PACK)}'
                f'{TlvPrint.SPACE_TL}'
                f'{PhUtil.to_hex_string(self.tlv_obj.len_list, PhConstants.FORMAT_HEX_STRING_AS_PACK)}') \
            + (f' ({self.tlv_obj.len_dec})' if self.length_in_decimal else '')

    def get_v_as_str(self):
        value_str = PhUtil.to_hex_string(self.tlv_obj.value_list, PhConstants.FORMAT_HEX_STRING_AS_PACK)
        value_str_ascii = PhUtil.hex_str_to_ascii(value_str) if value_str and self.value_in_ascii else ''
        space = TlvPrint.SPACE_ONE_LINER if self.one_liner else TlvPrint.SPACE * (self.level + 1)
        return (f'{space}{value_str}' if value_str else '') + (f' ({value_str_ascii})' if value_str_ascii else '')

    def get_tlv_as_str(self):
        sep = TlvPrint.SEP_TL_V_ONE_LINER if self.one_liner else TlvPrint.SEP_TL_V
        return sep.join(filter(None, [f'{self.get_tl_as_str()}', f'{self.get_v_as_str()}']))
