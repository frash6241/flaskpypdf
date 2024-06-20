@echo off
REM Iniciar servicios de XAMPP
cd C:\xampp
REM Iniciar Apache
start /B xampp_start.exe

REM Iniciar MySQL
start /B mysql_start.bat

REM Esperar unos segundos para asegurar que XAMPP y MySQL se inicien correctamente
timeout /t 10 /nobreak
REM Mantener la ventana del comando abierta
cmd /k