import turtle as t
t.hideturtle()
t.speed(0)


def smlie(x,y):
    t.penup()
    t.goto(x,y)
    t.pensize(6)
    t.fillcolor("yellow")
    t.begin_fill()
    t.pendown()
    t.circle(100)
    t.end_fill()
    #嘴
    
    
    t.pensize(6)
    t.setheading(90)
    t.pencolor("red")
    t.penup()
    t.forward(17)
    t.setheading(0)
    t.pendown()
    t.circle(100,40)
    t.circle(100,-80)
    t.circle(100,40)
    #右眼白
    t.pensize(3)
    t.pencolor("gold")
    t.penup()
    t.setheading(90)
    t.forward(100)
    t.setheading(0)
    t.forward(50)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    #右眼黑
    t.pensize(3)
    t.circle(20)
    t.end_fill()
    t.pencolor("black")
    t.fillcolor("black")
    t.begin_fill()
    t.circle(13)
    t.end_fill()
    #左眼白
    t.pensize(3)
    t.pencolor("gold")
    t.penup()
    t.setheading(180)
    t.forward(100)
    t.pendown()
    t.fillcolor("white")
    t.begin_fill()
    #左眼黑
    t.pensize(3)
    t.setheading(0)
    t.circle(20,360)
    t.end_fill()
    t.pencolor("black")
    t.fillcolor("black")
    t.begin_fill()
    t.circle(13)
    t.end_fill()
    
smlie(-200,100)
smlie(0,0)
smlie(200,-100)





