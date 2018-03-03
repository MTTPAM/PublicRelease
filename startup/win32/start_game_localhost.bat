@echo off
cd ../../

rem Get the user input:
set ttUsername=admin
rem set /P ttUsername="Username: "

rem Export the environment variables:
set TT_PLAYCOOKIE=%ttUsername%
set TT_GAMESERVER=127.0.0.1

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