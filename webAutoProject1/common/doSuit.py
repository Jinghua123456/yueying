#coding='utf-8'
#testSuit的添加方法
import unittest

from common import config
from demo.testCase.test_login import TestLogin
from demo.testCase.test_studgl import TestStudgl
from demo.testCase.test_work import TestWork


#通过测试类及测试方法添加用例
def addTestByMethod(suit):
    # suit=unittest.TestSuite()
    suit.addTest(TestLogin("test_login_name_pwd_ok"))
    suit.addTest(TestLogin("test_login_name_no_pwd_on"))
    # print(suit)
    return suit


#通过测试类的方法添加用例
def addTestByClass(suit):
    # suit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin))
    # suit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestStudgl))
    suit.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(TestWork))
    return suit



#使用第三种方法获取装满用例的箱子
def addTestByAuto():
    suit=unittest.TestLoader().discover(config.test_path,pattern="test*.py")
    return suit




#定义空箱子
suit1=unittest.TestSuite()

#向空箱子里添加用例，通过一个个用例名添加
#箱子里添加用例后，重命名为suit2
suit2=addTestByMethod(suit1)
#打印出装好用例的箱子里的内容
print("我调用的是第一个方法",suit2)

#向空箱子里添加用例，通过测试用例类名称的形式添加
#箱子里添加用例后，重命名为suit3
suit3=addTestByMethod(suit1)
#打印出装好用例的箱子里的内容
print("我调用的是第二个方法",suit3)



#通过py文件自动匹配的方式，集合用例并打包成一个箱子
suit4=addTestByAuto()
print("我调用的是第三个方法",suit4)