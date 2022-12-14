#coding='utf-8'
#log类，处理文件
import logging

from common import config


class Logger(object):
    def __init__(self,name,level=logging.DEBUG):
        #定义记录器(logging)，日记对象，日志文件的实例
        self.logger=logging.Logger(name)
        #定义输出等级(setLevel)
        self.logger.setLevel(level)
        #输出格式
        fmt = logging.Formatter \
            ('%(asctime)s - %(filename)s:[%(lineno)s] - [%(levelname)s] - %(message)s')
        #定义处理器,写信息到日志文件
        fh=logging.FileHandler(config.log_path+config.cur_data+".log",encoding='utf-8')
        # 指定让处理器按照什么格式书写日志
        fh.setFormatter(fmt)
        #把处理器加到记录器
        self.logger.addHandler(fh)

if __name__=="__main__":
    #实例化logduix
    log=Logger(__name__,logging.DEBUG)
    log.logger.debug("我是debug级别的日志，等级是10")
    log.logger.info("我是info级别的日志，等级是20")
    log.logger.warning("我是warning级别的日志，等级是30")
    log.logger.error("我是error级别的日志，等级是40")
    log.logger.critical("我是critical级别的日志，等级是50")