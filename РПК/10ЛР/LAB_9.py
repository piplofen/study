"""
Ввод разовых паролей (разных 12 штук) длиной 5-7 символов. Программа допускает трехкратный
неправильный набор, после чего прекращает работу на текущий день. После ввода последнего
файл с паролями уничтожается. Пароли закодированы, их нельзя посмтреть. При запуске последним
паролем в окне программы появляется кнопка перехода к созданию нового набора пароле.
"""

from cryptography.fernet import Fernet
from tkinter import *
from tkinter import messagebox
from datetime import date
import os, sys

root = Tk()

access = False
password_list_encrypt = []
attempts = 3

label = Label(root, text='Введите пароль')

entry_text = StringVar()

chiper_key = b'MYQ2VMEd_YC6OZoqeeuL0_JeAIwIvOmEM0k9lIyj4nc='
chiper = Fernet(chiper_key)


def check_file():
    '''
    Активируется, при запуске программы. Проверяет 2 файла на наличие в одной директории. Проверяет в дат-файле
    значение на сегодняшний день. Если сегодняшний день больше даты в файле, то записывает значение True на текущай
    день. В случае обратного значения, запрещает доступ к программе, выводя сообщение и завершая её! В случае отсутствия
    файла дат, создает новый и присвает доступ на сегодняшний день. Если отсутствует файл паролей, то создает новый
    и открывает окно добавления паролей.
    '''
    global access, password_list_encrypt, password_list_decrypt, chiper
    if os.path.isfile('date.txt'):
        date_file = open('date.txt', 'r')
        list_data = [line.strip() for line in date_file]
        date_today_file = list_data[0]
        accept_today = list_data[1]

        if accept_today == 'True' and (int(date_today_file[-2:]) == int(str(date.today())[-2:])):
            access = True

        elif (int(date_today_file[-2:]) < int(str(date.today())[-2:])):
            date_file = open('date.txt', 'w')
            date_file.write(str(date.today()) + '\n' + 'True')
            date_file.close()
            access = True

        else:
            print('Доступ на сегодня запрещен!')
            sys.exit()
    else:
        date_file = open('date.txt', 'w')
        date_file.write(str(date.today()) + '\n' + 'True')
        date_file.close()
        access = True

    if access:
        if os.path.isfile('password.txt'):
            password_file = open('password.txt', 'r')
            password_list_encrypt = [line.strip() for line in password_file]
            if password_list_encrypt:
                password_list_decrypt = []
                for line in password_list_encrypt:
                    encrypt_str = chiper.decrypt(bytes(line[1:], encoding = 'utf-8'))
                    password_list_decrypt.append(encrypt_str.decode('utf-8'))
                print(f'Закодированный файл:\n{password_list_encrypt}')
                print(f'Декодированый файл:\n{password_list_decrypt}')
                print('##################################################')
            else:
                add_password_window()
        else:

            add_password_window()


def check_password():
    '''
    Основная функция программы. Проверяет пароли из поля энтри на главном окне, затем сверяет их с паролями в файле
    , также сверяет на ввод последнего пароля. Отсчитывет попытки, в случае окончания всех попыток, удаляет файл
    паролей и записывает анти-доступ к программе на сегодняшний день в файл дат
    '''
    global attempts, password_list_decrypt, chiper_key

    password = entry_text.get()
    if password in password_list_decrypt:
        if password == password_list_decrypt[-1]:
            update_password = messagebox.askyesno(title='Вопрос', message='Открыть окно изменения паролей?')
            if update_password:
                add_password_window()
        else:
            messagebox.showinfo('Успех', f'Пароль {password} есть в файле!')
    else:
        attempts -= 1
        messagebox.showinfo('Ошибка', f'Пароль {password} отсутствует в файле,\n'
                             f'Осталось попыток - {attempts} !')
        if attempts == 0:
            date_file = open('date.txt', 'w')
            date_file.write(str(date.today()) + '\n' + 'False')
            date_file.close()
            os.remove('password.txt')
            sys.exit()


def add_password_window():
    '''
    Функция открытия окна добавления паролей. Открывает фал на запись и скрывает главное окно.

    '''
    global password_add_window, count, password_file, entry_text_2, button_add_password ,root
    root.withdraw()
    password_add_window = Toplevel()
    password_add_window.title('Окно добавления паролей')
    password_add_window.geometry('300x100')
    Label(password_add_window, text='Так как файл с паролями не найден,\n либо пуст, необходимо добавить новые!').pack()
    entry_text_2 = StringVar()
    password_file = open('password.txt', 'w')
    entry_password_get_2 = Entry(password_add_window, textvariable=entry_text_2).pack()
    button_add_password = Button(password_add_window, text='Добавить пароль', command=add_password).pack()
    count = 1


def add_password():
    '''
    Функция для добавления нового пароля в файл. Срабатывает при нажатии на кнопку. Принимает текст из поля Entry,
    затем переводит текст в байты и шифрует его. Если введено 12 паролей, ввод прекращается и программа закрываается,
    выводя сообщение в консоль
    '''
    global count, password_file, entry_text_2, button_add_password, password_add_window, chiper

    if count < 13:
        password = entry_text_2.get()
        text = bytes(password, encoding = 'utf-8')
        encrypt_pass = chiper.encrypt(text)
        print('---------------------------------------------------------')
        print(f'Пароль №{count}\nASCII символы: {password}\nЗашифрованые символы: {encrypt_pass}\nбыл добавлен в файл!')
        password_file.write(str(encrypt_pass) + '\n')
        count += 1
    else:
        password_file.close()
        password_add_window.destroy()
        print('##########################################################')
        print('Пароли добавлены!')

        print('Перезайдите в программу!')
        root.destroy()


def author():
    messagebox.showinfo('Автор', 'Подковыров Даниил')

check_file()


entry_password_get = Entry(root, textvariable=entry_text)
button_accept_password_get = Button(root,text='Вход', command=check_password)
but_aut = Button(root, text='Вывести имя автора')
root.geometry('200x100')

label.pack()
entry_password_get.pack()
button_accept_password_get.pack()

root.mainloop()