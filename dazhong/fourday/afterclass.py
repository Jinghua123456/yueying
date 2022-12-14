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
# #定义类 student
# class student():
#     name="你猜"
#     def __init__(self,age,aex,name):#构析函数
#         self.age=20
#         self.aex="男"
#         self.name="zhaohao"
#       #类方法，后更self
#     def say_name(self):
#         print(self.name)
#        #实例方法，后跟cls
#     @classmethod
#     def my_name(cls):
#         print(cls.name
#        #静态方法，后不用跟self
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
