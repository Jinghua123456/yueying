#coding='utf-8'
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import addtree
#定义浏览器
driver=addtree.getDriver(addtree.bai)
#最大化
driver.maximize_window()
#定义右上级登录按钮(定位登录1)
a=driver.find_element_by_link_text("登录")
la1=(By.LINK_TEXT,"登录")#(定位登录2)
# la=driver.find_element(By.LINK_TEXT,"登录")#(定位登录3)
#显示等待（既定位元素有判断，是否可见。如果可见，返回该元素，反之则异常(超时）--局部，常用于移动端自动化，用于一闪而过的元素
# a=WebDriverWait(driver,5,0.1).until(EC.visibility_of_element_located(la1))
#显示等待（仅有判断，是否可见）
# a=WebDriverWait(driver,5,0.1).until(EC.visibility_of(la))
#显示等待，元素出现(定位并判断）
# a=WebDriverWait(driver,5,0.1).until(EC.presence_of_element_located(la1))
#显示等待，（判断右上角的登录按钮是否与预期的一致，预期值是：登录。做两件事：既定位又判断，如果一致返回TRUE）
r=WebDriverWait(driver,5,0.1).until(EC.text_to_be_present_in_element(la1,"登录"))

#定位百度一下
bai=(By.CSS_SELECTOR,"#su")
#判断百度一下的value值是否与预期的一致：预期值是：百度一下做两件事：既定位又判断，如果一致返回TRUE
r1=WebDriverWait(driver,5,0.1).until(EC.text_to_be_present_in_element_value(bai,"百度一下"))
print("百度一下的value值:%s"%r1)
if r==True:
    print("右上角的登录文本值是否正确:%s"%r)
    a.click()
#点击
# a.click()
#强制等待
# sleep(1)
#定位百度用户协议
b=driver.find_element_by_link_text("百度用户协议")
#点击
b.click()
sleep(1)
#定义当前的标题、句柄、url,并打印
addtree.handler(driver)
#移交句柄
handler=driver.window_handles
driver.switch_to.window(handler[-1])
sleep(2)
#定义当前的标题、句柄、url,并打印
addtree.handler(driver)
#获取当前title
title=driver.title
# sjtitle="百度用户协议"
sjtitle="协议"
# r=WebDriverWait(driver,5,0.1).until(EC.title_is(sjtitle))
r=WebDriverWait(driver,5,0.1).until(EC.title_contains(sjtitle))
print(r)

#操作滚动条
#定义js字符串
js="window.scrollTo(0,5000)"
#执行js脚本
driver.execute_script(js)
sleep(1)

#关闭当前页面
driver.close()
sleep(1)
#退出浏览器
driver.quit()

