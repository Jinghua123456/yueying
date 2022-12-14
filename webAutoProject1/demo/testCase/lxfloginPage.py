#coding='utf-8'
#雷晓峰登录页面
from selenium.webdriver.common.by import By
from selenium import webdriver
from demo.pageObj.basePage import BasePage

#查询平均成绩大于70的男生的信息
#select * from student group by id having avg(grade)>70;

#select * from student  where sex = "男" group by id having avg(grade)>70;
#查询同名的学生姓名
#select name from student group by having count（*）>1;
#内连接，外连接（左连接，右链接）
# select name from student as s join grade as g on s.id=g.g_id where grade>80 GROUP BY id having count(*)>2;
# select name from student as s left join grade as g on s.id=g.g_id where grade>80 GROUP BY id having count(*)>2;
# select name from student as s right join grade as g on s.id=g.g_id where grade>80 GROUP BY id having count(*)>2;
driver=webdriver.Chrome()
lxf=BasePage(driver)
#打开雷晓峰页面
lxf.open()
#隐式等待
lxf.driver.implicitly_wait(3)
#定位账号
zh=(By.CSS_SELECTOR,"body > app-root > layout-passport > div > div > passport-login > div > form > nz-form-item:nth-child(2) > nz-form-control > div > span > nz-input-group > input")
lxf.findElement(zh)
#输入12345
lxf.inputValue(zh,"12345")
#定位密码
m=(By.CSS_SELECTOR,"body > app-root > layout-passport > div > div > passport-login > div > form > nz-form-item:nth-child(4) > nz-form-control > div > span > nz-input-group > input")
#输入121121
lxf.inputValue(m,"121121")
#定位登录
d=(By.CSS_SELECTOR,"body > app-root > layout-passport > div > div > passport-login > div > form > nz-form-item:nth-child(6) > button")
#点击登录
lxf.doClick(d)
#获取错误信息
w=(By.CSS_SELECTOR,"body > app-root > layout-passport > div > div > passport-login > div > form > nz-form-item:nth-child(4) > nz-form-control > div > nz-form-explain > div")
lxf.getElementValue(w)
#截图
lxf.doPhoto("lxf")
#关闭
lxf.driver.quit()
