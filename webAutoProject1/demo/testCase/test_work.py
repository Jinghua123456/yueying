#coding='utf-8'
#雷晓峰工作台测试用例
import logging
import unittest
from time import sleep

from common.doExcel import DoExcel
from common.doLog import Logger

from demo.testCase.baseUnittest import BaseUnitTest




log=Logger(__name__,logging.DEBUG)
testData1=DoExcel()
class TestWork(BaseUnitTest):
    #个人信息
    def test_p(self):
        #登录成功
        self.loginPage.loginFun()
        sleep(1)
        self.driver.implicitly_wait(5)
        #点击个人信息
        self.loginPage.perinfo(self.driver)
        # 获取学员管理页面的url
        self.url = self.driver.current_url
        try:
            # 判断是否是当前页面
            self.assertIn("info", self.url)
        except Exception as e:
            print("断言失败！原因是:%s"%e)
            log.logger.error("断言失败！原因是:%s"%e,exc_info=True)
        else:
            log.logger.info("断言成功")



    #菜单列表
    def test_sg(self):
        # 登录成功
        self.loginPage.loginFun()
        sleep(1)
        self.driver.implicitly_wait(5)
        self.loginPage.gl()
        sleep(1)
        #获取学员管理页面的url
        self.url=self.driver.current_url
        try:
            # 判断是否是当前页面
            self.assertIn("stuAdmin", self.url)
        except Exception as e:
            print("断言失败！原因是:%s"%e)
            log.logger.error("断言失败！原因是:%s"%e,exc_info=True)
        else:
            log.logger.info("断言成功")

    def test_jw(self):
        # 登录成功
        self.loginPage.loginFun()
        sleep(1)
        self.driver.implicitly_wait(5)
        self.loginPage.jwgl()
        sleep(1)
        #获取教务管理页面的url
        self.url=self.driver.current_url
        try:
            # 判断是否是当前页面
            self.assertIn("jiaowuAdmin", self.url)
        except Exception as e:
            print("断言失败！原因是:%s"%e)
            log.logger.error("断言失败！原因是:%s"%e,exc_info=True)
        else:
            log.logger.info("断言成功")


    def test_jg(self):
        # 登录成功
        self.loginPage.loginFun()
        sleep(1)
        self.driver.implicitly_wait(5)
        self.loginPage.jggl()
        sleep(1)
        #获取机构管理页面的url
        self.url=self.driver.current_url
        try:
            # 判断是否是当前页面
            self.assertIn("orgAdmin", self.url)
        except Exception as e:
            print("断言失败！原因是:%s"%e)
            log.logger.error("断言失败！原因是:%s"%e,exc_info=True)
        else:
            log.logger.info("断言成功")


    def test_sj(self):
        # 登录成功
        self.loginPage.loginFun()
        sleep(1)
        self.driver.implicitly_wait(5)
        self.loginPage.sjfx()
        sleep(1)
        # 获取数据分析页面的url
        self.url = self.driver.current_url
        try:
            # 判断是否是当前页面
            self.assertIn("analysisMain", self.url)
        except Exception as e:
            print("断言失败！原因是:%s"%e)
            log.logger.error("断言失败！原因是:%s"%e,exc_info=True)
        else:
            log.logger.info("断言成功")


    def test_zs(self):
        # 登录成功
        self.loginPage.loginFun()
        sleep(1)
        self.driver.implicitly_wait(5)
        self.loginPage.zsb()
        sleep(1)
        # 获取招生吧页面的url
        self.url = self.driver.current_url
        try:
            # 判断是否是当前页面
            self.assertIn("admissionsMain", self.url)
        except Exception as e:
            print("断言失败！原因是:%s"%e)
            log.logger.error("断言失败！原因是:%s"%e,exc_info=True)
        else:
            log.logger.info("断言成功")


    def test_kj(self):
        # 登录成功
        self.loginPage.loginFun()
        sleep(1)
        self.driver.implicitly_wait(5)
        self.loginPage.kjgl()
        sleep(1)
        # 获取考级管理页面的url
        self.url = self.driver.current_url
        try:
            # 判断是否是当前页面
            self.assertIn("kaoJiAdmin", self.url)
        except Exception as e:
            print("断言失败！原因是:%s" % e)
            log.logger.error("断言失败！原因是:%s" % e, exc_info=True)
        else:
            log.logger.info("断言成功")




if __name__ == '__main__':
    unittest.main()