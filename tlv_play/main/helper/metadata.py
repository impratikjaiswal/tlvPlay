from collections import OrderedDict

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys
from python_helpers.ph_util import PhUtil


class MetaData:
    def __init__(self, input_data_org):
        self.input_data_org = input_data_org
        self.transaction_id = PhUtil.generate_transaction_id()
        self.parsed_data = None
        self.output_dic = OrderedDict()

    def get_info_data(self):
        if self.output_dic:
            info = self.output_dic.get(PhKeys.INFO, None)
            if info is not None:
                return str(info)
        return PhConstants.STR_EMPTY

    def get_parsed_data(self):
        return self.parsed_data
