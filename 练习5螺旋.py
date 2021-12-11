import turtle

turtle.pensize(1)
turtle.bgcolor('black')
a=10
b=15
turtle.speed(0)
turtle.penup()
turtle.goto(-a,a)
turtle.pendown()
turtle.color('green')
turtle.goto(a,a)
turtle.color('red')
turtle.goto(a,-a)
turtle.color('blue')
turtle.goto(-b,-a)
turtle.color('yellow')
turtle.goto(-b,b)
a=a+5
b=b+5
for i in range(100):
    turtle.goto(-a,a)
    turtle.color('green')
    turtle.goto(a,a)
    turtle.color('red')
    turtle.goto(a,-a)
    turtle.color('blue')
    turtle.goto(-b,-a)
    turtle.color('yellow')
    turtle.goto(-b,b)
    a=a+5
    b=b+5
    
