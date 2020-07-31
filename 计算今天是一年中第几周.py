# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 15:59:52 2019

@author: Administrator
"""

#! /usr/bin/env python
 

if __name__ == '__main__': 
    import time

    dates = {'Sun':'星期天', 'Mon':'星期一', 'Tue': '星期二', 'Wed': '星期三',
             'Thu':'星期四', 'Fri': '星期五', 'Sat':'星期六'}

    week = dates.get( time.ctime()[0:3])

    print(u"今天是:",time.localtime()[0],u"年",time.localtime()[1],u"月",time.localtime()[2],u"日",week)
    print(u"今天是:",week) 
    print(u"今天是今年的第", int(time.localtime()[7]/7+1), u"周")
    print(u"今天是今年的第",time.localtime()[7],u"天")
    print(time.ctime())
