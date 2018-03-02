# -*- coding:utf-8 -*-
try:
	import tkinter
	from tkinter import ttk
	import tkinter.messagebox as message_box
except:
	import Tkinter as tkinter
	import ttk
	import tkMessageBox as message_box
import os

windows = tkinter.Tk()
windows.title("Python 自動關機 for WINDOWS")
# window 居中
windows.update()  # update window ,must do
curWidth =  360   # get current width
curHeight = windows.winfo_reqheight()  # get current height
scnWidth, scnHeight = windows.maxsize()  # get screen width and height
# now generate configuration information
config = '%dx%d+%d+%d' % (curWidth, curHeight,
                          (scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
windows.geometry(config)
# root 容器
root = ttk.LabelFrame(windows, text="自動關機時間設定")
root.grid(column=0, row=0, padx=15, pady=15)
# 提醒文本
tkinter.Label(root, text="Enter a num:").grid(column=0, row=0, sticky=tkinter.W)
tkinter.Label(root, text="Choose unit").grid(column=1, row=0)

# 存儲輸入的值
time = tkinter.StringVar()
unit = tkinter.StringVar()
# 輸入框
time_edit = tkinter.Entry(root, width=10, textvariable=time)
time_edit.grid(column=0, row=1, padx=4, sticky=tkinter.W)
time_edit.focus()
# 下拉單位選擇
unit_arr = ('hour', 'minute', 'second')
unit_chosen = ttk.Combobox(root, width=6, textvariable=unit, state='readonly')
unit_chosen['values'] = unit_arr
unit_chosen.grid(column=1, row=1)
unit_chosen.current(0)


def change_edit(to_time):
    time_edit.delete(0, 10)
    time_edit.insert(0, to_time)
    unit_chosen.current(1)


# start
def start():
    if time.get() and unit.get():
        message_box.showwarning("Warning", "Your pc will shutdown after %s %s" % (time.get(), unit.get()))
        # shutdown 的秒數
        count_down_second = int(time.get())
        if unit.get() == 'hour':
            count_down_second *= 3600
        elif unit.get() == 'minute':
            count_down_second *= 60
        # execute
        os.system("shutdown -s -t %s" % count_down_second)
        windows.quit()


# cancel
def cancel():
    os.system("shutdown -a")
    windows.quit()


# start 按鈕
start_action = tkinter.Button(root, text="START", command=start)
start_action.grid(column=2, row=1)
# 文本
tip_label = tkinter.Label(root, text="shot cut options")
tip_label.grid(row=2, column=0, pady=2)
# 快捷選擇時間
fram = tkinter.Frame(root)
fram.grid(row=3, column=0, columnspan=3)
# 常用的時間
for i in range(2, 7):
    button = tkinter.Button(fram, text=str(i * 15) + "min", command=lambda x=i: change_edit(str(x * 15)))
    button.grid(row=0, column=i - 2, padx=2, pady=2, sticky=tkinter.W)
# cancel 按鈕
cancel_action = tkinter.Button(root, text="CANCEL", command=lambda: cancel())
cancel_action.grid(row=4, column=1, pady=10, sticky=tkinter.W)

root.mainloop()
