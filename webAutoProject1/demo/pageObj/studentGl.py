#coding='utf-8'
#学员管理页面
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from demo.pageObj.basePage import BasePage
from demo.pageObj.loginPage import LoginPage



class Student(BasePage):
    #学员档案
    stud=(By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.nav2.ng-star-inserted > div:nth-child(1)")
    #招生跟进
    gj=(By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.nav2.ng-star-inserted > div:nth-child(2)")
    #学员费用
    cost=(By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.nav2.ng-star-inserted > div:nth-child(3)")
    #导入/导出
    imp=(By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.nav2.ng-star-inserted > div:nth-child(4)")
    #新生统计
    count=(By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.nav2.ng-star-inserted > div:nth-child(3)")
    #费用完结统计
    free=(By.CSS_SELECTOR,"body > app-root > layout-default > layout-sidebar > div > div > div:nth-child(2) > div.nav2.ng-star-inserted > div:nth-child(4)")
    #页面跳转

    # # 查询
    # cx = (By.CSS_SELECTOR, "[placeholder='请输入学员姓名、昵称、联系电话、招生老师']")
    # qr = (By.CSS_SELECTOR, "[style='background: #fafbfd;']")
    # # 待跟进学员
    # gj = (By.CSS_SELECTOR,
    #       "body > app-root > layout-default > section > app-stu-file > div > div.bg-primary > app-tab2 > div > div:nth-child(3) > div")
    # # 在读学员
    # zd = (By.CSS_SELECTOR,
    #       "body > app-root > layout-default > section > app-stu-file > div > div.bg-primary > app-tab2 > div > div.tab-outer.ng-star-inserted.tab-sel")
    # # 流失学员
    # ls = (By.CSS_SELECTOR,
    #       "body > app-root > layout-default > section > app-stu-file > div > div.bg-primary > app-tab2 > div > div:nth-child(5) > div")


if __name__=="__main__":

    driver=webdriver.Chrome()
    st = Student(driver)
    lxf = "http://139.199.0.102"
    login=LoginPage(driver,lxf)
    login.open()
    login.loginFun("15003807446","12345678qwe")
    sleep(1)
    login.gl()
    sleep(1)
    # st.doClick(st.stud)
    # sleep(1)
    st.doClick(st.gj)
    # sleep(1)
    # st.doClick(st.cost)
    # sleep(1)
    # st.doClick(st.imp)
    # sleep(1)
    # st.doClick(st.count)
    # sleep(1)
    # st.doClick(st.free)
    login.driver.quit()







