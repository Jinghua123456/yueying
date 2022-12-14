#coding='utf-8'
#所有的配置文件信息
import os
import time


#当前时间
cur_time=time.strftime("%Y_%m_%d %H_%M_%S")

#当前日期
cur_date=time.strftime("%Y_%m_%d ")

#基本的页面地址
base_url="http://139.199.0.102/passport/login"

#项目路径
base_path=r"D:\pythonCoding\webAutoProject1\\"

#截图路径
photo_path=base_path+"/data/photos/"
photo_oath=os.path.join(base_path,"data/photos/")

#log(日志)路径
# log_path=base_path+'/data/logs/'
log_path=os.path.join(base_path,"data/logs/")

#数据连接
data_path=os.path.join(base_path,"data/testDatas/")

#测试用例路径
test_path=os.path.join(base_path,"demo/testCase/")

#测试报告路径
report_path=os.path.join(base_path,"data/reports/")