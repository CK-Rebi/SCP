
def xvefenjidian(x,b):
    x,b=eval(x),eval(b)
    if x>90:
        x=90
    v_xvefenjidian=b*(x/10-5)
    return v_xvefenjidian
c=0
while c!=('n'):
    x=input('请输入你的英语成绩：')
    b=('3')
    xvefenjidian(x,b)
    english=xvefenjidian(x,b)
    print (english)

    x=input('请输入你的数学成绩：')
    b=('3.5')
    xvefenjidian(x,b)
    math=xvefenjidian(x,b)
    print (math)

    x=input('请输入你的计算机导论成绩：')
    b=('2.5')
    xvefenjidian(x,b)
    computer=xvefenjidian(x,b)
    print (computer)

    ave=(math+english+computer)/(2.5+3.5+3)
    print ('这位同学的平均绩点为{:.1f}'.format(ave))
    print (ave)
    c=input('输入n退出')
