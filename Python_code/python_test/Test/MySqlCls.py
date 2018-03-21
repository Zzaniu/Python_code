# coding=utf-8


from MySQLdb import connect


class MySqlCls(object):
    def __init__(self, host, port, user, password, database):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None

    def open(self):
        self.conn = connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.database, charset='utf8')
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    def cute(self, sql, params=()):
        try:
            self.open()
            self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception, e:
            print e.message

    def query(self, sql, params=()):
        try:
            self.open()
            self.cursor.execute(sql, params)
            self.conn.commit()
            result = self.cursor.fetchall()
            self.close()
            return result
        except Exception, e:
            print e.message


