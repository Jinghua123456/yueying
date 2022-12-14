#coding='utf-8'
#基础页面类：存放所有页面可能用到的公共方法及属性
#所有page类均继承该基础类
import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import config
from common.doExcel import DoExcel
from common.doLog import Logger


#定义log对象
log=Logger(__name__,logging.ERROR)
#元素定位数据
testData=DoExcel()

class BasePage(object):
    #定位登录成功后右上角退出按钮
    #右上角的个人头像
    # img = (By.CSS_SELECTOR, ".teachHeadPic.ng-star-inserted")
    img = (By.CSS_SELECTOR,testData.readExcel(8,4))
    #个人信息
    per=(By.CSS_SELECTOR,"#headerH > div:nth-child(2) > div:nth-child(5) > div.userInfo-popPanel > div:nth-child(1)")
    # 退出账号
    # logout=(By.XPATH,"//div[text()='退出账号']")
    # logout=(By.CSS_SELECTOR,".userInfo-popPanel>:nth-child(4)")
    logout = (By.CSS_SELECTOR,testData.readExcel(9,4))

    # 退出账号的弹窗的确定按钮
    # logoutOk = (By.CSS_SELECTOR, ".ant-modal-confirm-btns>button:nth-child(2)")
    logoutOk = (By.CSS_SELECTOR,testData.readExcel(10,4))

    # 学员管理
    # sg = (By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.flex_H_Center.nav1.dis.ng-star-inserted > span")
    sg = (By.CSS_SELECTOR,testData.readExcel(11,4))
    # 学员档案
    # stud = (By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.nav2.ng-star-inserted > div:nth-child(1)")
    stud=(By.CSS_SELECTOR,testData.readExcel(12,4))
    # 招生跟进
    # gj = (By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.nav2.ng-star-inserted > div:nth-child(2)")
    gj=(By.CSS_SELECTOR,testData.readExcel(13,4))
    # 学员费用
    # cost = (By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.nav2.ng-star-inserted > div:nth-child(3)")
    cost1=(By.CSS_SELECTOR,testData.readExcel(14,4))
    # 导入/导出
    # imp = (By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.nav2.ng-star-inserted > div:nth-child(4)")
    imp=(By.CSS_SELECTOR,testData.readExcel(15,4))
    # 新生统计
    # count = (By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.nav2.ng-star-inserted > div:nth-child(3)")
    count1=(By.CSS_SELECTOR,testData.readExcel(16,4))
    # 费用完结统计
    # free1= (By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.nav2.ng-star-inserted > div:nth-child(4)")
    free1=(By.CSS_SELECTOR,testData.readExcel(17,4))
    # 教务管理
    # jw = (By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(4) > div.flex_H_Center.nav1.dis.ng-star-inserted > span")
    jw=(By.CSS_SELECTOR,testData.readExcel(18,4))
    # 管理机构
    # jg = (By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(4) > div.flex_H_Center.nav1.dis.ng-star-inserted > span")
    jg=(By.CSS_SELECTOR,testData.readExcel(19,4))
    # 数据分析
    # sj = (By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(5) > div.flex_H_Center.nav1.dis.ng-star-inserted > span")
    sj=(By.CSS_SELECTOR,testData.readExcel(20,4))
    # 招生吧
    # zs = (By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(6) > div.flex_H_Center.nav1.dis.ng-star-inserted > span")
    zs=(By.CSS_SELECTOR,testData.readExcel(21,4))
    # 考级管理
    # kj = (By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(10) > div.flex_H_Center.nav1.dis.ng-star-inserted > span")
    kj=(By.CSS_SELECTOR,testData.readExcel(22,4))
    #重构初始化方法
    def __init__(self,driver,url=config.base_url):

        self.driver=driver
        self.url=url

    #打开页面
    def open(self):
        try:
            self.driver.get(self.url)
        except Exception as e:
            print("异常发生，页面打开失败，失败内容是:%s\n失败的页面是:%s"%(e,self.url))
            log.logger.critical("异常发生，页面打开失败，失败内容是:%s\n失败的页面是:%s"%(e,self.url),exc_info=True)
        else:
            print("未发生异常，页面打开成功! %s"%self.url)
            log.logger.info("未发生异常，页面打开成功! %s"%self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)

    #定位元素
    def findElement(self,*locater):
        try:
            ele=WebDriverWait(self.driver,5,0.1).until(EC.visibility_of_element_located(locater))
        except Exception as e:
            print("元素定位失败，错误信息是:%s\n该元素是:%s"%(e,str(locater)))
            log.logger.error("元素定位失败，错误信息是:%s\n该元素是:%s"%(e,str(locater)),exc_info=True)
        else:
            print("元素定位成功，元素是:%s"%str(locater))
            log.logger.info("元素定位成功，元素是:%s"%str(locater))
            return ele

    #文本框输入
    def inputValue(self, inputBox , value):
        #定位元素
        ele = self.findElement(*inputBox)
        #输入内容
        try:
            ele.send_keys(value)
        except Exception as e:
            print("输入内容失败!值是:%s，原因是:%s"%(value,e))
            log.logger.error("输入内容失败!值是:%s，原因是:%s"%(value,e),exc_info=True)
        else:
            print("输入成功！内容是:%s"%value)
            log.logger.debug("输入成功！内容是:%s"%value)

    #获取标签值
    def getElementValue(self,element):
        #定位这个元素
        ele=self.findElement(*element)
        #获取该元素的文本值
        try:
            eleText=ele.text
        except Exception as e:
            print("获取文本失败!值是:%s \n错误信息是:%s"%(str(element),e))
            log.logger.error("获取文本失败!值是:%s \n错误信息是:%s"%(str(element),e),exc_info=True)
        else:
            print("文本获取成功！，值是:%s"%eleText)
            log.logger.info("文本获取成功！，值是:%s"%eleText)
            return eleText

    #截图
    def doPhoto(self,name):
        filename=config.photo_path+config.cur_time+name+".png"
        try:
            self.driver.get_screenshot_as_file(filename)
        except Exception as e:
            print("截图失败，原因是:%s"%e)
            log.logger.error("截图失败，原因是:%s"%e,exc_info=True)
        else:
            print("截图成功！")
            log.logger.info("截图成功！")

    #控件（元素）点击
    def doClick(self,element):
        # 定位这个元素
        ele=self.findElement(*element)
        try:
            # ele.click()
            self.driver.execute_script("arguments[0].click();", ele)
        except Exception as e:
            print("元素%s点击失败，原因是:%s"%(str(element),e))
            log.logger.error("元素%s点击失败，原因是:%s"%(str(element),e),exc_info=True)
        else:
            print("元素点击成功！%s"%str(element))
            log.logger.info("元素点击成功！%s"%str(element))



    #个人信息
    def perinfo(self,driver):
        action = ActionChains(driver)
        # 悬浮到头像上
        action.move_to_element(self.findElement(*self.img))
        action.perform()
        # 点击个人信息
        self.doClick(self.per)
        sleep(1)

    #学员管理
    def gl(self):
        self.doClick(self.sg)
        sleep(1)

    #教务管理
    def jwgl(self):
        self.doClick(self.jw)

    # 机构管理
    def jggl(self):
        self.doClick(self.jg)

    # 数据分析
    def sjfx(self):
        self.doClick(self.sj)

    # 招生吧
    def zsb(self):
        self.doClick(self.zs)

    # 招生吧
    def kjgl(self):
        self.doClick(self.kj)
    #退出登录
    def logoutFun(self,driver):
        action=ActionChains(driver)
        #悬浮到头像上
        action.move_to_element(self.findElement(*self.img))
        # action.move_to_element(self.img)
        action.perform()
        #点击退出登录按钮
        self.doClick(self.logout)
        #点击弹窗中的确定按钮
        self.doClick(self.logoutOk)
        sleep(1)







