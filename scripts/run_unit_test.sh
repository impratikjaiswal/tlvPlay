#!/bin/bash

source "$(dirname "$0")/activate_vir_env.sh"
echo "Starting App"
cd ..
# python -m unittest discover -s play_helpers/test
python -m unittest play_helpers/test/test_util.py
cd scripts
source "$(dirname "$0")/deactivate_vir_env.sh"

