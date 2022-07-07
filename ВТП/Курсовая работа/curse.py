from tkinter import*
from tkinter import messagebox
from winsound import*
from tkinter import ttk

root = Tk()
root.title("Калькулятор")
root.resizable(False,False)
root.iconbitmap('calc.ico')
mainmenu = Menu(root, font = ("Times",16,"bold"), bg = "grey")
filemenu = Menu(mainmenu, tearoff=0)
filemenu1 = Menu(mainmenu, tearoff=0)
root.config(menu = mainmenu)
v0 = IntVar()
v00 = IntVar()
n = 0
journal = []

def info():#функция позволяющая выводить информацию о студенте, при нажатии на опцию "Информация"
	root1= Tk()
	root1.resizable(False, False)
	root1.title("Информация о студенте")
	root1.iconbitmap("inf.ico")
	labelinfo = Label(root1, text = "Курсовую работу выполнил:\n студент группы 18ВТ2\n Подковыров Д.Р.")
	bttnexit =  ttk.Button(root1, text = "Выход", command = root1.destroy)
	labelinfo.pack()
	bttnexit.pack()

def printSkyblue():#функция меняющая цвет кнопок на бирюзовый
	r = 1
	c = 0
	for i in bttnList:
		rel = ""
		cmd = lambda x=i: calc(x)
		x = Button(root, text=i, command = cmd, width = 7, height = 3, activeforeground = "white", activebackground = "grey",fg = "black", font = ("Times",16,"bold"), bd = 4, bg = "skyblue")
		x.grid(row = r, column = c)
		c += 1
		if c>4:
			c=0
			r += 1

def printMediumslateblue():#функция меняющая цвет кнопок на бледно-фиолетовый
	r = 1
	c = 0
	for i in bttnList:
		rel = ""
		cmd = lambda x=i: calc(x)
		x = Button(root, text=i, command = cmd, width = 7, height = 3, activeforeground = "white", activebackground = "grey",fg = "black", font = ("Times",16,"bold"), bd = 4, bg = "mediumslateblue")
		x.grid(row = r, column = c)
		c += 1
		if c>4:
			c=0
			r += 1


def printWheat():#функция меняющая цвет кнопок на песочный
	r = 1
	c = 0
	for i in bttnList:
		rel = ""
		cmd = lambda x=i: calc(x)
		x = Button(root, text=i, command = cmd, width = 7, height = 3, activeforeground = "white", activebackground = "grey",fg = "black", font = ("Times",16,"bold"), bd = 4, bg = "wheat")
		x.grid(row = r, column = c)
		c += 1
		if c>4:
			c=0
			r += 1


def printViolet():#функция меняющая цвет кнопок на фиолетовый
	r = 1
	c = 0
	for i in bttnList:
		rel = ""
		cmd = lambda x=i: calc(x)
		x = Button(root, text=i, command = cmd, width = 7, height = 3, activeforeground = "white", activebackground = "grey",fg = "black", font = ("Times",16,"bold"), bd = 4, bg = "violet")
		x.grid(row = r, column = c)
		c += 1
		if c>4:
			c=0
			r += 1

def printStandart():#функция меняющая цвет кнопок к стандартному виду
	r = 1
	c = 0
	for i in bttnList:
		rel = ""
		cmd = lambda x=i: calc(x)
		x = Button(root, text=i, command = cmd, width = 7, height = 3, activeforeground = "white", activebackground = "grey",fg = "black", font = ("Times",16,"bold"), bd = 4)
		x.grid(row = r, column = c)
		c += 1
		if c>4:
			c=0
			r += 1

def printWindowPink():#функция меняющая цвет окна на розовый
	global calcEntry
	calcEntry = Entry(root, width = 33, borderwidth = 10, bg = "pink", fg = "black", font = ("Times",16,"bold"), selectbackground = "blue", selectforeground = "white")
	calcEntry.grid(row = 0, column =0,columnspan =5)

def printWindowYellow():#функция меняющая цвет окна на желтый
	global calcEntry
	calcEntry = Entry(root, width = 33, borderwidth = 10, bg = "yellow", fg = "blue", font = ("Times",16,"bold"), selectbackground = "blue", selectforeground = "white")
	calcEntry.grid(row = 0, column =0,columnspan =5)

def printWindowDarkred():#функция меняющая цвет окна на темно-красный
	global calcEntry
	calcEntry = Entry(root, width = 33, borderwidth = 10, bg = "darkred", fg = "white", font = ("Times",16,"bold"), selectbackground = "blue", selectforeground = "white")
	calcEntry.grid(row = 0, column =0,columnspan =5)

def printWindowOlive():#функция меняющая цвет окна на оливковый
	global calcEntry
	calcEntry = Entry(root, width = 33, borderwidth = 10, bg = "olive", fg = "white", font = ("Times",16,"bold"), selectbackground = "blue", selectforeground = "white")
	calcEntry.grid(row = 0, column =0,columnspan =5)

def printWindowStandart():#функция меняющая цвет окна к стандартному виду
	global calcEntry
	calcEntry = Entry(root, width = 33, borderwidth = 10, bg = "black", fg = "white", font = ("Times",16,"bold"), selectbackground = "blue", selectforeground = "white")
	calcEntry.grid(row = 0, column =0,columnspan =5)

