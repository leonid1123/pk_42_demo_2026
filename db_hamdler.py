import pymysql.cursors


class DB_hamdler():
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    user='pupupu',
                                    password='pupupu',
                                    database='pupsiK')
        self.cur = self.conn.cursor()
