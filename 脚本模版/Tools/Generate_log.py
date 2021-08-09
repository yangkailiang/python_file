import sys
import os
import logging
from logging import handlers
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), "../")))
from Tools.tools import *


class Logger(object):
    logger1 = None
    # 日志级别关系映射
    level_relations = {
                        'debug': logging.DEBUG,
                        'info': logging.INFO,
                        'warning': logging.WARNING,
                        'error': logging.ERROR,
                        'crit': logging.CRITICAL
                        }

    def __init__(self,filename = os.path.abspath(os.path.join(os.getcwd(), "../")) + '/Journal/sys_log.txt',level='info',when='D',backCount=3):
        if self.logger1 is None:
            # 设置格式
            fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
            self.logger = logging.getLogger(filename)
            # 设置日志格式
            format_str = logging.Formatter(fmt)
            # 设置日志级别
            self.logger.setLevel(self.level_relations.get(level))
            # 往屏幕上输出
            sh = logging.StreamHandler()
            # 设置屏幕上显示的格式
            sh.setFormatter(format_str)
            # 往文件里写入#指定间隔时间自动生成文件的处理器
            th = handlers.TimedRotatingFileHandler(filename=filename, interval=30, when=when, backupCount=backCount, encoding='utf-8')
            # 设置文件里写入的格式
            th.setFormatter(format_str)
            # 把对象加到logger里
            self.logger.addHandler(sh)
            self.logger.addHandler(th)


if __name__ == '__main__':

    logg = Logger().logger.warning('ddddd')



'''
            #实例化TimedRotatingFileHandler
            #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
            # S 秒
            # M 分
            # H 小时、
            # D 天、
            # W 每星期（interval==0时代表星期一）
            # midnight 每天凌晨
'''