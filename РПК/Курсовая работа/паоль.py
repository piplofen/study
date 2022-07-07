from tkinter import*
from tkinter import ttk


def root_change_password():
    global root
    root = Tk()
    root.geometry('310x220+50+50')
    root.resizable(FALSE, FALSE)
    root.title("Cмена пароля")

    style = ttk.Style()
    style.configure('TButton', font = "Times, 12")
    style.configure('TLabel', font = "Times, 10")
    style.configure('TEntry', font = "Times, 10")
    style.map('TButton', background = [("active", "pink")])

    main_label = ttk.Label(text = "Необходимо поменять пароль", font = "Arial 14")
    main_label.place(x = 155, y = 30, anchor = CENTER)

    password_label = ttk.Label(text = "Введите новый пароль:", justify = LEFT)
    password_entry = ttk.Entry(width = 12, show = "•")
    password_label_help = ttk.Label(text = "Минимум 6 символов")
    password_label_help.place(x = 220, y = 105  , anchor  =CENTER)
    password_label.place(x = 80, y = 80, anchor = CENTER)
    password_entry.place(x = 225, y = 80, anchor = CENTER)

    password_label1 = ttk.Label(text = "Повторите ещё раз:", justify = LEFT)
    password_entry1 = ttk.Entry(width = 12, show = "•")
    password_label1.place(x = 80, y = 135, anchor = CENTER)
    password_entry1.place(x = 225, y = 135, anchor = CENTER)
    def change_password():
        global password
        if (password_entry.get() == password_entry1.get()):
            if (len(password_entry.get()) >= 6 and password_entry.get() != password):
                password = password_entry.get()
                password_day = datetime.date.today()
                f = open('secret.txt', 'r')
                lines = f.readlines()
                lines[0] = password + '\n'
                lines[1] = str(password_day) + '\n'
                f.close()
                save_changes = open('secret.txt', 'w')
                save_changes.writelines(lines)
                save_changes.close()
                main()

            elif(len(password_entry.get()) < 6):
                mb.showerror("Ошибка!", "Пароль должен состоять минимум из 6 символов")

            elif(password_entry.get() == password):
                mb.showerror("Ошибка!", "Новый пароль должен отличаться от предыдущего")
        else:
            mb.showerror("Ошибка!", "Пароли не совпадают")

    button = ttk.Button(text = "Готово")
    button.place(x = 155, y = 185, anchor = CENTER)
    root.mainloop()



root_change_password()