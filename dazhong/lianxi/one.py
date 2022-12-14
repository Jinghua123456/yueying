# -*- encoding：utf-8 -*-
# l=[]#定义空列表
# for i in range(200,321):#range函数（前闭后开）范围
#     if i%7==0 and i%5!=0:
#         l.append(str(i))
# print(",".join(l))

# n=int(input("请输入一个数："))
# a=1
# b=1
# while a<=n:
#     a=b+a
#     a=a+1
#     print(a)
# n=int(input("请输入一个数："))
# a=1
# b=1
# for a in range(1,n+1):
#     a=a+b
#     print(a)
# n=int(input("请输入一个数："))
# def yunsuan(x):
#     if 8<=x<=n+1:
#         return x
#     else:
#         print(int(x*2))
# print(yunsuan(int(input("输入一个数："))))
#for循环
# n=int(input("请输入一个数："))
# b=[]
# for i in range(1,n+1):
#     b.append(i*i)
#     print(b)
#字典{}或a=dice（）
# n = int(input("请输入一个数："))
# b={i:i*i for i in range(1,n+1)}
# print(b)

#第一
x=int(input("请输入一个数："))
y: int=int(input("请输入一个数："))
if x >y:
    temp=y
    y=x
    x=temp
for factor in range(x,0,-1):
    if x % factor == 0 and y % factor == 0:
        print('{}he{}de最大公约数：{}'.format(x,y,factor))
        print('{}he{}的最小公倍数：{}'.format(x,y,x*y//factor))
        break

