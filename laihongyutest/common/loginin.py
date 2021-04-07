# ！/usr/bin/env python
# encoding:utf-8
"登录接口"
from common.log import Log
from common.readfile import ReadFile
from common.runmethod import Runmethod


class Login_in():
    log = Log()
    def __init__(self):
        self.yaml_data = ReadFile().read_yaml("yaml_path")
        self.header = self.yaml_data["header"]
        self.url = self.yaml_data["url"]
        self.link_url = self.yaml_data["c_login"]["url"]
        self.login_method = self.yaml_data["c_login"]["method"]
        self.login_param = self.yaml_data["c_login"]["param"]

    def c_longin_in(self, mobile):
        """
        登录
        :param mobile:
        :return:
        """
        try:
            self.login_param["mobile"] = mobile
            result = Runmethod.run_main(self.login_method, url, self.login_param, self.header)
            return result
        except Exception as e:
            print("登录报错{}".format(e))
            self.log.error("登录报错{}".format(e))

if __name__=="__main__":
    test_login=Login_in()
    print(test_login.c_longin_in("15288241132"))