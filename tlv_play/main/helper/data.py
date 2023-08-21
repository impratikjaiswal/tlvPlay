from python_helpers.ph_util import PhUtil


class Data:
    def __init__(self,
                 raw_data,
                 length_in_decimal=None,
                 value_in_ascii=None,
                 one_liner=None,
                 print_input=None,
                 print_output=None,
                 print_info=None,
                 quite_mode=None,
                 remarks_list=[],
                 ):
        self.raw_data = raw_data
        self.length_in_decimal = length_in_decimal
        self.value_in_ascii = value_in_ascii
        self.one_liner = one_liner
        self.print_input = print_input
        self.print_output = print_output
        self.print_info = print_info
        self.quite_mode = quite_mode
        #
        self.__auto_generated_remarks = None
        self.__one_time_remarks = None
        self.__extended_remarks_needed = None
        #
        self.remarks_list = None
        self.set_user_remarks(remarks_list)

    def set_user_remarks(self, remarks_list):
        self.remarks_list = PhUtil.cast_to_list(remarks_list, trim_data=True, all_str=True)

    def __get_default_remarks(self):
        str_raw_data = PhUtil.combine_list_items(self.raw_data)
        return str_raw_data

    def reset_auto_generated_remarks(self):
        self.__auto_generated_remarks = None

    def set_auto_generated_remarks_if_needed(self, internal_remarks=None):
        internal_remarks = PhUtil.set_if_not_none(internal_remarks)
        default_remarks = self.__get_default_remarks()
        if self.remarks_list and self.remarks_list[0]:
            # User Remarks is already provided, default remarks are not needed
            default_remarks = None
        # auto generated comments are set
        self.__auto_generated_remarks = PhUtil.append_remarks(internal_remarks,
                                                              self.__auto_generated_remarks if self.__auto_generated_remarks else default_remarks,
                                                              append_mode_post=False)

    def get_remarks_as_str(self, user_original_remarks=False, force_mode=False):
        user_remarks = PhUtil.combine_list_items(self.remarks_list)
        if user_original_remarks:
            if user_remarks:
                return user_remarks.replace('\n', ' ')
            if not force_mode:
                return ''
        if user_remarks:
            user_remarks = PhUtil.trim_remarks(user_remarks)
        one_time_remarks = PhUtil.append_remarks(self.get_one_time_remarks(), self.__auto_generated_remarks,
                                                 append_mode_post=False)
        return PhUtil.append_remarks(one_time_remarks, user_remarks, append_mode_post=False).replace('\n', ' ')

    def set_extended_remarks_available(self, extended_remarks):
        self.__extended_remarks_needed = extended_remarks

    def get_extended_remarks_available(self):
        return self.__extended_remarks_needed

    def get_one_time_remarks(self):
        temp = self.__one_time_remarks
        self.__one_time_remarks = None
        return temp

    def set_one_time_remarks(self, one_time_remarks):
        self.__one_time_remarks = one_time_remarks
