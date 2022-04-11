from tkinter import*
from tkinter import ttk
import random

root = Tk()
root.title('8lab')
root.geometry('700x500')

widths = 1
hei = 50
wid = 50

def dra(event):
	x = event.x
	y = event.y
	print(x,y)

def create_oval(event):
	global x0, y0, x, y
	x = event.x
	y = event.y
	print(x,y)
	color = ("#%03x" % random.randint(0, 0xFFF))
	canv.create_oval(x - 70, y - 70, x + 70, y + 70, width = widths, outline = color)
	entry = Entry(root, font = ("Times",16,"bold"), width = 5)
	entry.delete(END, END)
	entry.insert(END, color)
	entry.place(x = 400, y = 20)

def create_rectangle(event):
	color = ("#%03x" % random.randint(0, 0xFFF))
	canv.create_rectangle(x - wid, y - hei, x + wid, y + hei, width = widths, outline = color)
	entry = Entry(root, font = ("Times",16,"bold"), width = 5)
	entry.delete(END, END)
	entry.insert(END, color)
	entry.place(x = 400, y = 20)

def pixes1(event):
	global widths
	widths = 4

def pixes2(event):
	global widths
	widths = 7

def pixes3(event):
	global widths
	widths = 2

def height(event):
	global hei
	hei = scale1.get()
	print(hei)

def width(event):
	global wid
	wid = scale2.get()
	print(wid)

canv = Canvas(root, height = 360, width = 550, bg = "white", xscrollcommand = 1)
canv.place(x = 25, y = 100)
scale1 = Scale(root, orient = HORIZONTAL, length = 300, from_ = 50, to = 150)
scale1.place(x = 50, y = 25)
scale2 = Scale(root, orient = VERTICAL, length = 300, from_ = 50, to = 150)
scale2.place(x = 580, y = 100)
lblheight = Label(root, text = "Высота прямоугольника", font = ("Times",12,"bold"))
lblheight.place(x = 110, y = 8)
lblwidth = Label(root, text = "Ширина\n прямоугольника", font = ("Times",12,"bold"))
lblwidth.place(x = 550, y = 50)
scale1.bind('<ButtonRelease>', height)
scale2.bind('<ButtonRelease>', width)
canv.bind('<Control-Button-1>', create_oval)
canv.bind('<Motion>', dra)
canv.bind('<Control-Button-3>', create_rectangle)
root.bind('1', pixes1)
root.bind('2', pixes2)
root.bind('3', pixes3)
root.mainloop()