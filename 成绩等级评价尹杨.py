a=input("请输入你的成绩(使用数字)")
while(a!="" and a!="n"):
 f=0
 for b in a :
     if(b!="0" and b!="1" and b!="2" and b!="3" and b!="4" and b!="5" and b!="6" and b!="7" and b!="8" and b!="9"):
         f+=1
        
 if(f!=0):
    a=input("输入有误，请重新输入")
 else:
     x=eval(a)

     if(x==100):
        print("满分")
     elif(x>=90 and x<100):
        print("优秀")
     elif(x>=80 and x<90):
        print("良好")
     elif(x>=70 and x<80):
        print("中等")    
     elif(x>=60 and x<70):
        print("及格")
     else:
        print("不及格")
     a=input("请输入你的成绩")   
        
