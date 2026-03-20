call activate_vir_env.bat
echo Starting App
cd ..
REM python -m unittest discover -s play_helpers/test
python -m unittest play_helpers/test/test_util.py
cd scripts
call deactivate_vir_env.bat
