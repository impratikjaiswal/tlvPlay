from python_helpers.ph_constants import PhConstants
from python_helpers.ph_util import PhUtil


class TlvData:
    def __init__(self,
                 raw_data,
                 length_in_decimal=None,
                 value_in_ascii=None,
                 one_liner=None,
                 remarks_list=[],
                 ):
        self.raw_data = raw_data
        self.length_in_decimal = length_in_decimal
        self.value_in_ascii = value_in_ascii
        self.one_liner = one_liner
        self.remarks_list = remarks_list
        #
        self.__internal_remarks = None
        #
        self.set_remarks(remarks_list)

    def set_remarks(self, remarks_list):
        if remarks_list is not None:
            self.remarks_list = remarks_list if isinstance(remarks_list, list) else [remarks_list]

    def __get_default_remarks(self):
        self.set_asn1_element_name()
        str_raw_data = str(self.raw_data)
        return PhConstants.SEPERATOR_MULTI_OBJ.join(
            [self.__asn1_element_name, str_raw_data]) if self.__asn1_element_name else str_raw_data

    def get_remarks_as_str(self):
        user_remarks = PhConstants.SEPERATOR_MULTI_OBJ.join(filter(None, self.remarks_list))
        if user_remarks:
            user_remarks = PhUtil.trim_remarks(user_remarks)
        return PhUtil.append_remarks(user_remarks, self.__internal_remarks)
