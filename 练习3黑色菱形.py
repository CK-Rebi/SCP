import turtle

turtle.pensize(1)
turtle.color('black')
a=10
turtle.speed(0)
for i in range(50):
    turtle.penup()
    turtle.goto()
    turtle.pendown()
    turtle.goto(a,0)
    turtle.goto(0,-a)
    turtle.goto(-a,0)
    turtle.goto(0,a)
    a=a+3
