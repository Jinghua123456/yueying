# -*- encoding：utf-8 -*-
# dict={"张悦":"1234561","刘远":"1234562","赵浩":"1234563","李歌":"1234564"}
#
# class checkuandp():
#  def __init__(self,u,p):
#     if u in dict.keys():
#         if p == dict[u]:
#             print("登录成功")
#         else:
#             print("用户名或密码不一致")
#     else:
#         print("用户名或密码不一致！")
#
# #注册
# class regpage():
#     def regpage1(self):
#         u = input("请输入用户名：")
#         if 6 <= len(u) <= 18:
#             p = input("请输入密码：")
#             if u not in dict.keys():
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
#
# #我的页面
# class mainpage():
#  def __init__(self,num1):
#         # num1 = int(input("请输入一个数字:"))
#         if num1 == 1:
#             a = checkuandp(input("请输入用户名："),input("请输入密码："))
#             print(a) # 登录函数
#         elif num1 == 2:
#             b = regpage().regpage1()
#             print(b)  # 注册函数
#         else:
#             print("请点击注册或登录")
#
# # 主程序入口
# if __name__ == '__main__':
#     e=mainpage(int(input("请输入一个数字:")))
#     print(e)
#
# #加法
# class add():
#     def __init__(self,x,y):
#         if 200 >= x >= 100 and 200 >= y >= 100:
#             print(f"{x} + {y} =", x + y)
#         else:
#             print("加法运算区间为100-200")
#
# # print(b)
# #减法
# class sub():
#     def __init__(self,x,y):
#         if 99 >= x >= 40 and 99 >= y >= 40:
#             print(f"{x} - {y} =", abs(x - y))
#         else:
#             print("减法运算区间为40-99")
#
# # print(c)
# #乘法
# class mul():
#     def __init__(self,x,y):
#         if 39 >= x >= 20 and 39 >= y >= 20:
#             print(f"{x} * {y} =", abs(x * y))
#         else:
#             print("乘法运算区间为20-39")
#
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
#
# # print(e)
#
# class calcFunction():
#     def __init__(self,x,operator,y):
#         if 200 >= x >= 0 and 200 >=y >= 0:
#             if operator == "+":
#                 b=add(eval(input("请输入第一个数：")), eval(input("请输入第二个数：")))
#                 print(b)
#             elif operator == "-":
#                 c = sub(eval(input("请输入第一个数：")), eval(input("请输入第二个数：")))
#                 print(c)
#             elif operator == "*":
#                 d = mul(eval(input("请输入第一个数：")), eval(input("请输入第二个数：")))
#                 print(d)
#             elif operator == "/":
#                 e = div(eval(input("请输入第一个数：")), eval(input("请输入第二个数：")))
#                 print(e)
#             else:
#                 print("运算符不合法！")
#         else:
#             print("运算数不在0-200区间范围内")
# # a=calcFunction(eval(input("请输入第一个数：")),input("请输入运算符："),eval(input("请输入第二个数：")))
# # print(a)
# if __name__ == '__main__':
#     a=calcFunction(eval(input("请输入第一个数：")),input("请输入运算符："),eval(input("请输入第二个数：")))
#     # print(a)

# class searchfunction():
#     x = input("请输入搜索内容：")
#     def precisesearch(self,x):
#         self.precisesearch(x)
#
#     def fuzzysearch(self):
#         self.fuzzysearch()
#         # if self.x is self.fuzzysearch():
#         #     print("显示包含词汇的内容")
#     def combinationsearch(self):
#         self.combinationsearch()
#         # if self.x is self.combinationsearch():
#         #     print("显示搜索内容")
#     def sensitivetermsearch(self):
#         self.sensitivetermsearch()
#         if self.x is self.sensitivetermsearch():
#             print("搜索内容不合法，请重新输入词汇")
    # def emptysearch(self):
    #     self.emptysearch()
    #     # if self.x is self.emptysearch():
    #     #     print("没有找到小主想要的")
    #     if self.x is self.precisesearch(input("请输入搜索内容：")):
    #         print("显示搜搜的全部内容")
    #     elif self.x is self.fuzzysearch():
    #         print("显示包含词汇的内容")
    #     elif self.x is self.combinationsearch():
    #         print("显示搜索内容")
    #     elif self.x is self.sensitivetermsearch():
    #         print("搜索内容不合法，请重新输入词汇")
    #     else:
    #         print("没有找到小主想要的")
# 定义类 student
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

class student():
    def info(self,age,sex,name):
        print(age)
        print(sex)
        print(name)
# #类的实例化
a=student()
#类方法入参
print(a.info("18","男","张飒"))






