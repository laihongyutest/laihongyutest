# ！/usr/bin/env python
# encoding:utf-8
# errHTML = '''
# <HTML><HEAD><TITLE>
# Friends CGI Demo</TITLE></HEAD>
# <BODY><H3>ERROR</H3>
# <B>%s</B><P>
# <FORM><INPUT TYPE=button VALUE=Back
# ONCLICK="window.history.back()"></FORM>
# </BODY></HTML>
# '''
# # a = "Hello"
# # if 'H' in  a:
# #     print("ZAI")
# print(errHTML)
#
# sql = "select * from test_table"
# list = ['Google', 'Runoob', "Zhihu", "Taobao", "Wiki"]
# print(list[0:-2])
# print(sql[-3:-1])
#
import logging
import os
import time

# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s- %(name)s- %(filename)s- %(message)s')
# logging.debug("THIS IS DEBUG MESSAGE")
# logging.info("THIS IS INFO MESSAGE")
# logging.warning("this is warning messsage ")
# 创建一个logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
# 创建一个handle，写入日志文件
re = time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time()))
#log_path =os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "logs/test_log")
log_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'\\logs\\test_log'
log_name = log_path + re+'.log'
fh = logging.FileHandler(log_name, mode='w')
ch=logging.StreamHandler()

fh.setLevel(logging.DEBUG)
# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(filename)s-line:%(lineno)d -%(levelname)s:%(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(ch)
# 第四步，将logger添加到handler里面
logger.addHandler(fh)
logger.debug('dubug message')
logger.info('info message')
logger.warning('warning message')
logging.warning('%s is %d years old.', 'Tom', 10)
logger.error('error message')
logger.critical('critical message')

# logger = logging.getLogger(__name__)
# logger.setLevel(level=logging.info)
# 定义一个RotatingFileHandler，最多备份3个日志文件，每个文件最大1k
