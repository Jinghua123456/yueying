#coding='utf-8'
import logging
import unittest
from time import sleep

from common.doLog import Logger
from demo.testCase.baseUnittest import BaseUnitTest
#第一步执行的代码：setUpClass（）类前置
#第二步执行的代码：setUp（） 方法前置
#第三步执行的代码是测试方法 OK
#第四步执行测试方法中的代码，直到完毕
#第五步执行代码：tearDown（）方法后置
#第六步，找还有没有测试方法。有，执行setUp（） 方法前置
#第七步，第六步有，执行测试方法中的代码，直到完毕
#第八步，第六步有，执行tearDown（）方法后置
#第九步，找还有没有测试方法。无，执行的代码是：tearDownClass（）类后置


log=Logger(__name__,logging.INFO)
#登录页面测试用例类
class TestLogin(BaseUnitTest):

    #登录成功用户名、密码均正确
    def test_login_name_pwd_ok(self):
        self.loginPage.loginFun()
        self.driver.implicitly_wait(5)
        sleep(1)
        #获取登录成功后的url
        self.url=self.driver.current_url
        try:
            #判断是否是登录成功后的页面信息
            self.assertIn("",self.url)
        except Exception as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
            # 退出登录
            self.loginPage.logoutFun(self.driver)
#dashboard


        sleep(1)
    #登录失败用户名空，密码空
    def test_login_name_no_pwd_on(self):
        self.loginPage.loginFun(self.loginPage.logindataList[5][0],self.loginPage.logindataList[5][1])
        try:
            # 断言
            # 判断是否登录失败
            #  判断手机号
            nameText = self.loginPage.getElementValue(self.loginPage.errorUname)
            self.assertEqual("请输入手机号码", nameText)
            # 判断密码
            pwdText = self.loginPage.getElementValue(self.loginPage.errorUpwd)
            self.assertEqual("请输入6-20位账户密码", pwdText)
        except Exception as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
    # #登录失败用户名空，密码正确
    # def test_login_name_no_pwd(self):
    #     self.loginPage.loginFun(self.loginPage.logindataList[10][0],self.loginPage.logindataList[10][1])
    #     # self.loginPage.loginFun("", "121121")
    #     #判断是否登录失败
    #     #  判断手机号
    #     nameText=self.loginPage.getElementValue(self.loginPage.errorUname)
    #     self.assertEqual("请输入手机号码",nameText)
        #判断密码
        # pwdText=self.loginPage.getElementValue(self.loginPage.errorUpwd)
        # self.assertEqual("请输入6-20位账户密码",pwdText)
    #登录失败用户名正确，密码空
    def test_login_name_pwd_on(self):
        self.loginPage.loginFun(self.loginPage.logindataList[2][0],self.loginPage.logindataList[2][1])
        try:
            # 断言
            # 判断是否登录失败
            #  判断手机号
            # nameText = self.loginPage.getElementValue(self.loginPage.errorUname)
            # self.assertEqual("请输入手机号码", nameText)
            # 判断密码
            pwdText = self.loginPage.getElementValue(self.loginPage.errorUpwd)
            self.assertEqual("请输入6-20位账户密码", pwdText)
        except Exception as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
        #判断是否登录失败
        #  判断手机号
        # nameText=self.loginPage.getElementValue(self.loginPage.errorUname)
        # self.assertEqual("请输入手机号码",nameText)

        # self.loginPage.loginFun("int(testdata1.readExcel(1,1))", "")
        #判断密码
        # pwdText=self.loginPage.getElementValue(self.loginPage.errorUpwd)
        # self.assertEqual("请输入6-20位账户密码",pwdText)
    #登录失败用户名错误（已存在），密码正确
    def test_login_name_t_pwd_on(self):
        self.loginPage.loginFun(self.loginPage.logindataList[3][0],self.loginPage.logindataList[3][1])
        # 获取弹窗错误信息
        errText=self.loginPage.getElementValue(self.loginPage.errorMesage)
        try:
            # 断言弹窗错误信息
            self.assertIn("用户名或密码错误",errText)
        except Exception as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
            # 点击弹窗中的确定按钮
            self.loginPage.doClick(self.loginPage.errorBut)





        # self.loginPage.loginFun("int(testdata1.readExcel(2,1))", "int(testdata1.readExcel(1,2))")
        # # 判断是否登录失败
        # #  判断手机号
        # nameText=self.loginPage.getElementValue(self.loginPage.errorUname)
        # self.assertEqual("请输入手机号码",nameText)
    #登录失败用户名正确，密码错误
    def test_login_name_ok_pwd_on(self):
        self.loginPage.loginFun(self.loginPage.logindataList[4][0],self.loginPage.logindataList[4][1])
        # 获取弹窗错误信息
        errText = self.loginPage.getElementValue(self.loginPage.errorMesage)
        try:
            # 断言弹窗错误信息
            self.assertIn("用户名或密码错误",errText)
        except Exception as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
            # 点击弹窗中的确定按钮
            self.loginPage.doClick(self.loginPage.errorBut)

        # # 断言弹窗错误信息
        # self.assertIn("用户名或密码错误", errText)
        # # 点击弹窗中的确定按钮
        # self.loginPage.doClick(self.loginPage.errorBut)

        # self.loginPage.loginFun("int(testdata1.readExcel(1,1))", "int(testdata1.readExcel(2,2))")
        # #  判断手机号
        # nameText = self.loginPage.getElementValue(self.loginPage.errorUname)
        # self.assertEqual("请输入手机号码", nameText)

    #登录失败用户名错误，密码错误
    def test_login_name_on_pwd_on(self):
        self.loginPage.loginFun(self.loginPage.logindataList[1][0], self.loginPage.logindataList[1][1])
        # 获取弹窗错误信息
        errText = self.loginPage.getElementValue(self.loginPage.errorMesage)

        try:
            # 断言弹窗错误信息
            self.assertIn("用户名或密码错误",errText)
        except Exception as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
            # 点击弹窗中的确定按钮
            self.loginPage.doClick(self.loginPage.errorBut)

        # # 断言弹窗错误信息
        # self.assertIn("用户名或密码错误", errText)
        # # 点击弹窗中的确定按钮
        # self.loginPage.doClick(self.loginPage.errorBut)

        # self.loginPage.loginFun("int(testdata1.readExcel(2,1))", "int(testdata1.readExcel(2,2))")
        # #  判断手机号
        # nameText = self.loginPage.getElementValue(self.loginPage.errorUname)
        # self.assertEqual("请输入手机号码", nameText)

    #用户名长度不足，密码正确
    def test_login_name_on1_pwd_on(self):
        self.loginPage.loginFun(self.loginPage.logindataList[6][0], self.loginPage.logindataList[6][1])
        try:
            # 断言
            # 判断是否登录失败
            #  判断手机号
            nameText = self.loginPage.getElementValue(self.loginPage.errorUname)
            self.assertEqual("请输入手机号码", nameText)
            # 判断密码
            # pwdText = self.loginPage.getElementValue(self.loginPage.errorUpwd)
            # self.assertEqual("请输入6-20位账户密码", pwdText)
        except Exception as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")

        # #  判断手机号
        # nameText = self.loginPage.getElementValue(self.loginPage.errorUname)
        # self.assertEqual("请输入手机号码", nameText)

    #用户名长度超出，密码正确
    def test_login_name_on2_pwd_on(self):
        self.loginPage.loginFun(self.loginPage.logindataList[7][0], self.loginPage.logindataList[7][1])
        # 获取弹窗错误信息
        errText = self.loginPage.getElementValue(self.loginPage.errorMesage)
        try:
            # 断言弹窗错误信息
            self.assertIn("用户名或密码错误", errText)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")
            # 点击弹窗中的确定按钮
            self.loginPage.doClick(self.loginPage.errorBut)

        # # 断言弹窗错误信息
        # self.assertIn("用户名或密码错误", errText)
        # # 点击弹窗中的确定按钮
        # self.loginPage.doClick(self.loginPage.errorBut)

    #用户名正确，密码长度不足
    def test_login_name_on_pwd_on1(self):
        self.loginPage.loginFun(self.loginPage.logindataList[8][0], self.loginPage.logindataList[8][1])
        try:
            # 断言
            # 判断是否登录失败
            # 判断密码
            pwdText = self.loginPage.getElementValue(self.loginPage.errorUpwd)
            self.assertEqual("请输入6-20位账户密码", pwdText)
        except Exception as e:
            log.logger.exception("断言失败：%s"%e,exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")

        #判断密码
        # pwdText=self.loginPage.getElementValue(self.loginPage.errorUpwd)
        # self.assertEqual("请输入6-20位账户密码",pwdText)

    #用户名正确，密码长度超出
    def test_login_name_on_pwd_on2(self):
        self.loginPage.loginFun(self.loginPage.logindataList[9][0], self.loginPage.logindataList[9][1])
        # 获取弹窗错误信息
        errText = self.loginPage.getElementValue(self.loginPage.errorMesage)
        try:
            # 断言弹窗错误信息
            self.assertIn("用户名或密码错误", errText)
        except Exception as e:
            log.logger.exception("断言失败：%s" % e, exc_info=True)
            self.loginPage.doPhoto("_faile")
        else:
            log.logger.info("断言成功")
            self.loginPage.doPhoto("_pass")

        # 点击弹窗中的确定按钮
        self.loginPage.doClick(self.loginPage.errorBut)

        # 断言弹窗错误信息
        # self.assertIn("用户名或密码错误", errText)
        # # 点击弹窗中的确定按钮
        # self.loginPage.doClick(self.loginPage.errorBut)




if __name__ == '__main__':
    unittest.main()
