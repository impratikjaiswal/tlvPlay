from python_helpers.ph_defaults import PhDefaults, PhDefaultTypesInclude, PhDefaultTypesExclude
from python_helpers.ph_file_extensions import PhFileExtensions


class Defaults:
    #############
    # Generic Objects
    #############
    EXECUTION_MODE = PhDefaults.EXECUTION_MODE
    ERROR_HANDLING_MODE = PhDefaults.ERROR_HANDLING_MODE
    OUTPUT_FILE_EXT = PhFileExtensions.TXT
    #############
    # Data Objects
    #############
    # Common Objects
    # INPUT_DATA
    PRINT_INPUT = PhDefaults.PRINT_INPUT
    PRINT_OUTPUT = PhDefaults.PRINT_OUTPUT
    PRINT_INFO = PhDefaults.PRINT_INFO
    QUITE_MODE = PhDefaults.QUITE_MODE
    # REMARKS
    ENCODING = PhDefaults.CHAR_ENCODING
    ENCODING_ERRORS = PhDefaults.ENCODING_ERRORS
    OUTPUT_PATH = PhDefaults.OUTPUT_PATH
    OUTPUT_FILE_NAME_KEYWORD = PhDefaults.OUTPUT_FILE_NAME_KEYWORD
    ARCHIVE_OUTPUT = PhDefaults.ARCHIVE_OUTPUT
    ARCHIVE_OUTPUT_FORMAT = PhDefaults.ARCHIVE_OUTPUT_FORMAT
    # Specific Objects
    LENGTH_IN_DECIMAL = False
    VALUE_IN_ASCII = False
    ONE_LINER = True
    NON_TLV_NEIGHBOR = True


class DefaultTypesInclude:
    # Common Objects
    # INPUT_DATA
    PRINT_INPUT = PhDefaultTypesInclude.PRINT_INPUT
    PRINT_OUTPUT = PhDefaultTypesInclude.PRINT_OUTPUT
    PRINT_INFO = PhDefaultTypesInclude.PRINT_INFO
    QUITE_MODE = PhDefaultTypesInclude.QUITE_MODE
    # REMARKS
    ENCODING = PhDefaultTypesInclude.ENCODING
    ENCODING_ERRORS = PhDefaultTypesInclude.ENCODING_ERRORS
    OUTPUT_PATH = PhDefaultTypesInclude.OUTPUT_PATH
    ARCHIVE_OUTPUT = PhDefaultTypesInclude.ARCHIVE_OUTPUT
    ARCHIVE_OUTPUT_FORMAT = PhDefaultTypesInclude.ARCHIVE_OUTPUT_FORMAT
    # Specific Objects
    LENGTH_IN_DECIMAL = bool
    VALUE_IN_ASCII = bool
    ONE_LINER = bool
    NON_TLV_NEIGHBOR = bool


class DefaultTypesExclude:
    # Common Objects
    INPUT_DATA: PhDefaultTypesExclude.INPUT_DATA
