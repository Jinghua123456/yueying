#coding='utf-8'
#百度登录页面的类
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from common.doExcel import DoExcel
from demo.pageObj.basePage import BasePage

#定义DoExcel类
read=DoExcel()
class BaiduLogin(BasePage):
    #用户名
    username=(By.CSS_SELECTOR,"#TANGRAM__PSP_11__userName")
    #密码
    userpass=(By.CSS_SELECTOR,"#TANGRAM__PSP_11__password")

    #登录按钮
    lin=(By.CSS_SELECTOR,"#TANGRAM__PSP_11__submit")

    #错误信息
    #用户名错误信息
    unmessage=(By.CSS_SELECTOR,"#TANGRAM__PSP_11__error")
    #密码错误信息
    upmassage=(By.CSS_SELECTOR,"#TANGRAM__PSP_11__error")

    #登录方法
    def login(self,uname,upass):
        #输入用户名
        self.inputValue(self.username,uname)
        #输入密码
        self.inputValue(self.userpass,upass)
        #点击登录
        self.doClick(self.lin)


if __name__=="__main__":
    driver=webdriver.Chrome()
    bdurl="https://www.baidu.com/"
    #BaiduLogin类的实例化
    baidu=BaiduLogin(driver,bdurl)
    #打开页面
    baidu.open()
    #点击登录
    ln=(By.LINK_TEXT,"登录")
    baidu.doClick(ln)
    #隐式等待
    baidu.driver.implicitly_wait(2)
    #登录
    baidu.login("","")
    # 隐式等待
    baidu.driver.implicitly_wait(2)
    sleep(1)
    #错误信息并打印
    errorMessage=baidu.getElementValue(baidu.unmessage)
    print(errorMessage)
    #关闭
    baidu.driver.quit()

