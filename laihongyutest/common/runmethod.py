# ！/usr/bin/env python
# encoding:utf-8
# 封装请求方法
import requests

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
        return res

    "封装post请求"

    def post_method(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.post(url=url, data=data, verify=False)
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
    url = "https://www.baidu.com"
    run = Runmethod()
    run.run_main("get", url)
