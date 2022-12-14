#coding='utf-8'
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from testpage import config

#地址
baidu="file:///C:/Users/%E5%88%98%E6%9C%8B%E5%BC%BA/Desktop/alert.html"
lxf="http://139.199.0.102"
bai="http://www.baidu.com"
mall="https://mail.163.com/"
qq="https://mail.qq.com/"

#定义当前时间变量，且格式化：2022_11_17 16_36_17
cur_time=time.strftime("%Y_%m_%d %H_%M_%S")

# #定义项目路径
# base_path="D:\pythonCoding\webAutoProject\webAutoProject"
#定义截图存放路径：当前项目目录下的data目录下的photos目录下
photo_path="D:\pythonCoding\webAutoProject\data\photos\\"

#浏览器实例化及打开页面，并返回对象
def getDriver(vurl):
    try:
        #实例化浏览器
        driver=webdriver.Chrome()
    except Exception as e:
        print("发生异常，浏览器实例化失败！,\n错误信息:%s"%e)
    else:
        print("未发生异常，浏览器实例化成功")

    try:
        #打开页面
        driver.get(vurl)
    except Exception as e:
        print("页面打开失败:%s,\n错误信息是:%s"%(vurl,e))
    else:
        print("未发生异常，页面打开成功")
        # sleep(1)
        #隐式等待(全局，常用于自动化）
        driver.implicitly_wait(2)
        #返回浏览器
        return driver

def handler(driver):
    # 所有句柄
    handlers = driver.window_handles
    # print("当前窗口所有的句柄是:%s" % handlers)
    # 当前页面的句柄
    onehandler = driver.current_window_handle
    # print("当前窗口句柄是:%s" % onehandler)
    # 当前页面的url
    url = driver.current_url
    # print("当前窗口的url是:%s" % url)
    # 当前页面的标题（title）
    title = driver.title
    # print("当前窗口的url是:%s" %title)
    print("新页面信息开始打印-------------------------")
    print("当前窗口所有的句柄是:%s,\n当前窗口句柄是:%s,\n当前窗口的url是:%s,\n当前窗口的标题是:%s" % (handlers,onehandler,url,title))
    print("新页面信息结束打印-------------------------")

def iframe(driver,name,pwd):
        # 定位iframe元素
        # iframe = driver.find_element_by_css_selector("#login_frame")
        iframe=config.finfElement(driver,By.CSS_SELECTOR,"#login_frame")
        # 将光标转移至小页面下
        driver.switch_to.frame(iframe)
        # sleep(1)
        # 定位账号,点击，输入
        # a = driver.find_element_by_css_selector("#u")
        # a=config.finfElement(driver,By.CSS_SELECTOR,"#u")
        a = finfElement(driver, By.CSS_SELECTOR, "#u")
        a.clear()
        # sleep(1)
        a.send_keys(name)
        # sleep(1)
        # 定位密码,点击，输入
        # b = driver.find_element_by_css_selector(".inputstyle.password")
        b=config.finfElement(driver,By.CSS_SELECTOR,".inputstyle.password")
        # sleep(1)
        b.send_keys(pwd)
        # sleep(1)
        # 定位登录
        # c = driver.find_element_by_css_selector("#login_button")
        c=config.finfElement(driver,By.CSS_SELECTOR,"#login_button")
        c.click()
        # sleep(1)
        # 隐式等待
        driver.implicitly_wait(2)
        # er = driver.find_element(By.CSS_SELECTOR, "#err_m").text
        er=config.finfElement(driver,By.CSS_SELECTOR,"#err_m").text
        print("登录失败，信息是:%s" % er)
        # 回到主页面
        driver.switch_to.default_content()
        sleep(1)

def finfElement(driver,locaer,value):
    #异常处理容易出错误的代码块
    try:
        ele = WebDriverWait(driver, 5, 0.1).until(EC.visibility_of_element_located((locaer, value)))
        # ele=driver.find_element(locaer,value)
    #发生异常时，捕获异常，并让程序继续执行下一个操作
    #异常类型是Exception且别名为e，并打印异常信息
    #Exception as e:as把Exception实例化为e
    except Exception as e:
        print("元素定位失败！%s\n错误信息是:%s"%(value,e))
    #未发生异常时，执行的代码块
    else:
        print("元素定位成功！%s"%value)
        return ele
    #不管是否发生异常，均继续执行的代码块
    finally:
        print("不管你成功还是失败你都要执行！")

#对点击在异常处理
def doClick(ele):
    try:
        ele.click()
    except Exception as e:
        print("发生异常，点击失败，错误信息是:%s"%e)
    else:
        print("未发生异常，点击成功")

#对输入文本进行异常处理
def doInputValue(ele,value):
    try:
        ele.send_keys(value)
    except Exception as e:
        print("发生异常，输入内容是:%s\n错误信息是:%s"%(value,e))
    else:
        print("未发生异常，输入内容成功！%s"%value)
#截图异常处理
def doPhoto(driver,value):
    filename=photo_path+cur_time+value+".png"
    try:
        driver.get_screenshot_as_file(filename)
    except Exception as e:
        print("截图失败，错误信息是:%s"%e)
    else:
        print("截图成功！")



