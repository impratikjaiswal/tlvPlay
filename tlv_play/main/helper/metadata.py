from collections import OrderedDict

from python_helpers.ph_constants import PhConstants
from python_helpers.ph_keys import PhKeys


class MetaData:
    def __init__(self, input_data_org):
        self.input_data_org = input_data_org
        self.parsed_data = None
        self.output_dic = OrderedDict()

    def get_info_data(self):
        if self.output_dic:
            info = self.output_dic.get(PhKeys.INFO, None)
            if info is not None:
                return str(info)
        return PhConstants.STR_EMPTY
