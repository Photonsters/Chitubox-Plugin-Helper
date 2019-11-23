cd /D %~dp0
%SystemRoot%\explorer.exe %~dp0
python debug.py %*

rem cmd /k python debug.py %*