#coding='utf-8'
#百度登录页面
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.doExcel import DoExcel
from demo.pageObj.basePage import BasePage

#数据驱动，调用表1
readdata=DoExcel()
#调用表1
readdata1=DoExcel("testDatas.xlsx","logindata")
class LoginPage(BasePage):
    #登录按钮，进入登录页面
    # lipg=(By.LINK_TEXT,"登录")
    lipg=(By.CSS_SELECTOR,readdata.readExxcel(1,4))
    #用户名
    # username=(By.CSS_SELECTOR,"#TANGRAM__PSP_11__userName")
    username = (By.CSS_SELECTOR,readdata.readExxcel(2,4))
    #密码
    # userpwd=(By.CSS_SELECTOR,"#TANGRAM__PSP_11__password")
    userpwd = (By.CSS_SELECTOR, readdata.readExxcel(3, 4))
    #登录按钮
    # lin=(By.CSS_SELECTOR,"#TANGRAM__PSP_11__submit")
    lin=(By.CSS_SELECTOR, readdata.readExxcel(4, 4))
    #登录失败，错误信息
    # unmessage=(By.CSS_SELECTOR,"#TANGRAM__PSP_11__error")
    # unmessage=(By.CSS_SELECTOR,"#TANGRAM__PSP_11__error")
    unmessage=(By.CSS_SELECTOR, readdata.readExxcel(5, 4))

    #登录数据
    logindataList=[[int(readdata1.readExxcel(1,1)),readdata1.readExxcel(1,2)],#用户名、密码都正确
                   [readdata1.readExxcel(2, 1), readdata1.readExxcel(2, 2)],#用户名、密码都为空
                   [int(readdata1.readExxcel(3, 1)), readdata1.readExxcel(3, 2)],#用户名正确，密码空
                   [int(readdata1.readExxcel(4, 1)), readdata1.readExxcel(4, 2)],#用户名正确，密码错误
                   [readdata1.readExxcel(5, 1), readdata1.readExxcel(5, 2)]]#用户名空，密码正确

    #登录方法
    # def longin(self,uname="18203694633",upwd="Lzp123456"):
    def longin(self, uname=logindataList[0][0], upwd=logindataList[0][1]):
        #点击登录进入登录页面
        self.doClick(self.lipg)
        #输入用户名
        self.inputWenben(self.username,uname)
        #输入密码
        self.inputWenben(self.userpwd,upwd)
        #点击登录按钮
        self.doClick(self.lin)

if __name__ == '__main__':
    driver=webdriver.Chrome()
    #LoginPage的实例化，调用
    baidu=LoginPage(driver)
    #打开页面
    baidu.open()
    sleep(1)
    #登录成功
    baidu.longin()

    #登录失败，并打印错误信息
    # baidu.longin("1513676233","")
    sleep(1)
    errormessage=baidu.findElement(baidu.unmessage)
    print(errormessage)
    #关闭浏览器
    baidu.driver.quit()

