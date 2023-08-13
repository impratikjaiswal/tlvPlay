from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes
from python_helpers.ph_util import PhUtil

from tlv_play.main.data_type.any_data import AnyData
from tlv_play.main.data_type.data_type_master import DataTypeMaster
from tlv_play.main.data_type.dev import Dev
from tlv_play.main.data_type.unit_testing import UnitTesting
from tlv_play.main.data_type.user_data import UserData
from tlv_play.main.helper.constants_config import ConfigConst
from tlv_play.main.helper.defaults import Defaults


def process_data(execution_mode, error_handling_mode):
    """

    :param error_handling_mode:
    :param execution_mode:
    :return:
    """
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
        AnyData(),
    ]
    data_type_unit_testing = [
        #####
        # Unit Testing
        #####
        UnitTesting(),
    ]
    data_types_pool = {
        PhExecutionModes.USER: data_type_user,
        PhExecutionModes.DEV: data_type_dev,
        PhExecutionModes.SAMPLE_GENERIC: data_types_sample_generic,
        PhExecutionModes.UNIT_TESTING: data_type_unit_testing,
        PhExecutionModes.ALL: data_types_sample_generic + data_type_unit_testing,
    }
    data_types = data_types_pool.get(execution_mode, Defaults.EXECUTION_MODE)
    for data_type in data_types:
        PhUtil.print_heading(str_heading=str(data_type.__class__.__name__))
        data_type.set_one_liner()
        data_type.set_value_in_ascii()
        data_type.set_length_in_decimal()
        data_type.set_remarks_list()
        data_type.set_data_pool()
        if isinstance(data_type, UnitTesting):
            error_handling_mode = PhErrorHandlingModes.CONTINUE_ON_ERROR
        if isinstance(data_type, Dev):
            error_handling_mode = PhErrorHandlingModes.STOP_ON_ERROR
        DataTypeMaster.parse(data_type, error_handling_mode)


def main():
    """

    :return:
    """
    """
    Set Execution Mode, If you are a first time user then try #ExecutionModes.SAMPLE_GENERIC
    """
    execution_mode = PhExecutionModes.USER
    error_handling_mode = PhErrorHandlingModes.CONTINUE_ON_ERROR
    # Print Versions
    PhUtil.print_version(ConfigConst.TOOL_NAME, ConfigConst.TOOL_VERSION)
    # Process Data
    process_data(execution_mode, error_handling_mode)
    PhUtil.print_done()


if __name__ == '__main__':
    main()
