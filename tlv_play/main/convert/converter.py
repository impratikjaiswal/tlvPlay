from python_helpers.ph_constants import PhConstants
from python_helpers.ph_data_master import PhMasterData, PhMasterDataKeys
from python_helpers.ph_defaults import PhDefaultTypesExclude
from python_helpers.ph_exception_helper import PhExceptionHelper
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from tlv_play.main.helper.data import Data
from tlv_play.main.helper.defaults import Defaults, DefaultTypesInclude


def print_data(data=None, meta_data=None, info_data=None, master_data=None):
    """
    
    :param data:
    :param meta_data:
    :param info_data:
    :param master_data:
    :return:
    """
    if master_data is not None and isinstance(master_data, PhMasterData):
        data = master_data.get_master_data(PhMasterDataKeys.DATA)
        meta_data = master_data.get_master_data(PhMasterDataKeys.META_DATA)
        info_data = master_data.get_master_data(PhMasterDataKeys.INFO_DATA)
    if data.quite_mode:
        return
    input_sep = PhConstants.SEPERATOR_ONE_LINE
    output_sep = PhConstants.SEPERATOR_MULTI_LINE
    len_sep = PhConstants.SEPERATOR_ONE_LINE
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
                PhUtil.get_dic_data_and_print(PhKeys.REMARKS, PhConstants.SEPERATOR_ONE_LINE, remarks_original))
        if remarks_generated:
            meta_data.output_dic.update(
                PhUtil.get_dic_data_and_print(PhKeys.REMARKS_GENERATED, PhConstants.SEPERATOR_ONE_LINE,
                                              remarks_generated))
        if info_data is not None:
            info_count = info_data.get_info_count()
            info_msg = info_data.get_info_str()
            info_present = info_msg
            if info_present:
                sep = PhConstants.SEPERATOR_MULTI_LINE_TABBED if info_count > 1 else PhConstants.SEPERATOR_ONE_LINE
                meta_data.output_dic.update(PhUtil.get_dic_data_and_print(PhKeys.INFO_DATA, sep, info_msg))
                if data.print_info:
                    meta_data.output_dic.update(
                        PhUtil.get_dic_data_and_print(PhKeys.INFO_DATA, len_sep, info_msg, length_needed=True))
        info_contents_pool = {
            PhKeys.TRANSACTION_ID: meta_data.transaction_id,
            PhKeys.LENGTH_IN_DECIMAL: data.length_in_decimal,
            PhKeys.VALUE_IN_ASCII: data.value_in_ascii,
            PhKeys.ONE_LINER: data.one_liner,
            PhKeys.NON_TLV_NEIGHBOR: data.non_tlv_neighbor,
            PhKeys.OUTPUT_PATH: data.output_path,
            PhKeys.OUTPUT_FILE_NAME_KEYWORD: data.output_file_name_keyword,
            PhKeys.ENCODING: data.encoding,
            PhKeys.ENCODING_ERRORS: data.encoding_errors,
            PhKeys.ARCHIVE_OUTPUT: data.archive_output,
            PhKeys.ARCHIVE_OUTPUT_FORMAT: data.archive_output_format,
            PhKeys.QUITE_MODE: data.quite_mode,
        }
        meta_data.output_dic.update(PhUtil.get_dic_data_and_print(PhKeys.INFO, PhConstants.SEPERATOR_INFO,
                                                                  PhUtil.decorate_info_data(info_contents_pool)))
    in_data = meta_data.input_data_org
    if data.print_input:
        meta_data.output_dic.update(PhUtil.get_dic_data_and_print(PhKeys.INPUT_DATA, input_sep, in_data))
    if data.print_info:
        meta_data.output_dic.update(
            PhUtil.get_dic_data_and_print(PhKeys.INPUT_DATA, len_sep, in_data, length_needed=True))
    output_present = meta_data.parsed_data
    if output_present:
        if data.print_output:
            meta_data.output_dic.update(
                PhUtil.get_dic_data_and_print(PhKeys.OUTPUT_DATA, output_sep, meta_data.parsed_data))
        if data.print_info:
            meta_data.output_dic.update(
                PhUtil.get_dic_data_and_print(PhKeys.OUTPUT_DATA, len_sep, meta_data.parsed_data, length_needed=True))
    PhUtil.print_separator()


def set_includes_excludes_files(data, meta_data):
    """

    :param data:
    :param meta_data:
    """
    # Always exclude output files
    meta_data.excludes = ['*_' + KeyWords.OUTPUT_FILE_NAME_KEYWORD + '.*']
    # Include Everything for now


