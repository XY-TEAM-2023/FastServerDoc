@echo off
chcp 65001
set "DEST_PATH=C:\Application\Work\win_android\plugins\vprj_win\classlib\user\FS\document"

echo 开始执行脚本...
echo 目标路径: %DEST_PATH%

if exist "%DEST_PATH%" (
    echo 清空目标文件夹...
    rd /S /Q "%DEST_PATH%"
)

echo 创建目标文件夹...
mkdir "%DEST_PATH%"

echo 开始复制文件夹...
for /D %%D in (*) do (
    set "dirname=%%D"
    setlocal enabledelayedexpansion
    set "firstChar=!dirname:~0,1!"
    if not "!firstChar!"=="." (
        echo 正在复制文件夹: %%D
        xcopy /S /E /Y /I "%%D" "%DEST_PATH%\%%D\"
    )
    endlocal
)

echo 开始复制文件...
for %%F in (*) do (
    set "filename=%%~nxF"
    setlocal enabledelayedexpansion
    set "firstChar=!filename:~0,1!"
    if not "%%~xF"==".bat" if not "!firstChar!"=="." (
        echo 正在复制文件: %%F
        copy /Y "%%F" "%DEST_PATH%\"
    )
    endlocal
)

echo 复制完成
echo 请检查目标文件夹: %DEST_PATH%
pause 