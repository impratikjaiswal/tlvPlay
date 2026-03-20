@echo off
SETLOCAL EnableDelayedExpansion

:: --- CONFIGURATION ---
:: Define your list of paths separated by semi colon
SET "env_list=..\venv_39;..\venv_314"
SET "fix_script_1=list_requirements.bat"
SET "fix_script_2=run_tests.bat"
SET "ini_file=config_vir_env_default.ini"

echo Starting the loop...

FOR %%P IN ("%my_paths:;=" "%") DO (
    SET "current_env=%%~P"
    echo current_env: %current_env%
    echo path=!current_env! > "%ini_file%"
    CALL "!fix_script_1!"
    CALL "%fix_script_2%"
    echo -----------------
)
echo Ending the loop...
pause