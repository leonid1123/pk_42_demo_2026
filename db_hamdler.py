import pymysql.cursors


class DB_hamdler():
    def __init__(self):
        self.conn = pymysql.connect(host='localhost',
                                    user='exam_student',
                                    password='1234',
                                    database='demo_pk42')
        self.cur = self.conn.cursor()
