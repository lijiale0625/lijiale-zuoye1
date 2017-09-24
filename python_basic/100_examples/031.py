# -*- coding:utf-8 -*-
# 题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
# 程序分析：用情况语句比较好，如果第一个字母一样，则判断用情况语句或if语句判断第二个字母。。
#参考
weeklist = {'M': 'Monday','T': {'u': 'Tuesday','h':'Thursday'}, 'W': 'Wednesday', 'F':'Friday','S':{'a':'Saturday','u':'Sunday'}}
sLetter1 = raw_input("请输入首字母：")
sLetter1 = sLetter1.upper()

if (sLetter1 in ['T','S']):
    sLetter2 = raw_input("请输入第二个字母：")#raw_input与input有什么区别
    print(weeklist[sLetter1][sLetter2])
else:
    print(weeklist[sLetter1])

#1)
import  re

def judge(first,list):
    li=[]
    first = first.upper()
    for a in list:
        if re.match(first,a):
            li.append(a)
    if len(li)==1:
        print li[0]
    else:
        second=raw_input('请输入第二个字母：')
        for b in li:
            if re.match(first+second,b):
                print b

list=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
first=raw_input('请输入第一个字母：')
judge(first,list)