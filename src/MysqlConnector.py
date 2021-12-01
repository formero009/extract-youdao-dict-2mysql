#coding:utf-8

import MySQLdb
import traceback
from Conf import host,username,password,database  #数据库配置


class MySQLConnector():
    def __init__(self, host = host, username = username, password = password, database = database):
        self.host = host
        self.username = username
        self.password = password
        self.database = database

    #连接数据库
    def connect_database(self):
        db = MySQLdb.connect(self.host,self.username,self.password,self.database,charset='utf8')
        return db

    #SQL 查询语句
    def select_data(self,selectsqlstr):
        db = self.connect_database()
        cursor = db.cursor()
        try:
            cursor.execute(selectsqlstr)
            results = cursor.fetchall()
            return results
        except:
            print("Error: unable to fetch data")
        db.close()


    #SQL 更新语句
    def update_data(self,updatesqlstr):
        db = self.connect_database()
        cursor = db.cursor()
        try:
            #updatesqlstr = "update"
            cursor.execute(updatesqlstr)
            db.commit()
        except:
            db.rollback()
        db.close()

    #SQL 删除语句
    def delete_data(self,deletesqlstr):
        db = self.connect_database()
        cursor = db.cursor()
        try:
            cursor.execute(deletesqlstr)
            db.commit()
        except:
            db.rollback()
        db.close()

    def insert_cluster_result(self,insertsql):
        db = self.connect_database()
        cursor = db.cursor()
        try:
            cursor.execute(insertsql)
            db.commit()
        except:
            traceback.print_exc()
            db.rollback()
        db.close()

    def get_substr_data(self,querysql):
        db = self.connect_database()
        cursor = db.cursor()
        try:
            cursor.execute(querysql)
            results = cursor.fetchall()
            return results
        except:
            print("Error: unable to fetch data")
        db.close()

    def insert_data(self,sql):
        db = self.connect_database()
        cursor = db.cursor()
        try:
            cursor.execute(sql)
            db.commit()
            return 'success'
        except Exception as err:
            db.rollback()
            return 'Error: '+str(err)
        finally:
            db.close()


if __name__ == '__main__':
    # sql = "select * from xdr_http where task_id = 25"
    # conn = MySQLConnector()
    # results = conn.select_data(sql)
    # print("==================================")
    # print(len(results))
    # print("==================================")
    
    sql = "insert into daily_book values(1,'CET4','https://www.baidu.com');"
    conn = MySQLConnector()
    result = conn.insert_data(sql)
    print(result)