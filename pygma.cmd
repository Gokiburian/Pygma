@echo off
set/p seed="�V�[�h�l >"
cd %1
for /r %%i in (*) do (
start /d%~dp0 /b pygma.py "%%i" %seed% o
)