#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time    : 2021/1/26 14:26
# @Author  : laihongyu
import json

import allure
import pytest
#测试测试测
from common.readfile import ReadFile
from common.transfer import Trans


@allure.feature("翻译")
class Test:
    @allure.story("直接翻译")
    @allure.title("输入汉字文字翻译-小牛+三方翻译")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description('翻译小程序描述')
    def test_commit_trans1(self):
        with allure.step('翻译'):
            allure.attach(ReadFile().read_yaml('yaml_path')['translate_url'] + '/trans/word', '请求地址',
                          allure.attachment_type.JSON)
            Trans().trans_text('这个是测试的模板001')
            allure.attach(str(Trans().trans_text('这个是测试的模板001')), '返回的请求内容', allure.attachment_type.JSON)
        with allure.step("断言"):
            with allure.step('断言code'):
                assert Trans().trans_text('这个是测试的模板001')['code'] == 1001
            with allure.step("断言message是否正确"):
                assert Trans().trans_text('这个是测试的模板001')['message'] == '小牛+三方翻译成功'
            with allure.step("断言data不为空"):
                assert Trans().trans_text('这个是测试的模板001')['data'] != ''

    @allure.story("直接翻译")
    @allure.title("小牛翻译")
    def test_commit_trans2(self):
        with allure.step('添加翻译'):
            Trans().trans_text('你好美丽啊')
            allure.attach(str(Trans().trans_text('你好美丽啊')), '返回的请求内容', allure.attachment_type.JSON)
        with allure.step('断言翻译code'):
            assert Trans().trans_text('你好美丽啊')['code'] == 1001
        with allure.step("断言data不为空"):
            assert Trans().trans_text('你好美丽啊')['data'] != ''

    @allure.story("直接翻译")
    @allure.title("翻译英文")
    def test_commit_trans3(self):
        with allure.step('翻译英文'):
            Trans().trans_text("I LOVE U")
            allure.attach(str(Trans().trans_text('I LOVE U')), '返回的请求内容', allure.attachment_type.JSON)
        with allure.step('断言code'):
            assert Trans().trans_text('I LOVE U')['code'] == 1001
        with allure.step('断言data'):
            assert Trans().trans_text('I LOVE U')['data'] != ''
        with allure.step('断言message'):
            assert Trans().trans_text('I LOVE U')['message'] != ''

    @allure.story("直接翻译")
    @allure.title("翻译符号")
    def test_commit_trans4(self):
        with allure.step('特殊符号翻译'):
            Trans().trans_text("，。/；‘1")
            allure.attach(str(Trans().trans_text('，。/；‘1')), '返回的请求内容', allure.attachment_type.JSON)
        with allure.step('断言code'):
            assert Trans().trans_text('，。/；‘1')['code'] == 1001
        with allure.step('断言data'):
            assert Trans().trans_text('，。/；‘1')['data'] != ''
        with allure.step('断言message'):
            assert Trans().trans_text('，。/；‘1')['message'] != ''


    # @allure.story('用户自己提交翻译')
    # @allure.title('自己提交正常的翻译')
    # def test_user_commit_tran(self):
    #     with allure.step('提交正常的翻译'):
    #         Trans().user_submit_trans('我是中国人','')
    #     with allure.attach
