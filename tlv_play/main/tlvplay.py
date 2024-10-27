from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes
from python_helpers.ph_time import PhTime
from python_helpers.ph_util import PhUtil

from tlv_play.main.data_type.data_type_master import DataTypeMaster
from tlv_play.main.data_type.dev import Dev
from tlv_play.main.data_type.sample import Sample
from tlv_play.main.data_type.unit_testing import UnitTesting
from tlv_play.main.data_type.user_data import UserData
from tlv_play.main.helper.constants_config import ConfigConst
from tlv_play.main.helper.defaults import Defaults
from tlv_play.test.test import Test

"""
Global Variables
"""
execution_mode = None
error_handling_mode = None


def process_data():
    """

    :return:
    """
    global execution_mode, error_handling_mode
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
    data_types_sample_generic = [
        #####
        # Sample With Plenty vivid Examples
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
        PhExecutionModes.DEV: data_type_dev,
        PhExecutionModes.SAMPLE_GENERIC: data_types_sample_generic,
        PhExecutionModes.SAMPLES_LIST: data_types_samples,
        PhExecutionModes.SAMPLE_SPECIFIC: data_types_sample_specific,
        PhExecutionModes.UNIT_TESTING: data_type_unit_testing,
        PhExecutionModes.UNIT_TESTING_EXTERNAL: data_type_unit_testing_external,
        PhExecutionModes.ALL: data_types_sample_generic + data_types_sample_specific + data_type_unit_testing + data_type_user,
    }
    data_types = data_types_pool.get(execution_mode, Defaults.EXECUTION_MODE)
    for data_type in data_types:
        PhUtil.print_heading(str_heading=str(data_type.__class__.__name__))
        # if isinstance(data_type, UnitTesting):
        #     error_handling_mode = PhErrorHandlingModes.CONTINUE_ON_ERROR
        # if isinstance(data_type, Dev):
        #     error_handling_mode = PhErrorHandlingModes.STOP_ON_ERROR
        if isinstance(data_type, Test):
            Test.test_all()
            continue
        if isinstance(data_type, Sample):
            # Validate & Print Sample Data For Web
            PhUtil.print_iter(Sample().get_sample_data_pool_for_web(), header='Sample Data')
        data_type.set_print_input()
        data_type.set_print_output()
        data_type.set_print_info()
        data_type.set_quiet_mode()
        data_type.set_remarks()
        data_type.set_one_liner()
        data_type.set_value_in_ascii()
        data_type.set_length_in_decimal()
        data_type.set_data_pool()
        DataTypeMaster.process_safe(data_type, error_handling_mode)


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


def print_configurations():
    # Print Versions
    PhUtil.print_version(ConfigConst.TOOL_NAME, ConfigConst.TOOL_VERSION)


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


if __name__ == '__main__':
    main()
