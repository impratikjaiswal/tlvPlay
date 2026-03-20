#!/bin/bash

# --- CONFIGURATION ---
# Define your list of paths separated by space or in an array
env_list=("../venv_39" "../venv_314")
fix_script_1="list_requirements.sh"
fix_script_2="run_tests.sh"
ini_file="config_vir_env_default.ini"

echo "Starting the loop..."

for current_env in "${env_list[@]}"; do
    echo "current_env: $current_env"
    echo "path=$current_env" > "$ini_file"
    bash "$fix_script_1"
    bash "$fix_script_2"
    echo "-----------------"
done

echo "Ending the loop..."

