import os


class Folders:
    top_folder_path = [os.pardir, os.pardir]

    DIR_DATA = 1

    DIR_USER_DATA = 2
    DIR_USER_DATA_GENERIC = 24

    DIR_SAMPLE_DATA = 3
    DIR_SAMPLE_DATA_GENERIC = 34

    LOCATIONS_MAPPING = {
        #
        DIR_DATA: ['Data'],
        #
        DIR_SAMPLE_DATA: ['Data', 'SampleData'],
        DIR_SAMPLE_DATA_GENERIC: ['Data', 'SampleData', 'Generic'],
        #
        DIR_USER_DATA: ['Data', 'UserData'],
        DIR_USER_DATA_GENERIC: ['Data', 'UserData', 'Generic'],
        #
    }

    @classmethod
    def in_sample(cls, relative_path=''):
        return cls.get_path(Folders.DIR_SAMPLE_DATA, relative_path)

    @classmethod
    def in_sample_gen(cls, relative_path=''):
        return cls.get_path(Folders.DIR_SAMPLE_DATA_GENERIC, relative_path)

    @classmethod
    def in_user(cls, relative_path=''):
        return cls.get_path(Folders.DIR_USER_DATA, relative_path)

    @classmethod
    def in_user_gen(cls, relative_path=''):
        return cls.get_path(Folders.DIR_USER_DATA_GENERIC, relative_path)

    @classmethod
    def get_path(cls, folder_name, relative_path):
        if folder_name not in cls.LOCATIONS_MAPPING:
            raise ValueError('Unknown folder name')
        return os.sep.join(filter(None,
                                  Folders.top_folder_path +
                                  cls.LOCATIONS_MAPPING.get(folder_name) +
                                  [relative_path]
                                  ))
