from tlv_play import _defaults
from tlv_play._tool_name import TOOL_NAME, TOOL_TITLE, TOOL_SW_PACKAGE_NAME, TOOL_TEST_PACKAGE_NAME, TOOL_SW_MODULE_NAME

_run_time_incremental = False
_run_time_play_helpers = False
try:
    from tlv_play._version import __version__

    # incremental module is available post installation, run time only,
    _run_time_incremental = True
except ImportError:
    pass
try:
    from play_helpers.ph_defaults import PhDefaults
    from tlv_play._git_info import GIT_SUMMARY

    # play_helpers module is available post installation, run time only,
    _run_time_play_helpers = True
except ImportError:
    pass


class ConfigConst:
    TOOL_VERSION = __version__.public() if _run_time_incremental else (
        PhDefaults.VERSION if _run_time_play_helpers else _defaults.VERSION)
    TOOL_VERSION_DETAILED = f'v{TOOL_VERSION}'
    TOOL_NAME = TOOL_NAME
    TOOL_TITLE = TOOL_TITLE
    TOOL_SW_PACKAGE_NAME = TOOL_SW_PACKAGE_NAME
    TOOL_TEST_PACKAGE_NAME = TOOL_TEST_PACKAGE_NAME
    TOOL_SW_MODULE_NAME = TOOL_SW_MODULE_NAME
    TOOL_GIT_SUMMARY = GIT_SUMMARY if _run_time_play_helpers else _defaults.GIT_SUMMARY
    TOOL_DESCRIPTION = f'Generic TLV Parser based on TLV and related standards. Can parse any Simple or BER TLV upto *nth Level* automatically. Multi byte Tag, Multi byte Length are also Supported.'
    TOOL_META_DESCRIPTION = f'{TOOL_DESCRIPTION}'
    TOOL_META_KEYWORDS = f'{TOOL_TITLE}, TLV, Tag Length Value, Type Length Value, length value, tlv encoder, tlv decoder, tlv parser, multi byte tag, multi byte length, simple tlv, ber tlv, tlv utilities'
    TOOL_URL = 'https://github.com/impratikjaiswal/tlvPlay'
    TOOL_URL_BUG_TRACKER = 'https://github.com/impratikjaiswal/tlvPlay/issues'
