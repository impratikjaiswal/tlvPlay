echo Attempting to activate existing Virtual Environment

SET output_path=logs

# 1. Read the first line of the config file into a variable
SET /P vir_env_path=<config_vir_env.ini
# 2. Extract the base directory name
for %%A in ("%vir_env_path%") do set "vir_env_name=%%~nxA"

# Debugging
# echo Virtual Environment Path: %vir_env_path%
# echo Virtual Environment Name: %vir_env_name%

call %vir_env_path%\Scripts\activate

echo .
echo Python Version
python --version

echo .
echo Python Location
which python

IF NOT EXIST "%output_path%" (
    MD "%output_path%"
    echo "%output_path%" Directory created successfully.
)

echo .