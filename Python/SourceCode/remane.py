# -*- coding:utf-8 -*-
#!/usr/local/bin/python

import os
from datetime import datetime
import shutil
import sys

#判斷檔案是否為圖片
def is_imag(filename):
    return os.path.splitext(filename)[-1] in [".png", ".jpg"]

	#取得圖片建立時間
def get_time(filename):
    timestamp = os.stat(filename).st_mtime
    return datetime.fromtimestamp(timestamp)

#listdir 會列出目標資料夾的所有檔案名稱
if len(sys.argv) < 2:
    filenames = os.listdir(".")
else :
    filenames = os.listdir(sys.argv[1])


#取得所有圖片的檔名
images = filter(is_imag, filenames)

filenames = images

#將檔案依時間排序
#filenames.sort(key=get_time)

last_modified = None
for filename in filenames:
    modified = get_time(sys.argv[1]+"/"+filename)

    #決定流水號，若修改的日期與前一個檔案相同時流水號加 1
    if last_modified and last_modified.date() == modified.date():
        num += 1
    else:
        num = 1

    #依據時間和流水號決定檔案
    targetname = "{}.jpg".format(modified.strftime("%Y%m%d-%H%M%S"))

    #改名
    shutil.move(sys.argv[1]+"/"+filename, sys.argv[1]+"/"+targetname)

    last_modified = modified