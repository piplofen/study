from tkinter import *
root = Tk()
root.geometry('650x400')
root.title('4lab')
c = Canvas(root, width=700, height=400,bg='white')
c.place(x=0, y=0)
c.create_text(250, 10, text='Variant - 19', font = ("Times",16,"bold"))
c.create_text(250, 25, text='Calendar for July 2020', font = ("Times",16,"bold"))
c.create_text(525, 55, text='Подковыров Даниил\nСтудент группы 18ВТ2', font = ("Times",16,"bold"))
button1 = False
button2 = False

Day=c.create_line(135 ,155 ,165 ,155 ,165 ,155 ,165 ,185 ,165 ,185 ,135 ,185 ,135 ,185 ,135 ,155 , fill="pink", width=3)
tick = 800
x0 = 0
y0 = 0
foots = 0
t = 0

def Kalendar(c):
    global Day
    c.place(x = 0, y = 0)
    c.create_text(250, 10, text='Variant - 19', font = ("Times",16,"bold"))
    c.create_text(250, 25, text='Calendar for July 2020', font = ("Times",16,"bold"))
    c.create_text(525, 55, text='Подковыров Даниил\nСтудент группы 18ВТ2', font = ("Times",16,"bold"))

    Week=["Sunday","Saturday","Friday","Thursday","Wednesday","Tuesday","Monday"]
    for i in range(7):
        c.create_text(68, 50+40*(1+i), text=Week.pop(), font = ("Times",16,"bold"))
    for i in range(5):
        c.create_text(150, 90+40*(i+2), text=1 + i, font = ("Times",16,"bold"))
    for i in range(7):
        c.create_text(200, 50+40*(i+1), text=6 + i, font = ("Times",16,"bold"))
    for i in range(7):
        c.create_text(250, 50+40*(i+1), text=13 + i, font = ("Times",16,"bold"))
    for i in range(7):
        c.create_text(300, 50+40*(i+1), text=20 + i, font = ("Times",16,"bold"))
    for i in range(5):
        c.create_text(350, 50+40*(i+1), text=27 + i, font = ("Times",16,"bold"))

def stopButton():
    global button1, foots, button2, x0, y0
    foots = 0
    x0 = 0
    y0 = 0
    if Var.get() == 0:
        button1 = True

def ove():
    global t
    t += 1
    if t == 1:
        Move()

def Move():
    global Day, button1, button2, foots, x0, y0, tick, t
    if (Var.get() == 1):
        c.delete(Day)
        foots += 1
        Day = c.create_line(x0 + 135, y0 + 155, x0 + 165, y0 + 155, x0 + 165, y0 + 155, x0 + 165, y0 + 185, x0 + 165, y0 + 185, x0 + 135, y0 + 185, x0 + 135, y0 + 185, x0 + 135, y0 + 155, fill="pink", width=3)
        y0 = y0 + 40

        if foots == 5:
            x0 = x0 + 50
            y0 = y0 - 280
        if foots == 12:
            x0 = x0 + 50
            y0 = y0 - 280
        if foots == 19:
            x0 = x0 + 50
            y0 = y0 - 280
        if foots == 26:
            x0 = x0 + 50
            y0 = y0 - 280
    else:
        c.delete(Day)
        Day = c.create_line(135, 155, 165, 155, 165, 155, 165, 185, 165, 185, 135, 185, 135, 185, 135, 155, fill = "pink", width = 3)
    if foots < 32:
        c.after(800, Move)

    if foots >= 32:
        foots = 0
        x0 = 0
        y0 = 0
        Move()

Kalendar(c)

Var = IntVar()
Var.set(0)
mainmenu = Menu(root)
helpmenu = Menu(mainmenu, tearoff=0)
root.config(menu=mainmenu)
mainmenu.add_cascade(label = 'Информация о программе', menu = helpmenu)
helpmenu.add_radiobutton(label="Start programm", value = 1, variable = Var, command=ove)
helpmenu.add_radiobutton(label="Stop", value = 0, variable = Var, command=stopButton)

root.mainloop()
