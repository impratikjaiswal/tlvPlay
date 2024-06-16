from tlv_play.main.data_type.data_type_master import DataTypeMaster


class Dev(DataTypeMaster):

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

    def set_one_liner(self):
        one_liner = None
        super().set_one_liner(one_liner)

    def set_value_in_ascii(self):
        value_in_ascii = None
        super().set_value_in_ascii(value_in_ascii)

    def set_length_in_decimal(self):
        length_in_decimal = None
        super().set_length_in_decimal(length_in_decimal)

    def set_data_pool(self):
        data_pool = [
            #
        ]
        super().set_data_pool(data_pool)
