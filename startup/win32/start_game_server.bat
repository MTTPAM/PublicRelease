@echo off
cd ../../

rem Get the user input:
set /P ttUsername="Username: "

rem Get the user input:
set /P ttPassword="Password: "

rem Export the environment variables:
set TT_PLAYCOOKIE=%ttUsername%
set TT_USERNAME=%ttUsername%
set TT_PASSWORD=%ttPassword%
set TT_GAMESERVER=71.207.123.240

echo ===============================
echo Starting Toontown Project Altis...
echo ppython: "panda/python/ppython.exe" 
echo Username: %ttUsername%
echo Gameserver: %TT_GAMESERVER%
echo ===============================

:goto

"panda/python/ppython.exe" -m toontown.toonbase.ClientStart
pause

goto :goto