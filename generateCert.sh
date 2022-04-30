scriptCode="src\certificateGenerator.py"
configFile="config\config.yml"

python ${scriptCode} ${configFile}

read -n 1 -s -r -p "Press any key to exit"
