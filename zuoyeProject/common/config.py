#coding='utf-8'
#所有的配置文件
import os.path
import time

#基本的页面地址
# url="http://139.199.0.102/passport/login"
url="http://www.baidu.com"
#项目路径
base_path="D:\pythonCoding\zuoyeProject\\"

#截图路径
photo_path=base_path+"/data/photos/"

#当前时间
cur_time=time.strftime("%Y_%m_%d %H_%M_%S")

#当前日期
cur_data=time.strftime("%Y_%m_%d")

#log路径
log_path=os.path.join(base_path,"data/logs/")

#数据连接
data_path=os.path.join(base_path,"data/testDatas/")