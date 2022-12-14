#coding='utf-8'
#qq邮箱
from time import sleep

from selenium.webdriver.common.by import By

from testpage import addtree
# #定义浏览器
# driver=addtree.getDriver(addtree.qq)
# #定位iframe元素
# iframe=driver.find_element_by_css_selector("#login_frame")
# #将光标转移至小页面下
# driver.switch_to.frame(iframe)
# sleep(1)
# #定位账号
# a=driver.find_element_by_css_selector("#u")
# sleep(1)
# a.send_keys("1391455214")
# #定位登录
# c=driver.find_element_by_css_selector("#login_button")
# c.click()
# sleep(1)
# er=driver.find_element(By.CSS_SELECTOR,"#err_m").text
# print("登录失败，信息是:%s"%er)
#
# #打印页面信息
# addtree.handler(driver)
# #回到主页面
# driver.switch_to.default_content()
# sleep(1)
# # addtree.iframe1(driver)
#
# #定位手机版
# s=driver.find_element_by_link_text("手机版")
# s.click()
# sleep(1)
# #移交句柄给新页面
# handler=driver.window_handles
# driver.switch_to.window(handler[1])
# sleep(1)
# #滚动到最后一行
# #js字符串
# js="window.scrollTo(0,5000)"
# #执行js字符串
# driver.execute_script(js)
# sleep(2)
# #关闭当前页面
# driver.close()
# sleep(1)
# #移交句柄
# # handler=driver.window_handles
# driver.switch_to.window(handler[0])
# sleep(1)
# #回到主页面
# # driver.switch_to.default_content()
# # sleep(1)
# #定位iframe元素
# iframe=driver.find_element_by_css_selector("#login_frame")
# #将光标转移至小页面下
# driver.switch_to.frame(iframe)
# sleep(1)
# #定位账号
# a=driver.find_element_by_css_selector("#u")
# sleep(1)
# a.clear()
# sleep(1)
# a.send_keys("1391455214")
# #定位密码
# b=driver.find_element_by_css_selector(".inputstyle.password")
# sleep(1)
# b.send_keys("qaswdefr")
# #定位登录
# c=driver.find_element_by_css_selector("#login_button")
# c.click()
# sleep(1)
# # addtree.iframe2(driver)
# # er=driver.find_element(By.CSS_SELECTOR,"#err_m").text
# # print("登录失败，信息是:%s"%er)
# #定义页面信息
# addtree.handler(driver)
# #回到主页面
# driver.switch_to.default_content()
# sleep(1)
# #定义页面信息
# addtree.handler(driver)
# #关闭浏览器
# driver.quit()

#代码精简

#定义浏览器
driver=addtree.getDriver(addtree.qq)
addtree.iframe(driver,"1391455214","1234")
#定位手机版
# s=driver.find_element_by_link_text("手机版")
s=addtree.finfElement(driver,By.LINK_TEXT,"手机版")
s.click()
#隐式等待
driver.implicitly_wait(2)
#移交句柄给新页面
handler=driver.window_handles
driver.switch_to.window(handler[1])
#滚动到最后一行
#js字符串
js="window.scrollTo(0,5000)"
#执行js字符串
driver.execute_script(js)
#关闭当前页面
driver.close()
#移交句柄
driver.switch_to.window(handler[0])
addtree.iframe(driver,"1391455214","qaswdefr")
#定义页面信息
addtree.handler(driver)
#回到主页面
driver.switch_to.default_content()
#定义页面信息
addtree.handler(driver)
#关闭浏览器
driver.quit()