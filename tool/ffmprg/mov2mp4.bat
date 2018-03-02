@echo off
REM 影像轉檔 mov to 3pg  手機專用
REM 使用FFMPEG 轉成H264(BASELINE)
REM 指令如下
C:\api\ffmpeg-20160825-01aee81-win64-static\bin\ffmpeg -i opening.mov -c:v libx264 -profile:v baseline -level 3.0 -acodec copy out.3gp