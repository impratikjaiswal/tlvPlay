from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil


class TestData:
    dynamic_data = {
        'user':
            {
                PhKeys.VAR_EXECUTION_MODE: 'USER',
            },
        'sample_list':
            {
                PhKeys.VAR_EXECUTION_MODE: 'SAMPLES_LIST',
            },
        'dev':
            {
                PhKeys.VAR_EXECUTION_MODE: 'DEV',
            },
        'unit_testing_external':
            {
                PhKeys.VAR_EXECUTION_MODE: 'UNIT_TESTING_EXTERNAL',
            },
        'all':
            {
                PhKeys.VAR_EXECUTION_MODE: 'ALL',
            },
    }

    default_data = {
        PhKeys.VAR_EXECUTION_MODE: 'ALL',
        PhKeys.VAR_ERROR_HANDLING_MODE: 'CONTINUE_ON_ERROR',
        PhKeys.VAR_TOP_FOLDER_PATH: '[]',
    }

    @classmethod
    def get_test_data(cls, key):
        dynamic_data = cls.dynamic_data.get(key, PhConstants.DICT_EMPTY)
        for temp_key in cls.default_data:
            if temp_key not in dynamic_data:
                dynamic_data[temp_key] = cls.default_data[temp_key]
        static_data = {
            PhKeys.TEST_CASE_ID: key,
            PhKeys.TEST_CASE_NAME: key,
            PhKeys.TEST_CASE_FILE_NAME: f'{key}.log'
        }
        return PhUtil.dict_merge(static_data, dynamic_data)
