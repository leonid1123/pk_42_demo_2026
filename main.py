import sys
from PyQt6.QtWidgets import (QApplication, QWidget,
                             QMainWindow, QVBoxLayout,
                             QLabel, QLineEdit, QPushButton)
from okno2 import Okno2
from db_hamdler import DB_hamdler


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.my_db = DB_hamdler()
        centeal_widget = QWidget()
        layout = QVBoxLayout()
        self.setCentralWidget(centeal_widget)
        centeal_widget.setLayout(layout)
        login_lbl = QLabel("Login")
        pass_lbl = QLabel("Password")
        self.login_ent = QLineEdit()
        self.pass_ent = QLineEdit()
        login_btn = QPushButton("Enter")
        login_btn.clicked.connect(self.user_login)
        guest_btn = QPushButton("Guest")
        guest_btn.clicked.connect(self.guest_login)
        layout.addWidget(login_lbl)
        layout.addWidget(self.login_ent)
        layout.addWidget(pass_lbl)
        layout.addWidget(self.pass_ent)
        layout.addWidget(login_btn)
        layout.addWidget(guest_btn)
        self.show()

    def user_login(self):
        inp_login = self.login_ent.text()
        inp_pass = self.pass_ent.text()
        sql = '''SELECT `Роль сотрудника`, `ФИО` FROM `user_import` 
        WHERE `Пароль`=%s AND `Логин`=%s'''
        self.my_db.cur.execute(sql,(inp_pass,inp_login))
        ans = self.my_db.cur.fetchone()
        print(ans)
        if ans:
            self.okno2 = Okno2()
            self.okno2.role = ans[1]
            self.okno2.fio = ans[0]
            self.okno2.show()

    def guest_login(self):
        self.okno2 = Okno2()
        self.okno2.fio = 'ГОСТЬ'
        self.okno2.role = 'гость'
        self.okno2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
