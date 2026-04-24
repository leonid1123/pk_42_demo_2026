
from PyQt6.QtWidgets import (QApplication, QWidget,
                             QGridLayout, QListWidget,
                             QPushButton, QComboBox,
                             QLineEdit, QFormLayout)
from db_hamdler import DB_hamdler


class Okno3(QWidget):
    def __init__(self, edit_items):
        super().__init__()
        self.edit_items=edit_items
        self.my_db = DB_hamdler()
        layout = QFormLayout()
        self.setLayout(layout)
        self.art = QLineEdit()
        if edit_items is not None:
            self.art.setText(edit_items[0])
        self.name = QLineEdit()
        if edit_items is not None:
            self.name.setText(edit_items[1])
        self.ed_izm = QLineEdit()
        if edit_items is not None:
            self.ed_izm.setText(edit_items[2])
        self.cena = QLineEdit()
        if edit_items is not None:
            self.cena.setText(edit_items[3])
        self.post = QLineEdit()
        self.proizv = QLineEdit()
        self.category = QLineEdit()
        self.skidka = QLineEdit()
        self.kol_vo = QLineEdit()
        self.opisanie = QLineEdit()
        layout.addRow('Артикул',self.art)
        layout.addRow('название',self.name)
        layout.addRow('Единица измерения', self.ed_izm)
        layout.addRow('Цена', self.cena)
        layout.addRow("Поставщик",self.post)
        layout.addRow("Производитель", self.proizv)
        layout.addRow("Категория",self.category)
        layout.addRow("Скидка", self.skidka)
        layout.addRow("Количество на складе", self.kol_vo)
        layout.addRow("Описание",self.opisanie)
        add_btn = QPushButton('Добавить')
        if edit_items is None:
            add_btn.clicked.connect(self.add_new_item)
        else:
            add_btn.clicked.connect(self.update_item)
            add_btn.setText('Изменить товар')
        layout.addRow(add_btn)

    def add_new_item(self):
        art = self.art.text()
        nme = self.name.text()
        ed = self.ed_izm.text()
        cena = self.cena.text()
        postav = self.post.text()
        pr = self.proizv.text()
        kat = self.category.text()
        sk = self.skidka.text()
        kol = self.kol_vo.text()
        op = self.opisanie.text()
        sql = '''INSERT INTO `tovar`(`Артикул`, 
        `Наименование товара`, `Единица измерения`, 
        `Цена`, `Поставщик`, `Производитель`, 
        `Категория товара`, `Действующая скидка`, 
        `Кол-во на складе`, `Описание товара`) 
        VALUES
        (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        new_vals=(art,nme,ed,cena,postav,pr,kat,sk,kol,op)
        self.my_db.cur.execute(sql,new_vals)
        self.my_db.conn.commit()
        self.close()

    def update_item(self):
        sql = '''UPDATE `tovar` SET 
        `Артикул`=%s,
        `Наименование товара`=%s,
        `Единица измерения`=%s,
        `Цена`=%s,
        `Поставщик`=%s,
        `Производитель`=%s,
        `Категория товара`=%s,
        `Действующая скидка`=%s,
        `Кол-во на складе`=%s,
        `Описание товара`=%s
        WHERE 
        `Артикул`=%s,
        `Наименование товара`=%s
        '''
        art = self.art.text()
        nme = self.name.text()
        ed = self.ed_izm.text()
        cena = self.cena.text()
        postav = self.post.text()
        pr = self.proizv.text()
        kat = self.category.text()
        sk = self.skidka.text()
        kol = self.kol_vo.text()
        op = self.opisanie.text()
        new_info=(art,nme,ed,cena,postav,pr,
                  kat,sk,kol,op,
                  self.edit_items[0],
                  self.edit_items[1])
        self.my_db.cur.execute(sql,new_info)
        self.my_db.conn.commit()
        self.close()
