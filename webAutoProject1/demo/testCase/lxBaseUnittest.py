#coding='utf-8'
import unittest

from selenium import webdriver

from demo.pageObj.baiduLoginPage import BaiduLogin




class Test(unittest.TestCase):
    #类方法的前置
    @classmethod
    def setUpClass(cls) -> None:
        #浏览器的实例化
        cls.driver=webdriver.Chrome()
        #最大化
        cls.driver.maximize_window()
    #类方法的后置
    @classmethod
    def tearDownClass(cls) -> None:
        #退出浏览器
        cls.driver.quit()
    #方法级别的前置
    def setUp(self) -> None:
        #登录页面实例化
        self.BaiduloginPage=BaiduLogin(self.driver)
        #打开页面
        self.BaiduloginPage.open()
    #方法级别的后置
    def tearDown(self) -> None:
        #刷新页面
        self.driver.refresh()