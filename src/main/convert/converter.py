from src.main.helper.defaults import Defaults


def set_defaults(data):
    """
    Set Default Values if nothing is set
    :param data:
    :return:
    """
    if data.length_in_decimal is None:
        data.length_in_decimal = Defaults.LENGTH_IN_DECIMAL
    if data.value_in_ascii is None:
        data.value_in_ascii = Defaults.VALUE_IN_ASCII
    if data.one_liner is None:
        data.one_liner = Defaults.ONE_LINER
