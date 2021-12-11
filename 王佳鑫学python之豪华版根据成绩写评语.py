a=input('请输入你的语文成绩:\n')
b=input('请输入你的数学成绩:\n')
c=input('请输入你的英语成绩:\n')
d=input('请输入你的体育成绩:\n')
e=input('请输入你的劳动成绩:\n')
f=input('请输入你的美术成绩:\n')
g=input('请输入你的音乐成绩:\n')
h=0
while(a!='n'and a!=""and b!='n'and b!=""and c!='n'and c!=""and d!='n'and d!=""and e!='n'and e!=""and f!='n'and f!=""and g!='n'and g!=""):
  for i in a:
        if(i!='0'and i!='1'and i!='2'and i!='3'and i!='4'and i!='5'and i!='6'and i!='7'and i!='8'and i!='9'):
          h+=1

  if(h==0):
        j=eval(a)
        if(j==100):
             print('如果说语文有珠穆朗玛峰，那你一定就是峰顶~')
        elif(j>=90):
             print('语文方面呢，人生因为失误才有阴差阳错，人生因为阴差阳错才有相逢即是有缘，找寻自己的错误，才会遇见更好的自己！')
        elif(j>=60):
             print('语文方面呢，基础较好，但有更进一步的空间，仔细分析自己的失误并进行改正，期待你的进步！')
        else:
             print('语文方面呢，需要加强对基础的练习，不要灰心，继续努力！')

  else:
    
        k=1
        for i in a:
            print('语文成绩输错啦，应该输入数字哟~第{}个字符为{}\n'.format(k,i))
            k+=1
  h=0

  for i in b:
        if(i!='0'and i!='1'and i!='2'and i!='3'and i!='4'and i!='5'and i!='6'and i!='7'and i!='8'and i!='9'):
          h+=1

  if(h==0):
        l=eval(b)
        if(l==100):
             print('这数学题是你出的吧，不然你怎么如此优秀，满分信手拈来~')
        elif(l>=90):
             print('数学是一种精确的语言，学习数学的过程中，逐渐培养自己的严谨，离成功就差一点啦，加油！')
        elif(l>=60):
             print('数学方面呢，掌握了一定的基础，可以考虑多多练习拔高性题目，继续加油！')
        else:
             print('数学方面呢，要巩固基础知识，多多练习，总会有站在峰顶的一天~')

  else:
    
        k=1
        for i in b:
            print('数学成绩输错啦，应该输入数字哟~第{}个字符为{}\n'.format(k,i))
            k+=1
  h=0

  for i in c:
        if(i!='0'and i!='1'and i!='2'and i!='3'and i!='4'and i!='5'and i!='6'and i!='7'and i!='8'and i!='9'):
          h+=1

  if(h==0):
        m=eval(c)
        if(m==100):
             print('努力终会有收获，熬过了黑暗，光明终于到来，祝贺你，英语状元！')
        elif(m>=90):
             print('词汇、语法和语感都非常不错哦，加强熟练度，多见题型，相信会更好！')
        elif(m>=60):
             print('英语方面呢，加大词汇量，巩固语法，你会发现英语也可以成为你的有力武器')
        else:
             print('英语方面呢，要多记单词，提高词汇量，这样阅读才不那么痛苦，尽量去理解语法知识，多读课文提高自己的语感，英语也会成为你的强项哦~')

  else:
    
        k=1
        for i in c:
            print('英语成绩输错啦，应该输入数字哟~第{}个字符为{}\n'.format(k,i))
            k+=1
  h=0

  for i in d:
        if(i!='0'and i!='1'and i!='2'and i!='3'and i!='4'and i!='5'and i!='6'and i!='7'and i!='8'and i!='9'):
          h+=1

  if(h==0):
        n=eval(d)
        if(n==100):
             print('我想此刻你应该理解了体育的本质，不单单是强健体魄，而是让我们成为一个精神焕发的人！你迎来了你的新生！')
        elif(n>=90):
             print('接近钢铁侠的体魄，继续锻炼，成为钢铁侠指日可待！')
        elif(n>=60):
             print('体育方面呢，让体育成为一种习惯，成为你生活的一部分!相信会有很大的提升。')
        else:
             print('体育方面呢，需要加强锻炼啦！体质过差的话，不利于自己健康快乐生活，身体可是革命的本钱呢~')

  else:
    
        k=1
        for i in d:
            print('体育成绩输错啦，应该输入数字哟~第{}个字符为{}\n'.format(k,i))
            k+=1
  h=0

  for i in e:
        if(i!='0'and i!='1'and i!='2'and i!='3'and i!='4'and i!='5'and i!='6'and i!='7'and i!='8'and i!='9'):
          h+=1

  if(h==0):
        o=eval(e)
        if(o==100):
             print('劳动最光荣，你就是最值得骄傲的小标兵~')
        elif(o>=90):
             print('劳动最光荣，你已经是一个优秀的劳动标兵啦，继续努力！')
        elif(o>=60):
             print('“一劳永逸”的话是有的，但是“一劳永逸”的事情却是极少的，热爱劳动吧，你会享受其中的快乐！')
        else:
             print('任何一个民族，如果停止劳动，不用说一年，就是几个星期，也要灭亡，这是每一个小朋友都应该知道的。')

  else:
    
        k=1
        for i in e:
            print('劳动成绩输错啦，应该输入数字哟~第{}个字符为{}\n'.format(k,i))
            k+=1
  h=0

  for i in f:
        if(i!='0'and i!='1'and i!='2'and i!='3'and i!='4'and i!='5'and i!='6'and i!='7'and i!='8'and i!='9'):
          h+=1

  if(h==0):
        p=eval(f)
        if(p==100):
             print('下一个美术史的开创就靠你了哟')
        elif(p>=90):
             print('对美的捕捉能力很强，具有很高的对美的鉴赏能力，继续努力！就快达到美术的珠穆朗玛峰了哟~')
        elif(p>=60):
             print('美，源自生活，生活中不是缺少美，而是缺少发现美的眼睛，多去寻找生活中的美，或许你会有新的发现呢。')
        else:
             print('美术方面呢，有些人的美术天赋是天生的，不必嫉妒，我们通过后天的培养也是可以哒，加油，老师看好你！')

  else:
    
        k=1
        for i in f:
            print('美术成绩输错啦，应该输入数字哟~第{}个字符为{}\n'.format(k,i))
            k+=1
  h=0

  for i in g:
        if(i!='0'and i!='1'and i!='2'and i!='3'and i!='4'and i!='5'and i!='6'and i!='7'and i!='8'and i!='9'):
          h+=1

  if(h==0):
        q=eval(g)
        if(q==100):
             print('你是登峰造极的音乐大师~')
        elif(q>=90):
             print('乐感超强的呢，下一个迈克尔杰克逊没准就是你哟~')
        elif(q>=60):
             print('音乐，培养人的精神，陶冶人的情操，学会去享受它，而不是当成一种负担去学习，大胆地去发挥自己！')
        else:
             print('音乐带给人热情，带给人希望，通过音乐，我希望它也能把光带给你。')

  else:
    
        k=1
        for i in g:
            print('音乐成绩输错啦，应该输入数字哟~第{}个字符为{}\n'.format(k,i))
            k+=1
  a=input('请输入你的语文成绩:\n')
  b=input('请输入你的数学成绩:\n')
  c=input('请输入你的英语成绩:\n')
  d=input('请输入你的体育成绩:\n')
  e=input('请输入你的劳动成绩:\n')
  f=input('请输入你的美术成绩:\n')
  g=input('请输入你的音乐成绩:\n')
  h=0
