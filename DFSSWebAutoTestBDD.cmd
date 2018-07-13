@echo off

pushd %~dp0 

xcopy F:\DFSS_Auto_Test_BDD C:\Windows\System32\features /D /S /E /Y

xcopy C:\Windows\System32\features\BDD C:\Windows\System32\features /D /S /E /Y