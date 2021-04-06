# ！/usr/bin/env python
# encoding:utf-8
# print("网站名:{name},地址：{url}".format(name='百度',url='www.baidu.com'))
# a=[{"name":"laihongyu","age":"18","pay":"10k"},{"name2":"hongyu","age":"19","pay":"30k"},{"name3":"yu","age":"20","pay":"30k"}]
# print("我的名字是{}、{}和{}".format(a[0]["name"],a[1]["name2"],a[2]["name3"]))
# import requests
# #requests.packages.urllib3.disable_warnings()
# re_url ="https://www.baidu.com/"
# res=requests.get(url=re_url,verify=False)
# print(res.status_code)

#
import os
import time

# import pytest
# import yaml
# #
# # file_path = os.path.join(os.path.dirname(__file__), "mysql.yaml")
# # print(type(file_path))
# with open("C:/Users/86182/PycharmProjects/laihongyutest/config/name.yaml", "r",
#           encoding="utf-8") as f:
#     print(yaml.load(f.read(), Loader=yaml.FullLoader))
# import os
#
# import yaml
#
# path=os.path.join(os.path.dirname(os.path.dirname(__file__)),"config/config.yaml")
# print(path)
# with open(path, "r", encoding="utf-8") as f:
#     print(yaml.load(f.read(), Loader=yaml.FullLoader))
# import pymysql
#
#
# sql = "select * from test_table"
# data2=[
#     ('错误密码错误登录', '5'),
#     ('密码位数错误登录', '6')
# ]
# sql2 = "update test_table set func=%s where id=%s"
# connecet = pymysql.connect(host="localhost", user="root", password="root", database="test_db", port=3306)
# cursor = connecet.cursor()
# #插入多条数据
# cursor.executemany(sql2, data2)
# result=cursor.execute(sql2,('测试z','5'))
# print(result)
# connecet.commit()
# cursor.execute(sql)
# data = cursor.fetchall()
# print(data)
#
# cursor.close()
# connecet.close()
# print(type(a))
log_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))+'\\logs'
log=os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "logs")
print(log_path)
print(log)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
