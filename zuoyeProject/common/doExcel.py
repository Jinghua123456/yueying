#coding='utf-8'
#数据驱动
import logging

import xlrd

from common import config
from common.doLog import Logger

#调用Longger
log=Logger(__name__,logging.INFO)
class DoExcel(object):
    #重构初始化方法
    def __init__(self,wk="testDatas.xlsx",st="elements"):
        #文件名
        filename=config.data_path+wk
        try:
            #打开工作簿
            self.workbook=xlrd.open_workbook(filename)
            #获取sheet页的名称
            self.sheet=self.workbook.sheet_by_name(st)
        except Exception as e:
            log.logger.error("打开工作簿失败！%s\n打开sheet页失败！%s"%(e),exc_info=True)
        else:
            log.logger.info("打开工作簿成功！打开sheet页成功！")


        #获取单元格的值
    def readExxcel(self,rownum,colnum):
        try:
            value=self.sheet.cell_value(rownum, colnum)
        except Exception as e:
            log.logger.error("读取失败！单元格（%s,%s），原因是:%s"%(rownum,colnum,e),exc_info=True)
        else:
            log.logger.info("读取成功！单元格（%s,%s），值是:%s"%(rownum,colnum,value))
            return value


if __name__ == '__main__':
    ex=DoExcel()
    value=ex.readExxcel(1,4)
    print(value)