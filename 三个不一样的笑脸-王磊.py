import turtle as t
t.speed(0)
t.hideturtle()


#脸
def face(x,y,z):
    t.pensize(5)
    t.color('pink','yellow')
    t.penup()
    t.goto(x,y)
    t.seth(-90)
    t.fd(z*6/5)
    t.pendown()
    t.seth(0)
    t.begin_fill()
    t.circle(z*6/5,360)
    t.end_fill()


#右眼
def right_eye(x,y,z):
    t.pensize(3)
    t.color('black','white')
    t.penup()
    t.goto(x,y)
    t.fd(z*2/5)
    t.seth(90)
    t.fd(z*12/25)
    t.seth(0)
    t.pendown()
    t.begin_fill()
    t.circle(z*1/4,360)
    t.end_fill()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(z*3/25,360)
    t.end_fill()


#左眼
def left_eye(x,y,z):
    t.pensize(3)
    t.color('black','white')
    t.penup()
    t.goto(x,y)
    t.fd(-z*2/5)
    t.seth(90)
    t.fd(z*12/25)
    t.seth(0)
    t.pendown()
    t.begin_fill()
    t.circle(z*1/4,360)
    t.end_fill()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(z*3/25,360)
    t.end_fill()


#嘴巴
def mouth(x,y,z):
    t.pensize(5)
    t.penup()
    t.goto(x,y)
    t.seth(-90)
    t.fd(z*7/10)
    t.seth(0)
    t.pendown()
    t.circle(z*7/10,60)
    t.penup()
    t.goto(x,y)
    t.seth(-90)
    t.fd(z*7/10)
    t.seth(180)
    t.pendown()
    t.circle(-z*7/10,60)




face(-300,150,100)
right_eye(-300,150,100)
left_eye(-300,150,100)
mouth(-300,150,100)



face(300,150,50)
right_eye(300,150,50)
left_eye(300,150,50)
mouth(300,150,50)




face(0,-300,150)
right_eye(0,-300,150)
left_eye(0,-300,150)
mouth(0,-300,150)













    
