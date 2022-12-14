#coding='utf-8'
#调用
from time import sleep

from selenium.webdriver.common.by import By

from testpage import addtree
#
# driver=webdriver.Chrome()
# driver.get("http://www.baidu.com")
driver=addtree.getDriver(addtree.bai)
sleep(1)
# addtree.handler(driver)
# a=addtree.finfElement(driver,By.LINK_TEXT,"新闻")
# a.click()
b=addtree.finfElement(driver,By.CSS_SELECTOR,"#kw")
b.send_keys("lianlian")
c=addtree.finfElement(driver,By.CSS_SELECTOR,"#su")
c.click()