print('----------------------------------------------------------------')      #使用说明
print('欢迎使用本系统')
print('接下来我将介绍一下基本规则')
print('首先本系统只支持有理数，若输入了其他东西，还请重新输入。')
print('在使用的时候，请先输入红旗个数')
print('接下来依次输入红旗左上角的x坐标，y坐标，以及长边长。')
print('作画窗口可能被遮挡，如没有显示，请找一下电脑底部窗口。')
print('再次感谢对本系统的抬爱，祝您使用愉快~')
print('----------------------------------------------------------------')
print('////////////////////////////////\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\')
print('||||||||||||----------------------------------------||||||||||||')
print('|||||||||||||   按回车确定阅读完成，开始本次使用   |||||||||||||')
print('||||||||||||----------------------------------------||||||||||||')
print('\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\////////////////////////////////')
l=input('----------------------------------------------------------------')


geshu=('')                              #初步定义变量，防止报错。
x=('')
y=('')
d=('')
p=1
#确定使用者想要画的红旗个数
while geshu==(''):
    geshu=input('请输入红旗个数:')
    for i in geshu:
        if i==('-'):
            geshu=('chonglai')
    try:
        geshu=int(geshu)
    except:
        geshu=('')
        print('请重新输入，必须是正整数')


#创建新变量 x1,x2……  y1,y2……  d1,d2……并赋值，用于下面作画

for i in range(geshu):

    while x==(''):  #x
        x=input('请输入第{}个红旗左上x坐标:'.format(p))
        try:
            x=eval(x)
            exec('x{} = x'.format(p))
        except:
            x=('')
            print('请重新输入，必须是有理数')

    while y==(''):  #y
        y=input('请输入第{}个红旗左上y坐标:'.format(p))
        try:
            y=eval(y)
            exec('y{} = y'.format(p))
        except:
            y=('')
            print('请重新输入，必须是有理数')

    while d==(''):  #d
        d=input('请输入第{}个红旗长边长:'.format(p))
        try:
            d=eval(d)
            exec('d{} = d'.format(p))
        except:
            d=('')
            print('请重新输入，必须是有理数')
            
    x=('')#从新定义变量，以回到循环
    y=('')
    d=('')
    p=p+1

#导入所需模块
import turtle as t
import math as m
#进行初步设置
t.speed(0)
t.screensize(4500,3000)
t.setup(900,600)


#通过三角函数，画出一个所需行星星
def xing(x,y,r,j):
    #  x:五角星中心点x坐标
    #  y:五角星中心点y坐标
    #  r:五角星外切圆半径
    #  j:五角星某个角相对中心点方向。
    t.penup()
    t.goto(x,y) #找得到中心点
    t.setheading(j)   #找到一个角的方向
    t.forward(r)      #到达其中一个五角星的顶点
    t.right(180/m.pi*(m.pi/2+m.atan(3)))  #转向五角星一条边的方向
    t.pendown()
    t.color('yellow')
    t.begin_fill()
    for i in range(5):                    #画出五角星
        t.forward(r*2*m.cos(m.atan(1/3))) #根据变量r求出五角星的边长并作画
        t.right(144)
    t.end_fill()

 
def hongqi(x,y,d):
    t.color('red')  #画出红旗
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.begin_fill()
    t.goto(x+d,y)
    t.goto(x+d,y-(2/3)*d)
    t.goto(x,y-(2/3)*d)
    t.goto(x,y)
    t.end_fill()

    #根据变量画出对应五角星
    xing(x+d/6,y-d/6,d/10,(180/m.pi)*(m.pi/2+m.atan(3)))  #这里面，x,y,r限定五角星的大小和
                                                          #相对红旗左上角的位置，j使大五角星正立
    
    xing(x+d/3,y-(2/30)*d,d/30,(180/m.pi)*(m.pi+m.atan(3/5)))  #j 做好预设，将第一个角的方向转向大五角星中心
    xing(x+d/3,y-(9/30)*d,d/30,(180/m.pi)*(m.pi/2+m.atan(5/4)))
    xing(x+12*d/30,y-(4/30)*d,d/30,(180/m.pi)*(m.pi+m.atan(1/7)))
    xing(x+12*d/30,y-(7/30)*d,d/30,(180/m.pi)*(m.pi/2+m.atan(7/2)))


p=1
for i in range(geshu):#调用打包的函数和设置好的变量，画出多个红旗。
    exec('x = x{}'.format(p))
    exec('y = y{}'.format(p))
    exec('d = d{}'.format(p))
    hongqi(x,y,d)
    p=p+1



t.hideturtle()
t.exitonclick()
   





























