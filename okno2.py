import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QListWidget, QPushButton, QComboBox, QLineEdit
from db_hamdler import DB_hamdler


class Okno2(QWidget):
    def __init__(self):
        super().__init__()
        self.role = ''
        self.fio = ''
        self.my_db = DB_hamdler()
        self.setWindowTitle(self.fio)
        layout = QGridLayout()
        self.setLayout(layout)
        self.all_goods = QListWidget()
        sort_up = QPushButton("По возрастанию")
        sort_up.clicked.connect(self.sort_up_slot)
        sort_down = QPushButton("По убыванию")
        sort_down.clicked.connect(self.sort_down_slot)

        self.filter = QComboBox()
        self.filter.currentIndexChanged.connect(self.filter_slot)
        self.my_db.cur.execute('SELECT DISTINCT `Производитель` FROM tovar')
        ans = self.my_db.cur.fetchall()
        for item in ans:
            self.filter.addItem(item[0])

        self.search = QLineEdit()
        self.search.textChanged.connect(self.search_slot)
        layout.addWidget(self.all_goods,0,0,1,2)
        layout.addWidget(sort_up,1,0)
        layout.addWidget(sort_down,1,1)
        layout.addWidget(self.filter,2,0,1,2)
        layout.addWidget(self.search,3,0,1,2)
        self.my_db.cur.execute('SELECT * FROM tovar')
        ans = self.my_db.cur.fetchall()
        for item in ans:
            self.all_goods.addItem(f'{item[1]} {item[2]} {item[3]} {item[4]}')

    def sort_up_slot(self):
        if self.role in ['Менеджер', 'Администратор']:
            sql = '''SELECT * FROM tovar 
            ORDER BY `Кол-во на складе` ASC'''
            self.my_db.cur.execute(sql)
            ans = self.my_db.cur.fetchall()
            self.all_goods.clear()
            for item in ans:
                self.all_goods.addItem(f'{item[1]} {item[2]} {item[3]} {item[4]}')


    def sort_down_slot(self):
        if self.role in ['Менеджер', 'Администратор']:
            sql = '''SELECT * FROM tovar 
                    ORDER BY `Кол-во на складе` DESC'''
            self.my_db.cur.execute(sql)
            ans = self.my_db.cur.fetchall()
            self.all_goods.clear()
            for item in ans:
                self.all_goods.addItem(f'{item[1]} {item[2]} {item[3]} {item[4]}')

    def filter_slot(self):
        if self.role in ['Менеджер', 'Администратор']:
            user_input = self.filter.currentText()
            sql='SELECT * FROM tovar WHERE `Производитель`=%s'
            self.my_db.cur.execute(sql,(user_input,))
            ans = self.my_db.cur.fetchall()
            self.all_goods.clear()
            for item in ans:
                self.all_goods.addItem(f'{item[1]} {item[2]} {item[3]} {item[4]}')

    def search_slot(self):
        if self.role in ['Менеджер', 'Администратор']:
            sql = '''SELECT * FROM tovar 
            WHERE `Наименование товара`
            LIKE %s'''
            user_input = '%' + self.search.text() + '%'
            self.my_db.cur.execute(sql,(user_input,))
            ans = self.my_db.cur.fetchall()
            self.all_goods.clear()
            for item in ans:
                self.all_goods.addItem(f'{item[1]} {item[2]} {item[3]} {item[4]}')