def dict_to_data(config_data):
    data_types_include = {
        # Common Param
        # PhKeys.INPUT_DATA:
        PhKeys.PRINT_INPUT: DefaultTypesInclude.PRINT_INPUT,
        PhKeys.PRINT_OUTPUT: DefaultTypesInclude.PRINT_OUTPUT,
        PhKeys.PRINT_INFO: DefaultTypesInclude.PRINT_INFO,
        PhKeys.QUITE_MODE: DefaultTypesInclude.QUITE_MODE,
        PhKeys.ENCODING: DefaultTypesInclude.ENCODING,
        PhKeys.ENCODING_ERRORS: DefaultTypesInclude.ENCODING_ERRORS,
        PhKeys.ARCHIVE_OUTPUT: DefaultTypesInclude.ARCHIVE_OUTPUT,
        PhKeys.ARCHIVE_OUTPUT_FORMAT: DefaultTypesInclude.ARCHIVE_OUTPUT_FORMAT,
        # Specific Param
        PhKeys.LENGTH_IN_DECIMAL: DefaultTypesInclude.LENGTH_IN_DECIMAL,
        PhKeys.VALUE_IN_ASCII: DefaultTypesInclude.VALUE_IN_ASCII,
        PhKeys.ONE_LINER: DefaultTypesInclude.ONE_LINER,
        PhKeys.NON_TLV_NEIGHBOR: DefaultTypesInclude.NON_TLV_NEIGHBOR,
    }
    data_types_exclude = {
        # Common Param
        PhKeys.INPUT_DATA: PhDefaultTypesExclude.INPUT_DATA,
        # PhKeys.REMARKS: ,
    }

    config_data = PhUtil.dict_to_data(user_dict=config_data, data_types_include=data_types_include,
                                      data_types_exclude=data_types_exclude, trim_data=False)
    # PhUtil.print_iter(config_data, 'config_data initial', verbose=True)
    for k, v in config_data.items():
        if not v:
            continue
        config_data[k] = v
    # PhUtil.print_iter(config_data, 'config_data before cleaning', verbose=True, depth_level=1)
    # PhUtil.print_iter(config_data, 'config_data processed', verbose=True, depth_level=1)
    return config_data


def set_defaults_for_common_objects(data):
    """

    :param data:
    :return:
    """
    # input_data
    data.print_input = PhUtil.set_if_none(data.print_input, Defaults.PRINT_INPUT)
    data.print_output = PhUtil.set_if_none(data.print_output, Defaults.PRINT_OUTPUT)
    data.print_info = PhUtil.set_if_none(data.print_info, Defaults.PRINT_INFO)
    data.quite_mode = PhUtil.set_if_none(data.quite_mode, Defaults.QUITE_MODE)
    # Remarks
    data.encoding = PhUtil.set_if_none(data.encoding, Defaults.ENCODING)
    data.encoding_errors = PhUtil.set_if_none(data.encoding_errors, Defaults.ENCODING_ERRORS)
    data.output_path = PhUtil.set_if_none(data.output_path, Defaults.OUTPUT_PATH)
    data.output_file_name_keyword = PhUtil.set_if_none(data.output_file_name_keyword, Defaults.OUTPUT_FILE_NAME_KEYWORD)
    data.archive_output = PhUtil.set_if_none(data.archive_output, Defaults.ARCHIVE_OUTPUT)
    data.archive_output_format = PhUtil.set_if_none(data.archive_output_format, Defaults.ARCHIVE_OUTPUT_FORMAT)


def set_defaults(data, meta_data):
    """
    Set Default Values if nothing is set
    :param data:
    :param meta_data:
    :return:
    """
    data.length_in_decimal = PhUtil.set_if_none(data.length_in_decimal, Defaults.LENGTH_IN_DECIMAL)
    data.value_in_ascii = PhUtil.set_if_none(data.value_in_ascii, Defaults.VALUE_IN_ASCII)
    data.one_liner = PhUtil.set_if_none(data.one_liner, Defaults.ONE_LINER)
    data.non_tlv_neighbor = PhUtil.set_if_none(data.non_tlv_neighbor, Defaults.NON_TLV_NEIGHBOR)
    if meta_data is None:
        return


def handle_web_request(request_form):
    return Data(**dict_to_data(request_form))


def read_input_file(data, meta_data, info_data):
    try:
        # Text File
        with open(data.input_data, mode='r', encoding=data.encoding, errors=data.encoding_errors) as the_file:
            resp = ''.join(the_file.readlines())
    except UnicodeDecodeError:
        # Binary File/Encoding Error
        with open(data.input_data, 'rb') as the_file:
            resp = the_file.read()
    if not resp:
        raise ValueError(PhExceptionHelper(msg_key=PhConstants.EMPTY_INPUT_FILE))
    return resp


def write_output_file(data, meta_data, info_data, flip_output=False):
    output_file_path = meta_data.output_file_path
    data_to_write = meta_data.parsed_data
    if flip_output is True:
        output_file_path = meta_data.re_output_file_path
        data_to_write = meta_data.re_parsed_data
    data_to_write = PhUtil.set_if_none(data_to_write, PhConstants.STR_EMPTY)
    with open(output_file_path, mode='w', encoding=data.encoding, errors=data.encoding_errors) as file:
        file.writelines(data_to_write)
