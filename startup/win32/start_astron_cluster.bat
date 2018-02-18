@echo off
title Astron
cd ../../astron
astrond --loglevel debug config/cluster.yml
pause