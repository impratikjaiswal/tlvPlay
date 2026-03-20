#!/bin/bash
# =============================================================================
# manage.sh — Unified management script
# version: 1.1
#
# Usage:
#   ./manage.sh <command> [options]
#
# Commands:
#   e, env [type]                             Manage virtual environment (default: activate)
#                                                 types: activate | deactivate
#   i, ins, install [type]                    Install required dependencies (default: all)
#                                                 types: all | internal_lib | internal_tool | external | build | cicd | experimental
#   un, rm, uninstall [type]                  Uninstall required dependencies (default: internal_lib)
#                                                 types: all | internal_lib | internal_tool | external | build | cicd | experimental | name
#   u, up, upgrade [type]                     Upgrade required dependencies (default: internal_lib)
#                                                 types: all | internal_lib | internal_tool | external | build | cicd | experimental | pip
#   l, ls, list [type]                        List & freeze installed dependencies (default: env)
#                                                 types: env | system
#   li, st, lint [type]                       Run lint checks (default: error)
#                                                 types: error | warning
#   t, test, tests, ut, unit-tests [type]     Run unit tests (default: full)
#                                                 types: full | unit | package
#   v, ver, version [type]                    Manage project version (default: patch)
#                                                 types: set | create | dev | patch | default
#   h, -h, --help, help                       Show this help message
#
# Aliases:
#   types: act, deact, all, lib, tool, ext, build, cicd, exp, env, sys, full, unit, pkg
#
# =============================================================================

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT_DIR="${SCRIPT_DIR}/.."
LOGS_DIR="${SCRIPT_DIR}/logs"

_lc() {
    # macOS default bash (3.x) does not support ${var,,}
    printf '%s' "$1" | tr '[:upper:]' '[:lower:]'
}

_load_venv_vars() {
    # Read the first line of the config file into a variable
    vir_env_path=$(head -n 1 "${SCRIPT_DIR}/config_vir_env.ini")
    # Extract the base directory name
    vir_env_name=$(basename "$vir_env_path")

    # Debugging
    # echo "Virtual Environment Path: $vir_env_path"
    # echo "Virtual Environment Name: $vir_env_name"
}

_fetch_python_version() {
    python_bin="$(command -v python3 || command -v python)"
    python_version="$("$python_bin" -c 'import sys; print(sys.version.split()[0])')"
}

_fetch_os_type() {
    local uname_out
    uname_out="$(uname -s 2>/dev/null || echo unknown)"
    os_type="unknown"

    case "$uname_out" in
      Darwin)
        os_type="macos"
        ;;
      Linux)
        if grep -qiE "(microsoft|wsl)" /proc/version 2>/dev/null; then
          os_type="wsl"
        else
          os_type="linux"
        fi
        ;;
      CYGWIN*|MINGW*|MSYS*)
        os_type="windows"
        ;;
      *)
        os_type="unknown"
        ;;
    esac
}

_activate() {
    echo "Attempting to activate existing Virtual Environment"
    _load_venv_vars

    source "$vir_env_path/bin/activate"
    _fetch_python_version

    echo ""
    echo "Python Version"
    "$python_bin" --version

    echo ""
    echo "Python Location"
    which "$python_bin"

    if [ ! -d "${LOGS_DIR}" ]; then
        mkdir -p "${LOGS_DIR}"
        echo "${LOGS_DIR} Directory created successfully."
    fi

    echo ""
}

_deactivate() {
    echo "Attempting to deactivate existing (and activated) Virtual Environment"
    deactivate
}

_version_specific() {
    # $1 = flag (--dev | --patch | --newversion | --create)
    # $2 = description message
    # $3 = version value (optional, used with --newversion)

    _activate

    local flag="$1"
    local desc="$2"
    local value="$3"
    local package_name

    package_name=$(cat "${ROOT_DIR}/package_name.txt")
    local package_path="${ROOT_DIR}/${package_name}"
    
    # Sample: python -m incremental.update --path=../play_helpers play_helpers --dev
    # Sample: python -m incremental.update --path=../play_helpers play_helpers --patch
    # REM Sample: python -m incremental.update --path=.\..\play_helpers play_helpers --dev
    # REM Sample: python -m incremental.update --path=.\..\play_helpers play_helpers --patch

    local cmd_data=""$python_bin" -m incremental.update --path=$package_path $package_name $flag $value"

    # Debugging
#    echo flag: "$flag"
#    echo desc: "$desc"
#    echo value: "$value"
#    echo package_name: "$package_name"
#    echo package_path: "$package_path"
#    echo cmd_data: "$cmd_data"

    echo "$desc"
    # $cmd_data "$1""$3"
    $cmd_data
    _deactivate
}

# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

cmd_env() {
    local type="${1:-activate}"
    case "$(_lc "$type")" in
        a|act) type="activate" ;;
        d|deact) type="deactivate" ;;
    esac

    case "$type" in
        activate)   _activate ;;
        deactivate) _deactivate ;;
        *)
            echo "ERROR: Unknown env type '$type'"
            echo "Valid types: activate | deactivate"
            exit 1
            ;;
    esac
}

cmd_install() {
    local type="${1:-all}"
    case "$(_lc "$type")" in
        a) type="all" ;;
        i|int|lib) type="internal_lib" ;;
        it|tool) type="internal_tool" ;;
        e|ext) type="external" ;;
        b) type="build" ;;
        c|ci) type="cicd" ;;
        x|exp) type="experimental" ;;
    esac

    _activate
    case "$type" in
        all)
            echo "Installing all requirements"
            pip install -r "${ROOT_DIR}/requirements.txt"
            ;;
        internal_lib)
            echo "Installing internal lib requirements"
            pip install -r "${ROOT_DIR}/requirements_internal_lib.txt"
            ;;
        internal_tool)
            echo "Installing internal tool requirements"
            pip install -r "${ROOT_DIR}/requirements_internal_tool.txt"
            ;;
        external)
            echo "Installing external requirements"
            pip install -r "${ROOT_DIR}/requirements_external.txt"
            ;;
        build)
            echo "Installing build requirements"
            pip install -r "${ROOT_DIR}/requirements_build.txt"
            ;;
        cicd)
            echo "Installing CI CD requirements"
            pip install -r "${ROOT_DIR}/requirements_cicd.txt"
            ;;
        experimental)
            echo "Installing experimental requirements"
            pip install -r "${ROOT_DIR}/requirements_experimental.txt"
            ;;
        *)
            echo "ERROR: Unknown install type '$type'"
            echo "Valid types: all | internal_lib | internal_tool | external | build | cicd | experimental"
            _deactivate; exit 1
            ;;
    esac
    _deactivate
}

cmd_uninstall() {
    local type="${1:-internal_lib}"
    case "$(_lc "$type")" in
        a) type="all" ;;
        i|int|lib) type="internal_lib" ;;
        it|tool) type="internal_tool" ;;
        e|ext) type="external" ;;
        b) type="build" ;;
        c|ci) type="cicd" ;;
        x|exp) type="experimental" ;;
        n|name) type="name" ;;
    esac

    _activate
    case "$type" in
        all)
            echo "UnInstalling all requirements"
            pip uninstall -r "${ROOT_DIR}/requirements.txt" -y
            ;;
        internal_lib)
            echo "UnInstalling internal lib requirements"
            pip uninstall -r "${ROOT_DIR}/requirements_internal_lib.txt" -y
            ;;
        internal_tool)
            echo "UnInstalling internal tool requirements"
            pip uninstall -r "${ROOT_DIR}/requirements_internal_tool.txt" -y
            ;;
        external)
            echo "UnInstalling external requirements"
            pip uninstall -r "${ROOT_DIR}/requirements_external.txt" -y
            ;;
        build)
            echo "UnInstalling build requirements"
            pip uninstall -r "${ROOT_DIR}/requirements_build.txt" -y
            ;;
        cicd)
            echo "UnInstalling CI CD requirements"
            pip uninstall -r "${ROOT_DIR}/requirements_cicd.txt" -y
            ;;
        experimental)
            echo "UnInstalling experimental requirements"
            pip uninstall -r "${ROOT_DIR}/requirements_experimental.txt" -y
            ;;
        name)
            echo "UnInstalling requirements by name"
            pip uninstall -r "${ROOT_DIR}/requirements_name.txt" -y
            ;;
        *)
            echo "ERROR: Unknown uninstall type '$type'"
            echo "Valid types: all | internal_lib | internal_tool | external | build | cicd | experimental | name"
            _deactivate; exit 1
            ;;
    esac
    _deactivate
}

