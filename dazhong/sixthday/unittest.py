# -*- encoding：utf-8 -*-
# import unittest#导入unittest
# #定义测试类，并继承TestCase
# class TestDemo(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls) -> None:#只在开始运行
#         print("这是：setUpClass")
#     @classmethod#静态方法
#     def tearDownClass(cls) -> None:#只在结尾运行
#         print("这是：tearDownClass")
#     def setUp(self) -> None:
#         print("这是初始化方法")
#     def tearDown(self) -> None:
#         print("这是结束清理方法")
#    # 定义测试用例方法（以test开头）
#     def test_A01(self):
#         print("我是测试用例：test_A01")
#     def test_B01(self):
#         print("我是测试用例：test_B01")
#     def test_12(self):
#         print("我是测试用例：test_12")
#     def test_32(self):
#         print("我是测试用例：test_32")
# if __name__ == '__main__':
#     unittest.main()




#导入unittest
import unittest
#定义测试用例类，并继承TestCase类
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("我是setUpClass")
    @classmethod
    def tearDownClass(cls) -> None:
        print("我是tearDownClass")
    def setUp(self) -> None:
        print("我是初始化方法")
    def tearDown(self) -> None:
        print("我是结束清理方法")
    #定义测试用例方法
    def test_a001(self):
        print("我是测试用例：test_a001")
    def test_A002(self):
        print("我是测试用例：test_A002")
        self.assertEqual(1,2)
    def test_A003(self):
        print("我是测试用例：test_A003")
    def test_A004(self):
        print("我是测试用例：test_A004")

if __name__ == '__main__':
    unittest.main()