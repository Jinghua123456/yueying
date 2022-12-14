#coding='utf-8'
##处理excel文件
import logging
import xlrd
from common import config
from common.doLog import Logger

log=Logger(__name__,logging.DEBUG)
class DoExcel(object):
    #重构初始化方法
    def __init__(self,wk="testData.xlsx",st="elements"):
        #文件名
        filename=config.data_path+wk
        try:
            #打开工作簿
            self.workbook=xlrd.open_workbook(filename)
        except Exception as e:
            print("打开工作簿失败!原因是:%s"%e)
            log.logger.error("打开工作簿失败!原因是:%s"%e,exc_info=True)
        else:
            # print("打开工作簿成功!")
            log.logger.info("打开工作簿成功!")
        try:
            #获取sheet页,三种方式获取sheet页
            # stnames=self.workbook.sheet_names()
            # print(stnames)
            #第一种：列表的下标
            # self.sheet = stnames[0]
            # self.sheet =self.workbook.sheet_names()[0]同上一行
            # #第二种：索引 index
            # self.sheet=self.workbook.sheet_by_index(0)
            #第三种：sheet页名称
            self.sheet=self.workbook.sheet_by_name(st)
        except Exception as e:
            print("获取sheet页失败!原因是:%s"%e)
            log.logger.error("获取sheet页失败!原因是:%s"%e,exc_info=True)
        else:
            # print("获取sheet页成功!")
            log.logger.info("获取sheet页成功!")

    #读取单元格的值
    def readExcel(self,rownum,colnum):
        try:
            value=self.sheet.cell_value(rownum,colnum)
        except Exception as e:
            print("读取文件异常!原因是:%s"%e)
            log.logger.error("读取文件异常!单元格值(%s,%s)原因是:%s"%(rownum,colnum,e),exc_info=True)

        else:
            # print("读取文件成功!值是:%s"%value)
            log.logger.info("读取文件成功!单元格值(%s,%s)，值是:%s"%(rownum,colnum,value))
            return value

if __name__=="__main__":
    # ex=DoExcel()
    # value1=ex.readExcel(1,3)
    # value=ex.readExcel(1,4)
    # value3=ex.readExcel(10,3)
    # value2=ex.readExcel(10,4)
    # print(value,value1,value3,value2)
    ex=DoExcel("testData.xlsx","loginData")
    value=int(ex.readExcel(1,1))
    value1= int(ex.readExcel(1, 2))
    value2 = int(ex.readExcel(2, 1))
    value3= int(ex.readExcel(2, 2))
    print("11:%s,12:%s,21%s,22:%s"%(value,value1,value2,value3))

