#coding='utf-8'
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
# from testpage.testwebdriver import driver
from testpage import addtree
from selenium.webdriver.common.by import By
#
# #定义浏览器
# driver=webdriver.Chrome()
# #打开页面
# driver.get("http://www.baidu.com")
# #最大化
# driver.maximize_window()
# #等待一秒
# sleep(1)
#
# #鼠标操作
action=ActionChains(driver)


#悬停
# #定位设置
# a=driver.find_element_by_css_selector("#u1>span")
# #使用鼠标悬停操作
# action.move_to_element(a)
# #执行悬停操作
# action.perform()
# #等待1秒
# sleep(1)

#点击
# #定位新闻
# b=driver.find_element_by_link_text("新闻")
# #点击
# action.click(b)
# sleep(1)
# #执行点击操作
# action.perform()
# #等待1秒
# sleep(2)

#双击
# #定位换一换
# c=driver.find_element_by_css_selector("#hotsearch-refresh-btn>i")
# sleep(2)
# #双击
# action.double_click(c)
# sleep(2)
# #执行双击操作
# action.perform()
# sleep(1)

#右击
# #定位更多
# d=driver.find_element_by_link_text("更多")
# sleep(1)
# #右击
# action.context_click(d)
# sleep(2)
# #执行右击操作
# action.perform()
# sleep(1)

#拖拽
# #定位网盘和“壮志凌云”
# e=driver.find_element_by_link_text("网盘")
# d=driver.find_element_by_partial_link_text("壮志凌云")
# sleep(1)
# #d拖拽到e
# action.drag_and_drop(d,e)
# sleep(1)
# #执行拖拽操作
# action.perform()
# sleep(1)
#
# #退出
# driver.quit()
# from time import sleep
#
# from testpage import addtree
#
# #定义浏览器，打开页面
# driver=addtree.getDriver(addtree.bai)
# #最大化
# driver.maximize_window()
# sleep(1)
# #鼠标对象
# action=ActionChains(driver)
# #定位网盘和“中国”
# e=driver.find_element_by_link_text("网盘")
# d=driver.find_element_by_partial_link_text("中国")
# sleep(1)
# #d拖拽到e
# action.drag_and_drop(d,e)
# sleep(1)
# #执行拖拽操作
# action.perform()
# sleep(1)
# #关闭
# driver.quit()

#定义浏览器实例化,并打开百度页面
m=addtree.getDriver(addtree.bai)
#定位新闻
b=addtree.finfElement(driver,By.LINK_TEXT,"新闻")
#点击
action1.click(b)
#执行点击操作
action1.click(b)
#隐式等待
driver.implicitly_wait(1)

