set scriptCode="src\certificateGenerator.py"
set configFile="config\config.yml"

python %scriptCode% %configFile%

echo Press any key to exit
set /p input=