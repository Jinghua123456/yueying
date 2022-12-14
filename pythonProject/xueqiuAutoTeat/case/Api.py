import time

from appium import webdriver

_appPackage = 'com.xueqiu.android'
_appActivity = '.view.WelcomeActivityAlias'

caps = {}
# caps['uuid']='127.0.0.1:62001'#设备ios
caps['platformName'] = 'Android'
caps['platformVersion'] = '7.1.2'
caps['deviceName'] = '127.0.0.1:62001'
caps['appPackage'] = _appPackage
caps['appActivity'] = _appActivity
caps['noReset'] = True
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
driver.implicitly_wait(30)
#关闭app，一般与launch_app 一起使用
driver.close_app()
#判断APP是否安装
print(driver.is_app_installed(_appPackage))#判断是否安装
#print(driver.is_app_installed(_appPackage))判断是否安装
#安装app,存在卸载后再安装
driver.install_app("C:\\Users\\刘朋强\\Desktop\\xueqiu.apk")
#driver.install_app("C:\\Users\\刘朋强\\Desktop\\xueqiu.apk")跟路径
time.sleep(3)
#打开页面
driver.start_activity(_appPackage,_appActivity)
time.sleep(2)
#置后台
driver.background_app(5)
time.sleep(2)
#重置
driver.reset()
#隐藏键盘
driver.press_keycode()
#手势类的操作，拖动，滑动，长按
from appium.webdriver.common.touch_action import TouchAction
#TouchAction(driver),鼠标操作的实例化
#按压控件,element\坐标点[x，y],不能同时写，release()结束，释放按压指针perfrom()执行
#TouchAction(driver).press(element\坐标点[x，y]).release().perfrom()
#长按，先执行后释放
#TouchAction(driver).long_press(element=).perform().release()
#点击，注意：语法（[(x.y)]）1,内置tap函数2使用TouchAction类
driver.tap([(100,200)])
#TouchAction(driver).tap(element=).perform().release()
#暂停,单位是毫秒
TouchAction(driver).wait(2000)
#移动,element目标位置元素
#TouchAction(driver).move_to(element=)
#长按移动到
TouchAction(driver).long_press().move_to().perform().release()
#滑动
#driver.swipe(x1,y1,x2,y2,times)
#收起键盘
driver.hide_keyboard()
#摇一摇
driver.shake()
#滚动，从a到b
#driver.scroll(a_element,b_element)元素
#driver.flick(x1,y1,x2,y2)#坐标点
#放大，缩小
from appium.webdriver.common.multi_action import MultiAction
#获取屏幕分辨率
x=driver.get_window_size()["widch"]
y=driver.get_window_size()["hight"]
driver.swipe(0.8*x,0.5*y,0.1*x,0.2*y,2000)
#网络
driver.set_network_connection(4)
#通知栏
driver.open_notifications()
#修改经纬度
driver.set_location(latitude=12,longitude=20,altitude=None)
#is_enabled编辑，is_selected选中，is_displayed是否可见
driver.find_element().is_displayed()
assert driver.find_element().is_enabled()==False
#元素定位
from appium.webdriver.common.mobileby import MobileBy
#切换页面
driver.switch_to.context("页面")