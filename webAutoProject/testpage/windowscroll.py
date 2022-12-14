#coding='utf-8'
#页面滚动
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import addtree
#
# #定义浏览器
# driver=addtree.getDriver(addtree.bai)
# #最大化
# driver.maximize_window()
# #定义右上级登录按钮
# # a=driver.find_element_by_link_text("登录")
# #显示等待（元素可见）
# la1=(By.LINK_TEXT,"登录")
# a=WebDriverWait(driver,5,0.1).until(EC.visibility_of_element_located(la1))
# #点击
# a.click()
# sleep(1)
# #定位百度用户协议
# b=driver.find_element_by_link_text("百度用户协议")
# #点击
# b.click()
# sleep(1)
# #定义当前的标题、句柄、url,并打印
# addtree.handler(driver)
# #移交句柄
# handler=driver.window_handles
# driver.switch_to.window(handler[-1])
# sleep(2)
# #定义当前的标题、句柄、url,并打印
# addtree.handler(driver)
#
# # #获取当前title
# title=driver.title
# sjtitle="百度用户协议"
# WebDriverWait(driver,5,0.1).until(EC.title_is(sjtitle))
#
# #操作滚动条
# #定义js字符串
# js="window.scrollTo(0,5000)"
# #执行js脚本
# driver.execute_script(js)
# sleep(1)
#
# #关闭当前页面
# driver.close()
# sleep(1)
# #退出浏览器
# driver.quit()


#定义浏览器
driver=addtree.getDriver(addtree.bai)
#定义右上级登录按钮
# a=driver.find_element_by_link_text("登录")
a=addtree.finfElement(driver,By.LINK_TEXT,"登录")
#点击
# a.click()
addtree.doClick(a)
#定位百度用户协议
# b=driver.find_element_by_link_text("百度用户协议")
b=addtree.finfElement(driver,By.LINK_TEXT,"百度用户协议")
#点击
# b.click()
addtree.doClick(b)
#截图
addtree.doPhoto(driver,"xy")
#定义当前的标题、句柄、url,并打印
addtree.handler(driver)
#获取当前所有句柄
handler=driver.window_handles
#移交句柄
driver.switch_to.window(handler[-1])
#定义当前的标题、句柄、url,并打印
addtree.handler(driver)
#操作滚动条
#定义js字符串
js="window.scrollTo(0,5000)"
#执行js脚本
driver.execute_script(js)
sleep(1)
# #隐式等待1秒
# driver.implicitly_wait(1)
#关闭当前页面
driver.close()
#隐式等待1秒
driver.implicitly_wait(1)
#截图
addtree.doPhoto(driver,"bd")
#退出浏览器
driver.quit()