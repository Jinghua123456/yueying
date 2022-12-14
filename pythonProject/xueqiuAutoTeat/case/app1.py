import time
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy as By
_appPackage = 'com.xueqiu.android'
_appActivity = '.view.WelcomeActivityAlias'
caps = {}
caps['platformName'] = 'Android'
caps['platformVersion'] = '7.1.2'
caps['deviceName'] = '127.0.0.1:62001'
caps['appPackage'] = _appPackage
caps['appActivity'] = _appActivity
caps['noReset'] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(30)
#判断是否安装,跟包名(返回True:安装)
print(driver.is_app_installed(_appPackage))
#安装APP
driver.install_app("C:\\Users\\刘朋强\\Desktop\\xueqiu.apk")
#打开页面
driver.start_activity(_appPackage,_appActivity)
time.sleep(3)
#置后台
driver.background_app(5)
#重置
#driver.reset()
#隐藏键盘
#driver.hide_keyboard()
#滑动
#driver.swipe(x1,y1,x2,y2,times)
#摇一摇
driver.flick()
#网络
driver.set_network_connection(4)
#通知栏
driver.open_notifications()
#获取屏幕分辨率
x=driver.get_window_size()["widch"]
y=driver.get_window_size()["hight"]
driver.swipe(0.8*x,0.5*y,0.1*x,0.2*y,2000)
#切换页面
driver.switch_to.context("页面")
#修改经纬度
driver.set_location(latitude=12,longitude=20,altitude=None)
#滚动，从a到b
#driver.scroll(a_element,b_element)元素
#driver.flick(x1,y1,x2,y2)#坐标点

#手势类操作
from appium.webdriver.common.touch_action import TouchAction
#TouchAction(driver),鼠标操作的实例化
#点击
# driver.tap([(100,753)])
TouchAction(driver).tap().perform().release()
#长按，先执行，后释放
TouchAction(driver).long_press().perform().release()
#按压控件（元素或坐标）,先释放，后执行
TouchAction(driver).press().release().perform()
#暂停
TouchAction(driver).wait(1000)
#移动到，目标元素的位置
TouchAction(driver).move_to()
#长按移动到，目标元素的位置
TouchAction(driver).long_press().move_to().perform().release()
