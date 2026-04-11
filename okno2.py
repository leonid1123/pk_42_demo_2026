import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QListWidget
from db_hamdler import DB_hamdler


class Okno2(QWidget):
    def __init__(self):
        super().__init__()
        self.my_db = DB_hamdler()
        self.setWindowTitle('Hello World')
        layout = QGridLayout()
        self.setLayout(layout)
        self.all_goods = QListWidget()
        layout.addWidget(self.all_goods)
        self.my_db.cur.execute('SELECT * FROM tovari')
        ans = self.my_db.cur.fetchall()
        for item in ans:
            self.all_goods.addItem(f'{item[1]} {item[2]} {item[3]} {item[4]}')

