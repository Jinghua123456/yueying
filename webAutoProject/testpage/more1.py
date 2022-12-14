#coding='utf-8'
from time import sleep

from selenium import webdriver
#多窗口切换

#定义浏览器实例，并打开页面：百度一下
# driver=addtree.getDriver(addtree.bai)
driver=webdriver.Chrome()
driver.get("http://www.baidu.com")
#点击百度一下页面下的超链接：hao123
a=driver.find_element_by_link_text("hao123")
a.click()
sleep(2)
#关键性一步:移交包柄
handlers=driver.window_handles
curhandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("当前窗口的标题是:%s,\n 当前窗口的URL是:%s"%(cur_URL,title))
print("当前窗口的句柄是:%s"%curhandler)
print("当前窗口的句柄是:%s"%str(handlers))

#句柄转移
driver.switch_to.window(handlers[-1])

#获取当前句柄
curhandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("移交句柄后当前窗口的句柄是:%s,\n转移后的窗口url是:%s,\nz转移后的窗口标题是:%s"%(curhandler,cur_URL,title))
#操作hao123页面
driver.close()
sleep(2)
#再次切换到最初页面
driver.switch_to.window(curhandler)

driver.quit()