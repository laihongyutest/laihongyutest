import os
import time

import allure
import pytest


# test03.py
class Test(object):
    @allure.feature('第一步')
    @allure.story('测试第二步')
    @allure.title('用例名称')
    def test3(self, get_token):
        token = 'qeehfjejwjwjej11sss@22'
        print("【执行test03.py-Test类-test3用例,获取get_token：%s】" % get_token)
        assert get_token == token

    @allure.feature('验证token2')
    def test4(self, get_token):
        token = 'qeehfjejwjwjej11sss@22'
        print("【执行test03.py-Test类-test4用例,获取get_token：%s】" % get_token)
        assert get_token == token


if __name__ == "__main__":
    print("---测试-----")
    pytest.main(["-s", "-q", "--alluredir=../report/result", 'test002.py'])
    # spilt = 'pytest -s test002.py --alluredir=report/result'
    # os.system(spilt)
    # time.sleep(10)
    split2 = 'allure ' + 'generate  ' + '../report/result ' + '-o ' + '../report/html ' + '--clean'
    os.system(split2)

# import pytest
#
#
# @pytest.fixture(scope='function')
# def before():
#     print('--测试之前---')
#     return '测试之前'
#
#
# @pytest.mark.parametrize("user,pwd", [("18221124104", 111111)])
# class Testcase:
#     def setup(self):
#         print("-----SETUP-----")
#
#     def teardown(self):
#         print('----TEARDOWN----')
#
#     @allure.feature('验证user')
#     def test_01(self, before, user, pwd):
#         print('---执行test_01----')
#         assert before == '测试之前'
#         assert user == '18221124104'
#
#     @allure.feature("验证pwd")
#     @pytest.mark.skipif(1 == 2, reason='满足1=1就跳过该用例')
#     def test_02(self, before, user, pwd):
#         print('---执行test_02----')
#         assert before == '测试之前'
#         assert pwd == 111111
#
#
# if __name__ == '__main__':
#     # 执行pytest单元测试，生成 Allure 报告需要的数据存在 /temp 目录
#     pytest.main(["-s", "-q", '--alluredir', './report'])
#     # 将测试报告转为html格式
