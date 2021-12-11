#输入成绩
a=input('学生姓名(回车退出)')
while (a!=''):
    b=input('语文成绩')
    while(b==''):
        print('输入错误，请重新输入该成绩')
        b=input('语文成绩')
    while (b!=''):    
        real=0
        for i in b:
            if (i!='0' and i!='1' and i!='2' and i!='3' and i!='4' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9'):
                real+=1
            else:
                real+=0
        if (real!=0):
            print('输入错误，请重新输入该成绩')
            b=input('语文成绩')
        else:
            break
    c=input('数学成绩')
    while(c==''):
        print('输入错误，请重新输入该成绩')
        c=input('数学成绩')
    while (c!=''):
        real=0
        for i in c:
            if (i!='0' and i!='1' and i!='2' and i!='3' and i!='4' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9'):
                real+=1
            else:
                real+=0
        if (real!=0):
            print('输入错误，请重新输入该成绩')
            c=input('数学成绩')
        else:
            break
    d=input('英语成绩')
    while (d==''):
        print('输入错误，请重新输入该成绩')
        d=input('英语成绩')        
    while (d!=''):
        real=0
        for i in d:
            if (i!='0' and i!='1' and i!='2' and i!='3' and i!='4' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9'):
                real+=1
            else:
                real+=0
        if (real!=0):
            print('输入错误，请重新输入该成绩')
            d=input('英语成绩')
        else:
            break
    e=input('体育成绩')
    while (e==''):
        print('输入错误，请重新输入该成绩')
        e=input('体育成绩')
    while (e!=''):
        real=0
        for i in e:
            if (i!='0' and i!='1' and i!='2' and i!='3' and i!='4' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9'):
                real+=1
            else:
                real+=0
        if (real!=0):
            print('输入错误，请重新输入该成绩')
            e=input('体育成绩')
        else:
            break
    f=input('劳动成绩')
    while (f==''):
        print('输入错误，请重新输入该成绩')
        f=input('劳动成绩')
    while (f!=''):
        real=0
        for i in f:
            if (i!='0' and i!='1' and i!='2' and i!='3' and i!='4' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9'):
                real+=1
            else:
                real+=0
        if (real!=0):
            print('输入错误，请重新输入该成绩')
            f=input('劳动成绩')
        else:
            break
    g=input('美术成绩')
    while (g==''):
        print('输入错误，请重新输入该成绩')
        g=input('美术成绩')
    while (g!=''):
        real=0
        for i in g:
            if (i!='0' and i!='1' and i!='2' and i!='3' and i!='4' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9'):
                real+=1
            else:
                real+=0
        if (real!=0):
            print('输入错误，请重新输入该成绩')
            g=input('美术成绩')
        else:
            break
    h=input('音乐成绩')
    while (h==''):
        print('输入错误，请重新输入该成绩')
        h=input('音乐成绩')        
    while (h!=''):
        real=0
        for i in h:
            if (i!='0' and i!='1' and i!='2' and i!='3' and i!='4' and i!='4' and i!='5' and i!='6' and i!='7' and i!='8' and i!='9'):
                real+=1
            else:
                real+=0
        if (real!=0):
            print('输入错误，请重新输入该成绩')
            h=input('音乐成绩')
        else:
            break
#比较分数
    yw=eval(b)
    sx=eval(c)
    en=eval(d)
    ty=eval(e)
    ld=eval(f)
    ms=eval(g)
    yy=eval(h) 
    if(yw<=sx):
        nu1=sx
        nu2=yw
        n1='数学'
        n2='语文'
    else:
        nu1=yw
        nu2=sx
        n1='语文'
        n2='数学'
    if(nu1<=en):
        nu2=nu1
        nu1=en
        n2=n1
        n1='英语'
    elif(nu2<=en):
        nu2=en
        n2='英语'       
    if(nu1<=ty):
        nu2=nu1
        nu1=ty
        n2=n1
        n1='体育'
    elif(nu2<=ty):
        nu2=ty
        n2='体育'
    if(nu1<=ld):
        nu2=nu1
        nu1=ld
        n2=n1
        n1='劳动'
    elif(nu2<=ld):
        nu2=ld
        n2='劳动'
    if(nu1<=ms):
        nu2=nu1
        nu1=ms
        n2=n1
        n1='美术'
    elif(nu2<=ms):
        nu2=ms
        n2='美术'
    if(nu1<=yy):
        nu2=nu1
        nu1=yy
        n2=n1
        n1='音乐'
    elif(nu2<=yy):
        nu2=yy
        n2='音乐'
    #最低的
    if (yw<=sx):
        un=yw
        u='语文'
    else:
        un=sx
        u='数学'
    if (un>=en):
        un=en
        u='英语'
    if(un>=ty):
        un=ty
        u='体育'
    if(un>=ld):
        un=ld
        u='劳动'
    if(un>=ms):
        un=ms
        u='美术'
    if(un>=yy):
        un=yy
        u='音乐'
#判断科目，给出评语
    #赞
    if (n1=='语文'):
        if(nu1<=100 and nu1>85):
            p1='你博学多才，学富五车;'
        elif(nu1<=85 and nul>70):
            p1='你文采不错，文章辞藻华丽;'
        elif(nul<=70):
            p1='你有一点语文天赋，但仍需努力;'
    if (n2=='语文'):
        if(nu2<=100 and nu2>85):
            p2='博学多才，学富五车。'
        elif(nu2<=85 and nu2>70):
            p2='文采不错，文章辞藻华丽。'
        elif(nu2<=70):
            p2='有一点语文天赋，但仍需努力。'
    if (n1=='数学'):
        if(nu1<=100 and nu1>85):
            p1='你思维缜密，可以举一反三;'
        elif(nu1<=85 and nul>70):
            p1='你有一点数学思维，懂得变通;'
        elif(nul<=70):
            p1='你有一点数学天赋，但仍需努力;'
    if (n2=='数学'):
        if(nu2<=100 and nu2>85):
            p2='思维缜密，可以举一反三。'
        elif(nu2<=85 and nu2>70):
            p2='有数学思维，懂得变通。'
        elif(nu2<=70):
            p2='有一点数学天赋，但仍需努力。'
    if (n1=='英语'):
        if(nu1<=100 and nu1>85):
            p1='你精通语法，有深不见底的词汇量;'
        elif(nu1<=85 and nul>70):
            p1='你可以熟读课文，对英语学习有着不错的热情;'
        elif(nul<=70):
            p1='你有一点英语天赋，但仍需努力;'
    if (n2=='英语'):
        if(nu2<=100 and nu2>85):
            p2='精通语法，有深不见底的词汇量。'
        elif(nu2<=85 and nu2>70):
            p2='可以熟读课文，对英语学习有着不错的热情。'
        elif(nu2<=70):
            p2='有一点英语天赋，但仍需努。'
    if (n1=='体育'):
        if(nu1<=100 and nu1>85):
            p1='你身体健壮，精通各种体育项目;'
        elif(nu1<=85 and nul>70):
            p1='你对自己体能有着不错的要求;'
        elif(nul<=70):
            p1='你有一点体育天赋，但仍需努力;'
    if (n2=='体育'):
        if(nu2<=100 and nu2>85):
            p2='身体健壮，精通各种体育项目。'
        elif(nu2<=85 and nu2>70):
            p2='对自己体能有着不错的要求。'
        elif(nu2<=70):
            p2='有一点体育天赋，但仍需努力。'
    if (n1=='劳动'):
        if(nu1<=100 and nu1>85):
            p1='你热爱劳动，并且乐于帮助同学;'
        elif(nu1<=85 and nul>70):
            p1='你能认真完成劳动任务;'
        elif(nul<=70):
            p1='你愿意劳动，但仍需努力;'
    if (n2=='劳动'):
        if(nu2<=100 and nu2>85):
            p2='热爱劳动，并且乐于帮助同学。'
        elif(nu2<=85 and nu2>70):
            p2='能认真完成劳动任务。'
        elif(nu2<=70):
            p2='愿意劳动，但仍需努力。'
    if (n1=='美术'):
        if(nu1<=100 and nu1>85):
            p1='你能发现美，并且可以创造美;'
        elif(nu1<=85 and nul>70):
            p1='你热爱美术，能欣赏美;'
        elif(nul<=70):
            p1='你有一点美术天赋，但仍需努力;'
    if (n2=='美术'):
        if(nu2<=100 and nu2>85):
            p2='能发现美，并且可以创造美。'
        elif(nu2<=85 and nu2>70):
            p2='热爱美术，能欣赏美。'
        elif(nu2<=70):
            p2='有一点美术天赋，但仍需努力。'
    if (n1=='音乐'):
        if(nu1<=100 and nu1>85):
            p1='你能发现音乐的奇妙，并且熟练地掌握一种乐器;'
        elif(nu1<=85 and nu1>70):
            p1='你热爱音乐，能欣赏音乐的奇妙;'
        elif(nu1<=70):
            p1='你有一点音乐天赋，但仍需努力;'
    if (n2=='音乐'):
        if(nu2<=100 and nu2>85):
            p2='能发现音乐的奇妙，并且熟练地掌握一种乐器。'
        elif(nu2<=85 and nu2>70):
            p2='热爱音乐，能欣赏音乐的奇妙。'
        elif(nu2<=70):
            p2='有一点音乐天赋，但仍需努力。'
    #批评
    if (u=='语文'):
        if(un<=100 and un>85):
            pp='你文采非常好，但还可以进步。'
        elif(un<=85 and un>70):
            pp='你语文不错，但相比其他学科还可以努力。'
        elif(un<=70):
            pp='语文是你的弱项，你继续巩固基础。'
    if (u=='数学'):
        if(un<=100 and un>85):
            pp='你计算能力不错，但还可以进步。'
        elif(un<=85 and un>70):
            pp='你数学还行，但相比其他学科还可以努力。'
        elif(un<=70):
            pp='数学是你的弱项，你要加倍努力。'
    if (u=='英语'):
        if(un<=100 and un>85):
            pp='你语感、语法都不错，但还可以进步。'
        elif(un<=85 and un>70):
            pp='你英语还行，但要多注意语法。'
        elif(un<=70):
            pp='英语是你的弱项，你应该多背单词。'
    if (u=='体育'):
        if(un<=100 and un>85):
            pp='你体能很好，但还可以进步。'
        elif(un<=85 and un>70):
            pp='你体育还行，但要注意规范。'
        elif(un<=70):
            pp='体育是你的弱项，你要多多锻炼。'
    if (u=='劳动'):
        if(un<=100 and un>85):
            pp='你积极劳动，但还可以进步。'
        elif(un<=85 and un>70):
            pp='你劳动认真，但要学会主动劳动。'
        elif(un<=70):
            pp='你要学着喜欢劳动，提升自我。'
    if (u=='美术'):
        if(un<=100 and un>85):
            pp='你美术创作能力可以，但还须进步。'
        elif(un<=85 and un>70):
            pp='你美术还行，但自己得多多创造。'
        elif(un<=70):
            pp='美术是你的弱项，你可以多学习大师的作品。'
    if (u=='音乐'):
        if(un<=100 and un>85):
            pp='你音乐天赋不错，但还须进步。'
        elif(un<=85 and un>70):
            pp='你天赋还行，但自己要练习。'
        elif(un<=70):
            pp='音乐是你的弱项，你可以多欣赏大师的作品。'
    print('{},老师发现{}{}不过，{}老师希望在接下来的日子里你能保持优点，改正不足。'.format(a,p1,p2,pp))
    print('---------------------------------------')
    a=input('学生姓名(回车退出)')


    
