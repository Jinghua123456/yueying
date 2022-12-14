# -*- encoding：utf-8 -*-
# import random
# c=(random.randint(1,36))
# while True:
#     a=int(input("请输入数字："))
#     if a==c:
#         print("恭喜你，蒙对了！")
#         break
#     elif a>c:
#         print("你猜错了，请输入小一点的数")
#     else :
#         print("你猜错了，请输入大一点的数")
# result=0#求和
# for i in range(1,101):
#  print(i)
#  result=result+i
# print(result)
# a=0#求和
# for i in range(1,101,2):
#   print(i)
#   b=a+i
# print(b)
# result1=0
# for i in range(1,101):
#     if i%2==0:
#         print(i)
#         result1=result1+i
#     print(result1)
# i=5
# a=int(input("q请输入一个数字："))
# while a>i:
#     print("小一点")
#     break
# else:
#     print("大于等于")
# result3=0
# while result3<=10:result3=result3+2
# else:
#     print("大于10")
# def jiafa(a,b):
#     return b+a
# def jiafa(a,b):
#     print("结果:",a+b)
#     return a+b
# a=1
# b=2
# c=jiafa(a,b)
# print(c)
# print("-----------")
# c1=jiafa(a,b)
# print(c1)
# def sub(a=1,b=3):
#     return a*b+b
# print(sub())
# def div(a=1,b=3):
#     a=4
#     b=2
#     print(div())
# def div():
#     x=4
#     y=2
#     print(x/y)
# div()
# def div():
#     x=4
#     y=2
#     return x/y
# div()
# def jia(a,b,c):
#     print("a的值：",a)
#     print("b的值：",b)
#     print("c的值：",c)
# jia(3,21,1)
# def jia1(a,b,c):
#     print("a的值：",a)
#     print("b的值：",b)
#     print("c的值：",c)
# jia1(b=32,a=1,c=6)
# jia1(32,c=3,b=2)
# def jia2(a=1,b=3,c=5):
#     print("a的值：", a)
#     print("b的值：", b)
#     print("c的值：", c)
# jia2()
# def jia3(*args):
#     print(*args)
# jia3(12,3,21,34,4,)
# jia3(1,2,3)
# def jia4(a,*,b,c):
#     print("a的值：",a)
#     print("b的值：",b)
#     print("c的值：",c)
# jia4(32,b=1,c=6)
# def sum1(x=1,y=2):
#     return x+y
# print(sum1())
# sum2=lambda x,y,z:x+y*z
# print(sum2(2,3,1))
# num1 = int(input("请输入一个数字："))
# def mainpage():
#  if num1==1:
#      print("注册")
#  elif num1==2:
#      print("登录")
#  else:
#      print("提示请点击登录或注册")

# dict={"张悦":"1234561","刘远":"1234562","赵浩":"1234563","李歌":"1234564"}
# def regpage():
#      u = input("请输入用户名：")
#      if __name__ == '_main_':
#         print("提示用户名已存在")
#         regpage()
#      elif len(u) < 6 or len(u) > 18:
#          print("提示用户名错误")
#      else:
#          print("提示用户名正确")
# p1 = input("请输入密码：")
# p2 = input("请再次确认密码：")
# def checkpwd(p1,p2):
#
#     if 6 <= len(p1) <= 20 and p1 == p2:
#           print(p1.isdigit())
#     else:
#           print("提示密码错误")
# checkpwd(p1,p1)
dict={"张悦":"1234561","刘远":"1234562","赵浩":"1234563","李歌":"1234564"}
# print(dict.items())
# u = input("请输入用户名：")
# p=input("请输入密码：")
def checkuserandpwd():
    u = input("请输入用户名：")
    p = input("请输入密码：")
    if (u,p) in dict.items():
     print("登录成功")
    else:
        print("提示用户名或密码错误")
checkuserandpwd()
# def checkuserandpwd():
    # u = input("请输入用户名：")
    # p = input("请输入密码：")
  # if dict.keys() == dict.values():
  #       print("登录成功")
# if u in dict.keys():
#     print("用户名正确")
# elif p in dict.values():
#     print("密码正确")
# else:
#     print("请输入正确的用户名")

  # result=checkuserandpwd(u,p)
  #   print(result)


# def regpage():
#     u = input("请输入用户名：")
#     if __name__ == '_main_':
#         if u == dict.keys():
#
#             print("提示用户名已存在")
#         regpage()
#     elif len(u) < 6 or len(u) > 18:
#         print("提示用户名错误")
#     else:
#         print("提示用户名正确")


# def checkpwd():
#     p1 = input("请输入密码：")
#     p2 = input("请再次确认密码：")
#     if 6 <= len(p1) <= 20 and p1 == p2:
#         print(p1.isdigit())
#     else:
#         print("提示密码错误")
# checkpwd()

# def loginpage():
#  u=input("请输入用户名：")
#  p=input("请输入密码：")
# if __name__ == '_main_':
#
#  loginpage()
# def checkuserandpwd():
#   # u = input("请输入用户名：")
#        # p = input("请输入密码：")
#
#
# if dict.keys()==dict.values():
#      print("登录成功")
# else:
#     print("提示用户名或密码错误")
# checkuserandpwd()
# loginpage()
