# -*- encoding：utf-8 -*-
# a="11bade2345611"
# print(a.find("d"))
# print(a.find("k"))
# print(a.find("b"))查找字符位置（从左开始找），找到（从0开始数）返回字符串位置，找不到返回-1
# print(a.replace("1","c",2))替换
# print(a.count("a"))统计摸个字符出现的次数
# print(len(a))字符串的长度
# print(a.lower())转化成小写
# print(a.upper())转化成大写
# print(a.startswith("1"))以指定字符开头
# print(a.endswith("1"))以指定字符结尾
# print(a+"你好")拼接
# print(a,"你好")拼接
# a='qw123456'
# b='123456'
# c='zxcvb'
# print(c.isdigit())
# print(c.isalpha())
# print(b.isdigit())
# print(a.isalnum())
# print(max(a))
# print(min(c))
# print(max(c))
# a='123456xa  '
# print(a.rsplit())
# print(a[3])
# print(a[::])
# print(a[2:5:1])
# c=1
# c=2
# print(c)
# c,d=20,10
# print(f"cdezhi{c}",f"ddezhi{d}")
# c,d=d,c
# print(c,d)
# a=[123]
# b=[]
# c=list()
# print(type(a))
# print(type(b))
# print(type(c))
# a.append("a")
# c.append("a")
# print(a)
# print(c)
# a.insert(0,"q")
# c.insert(2,"w")
# print(a)
# print(c)
# a=[1,23,"qz","d",(1,2),1]
# print(a.pop())
# print(a.pop(1))
# print(a)
# a.remove(23)
# print(a)
# a=[1,3,7,9,2,4,6,8]
# liu=a.sort()
# print(liu)
# a.sort(reverse=False)
# print(a)
# a.sort(reverse=Ture)
# print(a)
# a.sort(reverse=True)
# print(a)
# a.reverse()
# print(a)
# print(a.index(8))
# b=["a","b","d","e"]
# c=a+b
# print(c)
# a.extend(c)
# print(a)
# a.extend(b)
# print(a)
# print(0 and 1)
# print(1 and 2)
# print('' and 1)
# print(1 and [])
# print(0 or 0)
# print(1 or 1)
# print(1 or 0)
# print(0 or 1)
# print(not 0)
# print(not 1)
# a=[1,2,1,3,4,5,6,]
# print(set(a))
# print(list(set(a)))

# a=()
# b=tuple()
# c=(1,2)
# d=(1,3)
# print(type(a))
# print(type(a))
# print(type(a))
# print(operator.eq(c,d))
# print(b.count(1))

# a=[]
# b=list()
# c=[1,2,3,4,5]
# print(type(a))
# print(type(b))
# print(type(c))
# a.append("a""a""1""流" )
# print(a)
# c.append("a""a""1""流" )
# print(c)
# c.insert(4,"liu")
# print(c)
# a={}
# b=dict()
# c={"name":"zhangsan"}
# print(type(a))
# print(type(b))
# print(type(c))
# print(c)
# c["age"]="18"
# print(a)
# a.update(b=1)
# print(a)
# print(c["name"])
# print(c.get("c"))
# print(c.keys())
# print(c.values())
# print(c.items())
# print("add" in c)
# print("name" in c)
# c.pop("age")
# print(c)
# b=set()
# a={1,23,456,4,5}
# c={1,23,4,56}
# print(type(a))
# print(type(b))
# print(c.intersection(a))
# print(c.union(a))
# print(c.difference(a))
# print(a.difference(c))
# a=121
# if a<120:
#     print(a)
#     print("加油")
# else:print("Good bye")
# age=int(input("请输入年龄："))
# print(age)
# if age<=0:
#     print("你是在逗我玩的吧！")
# elif age==1:
#     print("相当于人类的14 岁")
# elif age==2:
#     print("相当于人类的22岁")
# elif age>2:
#     human=22+(age-2)*5
#     print("对应的人类年龄：",human)
# num=int(input("请输入一个数字："))
# if num%2==0:
#     if num%3==0:
#         print("你输入的数字可以整除2和3")
#     else:
#         print("你输入的数字可以整除 2，但不能整除 3")
# else:
#     if num%3==0:
#         print("你输入的数字可以整除 3，但不能整除 2")
#     else:
#         print("你输入的数字不能整除 2 和 3")
# a=1
# while a<12:
#     print(a)
#     a +=3
# n = 5
# while n > 0:
#     n -= 1
#     if n == 2:
#         break
#     print(n)
# print('循环结束。')
# a=input("sr:")
# b=input("sr:")
# def max(a,b):
#     if a>b:
#         print("huahaoyueyuan")
#     else:
#         return b
# print(max(a,b))
# def max(a,b):
#     if a>b:
#         print("huahaoyueyuan")
#     else:
#         return b
# a = 7
# b = 9
# print(max(a,b))
num=input("输入数字：")
if num < "5" :
    if num > "1":
        print("学习")
elif num>"5":
    print("看电影")
    print("吃大餐")
