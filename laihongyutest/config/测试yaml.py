# ！/usr/bin/env python
# encoding:utf-8

import yaml

# f= open(r'C:/Users/86182/PycharmProjects/laihongyutest/config/name.yaml','r',encoding='utf-8')


with open('D://laihongyutest//config//name.yaml', 'r', encoding='utf-8') as f:
    a = yaml.load(f.read(), Loader=yaml.FullLoader)
    print(a)
    print("我的名字是:", a["profession"]["name"])
    print("我的名字是：%s" % a["name"])
    print("我会的技能是{}、{}和{}".format(a["skill"][0]["namel"], a["skill"][1]["name2"], a["skill"][2]["name3"]))
