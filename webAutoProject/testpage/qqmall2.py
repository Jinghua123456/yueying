#coding='utf-8'
#qq邮箱
from time import sleep
from testpage import addtree
#定义浏览器
driver=addtree.getDriver(addtree.qq)
addtree.iframe(driver,"1391455214","1234")
#定位手机版
s=driver.find_element_by_link_text("手机版")
# s.click()
addtree.doClick(s)
#截图
addtree.doPhoto(driver,"sj")
# sleep(1)
driver.implicitly_wait(2)
#移交句柄给新页面
handler=driver.window_handles
driver.switch_to.window(handler[1])
# sleep(1)
#滚动到最后一行
#js字符串
js="window.scrollTo(0,5000)"
#执行js字符串
driver.execute_script(js)
# sleep(2)
#关闭当前页面
driver.close()
# sleep(1)
#移交句柄
driver.switch_to.window(handler[0])
# sleep(1)
addtree.iframe(driver,"1391455214","qaswdefr")
#截图
addtree.doPhoto(driver,"em")
#定义页面信息
addtree.handler(driver)
#回到主页面
driver.switch_to.default_content()
# sleep(1)
#定义页面信息
addtree.handler(driver)
#关闭浏览器
driver.quit()