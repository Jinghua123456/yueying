# -*- encoding：utf-8 -*-
# #定义类
# class liu():
#     a=1#变量
#     def __init__(self):#构析函数，接受属性，处理特殊情况
#          b=2#属性（方法的私有属性）
#     def liu1(self):#方法，方法后的self代表类，自我的意思。
#          self.c=3#属性（类的属性）
#     def liu2(self):
#         print(self.a)
#         print(self.c)
#         self.liu1()#类内调用方法
#
# #liu().liu1()#类外调用方法{liu（）类的实例化}  类外调用方法属性，必须进行类的实例化。
# liu().liu1()
# print(liu().a)
# #定义类 father
# class father():
#     def dabieye(self):
#          print("大别页")
#     def haoche(self):
#          print("豪车")
#     def __yuangong(self):#隐藏（无法继承）
#         print("员工")
# #定义类 mather
# class mather():
#     def shanliang(self):
#         print("善良")
#     def piaoliang(self):
#         print("漂亮")
# #定义类 子女
# class children(father,mather):#继承，可以多继承
#     print(father().haoche())
#     print(mather().shanliang())
#     def haoche(self):#（可以覆盖继承）
#         print("豪车1")
# a=children().haoche()#类的实例化
# print(a)
#定义类 student
# class student():
#     name="你猜"
#     def __init__(self,age,aex,name):#构析函数
#         self.age=20
#         self.aex="男"
#         self.name="zhaohao"
#     def say_name(self):
#         print(self.name)
#     @classmethod
#     def my_name(cls):
#         print(cls.name)
#     @staticmethod
#     def yuorage():
#         print("age")

# dict={"张悦":"1234561","刘远":"1234562","赵浩":"1234563","李歌":"1234564"}
# class regpage():
#     def regpage1(self):
#         u = input("请输入用户名：")
#         if 6 <= len(u) <= 18:
#             if u not in dict.keys():
#                 p = input("请输入密码：")
#                 if 6 <= len(p) <= 20:
#                     if p.isdigit():
#                         return "密码不能纯数字"
#                     else:
#                         p1 = int(input("请再次输入密码："))
#                         if p == p1:
#                             return "注册成功"
#                         else:
#                             return "两次密码不一致"
#                 else:
#                     "请输入密码，6-20位"
#             else:
#                 return "用户名已存在"
#         else:
#             return "用户名不符合规则"
# a=regpage().regpage1()
# print(a)
# -*- encoding：utf-8 -*-
# @Time:2022/10/31 09:09
# @Auto:guohuashang
# @FileName:CalcModel.py
# @Emial:
# @Function:

