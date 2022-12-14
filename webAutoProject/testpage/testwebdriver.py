#coding='utf-8'
#测试浏览器驱动
# from time import sleep
#
# from selenium import webdriver
#
# #定义浏览器驱动
# driver=webdriver.Chrome()
# #打开页面
# driver.get("http://www.baidu.com")
# #最大化
# driver.maximize_window()
# #等待3秒
# sleep(3)
#最小化
# driver.minimize_window()
# sleep(3)
# #打开新页面
# driver.get("https://www.w3school.com.cn")
# sleep(3)
# #刷新
# driver.refresh()
# sleep(1)
# #向后
# driver.back()
# sleep(1)
# #向前
# driver.forward()
# sleep(1)
# #关闭窗口,当前窗口
# driver.close()
# sleep(1)
#元素定位，通过id定位，百度输入框
# inp=driver.find_element_by_id("kw")
#通过name定位
# inp=driver.find_element_by_name("wd")
#通过classname定位
# inp=driver.find_element_by_class_name("s_ipt")
#通过标签定位（tag name不唯一，一般不使用）
# inp=driver.find_element_by_tag_name("input")
#通过xpath-绝对路径定位
# inp=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[1]/div[1]/form/span[1]/input")
#通过xpath-相对路径定位:相对加绝对
# inp=driver.find_element_by_xpath("//form/span[1]/input")
#通过xpath-相对路径定位:相对加相对，属性（@）
# inp=driver.find_element_by_xpath("//form//input[@id='kw']")
#通过xpath；相对路径，属性（@）
# inp=driver.find_element_by_xpath("//input[@id='kw']")

#css（选择器）定位元素(id:#加id值）
# inp=driver.find_element_by_css_selector("#kw")
#css（选择器）定位元素(class:点（.）加class值）
# inp=driver.find_element_by_css_selector(".s_ipt")
#css（选择器）定位元素(属性:[属性='属性值']）
# inp=driver.find_element_by_css_selector("[name ='wd']")
#css（选择器）定位元素(父子级:通过父级唯一定位，箭头（>)指向子级）
# b5=driver.find_element_by_css_selector("#u1>a")

# b5=driver.find_element_by_css_selector("#u>a:nth-child(3)")

#css（选择器）定位元素,模糊匹配:前半部分（开头 ^）
# b5=driver.find_element_by_css_selector("a[class^='s-top-login-btn']")
#css（选择器）定位元素,模糊匹配:后半部分（结尾 $）
# b5=driver.find_element_by_css_selector("a[id$='loginbtn']")
#css（选择器）定位元素,模糊匹配:包含部分(*)
# b5=driver.find_element_by_css_selector("a[class*='c-btn']")

# b5=driver.find_element(By.CSS_SELECTOR,"a[class*='c-btn']")
# b5=driver.find_element_by_css_selector("a[class*='s-top-login-btn']")

# sleep(1)
# b5.click()
# sleep(2)

#想文本框输入内容
# inp.send_keys("python")
# sleep(1)
#通过xpath:相对路径，模糊匹配，部分值，百度一下按钮（contains函数包含）
# but=driver.find_element_by_xpath("//input[contains(@class,'s_btn')]")
# set=driver.find_element_by_xpath("//span[contains text()='设置']")

##分别通过id、class、xpath（绝对、相对家绝对、相对（属性，分别通过type、value））
# but=driver.find_element_by_id("su")
#class='bg s_btn'bg与s_btn父级子级的关系，乘积写为bg.s_btn
# but=driver.find_element_by_class_name("bg.s_btn")

# but=driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div[2]/div[1]/form/span[2]/input")
# but=driver.find_element_by_xpath("//form/span[2]/input")
# but=driver.find_element_by_xpath("//input[@type='submit']")
# but=driver.find_element_by_xpath("//input[@value='百度一下']")
# but=driver.find_element_by_xpath("//input[@type='submit' and @value='百度一下']")
# but=driver.find_element_by_xpath("//*[@type='submit' and @value='百度一下']")
#点击按钮
# but.click()
# sleep(2)
#通过text值，text（）方法定位
# set=driver.find_element_by_xpath("//span[text()='设置']")
# set.click()
# sleep(2)

#通过超链接定位元素（a标签）
# a=driver.find_element_by_link_text("新闻")
#通过超链接部分内容定位元素
# a1=driver.find_element_by_partial_link_text("官方")

# a1.click()
# a.click()
# sleep(2)
# b3=driver.find_element_by_css_selector("#su")
# b3=driver.find_element_by_css_selector(".bg.s_btn")
# b3=driver.find_element_by_css_selector("[type='submit']")
# b3=driver.find_element_by_css_selector("[value='百度一下']")
# b3.click()
# sleep(2)
#关闭当前窗口
# driver.close()
# sleep(2)
# #退出
# driver.quit()
# sleep(3）

#元素定位优先级:cssid>xpath>name>class


