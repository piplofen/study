from tkinter import*
from tkinter import ttk
import random

root = Tk()
root.title('lab7')
root.geometry('500x500')
canv = Canvas(root, width = 350, height = 400)
canv.place(x = 0, y = 50)

Val0 = IntVar()
Val1 = IntVar()
k = 0
l = 0
l1 = 0
h = 0
dd = 0
u = u1 = 0
dd1 = 0

def column1(event):
    global J
    if combobox1.get() == '1 строка':
        J = 1
        print(J)
    if combobox1.get() == '2 строки':
        J = 2
        print(J)
    if combobox1.get() == '3 строки':
        J = 3
        print(J)
    if combobox1.get() == '4 строки':
        J = 4
        print(J)
    if combobox1.get() == '5 строк':
        J = 5
        print(J)
    if combobox1.get() == '6 строк':
        J = 6
        print(J)

def column(event):
	global I
	if combobox.get() == '1 столбец':
		I = 1
		print(I)
	if combobox.get() == '2 столбца':
		I = 2
		print(I)
	if combobox.get() == '3 столбца':
		I = 3
		print(I)
	if combobox.get() == '4 столбца':
		I = 4
		print(I)
	if combobox.get() == '5 столбцов':
		I = 5
		print(I)
	if combobox.get() == '6 столбцов':
		I = 6
		print(I)
	if combobox.get() == '7 столбцов':
		I = 7
		print(I)
	if combobox.get() == '8 столбцов':
		I = 8
		print(I)
	if combobox.get() == '9 столбцов':
		I = 9
		print(I)

def run():
    global naib
    for i in naib:
        x = i
        t1 = canv.create_rectangle(x + 32, 20, x + 58, 230, outline = "red", dash = 3, width = 2)

mainmenu = Menu(root)
root.config(menu=mainmenu)
helpmenu1 = Menu(mainmenu, tearoff=0)
helpmenu2 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label = 'Действия', menu = helpmenu2)
helpmenu2.add_command(label = 'Посчитать', command = run)

def matrix(event):
	global I, J, k, l, cc, dd, u1, u, d, naib, dd1, l1
	naib = []
	matrix = [[random.randrange(-100,100) for y in range(I)] for x in range(J)]
	maxim = 0
	c = 0
	cc = []
	for i in range(J):
		for j in range(I):
			canv.create_text(45+l, 30+k, text = matrix[i][j], font = ("Times",10,"bold"))
			l += 25
		k += 25
		l = 0
	d = 0
	v = 0
	l1 = 0

	for j in range (I):
		for i in range (J):
			a1 = matrix[i][j]
			result = []
			b = 0
			if a1 < 0:
				b = abs(a1)
			while b > 0:
				result.append(b % 10)
				b = b // 10
			c += len(result)
		cc.append(c)
		canv.create_text(45 + l, 220, text = c, font = ("Times",10,"bold"))
		v = abs(c)
		if v > d:
			d = v
		l += 25
		c = 0
	l = 0

	for j in range (I):
		for i in range (J):
			a1 = matrix[i][j]
			result = []
			b = 0
			if a1 < 0:
				b = abs(a1)
			while b > 0:
				result.append(b % 10)
				b = b // 10
			c += len(result)
		d1 = abs(c)

		if d1 == d:
			dd = l1
			naib.append(dd)
		l1 += 25
		c = 0


def clear():
	global canv, k
	canv.destroy()
	canv = Canvas(root, width = 350, height = 400)
	canv.place(x = 0, y = 50)
	canv.bind("<Double-Button-1>", matrix)
	k = 0

combobox1 = ttk.Combobox(root, values = ["1 строка","2 строки","3 строки","4 строки","5 строк","6 строк"], height = 6, state = 'readonly')#строки
combobox1.place(x = 340, y = 350)

combobox = ttk.Combobox(root, values = ["1 столбец","2 столбца","3 столбца","4 столбца","5 столбцов","6 столбцов","7 столбцов","8 столбцов","9 столбцов"], height = 9, state = 'readonly')#столбцы
combobox.place(x = 340, y = 310)

combobox.bind("<<ComboboxSelected>>", column)
combobox1.bind("<<ComboboxSelected>>", column1)

root.bind("<Double-Button-1>", matrix)

bttnClear = ttk.Button(root, text = "Очистить", command = clear)
bttnClear.place(x = 400, y = 150)

root.mainloop()