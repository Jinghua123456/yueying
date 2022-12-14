#coding='utf-8'
from time import sleep

from selenium import webdriver



#地址
baidu="file:///C:/Users/%E5%88%98%E6%9C%8B%E5%BC%BA/Desktop/alert.html"
lxf="http://139.199.0.102"
bai="http://www.baidu.com"

def getDriver(bd):
    # try:
        # 实例化浏览器
        driver = webdriver.Chrome()
    # except Exception as e:
    #     print("发生异常，浏览器实例化失败！,\n错误信息:%s" % e)
    # else:
    #     print("未发生异常，浏览器实例化成功")
    # try:
        # 打开页面
        driver.get(bd)
    # except Exception as e:
    #     print("页面打开失败:%s,\n错误信息是:%s" % (bd, e))
    # else:
    #     print("未发生异常，页面打开成功")
        # sleep(1)
        # 隐式等待(全局，常用于自动化）
        driver.implicitly_wait(2)
        # 返回浏览器
        return driver


def handLer(driver):
    # 所有句柄
    handlers = driver.window_handles
    print("当前窗口所有的句柄是:%s" % handlers)
    # 当前页面的句柄
    onehandler = driver.current_window_handle
    print("当前窗口句柄是:%s" % onehandler)
    # 当前页面的url
    url = driver.current_url
    print("当前窗口的url是:%s" % url)
    # 当前页面的标题（title）
    title = driver.title
    print("当前窗口的标题是:%s" % title)

def finfElement(driver,locaer,value):
    # print(locaer)
    #异常处理容易出错误的代码块
    try:
        ele=driver.find_element(locaer,value)
    #发生异常时，捕获异常，并让程序继续执行下一个操作
    #异常类型是Exception且别名为e，并打印异常信息
    except Exception as e:
        print("元素定位失败！%s\n错误信息是:%s"%(value,e))
    #未发生异常时，执行的代码块
    else:
        print("元素定位成功！%s"%value)
        return ele
    #不管是否发生异常，均继续执行的代码块
    finally:
        print("不管你成功还是失败你都要执行！")


driver=getDriver(bai)