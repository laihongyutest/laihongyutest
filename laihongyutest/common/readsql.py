# ！/usr/bin/env python
# encoding:utf-8
import pymysql

from common.readfile import ReadFile


class ReadSql():

    def get_sql(self):
        return ReadFile().read_yaml("yaml_path")['mysql']

    def connect_db(self):
        host = self.get_sql()["host"]
        user = self.get_sql()["user"]
        pwd = self.get_sql()["pwd"]
        databasename = self.get_sql()["test_db"]
        self.con = pymysql.connect(host=host, user=user, password=pwd, database=databasename, port=3306, charset="utf8")
        return self.con

    def get_cursor(self):
        return self.connect_db().cursor()

    def read_sql(self, sql_type, sql):
        #        sql2 = ReadFile().read_yaml("mysql_path")['查id']
        cursor = self.get_cursor()
        if sql_type == 'select_one':
            cursor.execute(sql)
            result = cursor.fetchone()

        elif sql_type == 'select_list':
            cursor.execute(sql)
            result = cursor.fetchal
        elif sql_type == 'update' or sql_type == 'insert' or sql_type == 'delete':
            result = cursor.execute(sql)
        self.con.commit()
        cursor.close()
        self.con.close()
        return result


if __name__ == "__main__":
    test = ReadSql().get_sql()
    print(test)
    test2 = ReadSql().connect_db()
    print(test2)
    sql = "select * from test_table"
    test3 = ReadSql().read_sql('select_one', sql)
    print(test3)
