#!/bin/bash

source "$(dirname "$0")/activate_vir_env.sh"

export_path="scripts/$output_path/run_tests_${vir_env_name}.log"
echo "Export Path: $export_path"

echo "Starting App"

cd ..
python -u -m play_helpers.test.test > "$export_path" 2>&1
cd scripts

source "$(dirname "$0")/deactivate_vir_env.sh"

