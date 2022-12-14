#coding='utf-8'
from time import sleep

from selenium import webdriver

from testpage import addtree
from testpage.testwebdriver import driver

# #定义浏览器
# driver=webdriver.Chrome()
# #打开页面
# driver.get("file:///C:/Users/%E5%88%98%E6%9C%8B%E5%BC%BA/Desktop/alert.html")
# #定位确认弹窗按钮
# l=driver.find_element_by_css_selector("[onclick='showAlert()']")
# #点击确认弹窗按钮
# l.click()
# #等待
# sleep(1)
# #移交权限
# r=driver.switch_to.alert
# sleep(1)
# #获取弹窗提示信息
# t=r.text
# sleep(1)
# #打印
# print("弹窗提示信息是:%s"%r.text)
# #点击确认按钮
# # a=r.accept()
# # sleep(1)
# #点击取消按钮
# a=r.dismiss()
# sleep(1)
# #定位最终结果
# r=driver.find_element_by_css_selector("#textSpan>font")
# #打印
# if a ==1:
#     print("点击确认按钮，最终结果是:%s"%r.text)
# else:
#     print("点击取消按钮，最终结果是:%s"%r.text)
# #关闭
# driver.quit()

#y定义浏览器实例，并打开页面
driver=addtree.getDriver(addtree.baidu)
#定位确认弹窗按钮
l=driver.find_element_by_css_selector("[onclick='showAlert()']")
#点击确认弹窗按钮
l.click()
#等待
sleep(1)
#移交权限
r=driver.switch_to.alert
sleep(1)
#获取弹窗提示信息
t=r.text
sleep(1)
#打印
print("弹窗提示信息是:%s"%r.text)
#点击确认按钮
a=r.accept()
sleep(1)
#点击取消按钮
# a=r.dismiss()
# sleep(1)
#定位最终结果
r=driver.find_element_by_css_selector("#textSpan>font")
#判断结果，确认点击按钮
r1="您为何如此自信？"
r2="您为何如此谦虚？"
if r==r1:
    print("点击的是确定按钮，结果是:%s"%r.text)
else:
    print("点击的是取消按钮，结果是:%s"%r.text)
#关闭
driver.quit()