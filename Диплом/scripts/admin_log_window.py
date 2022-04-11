import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import admin_log_design
from cryptography.fernet import Fernet

class admin_log_window(QtWidgets.QMainWindow, admin_log_design.Ui_Admin_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.edit_login.setFocus()
        self.key = Fernet.generate_key()
        self.f = Fernet(self.key)
        self.token1 = self.f.encrypt(b"piplofen")
        self.token2 = self.f.encrypt(b"maksimiboss2001")
        self.bttn_log.clicked.connect(self.authorization)

    def authorization(self):
        print("Авторизация", "Окно администратора")
        login = bytes(self.edit_login.text(), encoding = "utf-8")
        password = bytes(self.edit_password.text(), encoding = "utf-8")
        if (login == self.f.decrypt(self.token1)) and (password == self.f.decrypt(self.token2)):
            print("Полное совпадение", "Окно администратора")
        else:
            print("Ошибка", "Окно администратора")
            msgAccept = QMessageBox(self)
            msgAccept.setWindowTitle("Ошибка!")
            msgAccept.setText("Введите данные заново.")
            msgAccept.setIcon(QMessageBox.Warning)
            x = msgAccept.exec_()
   
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = admin_log_window()
    window.show()
    app.exec_()

#if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    #main()  # то запускаем функцию main()