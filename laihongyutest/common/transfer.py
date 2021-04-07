#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/7 15:45
# @Author  : laihongyu
import time

from common.gobal import global_exc_var
from common.log import Log
from common.readfile import ReadFile
from common.readsql import ReadSql
from common.runmethod import Runmethod

str_time = time.strftime('%Y-%m', time.localtime())


class Trans():
    log = Log()

    def __init__(self, trans_url=None):
        self.params = ReadFile().read_excel("翻译", "翻译文本", "输入汉字")
        self.yaml_data = ReadFile().read_yaml("yaml_path")
        if trans_url is None:
            self.url = self.yaml_data['translate_url']
        else:
            self.url = self.yaml_data[trans_url]

    # 翻译
    def trans_text(self, text):
        try:
            link_url = self.params[0][int(global_exc_var.URL)]
            url = self.url + link_url
            type = self.params[0][int(global_exc_var.Type)]
            data = eval(self.params[0][int(global_exc_var.Params)])
            data['text'] = text
            header = self.params[0][int(global_exc_var.Headers)]
            res = Runmethod().run_main(type, url, data, header)
            return res
        except Exception as e:
            self.log.error("登录报错{}".format(e))

    def user_submit_trans(self, src_text, tgt_text):
        """
        src_text原文档
        tgt_text翻译文档，翻译成维语
        """
        url = self.url + '/userTrans'
        data = {}
        data['src'] = src_text
        data['tgt'] = tgt_text
        res = Runmethod().run_main('post', url, data)
        return res

    # 审核翻译文本
    def check_trans(self, text, result=None):
        """"
        CHECK_STATE = 1 待审核
        CHECK_STATE = 2 审核通过
        CHECK_STATE = 3 审核不通过
        """
        # str_time =time.datetime ()
        data = {"time": str_time, "id": "0", "state": "1"}
        print(data)
        url = self.url + '/updateVerifyRecord'
        table_name = "verify_record_" + str_time
        sql = "select * from `{}` where src_text='{}'".format(table_name, text)
        sql_record = ReadSql().read_sql('select_one', sql)
        id = sql_record[0]
        # print(id)
        if result == "pass" or result == "Pass" or result == "PASS":
            check_state = 2
        elif result == "fail" or result == "Fail" or result == "FAIL":
            check_state = 3
        data['id'] = id
        data['state'] = check_state
        res = Runmethod().run_main("post", url, data)
        return res

    # 判断审核结果
    def get_trans_result(self):
        # url = self.url + '/getVerifyRecord'
        # data = {"time": "2021-01", "": ""}
        pass


if __name__ == "__main__":
    test = Trans('translate_url')
    # # print(test.user_submit_trans('这个是测试2', "سىز ماڭا ياتلىق بولۇشنى خالامسىز"))
    print(test.trans_text("你好美丽啊"))
    # print(test.check_trtest.trans_text("这个是测试的模板001")['code']ans('这个是测试001', 'Pass'))

