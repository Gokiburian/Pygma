@echo off
set/p seed="シード値 >"
cd %1
for /r %%i in (*) do (
start /d%~dp0 /b pygma.py "%%i" %seed% o
)