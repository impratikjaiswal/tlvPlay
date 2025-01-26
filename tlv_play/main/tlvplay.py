import sys
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes
from python_helpers.ph_time import PhTime
from python_helpers.ph_util import PhUtil

from tlv_play.main.convert.converter import handle_web_request
from tlv_play.main.data_type.data_type_master import DataTypeMaster
from tlv_play.main.data_type.dev import Dev
from tlv_play.main.data_type.known_issues import KnownIssues
from tlv_play.main.data_type.sample import Sample
from tlv_play.main.data_type.unit_testing import UnitTesting
from tlv_play.main.data_type.user_data import UserData
from tlv_play.main.helper.constants_config import ConfigConst
from tlv_play.main.helper.defaults import Defaults
from tlv_play.test.test import Test

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

"""
Global Variables
"""
data_cli = None
execution_mode = None
error_handling_mode = None


def process_data():
    """

    :return:
    """
    global execution_mode, error_handling_mode, data_cli
    data_type_user = [
        #####
        # Empty class for user usage
        ####
        UserData(),
    ]
    data_type_dev = [
        #####
        # class for dev
        #####
        Dev(),
    ]
    data_type_known_issues = [
        #####
        # class for known issues
        #####
        KnownIssues(),
    ]
    data_types_sample_generic = [
        #####
        # Sample With Plenty vivid Examples; Single as well as Bulk
        #####
    ]
    data_types_samples = [
        #####
        # Sample With Plenty vivid Examples; Single as well as Bulk
        #####
        Sample(),
    ]
    data_types_sample_specific = [
    ]
    data_type_unit_testing = [
        #####
        # Unit Testing
        #####
        UnitTesting(),
    ]
    data_type_unit_testing_external = [
        #####
        # Unit Testing External
        #####
        Test(),
    ]

    data_types_pool = {
        PhExecutionModes.USER: data_type_user,
        PhExecutionModes.SAMPLES_LIST: data_types_samples,
        PhExecutionModes.SAMPLE_GENERIC: data_types_sample_generic,
        PhExecutionModes.SAMPLE_SPECIFIC: data_types_sample_specific,
        PhExecutionModes.UNIT_TESTING: data_type_unit_testing,
        PhExecutionModes.UNIT_TESTING_EXTERNAL: data_type_unit_testing_external,
        PhExecutionModes.DEV: data_type_dev,
        PhExecutionModes.KNOWN_ISSUES: data_type_known_issues,
        PhExecutionModes.ALL: data_type_user
                              + data_types_samples
                              + data_types_sample_generic
                              + data_types_sample_specific
                              + data_type_unit_testing
                              + data_type_unit_testing_external
        # + data_type_dev
        # + data_type_known_issues
        ,
    }
    data_types = data_types_pool.get(execution_mode, Defaults.EXECUTION_MODE)
    if data_cli:
        _data_type = DataTypeMaster()
        _data_type.set_data_pool(data_pool=[data_cli])
        data_types = [_data_type]
    for data_type in data_types:
        PhUtil.print_heading(str_heading=f'Data Class: {str(data_type.__class__.__name__)}')
        if isinstance(data_type, UnitTesting):
            error_handling_mode = PhErrorHandlingModes.CONTINUE_ON_ERROR
        if isinstance(data_type, Dev):
            error_handling_mode = PhErrorHandlingModes.STOP_ON_ERROR
        if isinstance(data_type, Test):
            Test.test_all()
            continue
        if isinstance(data_type, Sample):
            # Validate & Print Sample Data For Web
            PhUtil.print_iter(Sample().get_sample_data_pool_for_web(), header='Sample Data')
        if not data_cli:
            data_type.set_print_input()
            data_type.set_print_output()
            data_type.set_print_info()
            data_type.set_quiet_mode()
            data_type.set_remarks()
            data_type.set_encoding()
            data_type.set_encoding_errors()
            data_type.set_output_path()
            data_type.set_output_file_name_keyword()
            data_type.set_archive_output()
            data_type.set_archive_output_format()
            #
            data_type.set_one_liner()
            data_type.set_value_in_ascii()
            data_type.set_length_in_decimal()
            data_type.set_non_tlv_neighbor()
            #
            data_type.set_data_pool()
        DataTypeMaster.process_safe(data_type, error_handling_mode)


def handle_cli_request(**kwargs):
    """

    :param kwargs:
    :return:
    """
    global data_cli
    data_cli = handle_web_request(kwargs)


def print_configurations():
    # Print Versions
    version_parameters_pool = [
        {'tool_name': ConfigConst.TOOL_NAME, 'tool_version': ConfigConst.TOOL_VERSION},
    ]
    PhUtil.print_version(parameters_pool=version_parameters_pool)


def main():
    """

    :return:
    """
    """
    Time Object
    """
    ph_time_obj = PhTime()
    ph_time_obj.start()
    """
    Handle Args
    """
    if len(sys.argv) > 1:
        standalone_mode = False
        # callback is not received for '--help', so handle differently
        if sys.argv[1] == '--help':
            # Print Configurations
            print_configurations()
            standalone_mode = True
        handle_cli_request(standalone_mode=standalone_mode)
    """
    Configurations
    """
    # Do Configurations, as per your Need
    set_configurations()
    # Print Configurations
    print_configurations()
    """
    Process
    """
    process_data()
    """
    Wrap up, All Done
    """
    ph_time_obj.stop()
    ph_time_obj.print()
    PhUtil.print_done()


def set_configurations():
    """

    :return:
    """
    global execution_mode, error_handling_mode
    """
    Set Execution Mode, First time users can try #PhExecutionModes.SAMPLE_GENERIC
    """
    execution_mode = PhExecutionModes.USER
    error_handling_mode = PhErrorHandlingModes.CONTINUE_ON_ERROR


if __name__ == '__main__':
    main()
