import turtle as t
import math as m
t.speed(0)
t.screensize(4500,3000)
t.setup(900,600)


def xing(x,y,r,j):
    t.penup()
    t.goto(x,y)
    t.setheading(j)
    t.forward(r)
    t.right(180/m.pi*(m.pi/2+m.atan(3)))
    t.pendown()
    t.color('yellow')
    t.begin_fill()
    for i in range(5):
        t.forward(r*2*m.cos(m.atan(1/3)))
        t.right(144)
    t.end_fill()

 
def hongqi(x,y,d):
    t.color('red')
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.goto(x+d,y)
    t.goto(x+d,y-(2/3)*d)
    t.goto(x,y-(2/3)*d)
    t.goto(x,y)
    t.end_fill()

    xing(x+d/6,y-d/6,d/10,(180/m.pi)*(m.pi/2+m.atan(3)))
    xing(x+d/3,y-(2/30)*d,d/30,(180/m.pi)*(m.pi+m.atan(3/5)))
    xing(x+d/3,y-(9/30)*d,d/30,(180/m.pi)*(m.pi/2+m.atan(5/4)))
    xing(x+12*d/30,y-(4/30)*d,d/30,(180/m.pi)*(m.pi+m.atan(1/7)))
    xing(x+12*d/30,y-(7/30)*d,d/30,(180/m.pi)*(m.pi/2+m.atan(7/2)))

hongqi(-450,300,900)




