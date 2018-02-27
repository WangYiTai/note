:: encoding convert
:: IconvRun.bat source_file src_enc dst_enc
@ECHO OFF
SETLOCAL ENABLEEXTENSIONS

SET /A errno=0
SET /A ERROR_HELP_SCREEN=1
SET /A ERROR_SOMECOMMAND_NOT_FOUND=2
SET /A ERROR_OTHERCOMMAND_FAILED=4

iconv -f %3 %1 >nul 2>&1 && goto _NOT_DONE
iconv -f %2 %1 >nul 2>&1 && goto _DONE
goto _ERROR
:_DONE
iconv -f %2 -t %3 %1 > %1.tmp
copy /B %1.tmp %1
del %1.tmp
:_SUCCESS
echo "成功"
goto _EXIT
:_NOT_DONE
echo "無需更改"
goto _EXIT
:_ERROR
echo "失敗"
:_EXIT
