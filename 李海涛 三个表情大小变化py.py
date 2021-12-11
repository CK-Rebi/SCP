
import turtle as t
t.speed(50)
t.setup(1000,1000)
t.screensize(3000,3000)
#脸
def face(x,y,s): 
    t.hideturtle()
    t.penup()
    t.goto(x*s,(y-300)*s)
    t.pendown()
    t.begin_fill()
    t.pencolor('orange')
    t.fillcolor('yellow')
    t.circle(300*s)
    t.end_fill()
    t.penup()
#嘴
def mouth(x,y,s,m):
    t.goto(x*s,(y-200)*s)
    t.pendown()
    t.setheading(0)
    t.pencolor('brown')
    t.pensize(3*s)
    if m==0:
        t.circle(180*s,60)
        t.circle(180*s,-120)
        t.pensize(1)
        t.penup()
    else:
        t.penup()
        t.setheading(90)
        t.forward(100*s)
        t.setheading(0)
        t.pendown()
        t.circle(-180*s,60)
        t.circle(-180*s,-120)
        t.penup()
#左眼
def l_eye(x,y,s):
    t.pensize(1)
    t.goto((x-100)*s,(y+100)*s)
    t.pendown()
    t.setheading(0)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(50*s)
    t.end_fill()
    t.begin_fill()
    t.color('black')
    t.circle(30*s)
    t.end_fill()
    t.penup()
#右眼
def r_eye(x,y,s):
    t.pensize(1)
    t.goto((x+100)*s,(y+100)*s)
    t.pendown()
    t.pencolor('brown')
    t.setheading(0)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(50*s)
    t.end_fill()
    t.begin_fill()
    t.color('black')
    t.circle(30*s)
    t.end_fill()
#表情
def emojy(x,y,s,m):
    face(x,y,s)
    mouth(x,y,s,m)
    l_eye(x,y,s)
    r_eye(x,y,s)

emojy(-300,-300,1.0,0)
emojy(300,-300,1.5,0)
emojy(0,300,0.5,1)

t.exitonclick()
