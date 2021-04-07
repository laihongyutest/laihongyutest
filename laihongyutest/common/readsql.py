# ！/usr/bin/env python
# encoding:utf-8
import pymysql
from common.readfile import ReadFile


class ReadSql():

    def get_sql(self):
        return ReadFile().read_yaml("yaml_path")['mysql']['tranlate']

    def connect_db(self):
        host = self.get_sql()["host"]
        user = self.get_sql()["user"]
        pwd = self.get_sql()["pwd"]
        if not isinstance(pwd, str):
            password = str(pwd)
        else:
            password = pwd
        db_name = self.get_sql()["test_db"]
        self.con = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db_name,
            port=3306,
            charset="utf8")
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
            result = cursor.fetchall()
        elif sql_type == 'update' or sql_type == 'insert' or sql_type == 'delete':
            result = cursor.execute(sql)
        self.con.commit()
        cursor.close()
        self.con.close()
        return result


if __name__ == "__main__":
    print(ReadSql().get_sql())
    print(ReadSql().get_cursor())
    a = '这个是测试'
    sql = "select * from `verify_record_2021-01` where src_text='{}'".format(a)
    sql2 = "insert into `verify_record_2021-01`(id,src_text,tgt_text,state,trans_type,trans_from,created_at,updated_at)   values (192,'这个是没有的翻译1', 'بۇ تەرجىمە يوق', '1','1','1','2021-01-10 14:58:19','2021-01-10 14:58:19')"
    sql3 = "delete  from `verify_record_2021-01` where src_text='{}'".format(a)
    print(sql2)
    删除id = 192
    # test_delect = ReadSql().read_sql('delete',sql3)
    # 插入
    # test_insert =ReadSql().read_sql('insert',sql2)
    # 获取
    test = ReadSql().read_sql('select_list', sql)[0]
    print(test, type(test))
    # test_delete = ReadSql().read_sql('delete', sql3)
    # print(test_delete)