def clearjour():#функция очищающая окно "Журнал"
	global journal
	c.destroy()
	c1 = Canvas(root2, width=350, height=320,bg='white')
	c1.place(x=0, y=0)
	journal.clear()

def makeJournal():#функция создания и заполнения окна "Журнал"
	global c, c1, root2
	root2 = Tk()
	c = Canvas(root2, width=350, height=320,bg='white')
	bttnexit1 = ttk.Button(root2, text = "Очистить", command = clearjour)
	bttnexit2 = ttk.Button(root2, text = "Выход", command = root2.destroy)
	bttnexit2.place(x = 65, y = 325)
	bttnexit1.place(x = 205, y = 325)
	c.place(x=0, y=0)
	root2.title("Журнал")
	root2.geometry("350x350")
	root2.iconbitmap("jour.ico")
	x = (root2.winfo_screenwidth() - root.winfo_reqwidth()) / 2
	y = (root2.winfo_screenheight() - root.winfo_reqheight()) / 2
	root2.wm_geometry("+%d+%d" % (x, y))
	for i in range(999):
		c1 = c.create_text(175, 10+18*(1+i), text = str(i+1) + ') ' + journal[i], justify = CENTER, font = ("Times",16,"bold"))
		
def calc(key):#основная функция работы калькулятора
	if key == "=":
		strL = "+-0123456789.*/"
		if calcEntry.get()[0] not in strL:
			calcEntry.insert(END, "Первый символ не число")
			messagebox.showerror("Ошибка!","Вы ввели не число!")
		try:
			result = eval(calcEntry.get())
			calcEntry.insert(END, "="+str(result))
			journal.append(calcEntry.get())
		except:
			calcEntry.insert(END, "Ошибка!")
			messagebox.showerror("Ошибка!","Проверь правильность данных")
			calcEntry.delete(0, END)

	elif key == "DEL":
		calcEntry.delete(0, END)
	elif key == "-/+":
		if "=" in calcEntry.get():
			calcEntry.delete(0, END)
		try:
			if calcEntry.get()[0] == "-":
				calcEntry.delete(0)
			else:
				calcEntry.insert(0, "-")
		except IndexError:
			pass
	else:
		if "=" in calcEntry.get():
			calcEntry.delete(0, END)
		calcEntry.insert(END, key)


bttnList = [             #список кнопок
    "7", "8","9","+","-",
    "4","5","6","*","/",
    "1","2","3","-/+","=",
    "0",".","DEL","(",")",
    ]

r = 1
c = 0

for i in bttnList:#заполнение формы кнопками через цикл
    rel = ""
    cmd = lambda x=i: calc(x)
    x = Button(root, text=i, command = cmd, width = 7, height = 3, activeforeground = "white", activebackground = "grey",fg = "black", font = ("Times",16,"bold"), bd = 4)
    x.grid(row = r, column = c)
    c += 1
    if c>4:
        c=0
        r += 1

mainmenu.add_command(label = "Информация", command = info)
mainmenu.add_command(label = "Журнал", command = makeJournal)
mainmenu.add_cascade(label = "Изменение цвета кнопок", menu = filemenu)
mainmenu.add_cascade(label = "Изменение цвета окна", menu = filemenu1)
filemenu.add_checkbutton(label= "Бирюзовый цвет кнопок", command = printSkyblue, variable = v0, onvalue = 1, offvalue = 0)
filemenu.add_checkbutton(label= "Бледно-фиолетвый цвет кнопок", command = printMediumslateblue, variable = v0, onvalue = 2, offvalue = 0)
filemenu.add_checkbutton(label= "Песочный цвет кнопок", command = printWheat, variable = v0, onvalue = 3, offvalue = 0)
filemenu.add_checkbutton(label= "Фиолетовый цвет кнопок", command = printViolet, variable = v0, onvalue = 4, offvalue = 0)
filemenu.add_checkbutton(label= "Стандартный цвет кнопок", command = printStandart, variable = v0, onvalue = 5, offvalue = 0)
filemenu1.add_checkbutton(label= "Розовый цвет окна", command = printWindowPink, variable = v00, onvalue = 6, offvalue = 0)
filemenu1.add_checkbutton(label= "Желтый цвет окна", command = printWindowYellow, variable = v00, onvalue = 7, offvalue = 0)
filemenu1.add_checkbutton(label= "Темно-красный цвет кнопок", command = printWindowDarkred, variable = v00, onvalue = 8, offvalue = 0)
filemenu1.add_checkbutton(label= "Оливковый цвет кнопок", command = printWindowOlive, variable = v00, onvalue = 9, offvalue = 0)
filemenu1.add_checkbutton(label= "Стандартный цвет кнопок", command = printWindowStandart, variable = v00, onvalue = 10, offvalue = 0)
calcEntry = Entry(root, width = 33, borderwidth = 10, bg = "black", fg = "white", font = ("Times",16,"bold"), selectbackground = "blue", selectforeground = "white")
calcEntry.grid(row = 0, column =0,columnspan =5)
root.mainloop()