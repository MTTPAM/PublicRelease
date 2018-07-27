@echo off
rem path/to/cmds
start start_astron_cluster.bat

start start_uberdog_server.bat

start start_ai_server_auto.bat

cd ../../

set /P PPYTHON_PATH=<PPYTHON_PATH
set TT_GAMESERVER=localhost
set TT_PLAYCOOKIE=localuser
:client

echo ===============================
echo Starting Toontown Project Altis...
echo ppython: %PPYTHON_PATH%
echo Username: %TT_PLAYCOOKIE%
echo Gameserver: %TT_GAMESERVER%
echo ===============================

%PPYTHON_PATH% -m toontown.toonbase.ClientStart
pause
goto :client