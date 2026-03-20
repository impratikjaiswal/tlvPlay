call activate_vir_env.bat

set export_path=scripts/%output_path%/run_tests_%vir_env_name%.log
echo Export Path: %export_path%

echo Starting App

cd ..
python -u -m play_helpers.test.test > %export_path% 2>&1
cd scripts

call deactivate_vir_env.bat