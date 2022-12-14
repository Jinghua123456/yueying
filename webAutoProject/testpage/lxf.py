#coding='utf-8'
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from testpage import addtree

# # #驱动浏览器
# driver=webdriver.Chrome()
# # #打开雷晓峰
# driver.get("http://139.199.0.102")
# # driver=addtree.getlxf(addtree.lxf)
# #等待2秒
# sleep(2)
# #定位账号
# # a=driver.find_element_by_xpath("//span//input[@placeholder='请输入手机号码']")
# a=driver.find_element_by_css_selector("input[placeholder='请输入手机号码']")
# sleep(2)
# #输入账号
# a.send_keys("18971481029")
# sleep(2)
# #定位密码
# # a1=driver.find_element_by_xpath("//input[@type='password']")
# a1=driver.find_element_by_css_selector("[type='password']")
# sleep(2)
# #输入密码
# a1.send_keys("121121")
# sleep(2)
# # #记住密码
# ###
# # b1=driver.find_element_by_xpath("//from//input[@type='checkbox' and @class='ant-checkbox-input']")
# # b1=driver.find_element_by_partial_link_text("记住密码")
# # b1=driver.find_element_by_link_text("记住密码")
# # b1=driver.find_element_by_xpath("//from/nz-from-item[3]/nz-col[1]/label/span[1]/input")
# ###
# # b1=driver.find_element_by_class_name("ant-checkbox-input")
# b1=driver.find_element_by_css_selector(".ant-checkbox-input")
# # #点击记住密码
# b1.click()
# sleep(1)
# #定位忘记密码
# # b2=driver.find_element_by_xpath("//from//span//nz-col//a[@class='forgot.ng-tns-c1-0']")
# # b2=driver.find_element_by_link_text("忘记密码？")
# # b2=driver.find_element_by_css_selector(".forgot.ng-tns-c1-0")
# # #点击忘记密码
# # b2.click()
# # sleep(1)
# #退一步
# # driver.back()
# # sleep(2)
# # #定位注册
# # b3=driver.find_element_by_xpath("//form//a[@class='register']")
# # b3=driver.find_element_by_partial_link_text("立即注册")
# # b3=driver.find_element_by_css_selector(".register")
# # #d点击立即注册
# # b3.click()
# # sleep(2)
# # driver.back()
# #定位登录按钮
# # b=driver.find_element_by_xpath("//form//button[@type='submit'] ")
# b=driver.find_element_by_css_selector("[type='submit']")
# # #点击登录按钮
# b.click()
# sleep(3)
# #退出
# driver.quit()

#驱动浏览器
driver=addtree.getDriver("http://139.199.0.102")

#隐式等待
driver.implicitly_wait(1)
#定位账号
b=addtree.finfElement(driver,By.CSS_SELECTOR,"input[placeholder='请输入手机号码']")
#输入账号
b.send_keys("18971481029")
#定位密码
c=addtree.finfElement(driver,By.CSS_SELECTOR,"[type='password']")
#输入密码
c.send_keys("121121")
#定位登录按钮
l=addtree.finfElement(driver,By.CSS_SELECTOR,"[type='submit']")
# #点击登录按钮
b.click()
sleep(5)
#退出
driver.quit()