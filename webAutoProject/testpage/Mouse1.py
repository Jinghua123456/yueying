#coding='utf-8'
from time import sleep
from selenium.webdriver import ActionChains
from testpage import addtree
from selenium.webdriver.common.by import By

#定义浏览器实例化,并打开百度页面
driver=addtree.getDriver(addtree.bai)
#鼠标操作
action1=ActionChains(driver)

#双击
#定位换一换
d=addtree.finfElement(driver,By.CSS_SELECTOR,"#hotsearch-refresh-btn>i")
#双击
action1.double_click(d)
#执行操作
action1.perform()
#等待
# sleep(1)
driver.implicitly_wait(1)

#右击
#定位更多
e=addtree.finfElement(driver,By.LINK_TEXT,"更多")
#右击
action1.context_click(e)
#执行右击
action1.perform()
# sleep(1)

# #定位设置
# a=addtree.finfElement(driver,By.LINK_TEXT,"设置")
a=addtree.finfElement(driver,By.CSS_SELECTOR,"#s-usersetting-top")
#使用鼠标悬停操作
action1.move_to_element(a)
#执行悬停操作
action1.perform()
#等待
sleep(1)
#隐式等待
# driver.implicitly_wait(1)

#拖拽
l=addtree.finfElement(driver,By.LINK_TEXT,"更多")
p=addtree.finfElement(driver,By.CSS_SELECTOR,"#s-hotsearch-wrapper > div > a.hot-title > div > i:nth-child(1)")
#拖拽
action1.drag_and_drop(p,l)
#执行拖拽
action1.perform()
sleep(1)


#定位新闻
b=addtree.finfElement(driver,By.LINK_TEXT,"新闻")
#点击
action1.click(b)
#执行点击操作
action1.perform()
#隐式等待
# driver.implicitly_wait(1)


#关闭
driver.quit()