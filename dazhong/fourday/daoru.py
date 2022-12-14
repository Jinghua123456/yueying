# -*- encoding：utf-8 -*-
#导入类（来自包，模块）
# from fourday.class1 import student
# class cd(object):
#     student.info("18","男","张飒")
# from fourday.class1 import student
# class wo():
#     print(student.a)
#

#导入模块
# from fourthday import class2
# class classDemo2(class.father,class.mother):
#     pass
# # 导入classmodel3模块下所有内容
# from fourthday.class1 import *
# class classDe(class.father,class.mother):
#     pass

#引入标准库中的模块
import time,sys,datetime,json
print(sys.path)#打印当前文件位置
#打印时间戳

print(time.time())
print(datetime.datetime.now())#打印当前时间
a={"a":1,'b':2}
print(type(a))
b=json.dumps(a)#dumps把字典转成json字符串
print(type(b))
c=json.loads(b)#loads把json字符串转为字典
print(type(c))




