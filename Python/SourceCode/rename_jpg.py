# -*- coding:utf-8 -*-
#!/usr/local/bin/python

import os
from datetime import datetime
import shutil
import sys

#判斷檔案是否為圖片
def is_imag(filename):
    return os.path.splitext(filename)[-1].lower()  in [".jpg", ".png"]

#取得圖片建立時間
def get_time(filename):
    timestamp = os.stat(filename).st_mtime
    return datetime.fromtimestamp(timestamp)

#listdir 會列出目標資料夾的所有檔案名稱
if len(sys.argv) < 2:
    filenames = os.listdir(".")
else :
    filenames = os.listdir(sys.argv[1])
    os.chdir(sys.argv[1])


#取得所有圖片的檔名
images = filter(is_imag, filenames)
for i in filter(is_imag, filenames):
    print(i)
#images.sort(key=get_time)
filenames = images

#將檔案依時間排序
#filenames.sort(key=get_time)
filenames = sorted(filenames, key=get_time)

last_modified = None
for filename in filenames:
    modified = get_time(filename)

    #決定流水號，若修改的日期與前一個檔案相同時流水號加 1
    if last_modified and last_modified.time() == modified.time():
        num += 1
        #依據時間和流水號決定檔案
        targetname = "{}_{}.jpg".format(modified.strftime("%Y%m%d-%H%M%S"),num)
    else:
        num = 0
        targetname = "{}.jpg".format(modified.strftime("%Y%m%d-%H%M%S"))



    #改名
    shutil.move(sys.argv[1]+"/"+filename, sys.argv[1]+"/"+targetname)

    last_modified = modified