cmd_upgrade() {
    local type="${1:-internal_lib}"
    case "$(_lc "$type")" in
        a) type="all" ;;
        i|int|lib) type="internal_lib" ;;
        it|tool) type="internal_tool" ;;
        e|ext) type="external" ;;
        b) type="build" ;;
        c|ci) type="cicd" ;;
        x|exp) type="experimental" ;;
        p) type="pip" ;;
    esac

    _activate
    case "$type" in
        all)
            echo "Upgrading all requirements"
            "$python_bin" -m pip install --upgrade pip
            pip install -r "${ROOT_DIR}/requirements.txt" --upgrade
            ;;
        internal_lib)
            echo "Upgrading internal lib requirements"
            pip install -r "${ROOT_DIR}/requirements_internal_lib.txt" --upgrade
            ;;
        internal_tool)
            echo "Upgrading internal tool requirements"
            pip install -r "${ROOT_DIR}/requirements_internal_tool.txt" --upgrade
            ;;
        external)
            echo "Upgrading external requirements"
            pip install -r "${ROOT_DIR}/requirements_external.txt" --upgrade
            ;;
        build)
            echo "Upgrading build requirements"
            pip install -r "${ROOT_DIR}/requirements_build.txt" --upgrade
            ;;
        cicd)
            echo "Upgrading CI CD requirements"
            pip install -r "${ROOT_DIR}/requirements_cicd.txt" --upgrade
            ;;
        experimental)
            echo "Upgrading experimental requirements"
            pip install -r "${ROOT_DIR}/requirements_experimental.txt" --upgrade
            ;;
        pip)
            "$python_bin" -m pip install --upgrade pip
            ;;
        *)
            echo "ERROR: Unknown upgrade type '$type'"
            echo "Valid types: all | internal_lib | internal_tool | external | build | cicd | experimental | pip"
            _deactivate; exit 1
            ;;
    esac
    _deactivate
}

cmd_list() {
    local type="${1:-env}"
    case "$(_lc "$type")" in
        e) type="env" ;;
        s|sys) type="system" ;;
    esac

    _load_venv_vars

    if [[ "$type" == "env" ]]; then
        _activate
        local env_name=${vir_env_name}
    else
        local env_name=""
        _fetch_python_version
    fi

    _fetch_os_type

    local export_list_path="${LOGS_DIR}/requirements_list_${type}_${env_name}_${python_version}_${os_type}.log"
    local export_freeze_path="${LOGS_DIR}/requirements_freeze_${type}_${env_name}_${python_version}_${os_type}.log"

    echo "Listing requirements"
    pip list

    echo "Listing requirements to $export_list_path"
    pip list > "$export_list_path"

    echo "Freezing requirements to $export_freeze_path"
    pip freeze > "$export_freeze_path"


    if [[ "$type" == "env" ]]; then
        _deactivate
    fi
}

cmd_lint() {
    local type="${1:-error}"
    shift || true

    case "$(_lc "$type")" in
        e|err) type="error" ;;
        w|wa|warn) type="warning" ;;
    esac

    _activate
    _fetch_python_version
    _fetch_os_type

    local export_lint_error_path="${LOGS_DIR}/lint_${type}_${python_version}_${os_type}.log"
    local export_lint_warn_path="${LOGS_DIR}/lint_${type}_${python_version}_${os_type}.log"

    case "$type" in
        error)
            echo "Exporting Errors to $export_lint_error_path"
            echo "Error Count is: "
            # Check for Python syntax errors or undefined names
            flake8 "${ROOT_DIR}" --tee --exit-zero --select=E9,F63,F7,F82 --output-file="${export_lint_error_path}"
            ;;
        warning)
            echo "Exporting Warnings to $export_lint_warn_path"
            echo "Warning Count is: "
            # Check for other types of warnings.
            flake8 "${ROOT_DIR}" --tee --exit-zero --max-complexity=10 --output-file="${export_lint_error_path}"
            ;;
        *)
            echo "ERROR: Unknown lint type '$type'"
            echo "Valid types: error | warning"
            exit 1
            ;;
    esac

    _deactivate
}

