#coding='utf-8'
#学员档案
from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver

from demo.pageObj.basePage import BasePage
from demo.pageObj.loginPage import LoginPage

driver=webdriver.Chrome()

class Workbench(BasePage):
    #学员管理

        sg=(By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.flex_H_Center.nav1.dis.ng-star-inserted > span")

    #教务管理

        # jw=(By.XPATH,"/html/body/app-root/layout-default/layout-sidebar/div/div/div[3]/div[1]/span")
        jw=(By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(3) > div.flex_H_Center.nav1.dis.ng-star-inserted > span")
    #管理机构

        jg=(By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(4) > div.flex_H_Center.nav1.dis.ng-star-inserted > span")

    #数据分析

        sj=(By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(5) > div.flex_H_Center.nav1.dis.ng-star-inserted > span")

    #招生吧

        zs=(By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(6) > div.flex_H_Center.nav1.dis.ng-star-inserted > span")

    #考级管理

        kj=(By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(10) > div.flex_H_Center.nav1.dis.ng-star-inserted > span")
#冒泡排序，大到小
i=0
l=[23,57,87,99,56,20]
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]<l[j]:
            l[i],l[j]=l[j],l[i]
        print("大循环第%s次,小循环第%s次"%(i,j),l)
    print("大循环第%s次"%(i+1),l)
print("循环结束",l)












if __name__ == '__main__':

    l=LoginPage(driver)
    l.open()
    l.loginFun()
    sleep(1)
    s = Workbench(driver)
    l.driver.implicitly_wait(5)
    # l.doClick(s.jw)
    # sleep(1)
    l.jwgl()
    sleep(1)
    # l.doClick(s.kj)
    # sleep(1)
    # l.doClick(s.zs)
    # sleep(1)
    # l.doClick(s.jg)
    # sleep(1)
    l.doClick(l.zs)
    # l.sjfx()
    sleep(1)
    # 获取数据分析页面的url
    url = l.driver.current_url
    print(url)

    driver.quit()