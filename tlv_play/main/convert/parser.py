import copy
import os

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil

from tlv_play.main.convert import converter
from tlv_play.main.convert.handler import process_data
from tlv_play.main.helper.infodata import InfoData
from tlv_play.main.helper.metadata import MetaData


def process_all_data_types(data, meta_data=None, info_data=None):
    """

    :param info_data:
    :param meta_data:
    :param data:
    :return:
    """
    """
    Bulk Data Handling (Recursive)
    """
    converter.set_defaults_for_common_objects(data)
    if meta_data is None:
        meta_data = MetaData(input_data_org=data.input_data)
    if info_data is None:
        info_data = InfoData()
    multiple_inputs = False
    if isinstance(data.input_data, list):
        # List is provided
        multiple_inputs = True
        meta_data.input_mode_key = PhKeys.INPUT_LIST
    if isinstance(data.input_data, tuple):
        # CUI (Click) Multi is a tuple
        multiple_inputs = True
        meta_data.input_mode_key = PhKeys.INPUT_TUPLE
    if multiple_inputs:
        data.append_input_modes_hierarchy(meta_data.input_mode_key)
        data.set_auto_generated_remarks_if_needed()
        data.set_one_time_remarks(f'({len(data.input_data)} Elements)')
        PhUtil.print_heading(data.get_remarks_as_str(), heading_level=3)
        converter.print_data(data, meta_data)
        parsed_data_list = []
        actual_remarks_length = len(data.remarks)
        current_remarks = PhUtil.extend_list(data.remarks, expected_length=len(data.input_data))
        for index, input_data_item in enumerate(data.input_data, start=1):
            sub_data = copy.deepcopy(data)
            sub_data.input_data = input_data_item
            sub_data.reset_auto_generated_remarks()
            sub_data.set_extended_remarks_available(False if index <= actual_remarks_length else True)
            sub_data.set_user_remarks(current_remarks[index - 1])
            sub_data.set_auto_generated_remarks_if_needed(PhUtil.get_key_value_pair(key='item', value=index,
                                                                                    sep=PhConstants.SEPERATOR_TWO_WORDS,
                                                                                    dic_format=False))
            parsed_data_list.append(process_all_data_types(sub_data))
        return parsed_data_list
    if data.input_data and os.path.isdir(os.path.abspath(data.input_data)):
        # directory is provided
        meta_data.input_mode_key = PhKeys.INPUT_DIR
        data.append_input_modes_hierarchy(meta_data.input_mode_key)
        PhUtil.print_heading(data.get_remarks_as_str(), heading_level=3)
        converter.set_defaults(data, meta_data)
        converter.print_data(data, meta_data)
        converter.set_includes_excludes_files(data, meta_data)
        files_list = PhUtil.traverse_it(top=os.path.abspath(data.input_data), traverse_mode='Regex',
                                        include_files=meta_data.include_files, excludes=meta_data.excludes)
        if files_list:
            files_list_data = data
            files_list_data.input_data = files_list
            return process_all_data_types(files_list_data)
    """
    Individual File Handling
    """
    file_dic_all_str = {}
    data.set_auto_generated_remarks_if_needed()
    PhUtil.print_heading(data.get_remarks_as_str(), heading_level=2)
    if data.input_data and os.path.isfile(data.input_data):
        # file is provided
        resp = converter.read_input_file(data=data, meta_data=meta_data, info_data=info_data)
        # Treat all Files Equally; including YML
        meta_data.input_mode_key = PhKeys.INPUT_FILE
        meta_data.input_file_path = data.input_data
        # converter.set_input_output_format(data)
        data.input_data = resp
        data.append_input_modes_hierarchy(meta_data.input_mode_key)
    """
    Individual Data Handling
    """
    # Needed for a scenario when remarks will be fetched from YML
    data.set_auto_generated_remarks_if_needed()
    converter.set_defaults(data, meta_data)
    """
    Data Processing
    """
    process_data(data=data, meta_data=meta_data, info_data=info_data)
    converter.print_data(data=data, meta_data=meta_data, info_data=info_data)
    if meta_data.output_file_path:
        PhUtil.make_dirs(file_path=meta_data.output_file_path)
        converter.write_output_file(data=data, meta_data=meta_data, info_data=info_data)
    return meta_data.parsed_data
