#coding='utf-8'
from time import sleep

from selenium import webdriver

from testpage import addtree

# #定义浏览器驱动
# driver=webdriver.Chrome()
# # driver=addtree.getDriver()
# #打开页面
# driver.get("file:///C:/Users/%E5%88%98%E6%9C%8B%E5%BC%BA/Desktop/alert.html")
# #定位输入框弹窗按钮
# l=driver.find_element_by_id("1")
# #点击按钮
# l.click()
# sleep(1)
# #将光标移交给弹窗
# do=driver.switch_to.alert
# sleep(2)
# # #获取窗口信息，并打印
# rtext=do.text
# print("弹窗提示信息: %s"%rtext)
# # #输入框输入
# do.send_keys("1")
# # do.send_keys("2")
# #点击确定按钮
# a=do.accept()
# sleep(2)
#点击取消按钮
#a=do.dismiss()
# sleep(1)
# #定位最终结果
# r=driver.find_element_by_css_selector("#textSpan>font")
# # print("最终结果:%s"%r.text)
# #打印
# if a ==1:
#     print("点击确认按钮，最终结果是:%s"%r.text)
# else:
#     print("点击取消按钮，最终结果是:%s"%r.text)




#定义浏览器驱动
driver=webdriver.Chrome()
# driver=addtree.getDriver(addtree.baidu)
#打开页面
driver.get("file:///C:/Users/%E5%88%98%E6%9C%8B%E5%BC%BA/Desktop/alert.html")
#定位输入框弹窗按钮
l=driver.find_element_by_id("1")
#点击按钮
l.click()
sleep(1)
#将光标移交给弹窗
do=driver.switch_to.alert
sleep(2)
# #获取窗口信息，并打印
ix="One"
rtext=do.text
print("弹窗提示信息: %s"%rtext)
# #输入框输入
do.send_keys("1")
# do.send_keys("2")
#int=input("输入内容：1确定，2取消")
#点击确定按钮
a=do.accept()
ix="Two"
sleep(2)
# #定位最终结果
r=driver.find_element_by_css_selector("#textSpan>font")
#判断结果
r1='强哥是真聪明啊'
r2='左哥是真笨啊'
if r in (r1,r2):
    print("点击确定按钮")
elif ix=="Two":
#elif:int=="2"
    print("点击取消按钮")
else:
    print("点击确定，但不输入内容")
#关闭
driver.quit()

