#coding='utf-8'
#log类，处理log文件
import logging

from common import config


class Logger(object):
    def __init__(self,name,fileLevel=logging.WARNING):

        #定义记录器(logging)，日志对象，日志文件的实例
        self.logger=logging.Logger(name)

        #定义日志输出等级(setLevel)
        self.logger.setLevel(fileLevel)

        #格式化日志(模板）
        # fms='%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s'
        # fmt = logging.Formatter(fms)
        fmt=logging.Formatter\
            ('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')

        #处理器，写信息到日志文件
        logname=config.log_path+config.cur_date+".log"
        fh=logging.FileHandler(logname,encoding="utf-8")
        #指定让处理器按照什么格式书写日志
        fh.setFormatter(fmt)

        #将处理器加入记录器中：让处理器处理谁,让处理器给谁干活
        self.logger.addHandler(fh)


if __name__=="__main__":
    #实例化log日志对象
    logger=Logger(__name__,logging.DEBUG)
    #写日志
    # logging.DEBUG =10
    # logging.INFO =20
    # logging.WARNING =30
    # logging.ERROR =40
    # logging.CRITICAL =50
    #写debug级别的日志，等级10
    # logger.logger.log(logging.DEBUG,"我是DEBUG级别的日志，等级是10")
    logger.logger.debug("我是DEBUG级别的日志，等级是10")
    # 写INFO级别的日志，等级20
    # logger.logger.log(logging.INFO, "我是INFO级别的日志，等级是20")
    logger.logger.info("我是INFO级别的日志，等级是20")
    # 写WARNING级别的日志，等级30
    # logger.logger.log(logging.WARNING, "我是WARNING级别的日志，等级是30")
    logger.logger.warning("我是WARNING级别的日志，等级是30")
    # 写ERROR级别的日志，等级40
    # logger.logger.log(logging.ERROR, "我是ERROR级别的日志，等级是40")
    logger.logger.error("我是ERROR级别的日志，等级是40")
    # 写CRITICAL级别的日志，等级50
    # logger.logger.log(logging.CRITICAL, "我是CRITICAL级别的日志，等级是50")
    logger.logger.critical("我是CRITICAL级别的日志，等级是50")