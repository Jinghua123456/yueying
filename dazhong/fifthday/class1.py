# -*- encoding：utf-8 -*-
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

#
# class page():
#     def checkuandp(self,u, p):
#         if u in dict.keys():
#             if p == dict[u]:
#                 return "登录成功"
#             else:
#                 return "用户名或密码不一致"
#         else:
#             return "用户名或密码不一致！"
#
#     # 定义登录函数
#     def loginpage(self):
#         u = input("请输入用户名：")
#         p = input("请输入密码：")
#         print(dict.keys())
#         result = checkuandp(u, p)
#         print(result)
#
#     # 定义注册函数
#     def regpage(self):
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
#
#     # 我的页面
#     def mainpage(self):
#         num1 = int(input("请输入一个数字:"))
#         if num1 == 1:
#             loginpage()  # 登录函数
#         elif num1 == 2:
#             regpage()  # 注册函数
#         else:
#             print("请点击注册或登录")
#
#     # 主程序入口
#     if __name__ == '__main__':
#         mainpage()
