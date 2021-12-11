def nengli():
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
print('输入你的人际关系评价')
d=nengli()
print('输入你的自我反省评价')
b=nengli()
print('输入你的学习力评分')
z=nengli()
nengli=((d+b+z)/3-20*n)
print('你的成长性评价评分为')
print(nengli)
