# ！/usr/bin/env python
# encoding:utf-8
# 封装请求方法
import json

import requests

from common.gobal import global_exc_var
from common.log import Log


class Runmethod():
    "get方法封装"
    log = Log()

    def get_method(self, url, param=None, header=None):
        res = None
        if param != None:
            res = requests.get(url=url, params=param, headers=header)
        else:
            res = requests.get(url=url, headers=header)
            print(res.status_code)
        return res.json()

    "封装post请求"

    def post_method(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header, verify=True)
        else:
            res = requests.post(url=url, data=data, verify=True)
        return res.json()

    "调用get/post方法"

    def run_main(self, method, url, data=None, header=None):
        res = None
        try:
            if method == "post" or method == "POST" or method == "Post":
                res = self.post_method(url, data, header)
            elif method == "get" or method == "GET" or method == "Get":
                res = self.get_method(url, data, header)
            else:
                print("request传参错误")
                return "request传参错误"
            return res
        except Exception as e:
            print(e)
            self.log.error("请求报错{}".format(e))


if __name__ == "__main__":
    # url1 = ReadFile().read_yaml("yaml_path")['translate_url']
    # url=url1+'/trans/word'
    # url = "http://120.205.22.79:37785/koznak/yuandan/getUserIntegralInfo"
    # data = {'uid': 'qq_92100537288580228181565666462', 'web_token': 'c8274491b18a4508b606372620390335',
    #         'version': '8.1.0.android_Koznak_release'}
    run = Runmethod()
    url2 = 'https://api.sozman.shop:37741/getVerifyRecord'
    data2 = {"time": "2021-01", "page": "1"}
    print(run.run_main("get", url2, data2))
    # a=run.run_main("get", url)
    # b=a['code']
    # c=a['message']
    # print(b,type(b))
    # print(c,type(c))
    # header={"Content-Type": "application/json"}
    # url2 = "https://api.sozman.shop:37741/trans/word"
    # data = {"text": "ces"}
    # a=run.run_main("POST", url2, data)
    # b=a['code']
    # c=a['message']
    # print(b, type(b))
    # print(c, type(c))
    # print(run.run_main("POST", url2, data))
    # url3 = "https://api.sozman.shop:37741//userTrans"
    # data3 = {"src": "ceshias ", "tgt": "test111"}
    # print(run.run_main("post", url3, data3, header=''))
    # print(global_exc_var.Funciton,type(global_exc_var.Funciton))
    # a= ["A","B"]
    # url4=int(global_exc_var.Funciton)
    # print(a[url4])