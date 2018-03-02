# -*- coding: utf-8 -*-
'''一個時鐘程式'''
def createAlarm(master):
    ''' 創建時間選擇組件，包括小時、分鐘、秒
    系統預設的時間設置為當前的事件'''
    import time
    now = time.localtime(time.time())
    lfAlarm = LabelFrame(text = 'Add you alarm')
    master.vHour = StringVar()
    master.vHour.set(now[3])
    Label(lfAlarm,text = 'Hour:').grid(row = 0,column = 0)
    master.omHour = apply(OptionMenu,(lfAlarm,master.vHour) + tuple(range(0,24)))
    master.omHour.grid(row = 0,column = 1)
    
    master.vMinute = StringVar()
    master.vMinute.set(now[4])
    Label(lfAlarm,text = 'Minute:').grid(row = 0,column = 2)
    master.omMinute = apply(OptionMenu,(lfAlarm,master.vMinute) + tuple(range(0,60)))
    master.omMinute.grid(row = 0,column = 3)

    master.vSecond = StringVar()
    master.vSecond.set(now[5])
    Label(lfAlarm,text = 'Second:').grid(row = 0,column = 4)
    master.omSecond = apply(OptionMenu,(lfAlarm,master.vSecond) + tuple(range(0,60)))
    master.omSecond.grid(row = 0,column = 5)

    lfAlarm.grid(row = 1,column =0,columnspan = 6)
def addAlarm(master):
    '''將當前的設置添加為一個提醒
    設置最後一個為啟動態
    選中最後一個'''
    master.lbAlarm.insert(END,master.vHour.get() + ':' + master.vMinute.get() + ':' + master.vSecond.get())
    master.lbAlarm.selection_clear(0,END)
    master.lbAlarm.selection_set(END)
    master.lbAlarm.activate(END)
def deleteAlarm(master):
    '''刪除一個提醒'''
    master.lbAlarm.delete(ACTIVE)
    if master.lbAlarm.size() > 0:
        master.lbAlarm.selection_set(ACTIVE)
def modifyAlarm(master):
    '''修改提醒,
    刪除原來的提醒,添加一個新的提醒,索引使用原來'''
    t = master.vHour.get() + ':' + master.vMinute.get() + ':' + master.vSecond.get()
    n = master.lbAlarm.curselection()
    master.lbAlarm.delete(n)
    master.lbAlarm.insert(n,t)
    master.lbAlarm.selection_set(n)
    
def createAlarmList(master):
    '''創建提醒列表，目前所有可用的提醒均顯示在這裡'''
    master.lbAlarm = Listbox(master)
    master.lbAlarm.grid(row = 3,column = 0,
                 columnspan = 4,rowspan = 3,
                 stick = S + N + E + W)
def createOperation(master):
    '''創建操作列表，對提醒列表中的提醒進行添加、修改或刪除'''
    Button(master,text = 'Add alarm',
           command = lambda arg = master:addAlarm(arg)
           ).grid(
               row = 3,column = 4,
               columnspan = 2,
               stick = S + N + E + W)
    Button(master,text = 'Modify alarm',
           command = lambda arg = master:modifyAlarm(arg)
           ).grid(
               row = 4,column = 4,
               columnspan = 2,
               stick = S + N + E + W)
    Button(master,text = 'Delete alarm',
           command = lambda arg = master:deleteAlarm(arg)
           ).grid(row = 5,column = 4,
                  columnspan = 2,
                  stick = S + N + E + W)
def showCurrentTime(master):
    '''顯示當前時間'''
    lbCurrentTime = Label(master,text = 'Current Time:')
    lbCurrentTime.grid(row = 0,column = 0,
                       columnspan = 2,
                       stick = W)
    master.vCurrentTime = StringVar()
    master.etCurrentTime = Entry(master,textvariable = master.vCurrentTime,state = 'readonly')
    master.etCurrentTime.grid(row = 0,column = 2,
                       columnspan = 4,
                       stick = S + N + E + W)
def updateTime(master):
    '''時鐘回呼函數,用於更新當前時間;
    判斷是否滿足提醒條件'''
    import time
    now = time.localtime(time.time())
    t = '%d:%d:%d' % (now[3],now[4],now[5])
    master.vCurrentTime.set(t)
    
    for item in master.lbAlarm.get(0,END):
        if str(item) == t:
            # 如果當前時間與提醒列表中的一致,列印
            print 'you have a alarm',item
    
    root.after(100,updateTime,master)
    
from Tkinter import *
root = Tk()
showCurrentTime(root)
createAlarm(root)
createAlarmList(root)
createOperation(root)
# 將檢測週期設置為100ms
root.after(100,updateTime,root)
root.mainloop()

