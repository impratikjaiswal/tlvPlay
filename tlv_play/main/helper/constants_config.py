# from tlv_play._git_info import GIT_SUMMARY
from tlv_play._tool_name import TOOL_NAME, TOOL_TITLE, TOOL_PACKAGE_NAME, TOOL_TEST_PACKAGE_NAME

_run_time = False
try:
    from tlv_play._version import __version__

    # this is available post installation, run time only,
    _run_time = True
except ImportError:
    pass


class ConfigConst:
    # TODO:
    TOOL_VERSION = __version__.public() if _run_time else '1.0.0' #PhDefaults.VERSION
    TOOL_VERSION_DETAILED = f'v{TOOL_VERSION}'
    TOOL_NAME = TOOL_NAME
    TOOL_TITLE = TOOL_TITLE
    TOOL_PACKAGE_NAME = TOOL_PACKAGE_NAME
    TOOL_TEST_PACKAGE_NAME = TOOL_TEST_PACKAGE_NAME
    # TODO:
    # TOOL_GIT_SUMMARY = GIT_SUMMARY
    TOOL_GIT_SUMMARY = ''
    TOOL_DESCRIPTION = f'Generic TLV Parser based on TLV and related standards. Can parse any Simple or BER TLV upto *nth Level* automatically. Multi byte Tag, Multi byte Length are also Supported.'
    TOOL_META_DESCRIPTION = f'{TOOL_DESCRIPTION}'
    TOOL_META_KEYWORDS = f'{TOOL_TITLE}, TLV, Tag Length Value, Type Length Value, length value, tlv encoder, tlv decoder, tlv parser, multi byte tag, multi byte length, simple tlv, ber tlv, tlv utilities'
    TOOL_URL = 'https://github.com/impratikjaiswal/tlvPlay'
    TOOL_URL_BUG_TRACKER = 'https://github.com/impratikjaiswal/tlvPlay/issues'
