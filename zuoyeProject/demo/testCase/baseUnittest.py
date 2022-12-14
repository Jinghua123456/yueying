#coding='utf-8'
#基础的unittest.前置后置方法,（测试夹具）
import unittest
from time import sleep

from selenium import webdriver

from demo.pageObj.loginPage import LoginPage


class BaseUnittest(unittest.TestCase):
    #类的前置方法
    @classmethod
    def setUpClass(cls) -> None:
        #实例化浏览器
        cls.driver=webdriver.Chrome()
        cls.driver.maximize_window()
    #类的后置方法
    @classmethod
    def tearDownClass(cls) -> None:
        #退出浏览器
        cls.driver.quit()
    #方法级别的前置
    def setUp(self) -> None:
        #登录页面的实例化
        self.loginpage=LoginPage(self.driver)
        #打开页面
        self.loginpage.open()
    # 方法级别的后置
    def tearDown(self) -> None:
        #刷新页面
        self.driver.refresh()
        sleep(1)