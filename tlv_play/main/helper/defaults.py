from python_helpers.ph_defaults import PhDefaults
from python_helpers.ph_modes_error_handling import PhErrorHandlingModes
from python_helpers.ph_modes_execution import PhExecutionModes


class Defaults:
    PRINT_INFO = PhDefaults.PRINT_INFO
    PRINT_INPUT = PhDefaults.PRINT_INPUT
    PRINT_OUTPUT = PhDefaults.PRINT_OUTPUT
    ARCHIVE_OUTPUT = PhDefaults.ARCHIVE_OUTPUT
    QUITE_MODE = PhDefaults.QUITE_MODE
    EXECUTION_MODE = PhExecutionModes.USER
    ERROR_HANDLING_MODE = PhErrorHandlingModes.CONTINUE_ON_ERROR
    ENCODING = PhDefaults.CHAR_ENCODING
    ENCODING_ERRORS = PhDefaults.ENCODING_ERRORS
    ARCHIVE_OUTPUT_FORMAT = PhDefaults.ARCHIVE_OUTPUT_FORMAT
    #
    LENGTH_IN_DECIMAL = False
    VALUE_IN_ASCII = False
    ONE_LINER = True
    NON_TLV_NEIGHBOR = True
