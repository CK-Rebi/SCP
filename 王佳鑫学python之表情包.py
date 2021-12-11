import turtle as t
t.speed(0)
#画大黄脸
def face(x,y,z):
    t.penup()
    t.goto(x,y)
    t.setheading(270)
    t.forward(z)#z是半径
    t.left(90)
    t.pendown()
    t.color('pink','yellow')
    t.begin_fill()
    t.circle(z)#逆时针360画圆
    t.end_fill()#大黄脸填充好颜色

#画嘴角
def mouth(x,y,z):
    t.pencolor('purple')
    t.penup()
    t.goto(x,y)
    t.right(90)
    t.penup()
    t.forward(z/2)
    t.right(90)
    t.pendown()
    t.circle(z/2,60)
    t.circle(z/2,-120)
    t.circle(z/2,60)
  
#画左眼睛
def l_eye(x,y,z):
    t.penup()
    t.goto(x,y)
    t.left(90)
    t.forward(z/3)
    t.left(90)
    t.forward(z/3)
    t.right(180)
    t.color('black','white')
    t.pendown()
    t.begin_fill()
    t.circle(z/4)
    t.end_fill()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(z/6)
    t.end_fill()

#画右眼睛
def r_eye(x,y,z):
    t.penup()
    t.goto(x,y)
    t.left(90)
    t.forward(z/3)
    t.right(90)
    t.forward(z/3)
    t.pendown()
    t.color('black','white')
    t.pendown()
    t.begin_fill()
    t.circle(z/4)
    t.end_fill()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(z/6)
    t.end_fill()
    

def emoji(x,y,z):
    face(x,y,z)
    l_eye(x,y,z)
    r_eye(x,y,z)
    mouth(x,y,z)

emoji(-5,-52,30)
emoji(-100,52,70)
emoji(100,200,90)
