# -*- encoding：utf-8 -*-
#unittest:unittest(测试套件），用例执行顺序，按照添加的先后顺序取执行（不遵循ASCII码）
import unittest
from sixthday.unittest import TestDemo
def suitetest():
    # 定义测试套件
    suite=unittest.TestSuite
    #添加测试用例到测试套件
    suite.addTest(TestDemo("test_A01"))
    suite.addTest(TestDemo("test_B01"))
    #y运行测试套件
    unittest.TextTestRunner().run(suite)
suitetest()
#
# """
# unittest:testSuite(测试套件),用例执行顺序，按照添加的先后顺序去执行(不在遵循ASCII码)
# """
# import unittest
# from sixthday.unittest import TestDemo
# def suiteMoudel():
#     #定义测试套件
#     suite=unittest.TestSuite()
#     #添加用例到测试套件
#     suite.addTest(TestDemo("test_a001"))
#     suite.addTest(TestDemo("test_A002"))
#     suite.addTest(TestDemo("test_A004"))
#     #运行测试套件
#     unittest.TextTestRunner().run(suite)
# suiteMoudel()