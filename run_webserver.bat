cd /d %~dp0

cmd.exe /K "conda activate iot_env & python.exe webserver.py"

rem http://127.0.0.1:5000/