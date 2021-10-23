
import pymysql

class SqlHelper(object):

    def connect(self):
        self.conn = pymysql.connect(host='8.130.172.12', port=3307, user='root', password='Zjy559988!', db='eda-shopping', charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def get_list(self,sql,args):
        self.cursor.execute(sql, args)
        res = self.cursor.fetchall()
        return res

    def get_one(self,sql,args):
        self.cursor.execute(sql, args)
        res = self.cursor.fetchone()
        return res
    def modify(self,sql,args):
        self.cursor.execute(sql, args)
        self.conn.commit()

    def create(self,sql,args):
        self.cursor.execute(sql, args)
        self.conn.commit()
        return self.cursor.lastrowid # 添加并且拿返回值

    def multiple_modify(self,sql,args):
        self.cursor.executemany(sql,args)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    s = SqlHelper()
    s.connect()
    s = s.get_one("select * from users where u_tel = %s", ["15188397061",])
    print(s)
