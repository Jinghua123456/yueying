#coding=utf-8'
#百度登录页面测试用例类
from demo.testCase.lxBaseUnittest import Test


class TestLogin(Test):
    #登录成功，用户名，密码正确
    def test_u_ok_p_ok(self):
        self.BaiduloginPage.login("15136762855","l123456789")
        # 获取登录成功后的url
        self.url = self.driver.current_url
        print(self.url)
        # 判断是否是登录成功后的页面信息
        # self.assertIn("", self.url)