if __name__=="__main__":
    driver=webdriver.Chrome()
    url="http://www.baidu.com"
    lxf = "http://139.199.0.102"

    # basege=BasePage(driver,url)
    # #调用open方法
    # basege.open()
    # basege.driver.implicitly_wait(3)
    # #调用输入框输入内容
    # locater=(By.ID,"kw")
    # basege.inputValue(locater,"python")
    # basege.driver.implicitly_wait(3)
    # #调用点击方法
    # element=(By.ID,"su")
    # basege.doClick(element)
    # #调用截图
    # basege.doPhoto("1")
    # #获取文本值
    # basege.driver.quit()

    #调用打开雷晓峰
    lxf=BasePage(driver,lxf)
    #调用open方法
    lxf.open()
    lxf.driver.implicitly_wait(3)
    #调用输入内容
    zh=(By.CSS_SELECTOR,"[formcontrolname='userName']")
    lxf.inputValue(zh,"15003807446")
    mm=(By.CSS_SELECTOR,"[formcontrolname='password']")
    lxf.inputValue(mm,"12345678qwe")
    #调用点击方法
    dl=(By.CSS_SELECTOR,"body > app-root > layout-passport > div > div > passport-login > div > form > nz-form-item:nth-child(6) > button")
    lxf.doClick(dl)
    lxf.driver.implicitly_wait(2)
    #获取文本
    # t=(By.CSS_SELECTOR,"body > app-root > layout-passport > div > div > passport-login > div > form > nz-form-item:nth-child(2) > nz-form-control > div > nz-form-explain > div")
    # lxf.getElementValue(t)
    # #调用截图
    # lxf.doPhoto("2")
    #关闭
    lxf.driver.quit()

