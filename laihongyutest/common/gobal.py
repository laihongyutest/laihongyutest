#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/7 16:14
# @Author  : laihongyu
# 定义excel各个列名字
class global_exc_var:
    Funciton = '0'
    Casename = '1'
    Type = '2'
    Run = '3'
    URL = '4'
    Headers = '5'
    Params = '6'
    Expect1 = '7'

    # 获取url
    def get_url(self):
        return global_exc_var.URL

    # 获取header
    def get_header(self):
        return global_exc_var.Headers

    # 获取请求参数
    def get_params(self):
        return global_exc_var.Params

    # 获取期望结果1
    def get_expect1(self):
        return global_exc_var.Expect1