#
# #加法函数
# def addfuntion(x,y):
#     if 200>=x>=100 and 200>=y>=100:
#         print(f"{x} + {y} =",x+y)
#     else:
#         print("加法运算区间为100-200")
# #减法函数
# def sub(x,y):
#     if 99 >= x >= 40 and 99 >= y >= 40:
#         print(f"{x} - {y} =", abs(x - y))
#     else:
#         print("减法运算区间为40-99")
# #乘法函数
# def mul(x,y):
#     if 39 >= x >= 20 and 39 >= y >= 20:
#         print(f"{x} * {y} =", abs(x * y))
#     else:
#         print("乘法运算区间为20-39")
# #除法函数
# def div(x,y):
#     if 19 >= x >= 0 and 19 >= y >= 0:
#         if y==0:
#             if x==11 and y==2:
#                 print(f"{x} % {y} =",x%y)
#             elif x==18 and y==3:
#                 print(f"{x} // {y} =",x//y)
#             else:
#                 print(f"{x} / {y} =",x/y)
#         else:
#             print("两数都为0，不能进行计算！")
#     else:
#         print("除法运算区间为0-19")
# #运算函数
# def calcFunction():
#     first=eval(input("请输入第一个数："))
#     operator=input("请输入运算符：")
#     second=eval(input("请输入第二个数："))
#     if 200>=first>=0 and 200>=second>=0:
#         if operator=="+":
#             addfuntion(first,second)
#         elif operator=="-":
#             sub(first,second)
#         elif operator=="*":
#             mul(first,second)
#         elif operator=="/":
#             div(first,second)
#         else:
#             print("运算符不合法！")
#     else:
#         print("运算数不在0-200区间范围内")
#主函数
# if __name__ == '__main__':
#     calcFunction()
# class calcFunction():
#     def __init__(self,operator):
#         if operator == "+":
#
#             print(b)
#         elif operator=="-":
#
#             print(c)
#         elif operator=="*":
#             d = mul(eval(input("请输入第一个数：")), eval(input("请输入第二个数：")))
#
#             print(d)
#         elif operator=="/":
#
#             print(e)
#         else:
#             print("运算符不合法！")
# if __name__ == '__main__':
#     a=calcFunction(input("请输入运算符号："))
# # print(a)
#
# class add():
#     def __init__(self,x,y):
#         if 200 >= x >= 100 and 200 >= y >= 100:
#             print(f"{x} + {y} =", x + y)
#         else:
#             print("加法运算区间为100-200")
# b = add(eval(input("请输入第一个数：")), eval(input("请输入第二个数：")))
# print(b)
# #减法
# class sub():
#     def __init__(self,x,y):
#         if 99 >= x >= 40 and 99 >= y >= 40:
#             print(f"{x} - {y} =", abs(x - y))
#         else:
#             print("减法运算区间为40-99")
# c = sub(eval(input("请输入第一个数：")), eval(input("请输入第二个数：")))
# # print(c)
# #乘法
# class mul():
#     def __init__(self,x,y):
#         if 39 >= x >= 20 and 39 >= y >= 20:
#             print(f"{x} * {y} =", abs(x * y))
#         else:
#             print("乘法运算区间为20-39")
# d = mul(eval(input("请输入第一个数：")), eval(input("请输入第二个数：")))
# # print(d)
# #除法
# class div():
#     def __init__(self,x,y):
#         if 19 >= x >= 0 and 19 >= y >= 0:
#             if y == 0:
#                 if x == 11 and y == 2:
#                     print(f"{x} % {y} =", x % y)
#                 elif x == 18 and y == 3:
#                     print(f"{x} // {y} =", x // y)
#                 else:
#                     print(f"{x} / {y} =", x / y)
#             else:
#                 print("两数都为0，不能进行计算！")
#         else:
#             print("除法运算区间为0-19")
# e = div(eval(input("请输入第一个数：")), eval(input("请输入第二个数：")))
# print(e)
# dict={"a":1,"b":2}
# class searchfunction():
#     x = input("请输入搜索内容：")
#     def precisesearch(self,x):
#         self.precisesearch(x)
# b=searchfunction().precisesearch(input("请输入内容："))
# # c=searchfunction().x
# print(b)
# # print(c)
# if searchfunction().x==1:
#     print("q")
# class funtion():
#     def addfuntion(self,x,y):
#         if 200>=x>=100 and 200>=y>=100:
#             print(f"{x} + {y} =",x+y)
#         else:
#             print("加法运算区间为100-200")
#     def sub(self,x,y):
#         if 99 >= x >= 40 and 99 >= y >= 40:
#             print(f"{x} - {y} =", abs(x - y))
#         else:
#             print("减法运算区间为40-99")
#     #乘法函数
#     def mul(self,x,y):
#         if 39 >= x >= 20 and 39 >= y >= 20:
#             print(f"{x} * {y} =", abs(x * y))
#         else:
#             print("乘法运算区间为20-39")
#     #除法函数
#     def div(self,x,y):
#         if 19 >= x >= 0 and 19 >= y >= 0:
#             if y==0:
#                 if x==11 and y==2:
#                     print(f"{x} % {y} =",x%y)
#                 elif x==18 and y==3:
#                     print(f"{x} // {y} =",x//y)
#                 else:
#                     print(f"{x} / {y} =",x/y)
#             else:
#                 print("两数都为0，不能进行计算！")
#         else:
#             print("除法运算区间为0-19")
#     def calcFunction(self,x,operator,y):
#         # x = eval(input("请输入第一个数："))
#         # operator = input("请输入运算符：")
#         # y = eval(input("请输入第二个数："))
#         if 200 >= x >= 0 and 200 >= y >= 0:
#             if 200 >= x >= 0 and 200 >=y >= 0:
#                 if operator == "+":
#                     self.addfuntion(x, y)
#                 elif operator == "-":
#                     self.sub(x, y)
#                 elif operator == "*":
#                     self.mul(x, y)
#                 elif operator == "/":
#                     self.div(x, y)
#                 else:
#                     print("运算符不合法！")
#             else:
#                 print("运算数不在0-200区间范围内")
# if __name__=='__main__':
#     funtion().calcFunction(x = eval(input("请输入第一个数：")),operator = input("请输入运算符："),y = eval(input("请输入第二个数：")))



