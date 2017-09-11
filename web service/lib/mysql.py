#encoding=utf-8
import os, sys, string, random
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')
# 连接数据库　
class Mysql:
    conn = ''
    cursor = ''

    def __init__(self, host='127.0.0.1', usr='root', password='', charset='utf8',db='test'):
        try:
            self.conn = MySQLdb.connect(host=host,user=usr,passwd=password,charset=charset, db=db)
        except Exception, e:
            print e
            sys.exit()

        self.cursor = self.conn.cursor()
        # self.query('SET NAME %s ' % charset)


    def query(self, sql):
        return self.cursor.execute(sql)
    def manyquery(self,sql,args):
        return self.cursor.executemany(sql,args)
    def insertid(self):
        return int(self.conn.insert_id())
    # insert_id()一定要在commit()之前，否则会返回0
    def show(self):
        return self.cursor.fetchall()
    def commit(self):
        return self.conn.commit()


    def __del__ (self):
        self.cursor.close()
        self.conn.close()



if __name__ == "__main__":
    m = Mysql('127.0.0.1','root','test','utf8','test')