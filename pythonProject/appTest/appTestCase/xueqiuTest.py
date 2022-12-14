from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appTestCase import number

# des_caps={}
# des_caps['platformName']=number.PLatformName
# des_caps['platformVersion']=number.PLatformVersion
# des_caps['deviceName']=number.DEviceName
# des_caps['noReset']=number.NOReset
# des_caps['app']=number.APP
# des_caps['appPackage']=number.APPPackage
# des_caps['appWaitActivity']=number.APPWaitActivity
# des_caps['unicodeKeyboard']=number.UNicodeKeyboard
# des_caps['resetKeyboard']=number.REsetKeyboard
# driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=des_caps)


driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities={
   "platformName": "Android",
   "appium:platformVersion": "7.1.2",
   "appium:deviceName": "127.0.0.1:62001",
   "appium:noReset": True,
   "appium:app":"C:\\Users\\刘朋强\\Desktop\\xueqiu.apk",
   "appium:appPackage": "com.xueqiu.android",
   "appium:appWaitActivity": ".view.WelcomeActivityAlias",
   "appium:unicodeKeyboard": True,
   "appium:resetKeyboard": True
   })

driver.implicitly_wait(10)
# driver.find_element(MobileBy.ID,"iv_icon").click()
driver.find_element(MobileBy.ID,"tv_name").click()
