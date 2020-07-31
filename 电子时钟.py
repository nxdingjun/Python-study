# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 20:53:53 2020

@author: Administrator
"""

import tkinter
import time
 
def gettime():
    # 获取当前时间并转为字符串
    timestr = time.strftime("%H:%M:%S")
    # 重新设置标签文本
    lb.configure(text=timestr)
    # 每隔一秒调用函数gettime自身获取时间
    root.after(1000, gettime)

def getdate():
    # 获取当前日期并转为字符串
    datestr = time.localtime()[0],"年",time.localtime()[1],"月",time.localtime()[2],"日"
    # 重新设置标签文本
    lb1.configure(text=datestr)
    
def getweek():
    # 获取当前星期并转为中文字符串
    dates = {'Sun':'星期日', 'Mon':'星期一', 'Tue': '星期二', 'Wed': '星期三',
             'Thu':'星期四', 'Fri': '星期五', 'Sat':'星期六'}

    weekstr = dates.get( time.ctime()[0:3])
    #计算第几周
    weekstr1="今年第", int(time.localtime()[7]/7+1) ,"周"
    weekstr2=weekstr,weekstr1
    # 重新设置标签文本
    lb2.configure(text=weekstr2)
    #lb3.configure(text=weekstr1)
    
root = tkinter.Tk()
root.title('电子时钟')
#设置日期标签
lb1 = tkinter.Label(root, text='', fg='red', font=("黑体", 30))
lb1.pack()
#设置星期标签
lb2 = tkinter.Label(root, text='', fg='blue', font=("黑体", 20))
lb2.pack()
#设置周标签
#lb3 = tkinter.Label(root, text='', fg='green', font=("黑体", 20))
#lb3.pack()

#设置时间标签
lb = tkinter.Label(root, text='', fg='black', font=("黑体", 30))
lb.pack()

getdate()
getweek()
gettime()

root.mainloop()