cmd_unit_tests() {
    local type="${1:-full}"
    shift || true

    case "$(_lc "$type")" in
        f|all) type="full" ;;
        u) type="unit" ;;
        p|pkg) type="package" ;;
    esac

    case "$type" in
        full)
            _activate
            local export_path="${LOGS_DIR}/run_tests_${vir_env_name}.log"
            echo "Export Path: $export_path"
            echo "Starting App"
            cd "${SCRIPT_DIR}/.."
            "$python_bin" -u -m play_helpers.test.test > "$export_path" 2>&1
            cd "${SCRIPT_DIR}"
            _deactivate
            ;;
        unit)
            _activate
            echo "Starting App"
            cd "${SCRIPT_DIR}/.."
            # "$python_bin" -m unittest discover -s play_helpers/test
            "$python_bin" -m unittest play_helpers/test/test_util.py
            cd "${SCRIPT_DIR}"
            _deactivate
            ;;
        package)
            local env_list=("../venv_39" "../venv_314")
            local ini_file="${SCRIPT_DIR}/config_vir_env_default.ini"
            echo "Starting the loop..."
            for current_env in "${env_list[@]}"; do
                echo "current_env: $current_env"
                echo "path=$current_env" > "$ini_file"
                bash "${SCRIPT_DIR}/manage.sh" list
                bash "${SCRIPT_DIR}/manage.sh" run-tests full
                echo "-----------------"
            done
            echo "Ending the loop..."
            ;;
        *)
            echo "ERROR: Unknown run-tests type '$type'"
            echo "Valid types: full | unit | package"
            exit 1
            ;;
    esac
}

cmd_version() {
    local type="${1:-patch}"
    shift || true

    local default_version="1.0.0"

    case "$(_lc "$type")" in
        s) type="set" ;;
        c|init|f|first) type="create" ;;
        d) type="dev" ;;
        p) type="patch" ;;
        def) type="default" ;;
    esac

    case "$type" in
        set)
            read -p "Please Enter Project Version: " versionValue

            # Add quotes if not present
            # TODO: Quotes are really needed ?
            if [[ "$versionValue" != \"*\" ]]; then
                versionValue="\"$versionValue\""
            fi
            _version_specific --newversion "Setting Specific Version" "$versionValue"
            ;;
        create)
            # if the file was present previously and got deleted now, it will be recreated with same version as before
            # TODO: Need to see the use case when file was not present before, if default version is not set, explicit default version may need to set
            _version_specific --create "Creating Version File"
 #           _version_specific --newversion "Setting Default Version" "$default_version"
            ;;
        dev)
            _version_specific --dev "Setting Dev Version (Should be used for Internal versions only)"
            ;;
        patch)
            _version_specific --patch "Setting Patch Version (Should be used for Public versions only)"
            ;;
        default)
            _version_specific --newversion "Setting Default Version" "$default_version"
            ;;
        *)
            echo "ERROR: Unknown version type '$type'"
            echo "Valid types: set | create | dev | patch | default"
            exit 1
            ;;
    esac
}

cmd_help() {
    tail -n +2 "$0" | while IFS= read -r line; do
        [[ "$line" == \#* ]] || break
        stripped="${line#\#}"
        stripped="${stripped# }"
        printf '%s\n' "$stripped"
    done
}

# ---------------------------------------------------------------------------
# Dispatcher
# ---------------------------------------------------------------------------

COMMAND="${1:-help}"
shift || true

case "$(_lc "$COMMAND")" in
    e) COMMAND="env" ;;
    i|ins) COMMAND="install" ;;
    un|rm) COMMAND="uninstall" ;;
    u|up) COMMAND="upgrade" ;;
    l|ls) COMMAND="list" ;;
    li|st) COMMAND="lint" ;;
    t|test|tests|ut) COMMAND="unit-tests" ;;
    v|ver) COMMAND="version" ;;
    h|-h|--help) COMMAND="help" ;;
esac

case "$COMMAND" in
    env)            cmd_env "$@" ;;
    install)        cmd_install "$@" ;;
    uninstall)      cmd_uninstall "$@" ;;
    upgrade)        cmd_upgrade "$@" ;;
    list)           cmd_list "$@" ;;
    lint)           cmd_lint "$@" ;;
# TODO: This needs to be fixed
#    unit-tests)     cmd_unit_tests "$@" ;;
    version)        cmd_version "$@" ;;
    help)           cmd_help ;;
    *)
        echo "ERROR: Unknown command '$COMMAND'"
        echo "Run './manage.sh help' for usage."
        exit 1
        ;;
esac