import allure
import pytest

# from common.assertion import Assertion
from common.readfile import ReadFile
from common.runmethod import Runmethod

data = ReadFile().read_excel("翻译", "翻译文本")
data2 = ReadFile().read_excel("翻译", "用户提交翻译结果")
data3 = ReadFile().read_excel("翻译", "获取审核列表")
print(data)


@pytest.mark.parametrize('function,casename,type,run,url,headers,param,sql1,sql2,sql3,asserttype,expect1', data3)
class Test(object):
    '''翻译'''
    request = Runmethod()
    # assertion = Assertion()
    # exec_sql = ExecSql().exec_sql
    yaml_data = ReadFile().read_yaml('yaml_path')['translate_url']

    # sql_yaml_data = ReadFile().read_yaml('sql_yaml_path')['lxk']
    # prefix_sql_data = MakeSqlData('lxk').make_sql_data
    def setup_class(self):
        '''
        数据初始化
        :return:
        '''
        pass

    def teardown_class(self):
        '''
        数据清理
        :return:
        '''
        pass

    @allure.feature('翻译小程序')
    @allure.story('获取审核列表')
    # @allure.link(self.yaml_data + url)
    def test_translate(self, function, casename, type, run, url, headers, param, sql1, sql2, sql3, asserttype, expect1):
        if headers != '' and param != '':
            response_data = self.request.run_main(type, self.yaml_data + url, eval(param), headers)
        elif headers == '' and param != '':
            response_data = self.request.run_main(type, self.yaml_data + url, eval(param))
        elif headers != '' and param == '':
            response_data = self.request.run_main(type, self.yaml_data + url, header=headers)
        else:
            response_data = self.request.run_main(type, self.yaml_data + url)
        # self.assertion.get_response_data(response_data, eval(expect1))
        # self.assertion.asser(function, casename, expect1, response_data, asserttype)
        assert eval(expect1)['code'] == response_data['code']
        assert eval(expect1)['message'] == response_data['message']

#
# # if __name__ == "__main__":
# #     pytest.main(["-s", "test_translate.py"])
