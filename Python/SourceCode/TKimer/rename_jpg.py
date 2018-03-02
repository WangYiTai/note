# -*- coding:utf-8 -*-
#!/usr/local/bin/python

import os
from datetime import datetime
import shutil
import sys

import tkFileDialog
import tkMessageBox
from Tkinter import Tk, Label, Button

#判斷檔案是否為圖片（.lower()為副檔名不分大小寫）
def is_imag(filename):
    return os.path.splitext(filename)[-1].lower()  in [".jpg", ".png"]

#取得圖片建立時間
def get_time(filename):
    timestamp = os.stat(filename).st_mtime
    return datetime.fromtimestamp(timestamp)

#listdir 會列出目標資料夾的所有檔案名稱
#if len(sys.argv) < 2:
#    filenames = os.listdir(".")
#else :
#    filenames = os.listdir(sys.argv[1])
#    os.chdir(sys.argv[1])
# dirname =  tkFileDialog.askdirectory()
def rename_dir(dirname):
    filenames = os.listdir(dirname)
    if filenames is None:
        exit(0)
    os.chdir(dirname)
    #取得所有圖片的檔名
    filenames = filter(is_imag, filenames)

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
        if filename != targetname:
            shutil.move(filename, targetname)

        last_modified = modified
    return len(filenames)


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Python 修改照片名稱")

        self.label = Label(master, text="相片依時間修改成檔案名稱")
        self.label.pack()

        self.labelDir = Label(master, text="目錄位置")
        self.labelDir.pack()


        #self.greet_button = Button(master, text="Greet", command=self.greet)
        #self.greet_button.pack()

        self.open_dir_button = Button(master, text="啟開目錄", command=self.openDir)
        self.open_dir_button.pack()


        self.run_button = Button(master, text="修改檔案名稱", command=self.rename)
        self.run_button.pack()

        #self.close_button = Button(master, text="Close", command=master.quit)
        #self.close_button.pack()

    def greet(self):
        print("Greetings!")
    def openDir(self):
        self.dirname = tkFileDialog.askdirectory()
        self.labelDir.config(text=self.dirname)
    def rename(self):
        count = rename_dir(self.dirname)
        tkMessageBox.showinfo("修改檔案名稱", "共有{}張改名".format(count))



root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
