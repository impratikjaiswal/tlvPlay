from python_helpers.ph_util import PhUtil


class Test:

    @classmethod
    def test_sample_data(cls):
        PhUtil.print_separator()

    @classmethod
    def test_all_versions(cls):
        PhUtil.print_separator()

    @classmethod
    def test_all(cls):
        cls.test_sample_data()
        cls.test_all_versions()
