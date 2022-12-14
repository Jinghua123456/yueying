#coding=‘utf-8’
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from testpage import addtree
from testpage import config
from selenium.webdriver.common.by import By
# #定义浏览器实例.0.102")
# driver=webdriver.Chrome()
#打开雷晓峰
# driver.get("http://139.199")
driver=addtree.getDriver("http://139.199.0.102")
# sleep(2)
#隐式等待
driver.implicitly_wait(10)
#定位账号
# a=driver.find_element_by_css_selector("input[placeholder='请输入手机号码']")
a=addtree.finfElement(driver,By.CSS_SELECTOR,"input[placeholder='请输入手机号码']")
# sleep(2)
#输入账号
# a.send_keys("13986128128")
addtree.doInputValue(a,"13986128128")
# sleep(2)
#定位密码
# a1=driver.find_element_by_css_selector("[type='password']")
a1=addtree.finfElement(driver,By.CSS_SELECTOR,"[type='password']")
# sleep(2)
#输入密码
# a1.send_keys("121121")
addtree.doInputValue(a1,"121121")
# sleep(2)
#定位登录按钮
# b=driver.find_element_by_css_selector("[type='submit']")
b=addtree.finfElement(driver,By.CSS_SELECTOR,"[type='submit']")
# #点击登录按钮
# b.click()
addtree.doClick(b)
# sleep(2)
#隐式等待
driver.implicitly_wait(2)
#截图
addtree.doPhoto(driver,"lxf")
#定位龚老师1
# a=driver.find_element_by_xpath("//span[@style='font-size: .16rem;color: #999;padding-left: .1rem']")
a=addtree.finfElement(driver,By.XPATH,"//span[@style='font-size: .16rem;color: #999;padding-left: .1rem']")
#判断是否登录成功
if a.text =='龚老师1':
    print("恭喜登陆成功")
else:
    print("抱歉登录失败")
#所有句柄
# handlers=driver.window_handles
# print("当前窗口所有的句柄是:%s"%handlers)
# #登录成功页面的句柄
# onehandler=driver.current_window_handle
# print("当前窗口句柄是:%s"%onehandler)
# #登录成功页面的url
# url=driver.current_url
# print("当前窗口的url是:%s"%url)
# #登录成功页面的标题（title）
# title=driver.title
# print("当前窗口的标题是:%s"%title)
config.handLer(driver)
#鼠标实例
action=ActionChains(driver)
#悬停操作
action.move_to_element(a)
#执行cz
action.perform()
# sleep(2)
#定位退出账号
# b=driver.find_element_by_css_selector(".userInfo-popPanel>:nth-child(4)")
# b=driver.find_element_by_xpath("//div[text()=‘退出账号’]")
b1=addtree.finfElement(driver,By.CSS_SELECTOR,".userInfo-popPanel>:nth-child(4)")
sleep(1)
#点击
# b1.click()
addtree.doClick(b1)
# sleep(1)
#定位确认按钮
# c=driver.find_element_by_css_selector(".ant-modal-confirm-btns>button:nth-child(2)")
c=addtree.finfElement(driver,By.CSS_SELECTOR,".ant-modal-confirm-btns>button:nth-child(2)")
#移交给弹窗权限
# alert=driver.switch_to.alert
# sleep(2)
#点击确认按钮
# alert.accept()
# c.click()
addtree.doClick(c)
#截图
addtree.doPhoto(driver,"dl")
# sleep(2)
#当前登录页面的句柄
# twohandler=driver.current_window_handle
# print("当前登录页面的句柄是:%s"%twohandler)
# #当前登录页面的url，title
# url=driver.current_url
# title=driver.title
# print("当前登录页面的url是:%s,\n 当前登录页面的title是:%s"%(url,title))
config.handLer(driver)
#退出
driver.quit()