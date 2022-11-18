from turtle import *
import turtle
wn = turtle.Screen()
import time
wn.setup(width=800, height=650)

def my_goto(x, y):
    penup()

    goto(x, y)
    pendown()

def love():
    fillcolor('#ff4500')
    begin_fill()
    my_goto(0,0)
    seth(135)
    fd(7)
    seth(135)
    fd(150)
    seth(135)
    circle(-80, 180)
    seth(45)
    circle(-80, 180)
    seth(225)
    fd(160)
    end_fill()

def star():
    fillcolor('#ffd700')
    begin_fill()
    seth(70)
    fd(40)
    seth(290)
    fd(40)
    seth(-20)
    fd(40)
    seth(200)
    fd(40)
    seth(250)
    fd(40)
    seth(110)
    fd(40)
    seth(160)
    fd(40)
    seth(20)
    fd(40)
    end_fill()


if __name__ == '__main__':
    pensize(3)
    speed(1)
    love()
    my_goto(-50,170)
    star()
    # time.sleep(2.4)
    seth(285)
    my_goto(100, -200)
    seth(0)
    write('LOVE YOU', font=("Stantic Typeface", 30, "bold"))
    mainloop()
