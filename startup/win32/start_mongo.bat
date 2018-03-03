@echo off
title MongoDB
cd ../../astron

:main
"MongoDB\Server\3.0\bin\mongod.exe" --dbpath MongoDB/astrondb


pause
