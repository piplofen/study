import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from cryptography.fernet import Fernet
import user_log_design
import main_window

class user_log_window(QtWidgets.QMainWindow, user_log_design.Ui_User_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.edit_login.setFocus()
        self.key = Fernet.generate_key()
        self.f = Fernet(self.key)
        self.token1 = self.f.encrypt(b"123")
        self.token2 = self.f.encrypt(b"123")
        self.bttn_log.clicked.connect(self.authorization)
        self.main_window = main_window.MainWindow()

    def authorization(self):
        print("Авторизация", "Окно пользователя")
        login = bytes(self.edit_login.text(), encoding = "utf-8")
        password = bytes(self.edit_password.text(), encoding = "utf-8")
        if (login == self.f.decrypt(self.token1)) and (password == self.f.decrypt(self.token2)):
            print("Полное совпадение", "Окно пользователя")
        else:
            print("Ошибка", "Окно пользователя")
            msgAccept = QMessageBox(self)
            msgAccept.setWindowTitle("Ошибка!")
            msgAccept.setText("Введите данные заново.")
            msgAccept.setIcon(QMessageBox.Warning)
            x = msgAccept.exec_()
        try:
            self.close()
            self.main_window.show()
            self.main_window.line_choice.setText("Пользователь")
        except NameError:
            print("Ошибка!","Файла нет в директории")
   
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = user_log_window()
    window.show()
    app.exec_()

#if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    #main()  # то запускаем функцию main()