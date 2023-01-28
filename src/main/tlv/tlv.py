class Tlv:
    def __init__(self, tag_list=None, len_list=None, value_list=None, len_dec=0, level=0):
        if tag_list is None:
            tag_list = []
        if len_list is None:
            len_list = []
        if value_list is None:
            value_list = []
        self.tag_list = tag_list
        self.len_list = len_list
        self.value_list = value_list
        self.len_dec = len_dec
        self.level = level

    def __repr__(self):
        return f'TLV(tag_list={self.tag_list}, len_list={self.len_list}, value_list={self.value_list}, len_dec= {self.len_dec},level= {self.level}'

    def __eq__(self, other):
        result = False
        if isinstance(other, Tlv):
            result = self.tag_list == other.tag_list \
                     and self.len_list == other.len_list \
                     and self.len_dec == other.len_dec \
                     and self.level == other.level
            if result:
                # TODO: Nested Objects / list is not supported
                result = self.value_list == other.value_list
        return result
