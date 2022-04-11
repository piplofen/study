import sys
from PyQt5 import QtWidgets
import choice_design
import admin_log_window
import user_log_window

class choice_window(QtWidgets.QMainWindow, choice_design.Ui_Choice_Window):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.bttn_admin.clicked.connect(self.admin)
        self.bttn_user.clicked.connect(self.user)
        self.adminWindow = admin_log_window.admin_log_window()
        self.userWindow = user_log_window.user_log_window()

    def admin(self):
        print("Вызов окна администратор")
        try:
            self.close()
            self.adminWindow.show() 
        except NameError:
            print("Ошибка!","Файла нет в директории")

    def user(self):
        print("Вызов окна пользователь")
        try:
            self.close()
            self.userWindow.show()
        except NameError:
            print("Ошибка!","Файла нет в директории")
   
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = choice_window()
    window.show()
    app.exec_()

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()