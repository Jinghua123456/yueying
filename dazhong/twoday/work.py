# -*- encoding：utf-8 -*-
# b=int(input("请输入一个数："))
# for a in range(0,201):
#    if 0<=b<=200:
#     print(b)
# else:
#     print("运算数不在0-200区间范围内")

# b1=int(input("请输入一个数："))
# for a1 in range(100,201):
#     if 100<=b1<=200:
#         print(f"{a1}+{b1}={a1+b1}")
#     else:
#         print("加法运算区间为100-200")

# b2=int(input("请输入一个数："))
# for a2 in range(40,100):
#     if 40<=b2<=99:
#         print(f"{a2}-{b2}={abs(a2-b2)}")
#     else:
#         print("减法运算区间为40-99")

# b3=int(input("请输入一个数："))
# for a3 in range(20,40):
#     if 20<=b3<=40:
#         print(f"{a3}*{b3}={a3*b3}")
#     else:
#         print("乘法运算区间为20-40")

# b4=int(input("请输入一个数："))
# for a4 in range(0,20):
#     if a4 ==0:
#         print("除数为0，不能进行出发运算")
#     elif 0 <= b4 <= 20:
#         print(f"{b4} / {a4}={b4/a4}")
#     elif b4==11:
#         if a4==2:
#             print(f"{11}%{2}={11%2}")
#         elif b4==18:
#             if a4==3:
#                 print(f"{18}//{3}={18 // 3}")
#     else:
#         print("乘法运算区间为20-40")

# Login Page登录页面
# Registration page注册页面
# Main page主页面

# user = input("请输入用户名：")
# pwd = input("请输入密码：")

#
# dict={"张悦":"1234561","刘远":"1234562","赵浩":"1234563","李歌":"1234564"}
# # num1 = int(input("请输入一个数字："))
# # u = input("请输入用户名：")
#
# def regpage():
#      u = input("请输入用户名：")
#      if u in dict.keys():
#          print("提示用户名已存在")
#
#      elif len(u)<6 or len(u)>18:
#          print("提示用户名错误")
#      else:
#          print("提示用户名正确")
#
# regpage()
# def checkpwd():
#         p1=input("请输入密码：")
#         p2=input("请再次确认密码：")
#         if  6<=len(p1)<=20 and p1==p2:
#             print(p1.isdigit())
#         else:
#             print("提示密码错误")
# checkpwd()
# def loginpage():
#     u=input("请输入用户名：")
#     p=input("请输入密码：")
#     if (u,p)in dict.items():
#      print("登录成功")
#     else:
#         print("提示用户名或密码错误")
# loginpage()
# def mainpage():
#  num1 = int(input("请输入一个数字："))
#  if num1==1:
#      loginpage()
#  elif num1==2:
#      regpage()
#  else:
#      print("提示请点击登录或注册")
# mainpage()
#
# if __name__ =='_main_':
#     mainpage()
dict={"张悦":"1234561","刘远":"1234562","赵浩":"1234563","李歌":"1234564"}
def checkuandp(u,p):
    if u in dict.keys():
        if p==dict[u]:
            return "登录成功"
        else:
            return "用户名或密码不一致"
    else:
        return "用户名或密码不一致！"
#定义登录函数
def loginpage():
    u = input("请输入用户名：")
    p = input("请输入密码：")
    print(dict.keys())
    result=checkuandp(u,p)
    print(result)
#定义注册函数
def regpage():
    u = input("请输入用户名：")
    if 6<=len(u)<=18:
        if u not in dict.keys():
            p = input("请输入密码：")
            if 6<=len(p)<=20:
                if p.isdigit():
                    return "密码不能纯数字"
                else:
                    p1=int(input("请再次输入密码："))
                    if p==p1:
                        return "注册成功"
                    else:
                        return "两次密码不一致"
            else:"请输入密码，6-20位"
        else:
            return "用户名已存在"
    else:
        return "用户名不符合规则"

#我的页面
def mainpage():
    num1=int(input("请输入一个数字:"))
    if num1==1:
     loginpage()# 登录函数
    elif num1==2:
     regpage()#注册函数
    else:
        print("请点击注册或登录")
#主程序入口
if __name__=='__main__':
    mainpage()
