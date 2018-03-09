:: for c
SET VS90COMNTOOLS=%VS140COMNTOOLS%
::call "C:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools\"vsvars32.bat
SET PATH=%VS140COMNTOOLS%;%PATH%
call vsvars32.bat
cl prime_c.c
pause