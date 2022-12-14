#coding='utf-8'
#基础页面：存放所有页面用到的公共方法及属性
#所有page类均继承该基础类
import logging
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from common import config
from common.doLog import Logger

log=Logger(__name__,logging.DEBUG)
class BasePage(object):
    # 重构初始化方法
    def __init__(self,driver,url=config.url):
        self.driver=driver
        self.url=url

    #打开页面
    def open(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
        except Exception as e :
            print("发生异常页面打开失败，内容是:%s\n失败的页面是:%s"%(e,self.url))
            log.logger.error("发生异常页面打开失败，内容是:%s\n失败的页面是:%s"%(e,self.url),exc_info=True)
        else:
            print("未发生异常，页面打开成功！打开的页面是%s"%self.url)
            log.logger.info("未发生异常，页面打开成功！打开的页面是%s"%self.url)

    #定位元素
    def findElement(self,*locater):
        try:
            ele=WebDriverWait(self.driver,5,0.1).until(EC.visibility_of_element_located(locater))
        except Exception as e:
            print("元素定位失败，错误信息是:%s\n错误元素是:%s"%(e,str(locater)))
            log.logger.error("元素定位失败，错误信息是:%s\n错误元素是:%s"%(e,str(locater)),exc_info=True)
        else:
            print("元素定位成功，该元素是:%s"%str(locater))
            log.logger.info("元素定位成功，该元素是:%s"%str(locater))
            return ele

    #元素点击
    def doClick(self,ele):
        # 定位这个元素
        ele=self.findElement(*ele)
        try:
            ele.click()
        except Exception as e:
            print("元素点击失败，该元素是:%s\n失败原因是:%s"%(str(ele),e))
            log.logger.error("元素点击失败，该元素是:%s\n失败原因是:%s"%(str(ele),e),exc_info=True)
        else:
            print("元素点击成功！该元素是:%s"%str(ele))
            log.logger.info("元素点击成功！该元素是:%s"%str(ele))

    #文本框输入
    def inputWenben(self,ele,value):
        # 定位这个元素
        ele=self.findElement(*ele)
        try:
            ele.send_keys(value)
        except Exception as e:
            print("输入失败，输入内容是:%s\n原因是:%s"%(value,e))
            log.logger.error("输入失败，输入内容是:%s\n原因是:%s"%(value,e),exc_info=True)
        else:
            print("输入成功！输入内容是:%s"%value)
            log.logger.info("输入成功！输入内容是:%s"%value)

    #获取标签值
    def getValue(self,ele):
        # 定位这个元素
        ele=self.findElement(*ele)
        try:
            eleText=ele.text
        except Exception as e:
            print("文本获取失败，失败元素是:%s\n错误信息是:%s"%(str(ele),e))
            log.logger.error("文本获取失败，失败元素是:%s\n错误信息是:%s"%(str(ele),e),exc_info=True)
        else:
            print("文本获取成功！内容是:%s"%eleText)
            log.logger.info("文本获取成功！内容是:%s"%eleText)

    #截图
    def photo(self,name):
        filename=config.photo_path+config.cur_time+name+".png"
        try:
            self.driver.get_screenshot_as_file(filename)
        except Exception as e:
            print("截图失败，原因是:%s"%e)
            log.logger.error("截图失败，原因是:%s"%e,exc_info=True)
        else:
            print("截图成功")
            log.logger.info("截图成功")
if __name__=="__main__":
    driver=webdriver.Chrome()
    url = "http://www.baidu.com"
    base=BasePage(driver)
    #调用打开open
    base.open()
    base.driver.implicitly_wait(2)
    #输入内容
    e=(By.ID,"kw")
    base.inputWenben(e,"爱的二八定律")

    base.driver.implicitly_wait(2)
    #点击
    a=(By.ID,"su")
    base.doClick(a)
    sleep(2)
    #截图
    base.photo("l")
    #获取文本值
    w=(By.ID,"su")
    base.getValue(w)
    #退出浏览器
    base.driver.quit()

