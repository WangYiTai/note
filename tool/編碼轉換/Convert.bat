:: encoding convert files
:: Convert.bat *.txt utf-8 big-5
:: Convert.bat xxx.doc big-5 utf-8
@ECHO OFF
for /r %%i in (%1) do Call IconvRun.bat %%i %2 %3
