a=input('请输入你的成绩(按n或回车键停止)')
while (a!='' and a!='n'):
    s=0                        #判断错误               
    for b in a:
        if (b!='0' and b!='1' and b!='2' and b!='3' and b!='4' and b!='5' and b!='6' and b!='7' and b!='8' and b!='9'):
            s+=1
    if (s!=0):
        a=input('输入错误，只需输入成绩数字,请重新输入')  
    else:
        c=eval(a)              
        if(c<0 or 100<c):      #判断数值范围
            a=input('输入错误，只需输入成绩数字,请重新输入')
        else:                  #判断等级
            if(c==100):
                print('满分')
            elif(c>=90 and c<100):
                print('优秀')
            elif(c>=80 and c<90):
                print('良好')
            elif(c>=70 and c< 80):
                print('中等')
            elif(c>=60 and c<70):
                print('及格')
            else:
                print('不及格')
            a=input('请输入你的成绩(按n或回车键停止)')
            
                    

 
