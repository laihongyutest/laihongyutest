# ！/usr/bin/env python
# encoding:utf-8
import logging
import os
import time

log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
if not os.path.exists(log_path): os.mkdir(log_path)


class Log():
    """
    log类
    logging模块loggers，handlers，filters，formatters，
    loggers就是程序可以直接调用的一个日志接口，可以直接向logger写入日志信息。logging.getLogger(name)
    handles将logger发过来的信息进行准确地分布，送往正确的地方
    filters提供更细粒度的判断
    formatters指定打印的格式布局
    loggger，handle，filter，formatter
    logging，handle，filter，formatter
    logging, handel，filter，formatter
    noset，debug，info，warning，error，critical


    """

    def __init__(self):
        # 创建一个logger
        #        re=time.strftime("%Y-%m-%d %H_%M_%S")
        self.log_name = os.path.join(log_path, '%s.log' % time.strftime('%Y-%m-%d %H_%M_%S'))
        #      self.log_name=log_path+re+'.logs'
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        # 定义日志输出格式
        self.formatter = logging.Formatter('%(asctime)s-%(filename)s-%(lineno)d-%(levelname)s-%(message)s')

    def console(self, level, message):
        # 创建一个filehandle
        fh = logging.FileHandler(self.log_name, mode="w", encoding='utf-8')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        # 创建一个控制台handler
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        if level == "info":
            self.logger.info(message)
        elif level == "warning":
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
        elif level == 'debug':
            self.logger.debug(message)
        self.logger.removeHandler(fh)
        self.logger.removeFilter(ch)
        fh.close()

    def debug(self, message):
        self.console('debug', message)

    def info(self, message):
        self.console('info', message)

    def warning(self, message):
        self.console('waring', message)

    def error(self, message):
        self.console('error', message)


if __name__ == "__main__":
    log = Log()
    log.info('--测试--')
