# ！/usr/bin/env python
# encoding:utf-8
import os

import xlrd
import yaml

from common.log import Log

# from common.runmethod import Runmethod
# from common.runmethod import Runmethod

"读取配置文件"


class ReadFile():

    def __init__(self):
        self.yaml_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/config.yaml")
        self.mysql_yaml_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/mysql.yaml")
        self.excel_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "config/testcase.xls")
        self.log = Log()

    def read_yaml(self, path_type):
        try:
            if path_type == "yaml_path":
                file_path = self.yaml_path
            elif path_type == "mysql_path":
                file_path = self.mysql_yaml_path
            else:
                print("文件类型输入错误")
            """
            open与with open区别在于 open不关闭 需要手动f.close()
            with open会自动关闭
            """
            # f = open("file","r",encoding="utf-8")
            # print(yaml.load(f.read()))
            with open(file_path, "r", encoding="utf-8") as f:
                return yaml.load(f.read(), Loader=yaml.FullLoader)
        except Exception as e:
            print("读取文件报错{}".format(e))
            self.log.error("读取文件报错{}".format(e))

    def read_excel(self, sheet_name, function, casename=None, excel_path=None):
        if excel_path:
            excel_path = excel_path
        else:
            excel_path = self.excel_path
        """
        读取excel
        :param sheet_name:
        :param function:
        :param casename:
        :return:
        """
        try:
            book = xlrd.open_workbook(excel_path)
            data = book.sheet_by_name(sheet_name)
            param = []
            # print("列数:%s" % data.nrows)
            for i in range(0, data.nrows):
                get_func_name = data.row_values(i)[0]
                get_run = data.row_values(i)[3]
                get_cas_name = data.row_values(i)[1]
                if casename is None:
                    if get_func_name == function and get_run == 1:
                        param.append(data.row_values(i))
                else:
                    if get_func_name == function and get_cas_name == casename and get_run == 1:
                        param.append(data.row_values(i))
            return param
        except Exception as e:
            print("读取excel报错{}".format(e))


if __name__ == "__main__":
    print(ReadFile().read_yaml("yaml_path")['translate_url'])
    # print(ReadFile().read_yaml("mysql_path"""))
    test = ReadFile()
    print(test.read_excel("翻译", "翻译文本")[2])
    # print(ReadFile().read_yaml("yaml_path")['translate_url']+test.read_excel("翻译", "翻译文本", "输入汉字")[0][4])
    data = test.read_excel("翻译", "翻译文本", "输入汉字")
    print(data, type(data))
    # method = test.read_excel("翻译", "翻译文本", "输入汉字")[0][2]
    # expect = eval(test.read_excel("翻译", "翻译文本", "输入汉字")[0][11])['message']
    # print(expect, type(expect))
    # url = ReadFile().read_yaml("yaml_path")['translate_url'] + test.read_excel("翻译", "翻译文本", "输入汉字")[0][4]
    # print(Runmethod().run_main(method,url,data))
