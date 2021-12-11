print('\n')
print('当输入n或者按回车键完毕')
print('\n')
a=input('请输入你的成绩:')
b=0
while(a!=''and a!='n'):
    for i in a:
         if(i!='1' and i!='2'and i!='3'and i!='4'and i!='5'and i!='6'and i!='7'and i!='8'and i!='9'and i!='0'):
             print('输入的值为',i,'有误')
             b+=1
    if(b==0):
        c=eval(a)
        if(c<0 or c>100):
            a=input('输入数值有误，请重新输:')
        if(c==100):
            print('满分')
        elif(c>=90 and c<100):
            print('优秀')
        elif(c>=80 and c<90):
            print('良好')
        elif(c>=70 and c<80):
            print('中等')
        elif(c>=60 and c<70):
            print('及格')
        else:
            print('不及格')
        a=input('请输入你的成绩:')
    else:
        a=input('请重新输入你的成绩:')
    b=0
print('\n\n\n')
print('完毕')
