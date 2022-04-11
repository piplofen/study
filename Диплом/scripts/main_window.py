import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer, pyqtSignal
from PyQt5.QtCore import Qt, QEvent
import datetime
import main_window_design
import database

class MainWindow(QtWidgets.QMainWindow, main_window_design.Ui_Main_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.TableResidents.setMouseTracking(True)
        self.TableStorage.setMouseTracking(True)
        self.insert_data_for_residents()
        self.comboDatabase.currentTextChanged.connect(self.print)
        self.bttn_del.clicked.connect(self.delete)
        self.bttn_add.clicked.connect(self.add)
        self.bttn_refresh.clicked.connect(self.refresh)
        self.bttn_exit.clicked.connect(self.close)
        self.TableResidents.mousePressEvent = self.mousePressEvent

    def mousePressEvent(self, event):
        if event.button() == 1:
            try:
                item = self.TableResidents.itemAt(event.pos()).text()
                print(item)

            except AttributeError:
                print("Ошибка")
        else:
            pass
        

    def refresh(self):
        if self.comboDatabase.currentText() == "Жильцы":
            self.insert_data_for_residents()

        elif self.comboDatabase.currentText() == "Склад":
            self.insert_data_for_storage()

    def add(self):
        item = 0
        if self.comboDatabase.currentText() == "Жильцы":
            item = self.TableResidents.selectedIndexes()

        elif self.comboDatabase.currentText() == "Склад":
            item = self.TableStorage.item.text()

        print(item)

    #id не удаляется
    def delete(self):
        item = 0
        if self.comboDatabase.currentText() == "Жильцы":
            item = self.TableResidents.currentRow() + 1
            database.cur.execute("DELETE FROM residents WHERE residentsid = ?", (item,))
            database.conn.commit()
            print(f"{datetime.datetime.now()} Удаление {item} элемента в таблице residents прошло успешно")
        elif self.comboDatabase.currentText() == "Склад":
            item = self.TableStorage.currentRow() + 1
            database.cur.execute("DELETE FROM storage WHERE storageid = ?", (item,))
            database.conn.commit()
            print(f"{datetime.datetime.now()} Удаление {item} элемента в таблице storage прошло успешно")


    def print(self, value):
        if value == "Жильцы":
            self.insert_data_for_residents()
            print(f"{datetime.datetime.now()} переход в таблицу residents")
        elif value == "Склад":
            self.insert_data_for_storage()
            print(f"{datetime.datetime.now()} переход в таблицу storage")

    def insert_data_for_storage(self):
        self.TableResidents.hide()
        self.TableStorage.show()
        database.cur.execute("SELECT * FROM storage;")
        self.result_storage = database.cur.fetchall()
        self.TableStorage.setColumnWidth(0, 1)
        self.TableStorage.setColumnWidth(1, 265)
        self.TableStorage.setColumnWidth(2, 115)
        self.TableStorage.setColumnWidth(3, 115)
        self.TableStorage.verticalHeader().setVisible(False)
        try:
            self.TableStorage.setRowCount(len(self.result_storage))

            for i in range(len(self.result_storage)):
               self.TableStorage.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.result_storage[i][0])))

            for i in range(len(self.result_storage)):
                self.TableStorage.setItem(i, 1, QtWidgets.QTableWidgetItem(self.result_storage[i][1]))

            for i in range(len(self.result_storage)):
                self.TableStorage.setItem(i, 2, QtWidgets.QTableWidgetItem(str(self.result_storage[i][2])))

            for i in range(len(self.result_storage)):
                self.TableStorage.setItem(i, 3, QtWidgets.QTableWidgetItem(str(self.result_storage[i][3])))

        except AttributeError:
            print(f"{datetime.datetime.now()} Ошибка загрузки таблицы \"storage\"")

    def insert_data_for_residents(self):
        self.TableStorage.hide()
        self.TableResidents.show()
        database.cur.execute("SELECT * FROM residents;")
        self.result_residents = database.cur.fetchall()
        self.TableResidents.setColumnWidth(0, 1)
        self.TableResidents.setColumnWidth(1, 285)
        self.TableResidents.setColumnWidth(2, 1)
        self.TableResidents.setColumnWidth(3, 100)
        self.TableResidents.setColumnWidth(4, 375)
        self.TableResidents.setColumnWidth(5, 120)
        self.TableResidents.setColumnWidth(6, 250)
        self.TableResidents.verticalHeader().setVisible(False)
        try:
            #self.TableResidents.clearContents()
            self.TableResidents.setRowCount(len(self.result_residents))

            for i in range(len(self.result_residents)):
                self.TableResidents.setItem(i, 0, QtWidgets.QTableWidgetItem(str(self.result_residents[i][0])))

            for i in range(len(self.result_residents)):
                self.TableResidents.setItem(i, 1, QtWidgets.QTableWidgetItem(self.result_residents[i][1]))

            for i in range(len(self.result_residents)):
                self.TableResidents.setItem(i, 2, QtWidgets.QTableWidgetItem(self.result_residents[i][2]))

            for i in range(len(self.result_residents)):
                self.TableResidents.setItem(i, 3, QtWidgets.QTableWidgetItem(self.result_residents[i][3]))

            for i in range(len(self.result_residents)):
                self.TableResidents.setItem(i, 4, QtWidgets.QTableWidgetItem(self.result_residents[i][4]))

            for i in range(len(self.result_residents)):
                self.TableResidents.setItem(i, 5, QtWidgets.QTableWidgetItem(self.result_residents[i][5]))

            for i in range(len(self.result_residents)):
                self.TableResidents.setItem(i, 6, QtWidgets.QTableWidgetItem(self.result_residents[i][6]))

            #self.TableResidents.removeRow(2)

        except AttributeError:
            print(f"{datetime.datetime.now()} Ошибка загрузки таблицы \"residents\"")
   
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()