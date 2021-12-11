import types
print('-----------------------------------')
print('按回车确认收到')
print('请输入纯数字')
input('当输入n，或者按回车的时候停止程序')
print('-----------------------------------')
a=input('请输入你的分数：')
while(a!="n")and (a!=""):
    for i in a:
        c=('{}'.format(i))
        try:
            b=eval(c)
            d=eval(a)
        except:
            d=('错误')
            break
    if(d==('错误')):
        print('数据错误，请重新输入。')
    elif(d==100):
        print('满分')
    elif(d>=90):
        print('优秀')
    elif(d>=80):
        print('良好')
    elif(d>=70):
        print('中等')
    elif(d>=60):
        print('及格')
    else:
        print('不及格')
    a=input('请输入你的分数：')
print('感谢您的使用')

