#！/usr/bin/env python
# encoding:utf-8
from common.log import Log
from common.readsql import ReadSql


class Assertion():
    log=Log()
    sql_values_list=[]
    response_values=[]

    def __init__(self):
        self.test=ReadSql.read_sql()

    def get_sql_data(self,sql_type,sql):
        """
        查询sql数据组合list
        :param sql_type:
        :param sql:
        :return:
        """
        try:
            sql_values=self.test(sql_type, sql)
            for i in sql_values:
                for j in i:
                    self.sql_values_list.append(j)
        except Exception as  e:
            self.log.error('查询sql数据组合list报错{}'.format(e))




