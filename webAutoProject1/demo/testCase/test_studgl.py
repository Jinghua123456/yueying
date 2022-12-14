#coding='utf-8'
#学员管理页面的测试用例
import logging
import unittest
from time import sleep

from selenium.webdriver.common.by import By

from common.doLog import Logger
from demo.testCase.baseUnittest import BaseUnitTest

log=Logger(__name__,logging.DEBUG)
class TestStudgl(BaseUnitTest):
    #预约试课
    def test_yysk(self):
        self.loginPage.loginFun()
        sleep(1)
        #点击学员管理
        self.loginPage.gl()
        sleep(1)
        yysk=(By.XPATH,"/html/body/app-root/layout-default/section/app-stu-admin/div/div[1]/div[1]/div[2]/div[2]/div")
        self.loginPage.doClick(yysk)
        #获取url
        self.url=self.driver.current_url
        try:
            # 判断是否是确定页面
            self.assertIn("appointCourse", self.url)
        except Exception as e:
            print("断言失败！原因是:%s" % e)
            log.logger.error("断言失败！原因是:%s" % e, exc_info=True)
        else:
            log.logger.info("断言成功")
    #学员档案
    def test_xyda(self):
        # 登录成功
        self.loginPage.loginFun()
        sleep(1)
       #点击学员管理
        self.loginPage.gl()
        sleep(1)
        #点击学员档案
        self.loginPage.doClick(self.loginPage.stud)
        sleep(1)
        #获取当前页面的url
        self.url=self.driver.current_url
        try:
            # 判断是否是确定页面
            self.assertIn("stuFile", self.url)
        except Exception as e:
            print("断言失败！原因是:%s"%e)
            log.logger.error("断言失败！原因是:%s"%e,exc_info=True)
        else:
            log.logger.info("断言成功")


    # 招生跟进
    def test_zsgj(self):
        # 登录成功
        self.loginPage.loginFun()
        sleep(1)
        # 点击学员管理
        self.loginPage.gl()
        sleep(1)
        # 点击招生跟进
        self.loginPage.doClick(self.loginPage.gj)
        sleep(1)
        # 获取当前页面的url
        self.url = self.driver.current_url
        try:
            # 判断是否是确定页面
            self.assertIn("stuFollow", self.url)
        except Exception as e:
            print("断言失败！原因是:%s"%e)
            log.logger.error("断言失败！原因是:%s"%e,exc_info=True)
        else:
            log.logger.info("断言成功")


    # 学员费用
    def test_xyfy(self):
        # 登录成功
        self.loginPage.loginFun()
        sleep(1)
        # 点击学员管理
        self.loginPage.gl()
        sleep(1)
        # 点击学员档案
        self.loginPage.doClick(self.loginPage.cost1)
        sleep(1)
        # 获取当前页面的url
        self.url = self.driver.current_url
        try:
            # 判断是否是确定页面
            self.assertIn("stuFee", self.url)
        except Exception as e:
            print("断言失败！原因是:%s"%e)
            log.logger.error("断言失败！原因是:%s"%e,exc_info=True)
        else:
            log.logger.info("断言成功")


    # 导入导出
    def test_drdc(self):
        # 登录成功
        self.loginPage.loginFun()
        sleep(1)
        # 点击学员管理
        self.loginPage.gl()
        sleep(1)
        # 点击学员档案
        self.loginPage.doClick(self.loginPage.imp)
        sleep(1)
        # 获取当前页面的url
        self.url = self.driver.current_url
        try:
            # 判断是否是确定页面
            self.assertIn("importStuMenu", self.url)
        except Exception as e:
            print("断言失败！原因是:%s"%e)
            log.logger.error("断言失败！原因是:%s"%e,exc_info=True)
        else:
            log.logger.info("断言成功")



if __name__ == '__main__':
    unittest.main()

