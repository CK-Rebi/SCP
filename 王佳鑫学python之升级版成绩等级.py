a=input('请输入你的成绩:\n')
c=0
while(a!='n'and a!=""):
  for i in a:
        if(i!='0'and i!='1'and i!='2'and i!='3'and i!='4'and i!='5'and i!='6'and i!='7'and i!='8'and i!='9'):
          c+=1

  if(c==0):
        d=eval(a)
        if(d==100):
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
        a=input('请输入你的成绩:\n')

  else:
    
        j=1
        for i in a:
            print('您输入错误，应当输入的形式为数字。第{}个字符是{}\n'.format(j,i))
            j+=1
        a=input('请重新输入你的成绩:\n')
  c=0
