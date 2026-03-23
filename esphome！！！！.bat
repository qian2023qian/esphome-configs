@echo off
title ESPHome Dashboard

:: 1. 进入当前文件夹（脚本所在目录）
cd /d "%~dp0"

:: 2. 激活虚拟环境（假设虚拟环境文件夹叫 esphome-env）
call esphome-env\Scripts\activate.bat

:: 3. 启动 dashboard（使用当前目录下的配置文件）
esphome dashboard .

start http://localhost:6052

:: 不急着关窗口（方便看错误信息）
echo.
echo 按任意键关闭窗口...
pause