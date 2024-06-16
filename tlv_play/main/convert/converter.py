from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from tlv_play.main.helper.data import Data
from tlv_play.main.helper.defaults import Defaults


def print_data(data, meta_data):
    if data.quite_mode:
        return
    input_sep = PhConstants.SEPERATOR_ONE_LINE
    output_sep = PhConstants.SEPERATOR_MULTI_LINE
    if data.print_info:
        remarks_original = data.get_remarks_as_str(user_original_remarks=True)
        remarks_generated = data.get_remarks_as_str()
        remarks_generated_stripping_needed = True if remarks_generated.endswith(
            PhConstants.DEFAULT_TRIM_STRING) else False
        if remarks_original:
            if remarks_generated_stripping_needed:
                if remarks_generated.strip(PhConstants.DEFAULT_TRIM_STRING) in remarks_original:
                    remarks_generated = ''
            else:
                if remarks_original in remarks_generated:
                    remarks_generated = ''
            meta_data.output_dic.update(
                get_dic_data_and_print(PhKeys.REMARKS, PhConstants.SEPERATOR_ONE_LINE, remarks_original))
        if remarks_generated:
            meta_data.output_dic.update(
                get_dic_data_and_print(PhKeys.REMARKS_GENERATED, PhConstants.SEPERATOR_ONE_LINE,
                                       remarks_generated))
        info = PhConstants.SEPERATOR_MULTI_OBJ.join(filter(None, [
            get_dic_data_and_print(PhKeys.ONE_LINER, PhConstants.SEPERATOR_ONE_LINE, data.one_liner,
                                   dic_format=False, print_also=False) if data.one_liner else None,
            get_dic_data_and_print(PhKeys.VALUE_IN_ASCII, PhConstants.SEPERATOR_ONE_LINE, data.value_in_ascii,
                                   dic_format=False, print_also=False) if data.value_in_ascii else None,
            get_dic_data_and_print(PhKeys.LENGTH_IN_DECIMAL, PhConstants.SEPERATOR_ONE_LINE, data.length_in_decimal,
                                   dic_format=False, print_also=False) if data.length_in_decimal else None,
            get_dic_data_and_print(PhKeys.QUITE_MODE, PhConstants.SEPERATOR_ONE_LINE, data.quite_mode,
                                   dic_format=False, print_also=False) if data.quite_mode else None,
        ]))
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INFO, PhConstants.SEPERATOR_INFO, info))
    if data.print_input:
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.INPUT_DATA, input_sep, meta_data.input_data_org))
    print_output = data.print_output
    if data.print_output and print_output:  # and meta_data.parsed_data:
        meta_data.output_dic.update(get_dic_data_and_print(PhKeys.OUTPUT_DATA, output_sep, meta_data.parsed_data))
    PhUtil.print_separator()


def get_dic_data_and_print(key, sep, value, dic_format=True, print_also=True):
    return PhUtil.get_key_value_pair(key=key, value=value, sep=sep, dic_format=dic_format, print_also=print_also)


def parse_config(config_data):
    # PhUtil.print_iter(config_data, 'config_data initial', verbose=True)
    for k, v in config_data.items():
        if v:
            # Trim Garbage data
            v = PhUtil.trim_white_spaces_in_str(v)
            if v in ['None']:
                v = None
                config_data[k] = v
            if v in [PhConstants.STR_SELECT_OPTION]:
                v = None
                config_data[k] = v
            if v in ['True']:
                v = True
                config_data[k] = v
            if v in ['False']:
                v = False
                config_data[k] = v
        if not v:
            continue
        config_data[k] = v
    # PhUtil.print_iter(config_data, 'config_data processed', verbose=True, depth_level=1)
    return config_data


def set_defaults_for_printing(data):
    if data.quite_mode is None:
        data.quite_mode = Defaults.QUITE_MODE
    if data.print_input is None:
        data.print_input = Defaults.PRINT_INPUT
    if data.print_output is None:
        data.print_output = Defaults.PRINT_OUTPUT
    if data.print_info is None:
        data.print_info = Defaults.PRINT_INFO


def set_defaults(data, meta_data):
    """
    Set Default Values if nothing is set
    :param data:
    :param meta_data:
    :return:
    """
    if data.length_in_decimal is None:
        data.length_in_decimal = Defaults.LENGTH_IN_DECIMAL
    if data.value_in_ascii is None:
        data.value_in_ascii = Defaults.VALUE_IN_ASCII
    if data.one_liner is None:
        data.one_liner = Defaults.ONE_LINER


def read_web_request(request_form):
    return Data(**parse_config(request_form))
