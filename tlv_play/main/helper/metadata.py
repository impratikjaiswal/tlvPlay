from collections import OrderedDict


class MetaData:
    def __init__(self, raw_data_org):
        self.raw_data_org = raw_data_org
        self.parsed_data = None
        self.output_dic = OrderedDict()

    def get_info_data(self):
        if self.output_dic:
            info = self.output_dic.get(PhKeys.INFO, None)
            if info is not None:
                return str(info)
        return PhConstants.STR_EMPTY
