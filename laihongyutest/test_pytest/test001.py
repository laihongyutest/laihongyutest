# ！/usr/bin/env python


# encoding:utf-8

import pytest


# test01.py
class Test(object):
    def test2(self, get_token):
        token = 'qeehfjejwjwjej11sss@22'
        print("【执行test02.py-Test类-test2用例,获取get_token：%s】" % get_token)
        assert get_token == token


if __name__ == "__main__":
    pytest.main(["-s", "test001.py", "test002.py", '-html=./report.html'])
