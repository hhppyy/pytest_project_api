#!/usr/bin/python
# -*- coding:utf-8 -*-

import pymysql

dbinfo = {
    "host": "123.56.231.107",
    "user": "root",
    "password": "123456",
    "port": 3309
}


class DbConnect():
    def __init__(self, db_cof=dbinfo, database=""):
        self.db_cof = db_cof
        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)
        # 使用cursor()方式获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql):
        # SQL 查询语句
        # sql = "SELECT * FROM EMPLOYEE \
        #       WHERE INCOME > %s" % (1000)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交修改
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()


def select_sql(sql):
    '''查询函数'''
    db = DbConnect(database="hrun")
    result = db.select(sql)
    db.close()
    return result


def execute_sql(sql):
    '''执行函数（新增、删除、修改）'''
    db = DbConnect(database="hrun")
    db.execute(sql)
    db.close()


if __name__ == '__main__':
    sql = "select * from UserInfo where username='test001';"
    a = select_sql(sql)
    print(a)
    print(a[0]["email"])
    # for i in a:
    #     print(i)
    # insert_sql = """
    # INSERT INTO `hrun`.`UserInfo`(`id`, `create_time`, `update_time`, `username`, `password`, `email`, `status`)
    # VALUES (2, '2020-03-17 19:36:00.148797', '2020-03-17 19:36:00.148850', 'test003', '123456', '123544@qq.com', 1);
    # """
    # execute_sql(insert_sql)
