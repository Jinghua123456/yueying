#coding='utf-8'
from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver

from common.doExcel import DoExcel
from demo.pageObj.basePage import BasePage, testData


testdata1=DoExcel("testData.xlsx","loginData")
#登录页面
class LoginPage(BasePage):
    #用户名
    unameLocator=(By.CSS_SELECTOR,testData.readExcel(1,4))
    # unameLocator=(By.CSS_SELECTOR,"body > app-root > layout-passport > div > div > passport-login > div > form > nz-form-item:nth-child(2) > nz-form-control > div > span > nz-input-group > input")
    #密码
    upwdLocator = (By.CSS_SELECTOR,testData.readExcel(2,4))
    # upwdLocator=(By.CSS_SELECTOR,"body > app-root > layout-passport > div > div > passport-login > div > form > nz-form-item:nth-child(4) > nz-form-control > div > span > nz-input-group > input")
    #登录按钮
    # butLocator=(By.CSS_SELECTOR,"body > app-root > layout-passport > div > div > passport-login > div > form > nz-form-item:nth-child(6) > button")
    butLocator = (By.CSS_SELECTOR,testData.readExcel(3,4))
    #错误信息
    # errorUname=(By.CSS_SELECTOR,".ng-tns-c5-1.ng-trigger.ng-trigger-formExplainAnimation")
    errorUname = (By.CSS_SELECTOR,testData.readExcel(4,4))
    # errorUpwd=(By.CSS_SELECTOR,".ng-tns-c5-2.ng-trigger.ng-trigger-formExplainAnimation")
    errorUpwd = (By.CSS_SELECTOR,testData.readExcel(5,4))
    #错误信息，登录失败是的弹窗信息
    # errorMesage=(By.CSS_SELECTOR,".ant-modal-confirm-title>span")
    errorMesage = (By.CSS_SELECTOR,testData.readExcel(6,4))
    #错误信息,弹窗确定按钮
    # errorBut=(By.CSS_SELECTOR,".ant-modal-confirm-btns>button")
    errorBut = (By.CSS_SELECTOR,testData.readExcel(7,4))

    #登录数据
    logindataList=[[int(testdata1.readExcel(1,1)),int(testdata1.readExcel(1,2))],#用户名、密码正确
                   [int(testdata1.readExcel(2,1)),int(testdata1.readExcel(2,2))],#用户名、密码错误
                   [int(testdata1.readExcel(3,1)),testdata1.readExcel(3,2)],#用户名正确，密码空
                   [int(testdata1.readExcel(4,1)),int(testdata1.readExcel(4,2))],#用户名错误，密码正确
                   [int(testdata1.readExcel(5,1)),int(testdata1.readExcel(5,2))],#用户名正确，密码错误
                   [testdata1.readExcel(6,1),testdata1.readExcel(6,2)],#用户名、密码空
                   [int(testdata1.readExcel(7,1)),int(testdata1.readExcel(7,2))],#用户名长度不足，密码正确
                   [int(testdata1.readExcel(8,1)),int(testdata1.readExcel(8,2))],#用户名长度超出，密码正确
                   [int(testdata1.readExcel(9,1)),int(testdata1.readExcel(9,2))],#用户名正确，密码长度不足
                   [int(testdata1.readExcel(10,1)),int(testdata1.readExcel(10,2))],#用户名正确，密码长度超出
                   [testdata1.readExcel(11,1),int(testdata1.readExcel(11,2))]]#用户名空，密码正确

    #登录方法
    def loginFun(self,vname=logindataList[0][0],vpwd=logindataList[0][1]):
    # def loginFun(self, vname=int(testdata1.readExcel(1,1)), vpwd=int(testdata1.readExcel(1,2))):
        #输入用户名
        self.inputValue(self.unameLocator,vname)
        #输入密码
        self.inputValue(self.upwdLocator,vpwd)
        #点击登录按钮
        self.doClick(self.butLocator)
        sleep(2)

#自测方法
if __name__=="__main__":
    driver = webdriver.Chrome()
    login=LoginPage(driver)
    login.open()
    login.driver.implicitly_wait(3)
    #登陆成功
    login.loginFun()
    # #登录失败
    # # login.loginFun("1233","121121")
    # # login.loginFun("13986128128","123456")
    # #获取弹窗错误信息，并打印
    # errorMesage=login.getElementValue(login.errorMesage)
    # #点击弹窗确定按钮
    # # login.doClick(login.errorBut)
    # #获取错误信息的值，并打印
    # # errorName=login.getElementValue(login.errorUname)
    # # print(errorName)
    # # errorPwd=login.getElementValue((login.errorUpwd))
    # # print(errorPwd)
    # #登录成功
    # # login.loginFun()
    # login.driver.quit()
    print("我的登录数据:",login.logindataList)