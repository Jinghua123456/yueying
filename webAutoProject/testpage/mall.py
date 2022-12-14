#coding='utf-8'
#163邮箱
from time import sleep

from selenium.webdriver.common.by import By

from testpage import addtree

#定义浏览器
driver=addtree.getDriver(addtree.mall)

#定位iframe元素（大页面套小页面）
# iframe=driver.find_element_by_css_selector("[id^='x-URS-iframe']")
iframe=addtree.finfElement(driver,By.CSS_SELECTOR,"[id^='x-URS-iframe']")
#将光标转移至小页面下
driver.switch_to.frame(iframe)

sleep(1)
#定位用户名、密码、登录
a=addtree.finfElement(driver,By.XPATH,"//div[@id='account-box']/div[2]/input]")
b=addtree.finfElement(driver,By.CSS_SELECTOR,".j-inputtext.dlpwd")
c=addtree.finfElement(driver,By.CSS_SELECTOR,"#dologin")
# a=driver.find_element_by_xpath("//div[@id='account-box']/div[2]/input]")
# b=driver.find_element_by_css_selector(".j-inputtext.dlpwd")
# c=driver.find_element_by_css_selector("#dologin")
#填写
# a.send_keys("123")
addtree.doInputValue(a,"123")
# b.send_keys("456")
addtree.doInputValue(b,"456")
# c.click()
addtree.doClick(c)
sleep(2)
#截图，查看当前页面信息
addtree.doPhoto(driver,"1")
#打印信息
addtree.handler(driver)
#回到主页面
driver.switch_to.default_content()
#定位会员
v=addtree.finfElement(driver,By.LINK_TEXT,"会员")
addtree.doClick(v)
addtree.doPhoto(driver,"2")
#句柄转移
handler=driver.window_handles
driver.switch_to.window(handler[-1])
#定义页面信息
addtree.handler(driver)
#关闭
driver.quit()

