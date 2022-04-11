from tkinter import*

root = Tk()
root.title('3lab')
root.geometry('500x300')
Var1 = BooleanVar()
Var1.set(1)
Var0 = BooleanVar()
Var0.set(0)

def motionUPd1(event):
	global chkkbttn
	dayEntry7.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry7.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var1)
	chkkbttn.place(x = 250, y = 160)

def motionDOWNd1(event):
	global chkkbttn
	dayEntry2.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry2.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var0)
	chkkbttn.place(x = 250, y = 160)

def motionUPd2(event):
	global chkkbttn
	dayEntry1.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry1.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var1)
	chkkbttn.place(x = 250, y = 160)

def motionDOWNd2(event):
	global chkkbttn
	dayEntry3.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry3.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var0)
	chkkbttn.place(x = 250, y = 160)

def motionUPd3(event):
	global chkkbttn
	dayEntry2.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry2.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var1)
	chkkbttn.place(x = 250, y = 160)

def motionDOWNd3(event):
	global chkkbttn
	dayEntry4.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry4.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var0)
	chkkbttn.place(x = 250, y = 160)

def motionUPd4(event):
	global chkkbttn
	dayEntry3.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry3.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var1)
	chkkbttn.place(x = 250, y = 160)

def motionDOWNd4(event):
	global chkkbttn
	dayEntry5.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry5.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var0)
	chkkbttn.place(x = 250, y = 160)

def motionUPd5(event):
	global chkkbttn
	dayEntry4.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry4.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var1)
	chkkbttn.place(x = 250, y = 160)

def motionDOWNd5(event):
	global chkkbttn
	dayEntry6.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry6.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var0)
	chkkbttn.place(x = 250, y = 160)

def motionUPd6(event):
	global chkkbttn
	dayEntry5.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry5.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var1)
	chkkbttn.place(x = 250, y = 160)

def motionDOWNd6(event):
	global chkkbttn
	dayEntry7.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry7.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var0)
	chkkbttn.place(x = 250, y = 160)

def motionUPd7(event):
	global chkkbttn
	dayEntry6.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry6.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var1)
	chkkbttn.place(x = 250, y = 160)

def motionDOWNd7(event):
	global chkkbttn
	dayEntry1.focus()
	text.delete(1.0, END)
	text.insert(END, dayEntry1.get())
	chkkbttn.place_forget()
	chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var0)
	chkkbttn.place(x = 250, y = 160)

dayEntry1 = Entry(root, font = ("Times",16,"bold"), justify = CENTER)
dayEntry1.insert(END, 'Monday')
dayEntry2 = Entry(root, font = ("Times",16,"bold"), justify = CENTER)
dayEntry2.insert(END, 'Tuesday')
dayEntry3 = Entry(root, font = ("Times",16,"bold"), justify = CENTER)
dayEntry3.insert(END, 'Wednesday')
dayEntry4 = Entry(root, font = ("Times",16,"bold"), justify = CENTER)
dayEntry4.insert(END, 'Thursday')
dayEntry5 = Entry(root, font = ("Times",16,"bold"), justify = CENTER)
dayEntry5.insert(END, 'Friday')
dayEntry6 = Entry(root, font = ("Times",16,"bold"), justify = CENTER)
dayEntry6.insert(END, 'Saturday')
dayEntry7 = Entry(root, font = ("Times",16,"bold"), justify = CENTER)
dayEntry7.insert(END, 'Sunday')

text = Text(root, width = 10, height = 1, font = ("Times",16,"bold"))

close_bttn = Button(root, text = 'Закрыть', font = ("Times",16,"bold"), command = root.destroy)

chkkbttn = Checkbutton(root, text = 'Флажок', variable = Var0)

dayEntry1.place(x = 10, y = 10)
dayEntry2.place(x = 10, y = 40)
dayEntry3.place(x = 10, y = 70)
dayEntry4.place(x = 10, y = 100)
dayEntry5.place(x = 10, y = 130)
dayEntry6.place(x = 10, y = 160)
dayEntry7.place(x = 10, y = 190)
close_bttn.place(x = 230, y =265)
text.place(x = 250, y = 40)
chkkbttn.place(x = 250, y = 160)

dayEntry1.bind('<Up>', motionUPd1)
dayEntry1.bind('<Down>', motionDOWNd1)
dayEntry2.bind('<Up>', motionUPd2)
dayEntry2.bind('<Down>', motionDOWNd2)
dayEntry3.bind('<Up>', motionUPd3)
dayEntry3.bind('<Down>', motionDOWNd3)
dayEntry4.bind('<Up>', motionUPd4)
dayEntry4.bind('<Down>', motionDOWNd4)
dayEntry5.bind('<Up>', motionUPd5)
dayEntry5.bind('<Down>', motionDOWNd5)
dayEntry6.bind('<Up>', motionUPd6)
dayEntry6.bind('<Down>', motionDOWNd6)
dayEntry7.bind('<Up>', motionUPd7)
dayEntry7.bind('<Down>', motionDOWNd7)

root.mainloop()