@echo off
pushd %~dp0
echo.
echo.
echo.
echo.
echo "all"

cd ..
cd ..
cd scripts
call activate_vir_env.bat
cd ..
python -m tlv_play.main.tlvplay > tlv_play\test\logs\all.log
cd scripts
call deactivate_vir_env.bat
cd ..
echo.
echo.
echo.
echo.
echo "Batch Execution Done"
