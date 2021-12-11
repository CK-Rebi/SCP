def nengli():
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
print('输入你的电脑基础评分')
d=nengli()
print('输入你的编程基础评分')
b=nengli()
print('输入你的自学能力评分')
z=nengli()

pingfen=(d+b+z)/3
print('你的专业能力评分为')
print(pingfen)
