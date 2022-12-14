from appium import webdriver
from page.Basepage import Basepage
from page.Main import Main
class App(Basepage):
    def start(self):
        _appPackage='com.xueqiu.android'
        _appActivity='.view.WelcomeActivityAlias'
        if self._driver is None:
            caps={}
            #caps['uuid']='127.0.0.1:62001'
            caps['platformName']='Android'
            caps['platformVersion']='7.1.2'
            caps['deviceName']='127.0.0.1:62001'
            caps['appPackage']=_appPackage
            caps['appActivity']=_appActivity
            caps['noReset']=True
            self._driver=webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self._driver.implicitly_wait(30)
        else:
            #仅供安卓
            self._driver.start_activity(_appPackage,_appActivity)
        return self
    def main(self):
        return Main(self._driver)