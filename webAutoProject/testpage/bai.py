#coding='utf-8'

from time import sleep

from selenium import webdriver

#定义浏览器实例
driver=webdriver.Chrome()
#打开百度一下
driver.get("http://www.baidu.com")
#最大化
driver.maximize_window()
#等待
# sleep(1)
#隐式等待
driver.implicitly_wait(5)
#定位登录
a=driver.find_element_by_link_text("登录")
a.click()
# sleep(2)
#定位百度用户协议
c=driver.find_element_by_partial_link_text("百度用户")
# c=driver.find_element_by_link_text("百度用户协议")
# c=driver.find_element_by_css_selector(".tang-pass-sms-agreement.pass-link>a")
c.click()
# sleep(2)
#移交权柄
handler=driver.window_handles
onehandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title
print("当前窗口是:%s,当前窗口的url是:%s"%(cur_URL,title))
print("当前句柄是:%s"%onehandler)
print("当前窗口句柄是:%s"%str(handler))

#句柄转移
driver.switch_to.window(handler[-1])
#获取当前窗口句柄
twohandler=driver.current_window_handle
cur_URL=driver.current_url
title=driver.title

print("移交句柄后当前窗口的句柄是:%s,\n转移后的窗口url是:%s,\nz转移后的窗口标题是:%s"%(twohandler,cur_URL,title))
#定位百度用户协议
driver.find_element_by_css_selector(".mod-bread-wrapper>div")
#操作页面
driver.close()
# sleep(1)
#隐式等待
driver.implicitly_wait(5)
#再次切换到最初页面
driver.switch_to.window(onehandler)
#关闭浏览器
driver.quit()