#coding='utf-8'
#测试登录页面
import logging
import unittest
from time import sleep

from common.doLog import Logger
from demo.testCase.baseUnittest import BaseUnittest

log=Logger(__name__,logging.INFO)
class TestLogin(BaseUnittest):
    #登录成功
    def test_n_ok_p_ok(self):
        self.loginpage.longin()
        self.driver.implicitly_wait(3)
        sleep(1)
        #获取登录成功后的url
        self.url=self.driver.current_url
        try:
            #判断是否登录成功
            self.assertIn("com",self.url)
        except Exception as e:
            log.logger.exception("断言失败！%s"%e,exc_info=True)
            self.loginpage.photo("_faile")
        else:
            log.logger.info("断言成功！")
            self.loginpage.photo("_pass")

    #登录失败，用户名，密码都为空
    def test_n_no_p_no(self):
        # self.loginpage.longin("","")
        self.loginpage.longin(self.loginpage.logindataList[1][0], self.loginpage.logindataList[1][1])
        self.driver.implicitly_wait(3)
        sleep(1)
        #判断是否登录成功
        messageText=self.loginpage.getValue(self.loginpage.unmessage)
        try:
            #判断是否登录成功
            self.assertEqual("请您输入手机号/用户名/邮箱",messageText)
        except Exception as e:
            log.logger.exception("断言失败！%s"%e,exc_info=True)
            self.loginpage.photo("_faile")
        else:
            log.logger.info("断言成功！")
            self.loginpage.photo("_pass")


    # 登录失败，用户名正确，密码都为空
    def test_n_ok_p_no(self):
        # self.loginpage.longin("18203694633","" )
        self.loginpage.longin(self.loginpage.logindataList[2][0], self.loginpage.logindataList[2][1])
        self.driver.implicitly_wait(3)
        sleep(1)
        # 判断是否登录成功
        messageText = self.loginpage.getValue(self.loginpage.unmessage)
        try:
            #判断是否登录成功
            self.assertEqual("请您输入密码", messageText)
        except Exception as e:
            log.logger.exception("断言失败！%s"%e,exc_info=True)
            self.loginpage.photo("_faile")
        else:
            log.logger.info("断言成功！")
            self.loginpage.photo("_pass")


   # 登录失败，用户名正确，密码错误
    def test_n_ok_p_c(self):
        # self.loginpage.longin("18203694633","123456l")
        self.loginpage.longin(self.loginpage.logindataList[3][0], self.loginpage.logindataList[4][1])
        self.driver.implicitly_wait(3)
        sleep(1)
        # 判断是否登录成功
        messageText = self.loginpage.getValue(self.loginpage.unmessage)
        try:
            #判断是否登录成功
            self.assertEqual("请您输入密码", messageText)
        except Exception as e:
            log.logger.exception("断言失败！%s"%e,exc_info=True)
            self.loginpage.photo("_faile")
        else:
            log.logger.info("断言成功！")
            self.loginpage.photo("_pass")

 # 登录失败，用户名空，密码正确
    def test_n_no_p_ok(self):
        # self.loginpage.longin("","Lzp123456")
        self.loginpage.longin(self.loginpage.logindataList[4][0], self.loginpage.logindataList[4][1])
        self.driver.implicitly_wait(3)
        sleep(1)
        # 判断是否登录成功
        messageText = self.loginpage.getValue(self.loginpage.unmessage)
        try:
            #判断是否登录成功
            self.assertEqual("请您输入手机号/用户名/邮箱", messageText)
        except Exception as e:
            log.logger.exception("断言失败！%s"%e,exc_info=True)
            self.loginpage.photo("_faile")
        else:
            log.logger.info("断言成功！")
            self.loginpage.photo("_pass")


if __name__ == '__main__':
    unittest.main()