#coding='utf-8'
#元素的常用操作
from time import sleep
from selenium import webdriver
from testpage import  config

#定义浏览器
driver=webdriver.Chrome()
#打开页面
# driver.get("http://www.baidu.com")
#最大化
driver.maximize_window()

#导入
# driver.get(config.bai)
#定位输入框
# inp=driver.find_element_by_css_selector("#kw")

#鼠标类
# action=ActionChains(driver)
#定位更多超链接
# c=driver.find_element_by_link_text("更多")
#点击
# action.click(b)
#定位换一换并双击
# h=driver.find_element_by_xpath("//span[text()='换一换']")
# action.double_click(h)
# sleep(2)
#针对更多进行右击操作
# action.context_click(c)
# sleep(3)
#使用鼠标悬停操作
# action.move_to_element(c)

#去执行鼠标的操作 (必须有）
# action.perform()

# sleep(3)
#定位超链接，进行拖拽
# x=driver.find_element_by_partial_link_text("新进展")
#鼠标拖拽
# action.drag_and_drop(x,c)
# sleep(2)
#执行操作
# action.perform()
#等待1秒
# sleep(1)
#输入内容
# inp.send_keys("python")
# sleep(1)
# #模拟回车键功能
# inp.submit()

# sleep(2)
# print(inp.size)
#判断是否可见
# print("输入框是否可见：",inp.is_displayed())
#判断是否可用（inp-变量，点调用方法）
# print("输入框是否可用：",inp.is_enabled())
#判断是否选中
# print("输入框是否选中：",inp.is_selected())
# sleep(2)
# #清除文本内容
# inp.clear()
# sleep(2)
# #定位右上角的登录并点击
# a=driver.find_element_by_css_selector("#s-top-loginbtn")
# a.click()
# sleep(2)
# #定位登录按钮并点击
# b=driver.find_element_by_id("TANGRAM__PSP_11__submit")
# b.click()
#获取属性名
# f=a.get_attribute("id")
#打印
# print(a.get_attribute("id"))
# print(a.get_attribute("class"))
# sleep(2)
# #定位错误的提示信息
# error=driver.find_element_by_id("TANGRAM__PSP_11__submit")
# #获取错误信息并打印
# print("错误信息是: ", error.text)
# # print("错误信息:%s"%error.text)
# sleep(2)

#弹出框
#定位第一个弹出框按钮,要填写信息

# l1=driver.find_element_by_id("1")
# l1.click()
# sleep(2)

# #操作弹出框（后不带（））（鼠标移到弹出-移交权限）
# alert=driver.switch_to.alert

# #获取弹窗的文本信息，并打印
# atext=alert.text
# print("弹出文本：%s"%atext)
# #向输入框中输入内容
# alert.send_keys("1")
# #点击弹出框取消按钮
# # alert.dismiss()
# #点击弹出框确定按钮
# alert.accept()
# sleep(1)

# #定位第二个弹出框，仅提示
# l2=driver.find_element_by_id("2")
# #点击
# l2.click()
# sleep(2)
# #操作弹出框
# alert=driver.switch_to.alert
#点击弹出窗取消按钮
# alert.dismiss()
# sleep(2)

#点击弹出框确定按钮
# alert.accept()
# sleep(2)

#定位第三个弹出框，选择
l3=driver.find_element_by_css_selector("[onclick='showAlert()']")
l3.click()
#操作弹出框（ 注意： 后面不带括号 ）（鼠标移到弹出-移交权限）
alert=driver.switch_to.alert
sleep(2)
#获取弹窗的文本信息(text)，并打印
atext=alert.text
print("弹出文本：%s"%atext)
#点击弹出窗取消按钮
# alert.dismiss()
# sleep(2)

#点击弹出框确定按钮
# alert.accept()
# sleep(2)
#定位页面的结果
# r=driver.find_element_by_css_selector("#textSpan>font")
#打印结果

# #定位页面的结果(父子级）
# r=driver.find_element_by_css_selector("#textSpan>font")
# #打印结果
# print("结果输出：%s"%r.text)
# sleep(1)

#关闭浏览器
driver.quit()