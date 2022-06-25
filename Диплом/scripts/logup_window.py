import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from cryptography.fernet import Fernet
import datetime
import logup_design_window
import main_window

class LogUpWindow(QtWidgets.QMainWindow, logup_design_window.Ui_LogUpWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bttnExit.clicked.connect(self.close)
        self.bttnLog.clicked.connect(self.authentication)
        self.msgBox = QMessageBox()
        self.main = main_window.MainWindow()
        #self.write_key()
        self.key = self.load_key()
        self.file = 'crypto.data'
        self.encrypt(self.file, self.key)

    def write_key(self):

        key = Fernet.generate_key()
        print(key)

        with open('crypto.key', 'wb') as key_file:
            key_file.write(key)

    def load_key(self):
        return open('crypto.key', 'rb').read()

    def encrypt(self, filename, key):
        f = Fernet(key)

        with open(filename, 'rb') as file:
            file_data = file.read()

        encrypted_data = f.encrypt(file_data)

        with open(filename, 'wb') as file:
            file.write(encrypted_data)

    def decrypt(self, filename, key):
        f = Fernet(key)

        with open(filename, 'rb') as file:
            encrypted_data = file.read()

        self.decrypted_data = f.decrypt(encrypted_data)

        with open(filename, 'wb') as file:
            file.write(self.decrypted_data)

    def authentication(self):
        self.decrypt(self.file, self.key)
        with open(self.file, 'r') as file:
             login = file.readlines(1)
             login = [line.rstrip() for line in login]
             password = file.readlines(2)

        if self.LineEditLogin.text() == 'piplofen' and self.LineEditPassword.text() == '123':
            print(f"{datetime.datetime.now()} Вход в систему. Перевод на главное окно")
            self.close()
            self.main.show()
        else:
            print(f"{datetime.datetime.now()} Неуспешный вход в систему")
            self.msgBox.setIcon(QMessageBox.Critical)
            self.msgBox.setText("Некорректные данные для входа. Попробуйте еще раз!")
            self.msgBox.setWindowTitle("Ошибка!")
            self.msgBox.setStandardButtons(QMessageBox.Ok)
            retval = self.msgBox.exec_()
   
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = LogUpWindow()
    window.show()
    app.exec_()

if __name__ == '__main__':#Если мы запускаем файл напрямую, а не импортируем
    main()#то запускаем функцию main()