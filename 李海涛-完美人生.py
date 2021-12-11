
def xvefenjidian(x,b):#学分绩点部分
    x,b=eval(x),eval(b)
    if x>90:
        x=90
    v_xvefenjidian=b*(x/10-5)
    return v_xvefenjidian

def nengli():#专业能力评价部分
    print('选择：【a】超好  【b】好 【c】一般 【d】较差 【e】很差')
    a=input('输入你的专业能力评价等级：\n')
    if a==('a'):
        a=100
    elif a==('b'):
        a=80
    elif a==('c'):
        a=60
    elif a==('d'):
        a=40
    else:
        a=20
    return a

def nengli2():#成长性评价部分
    global n
    n=0
    print('选择：【a】超好  【b】好 【c】一般 【d】较差 【e】很差')
    a=input('输入你的等级：\n')
    if a==('a'):
        a=100
    elif a==('b'):
        a=80
    elif a==('c'):
        a=60
    elif a==('d'):
        a=40
        n=n+1
    else:
        a=20
        n=n+2
    return a

c=0
while c!=('n'):
    x=input('请输入你的英语成绩：')
    b=('3')
    xvefenjidian(x,b)
    english=xvefenjidian(x,b)
    x=input('请输入你的数学成绩：')
    b=('3.5')
    xvefenjidian(x,b)
    math=xvefenjidian(x,b)
    x=input('请输入你的计算机导论成绩：')
    b=('2.5')
    xvefenjidian(x,b)
    computer=xvefenjidian(x,b)
    ave=(math+english+computer)/(2.5+3.5+3)
    print ('这位同学的平均绩点为{:.1f}'.format(ave))#绩点部分完成

    print('---------------------------------------')

    print('输入你的电脑基础评分')
    d=nengli()
    print('输入你的编程基础评分')
    b=nengli()
    print('输入你的自学能力评分')
    z=nengli()
    pingfen=(d+b+z)/3
    print('你的专业能力评分为{:.3f}'.format(pingfen))#专业能力部分

    print('---------------------------------------')

    print('输入你的人际关系评价')
    d=nengli2()
    print('输入你的自我反省评价')
    b=nengli2()
    print('输入你的学习力评分')
    z=nengli2()
    nengli2=((d+b+z)/3-20*n)
    print('你的成长性评价评分为{:.3f}'.format(nengli2))#成长性评价部分
    
    print('---------------------------------------')
    
    rensheng=((ave/5)*100+pingfen+nengli2)/3
    print('\n\n你的完美人生得分为：{:.3f}'.format(rensheng))

  
    c=input('\n\n输入n退出,或按回车继续运行。\n\n\n')
