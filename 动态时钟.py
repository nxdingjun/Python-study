# coding=UTF-8
from turtle import *
from datetime import *
import time

def Skip(step):               #建立表的外框
    penup()
    forward(step)
    pendown()

def mkHand(name,length):      #注册turtle形状，建立表针turtle
    reset()
    Skip(-length*0.1)
    begin_poly()
    forward(length*1.1)
    end_poly()
    handForm = get_poly()
    register_shape(name,handForm)

def Init():
    global secHand,minHand,hurHand,printer
    mode("logo")             #重置turtle指向北

    mkHand("secHand",135)    #建立三个表针并初始化
    mkHand("minHand",115)
    mkHand("hurHand",90)

    secHand = Turtle()
    secHand.shape("secHand")
    minHand = Turtle()
    minHand.shape("minHand")
    hurHand = Turtle()
    hurHand.shape("hurHand")

    for hand in secHand,minHand,hurHand:
        hand.shapesize(1,1,3)
        hand.speed(0)

    printer = Turtle()        #建立输出文字turtle
    printer.hideturtle()
    printer.penup()

def SetupClock(radius):      #建立表外框
    reset()
    pensize(7)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            forward(20)
            Skip(-radius-20)
        else:
            dot(5)
            Skip(-radius)
        right(6)

def Week(t):
    #week = ["Mon", "Tues", "Wed","Thur", "Fri", "Sat", "Sun"]
    #return "星期" + week[t.weekday()]
    dates = {'Sun':'星期天', 'Mon':'星期一', 'Tue': '星期二', 'Wed': '星期三',
             'Thu':'星期四', 'Fri': '星期五', 'Sat':'星期六'}
    week = dates.get( time.ctime()[0:3])
    return week
def Date(t):
    y = t.year
    m = t.month
    d = t.day
    return "%s年%d月%d日" % (y, m, d)
def Tick():
    t = datetime.today()
    second = t.second + t.microsecond * 0.000001
    minute = t.minute + second/60.0
    hour = t.hour + minute/60.0
    secHand.setheading(6*second)
    minHand.setheading(6*minute)
    hurHand.setheading(30*hour)
    tracer(False)
    printer.forward(65)
    printer.write("南京",align="center",font=("Arial",20,"bold"))
    printer.back(150)
    printer.write(Date(t),align="center",font=("Courier",14,"bold"))
    printer.back(30)
    printer.write(Week(t),align="center",font=("Courier",14,"bold"))
    printer.home()
    tracer(True)
    ontimer(Tick,100)                #100ms后继续调用tick

def main():
    tracer(False)
    Init()
    SetupClock(160)
    tracer(True)
    Tick()
    mainloop()
if __name__ == "__main__":
    main()