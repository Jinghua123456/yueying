#coding='utf-8'
from time import sleep
from selenium import webdriver

from testpage import addtree

#定义浏览器
# driver=webdriver.Chrome()
# #打开页面
# driver.get("file:///C:/Users/%E5%88%98%E6%9C%8B%E5%BC%BA/Desktop/alert.html")
# #定位提示弹窗按钮
# l=driver.find_element_by_id("2")
# #点击按钮
# l.click()
# #等待
# sleep(1)
# # #操作弹窗
# w=driver.switch_to.alert
# #获取弹窗提示信息
# text=w.text
# # #打印提示信息
# print("弹窗提示信息是:%s"%text)
# # #点击确定按钮
# w.accept()
# sleep(1)
# #关闭
# driver.quit()

#定义浏览器,并打开页面
driver=addtree.getDriver(addtree.baidu)
#定位提示弹窗按钮
l=driver.find_element_by_id("2")
#点击按钮
l.click()
#等待
sleep(1)
# #操作弹窗
w=driver.switch_to.alert
#获取弹窗提示信息
text=w.text
# #打印提示信息
print("弹窗提示信息是:%s"%text)
# #点击确定按钮
w.accept()
sleep(1)
#获取浏览器信息
hello=driver.find_element_by_css_selector("[align='center']>h4")
print("浏览器页面信息:%s"%hello.text)

#关闭
driver.quit()
