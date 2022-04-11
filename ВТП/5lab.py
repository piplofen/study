from tkinter import*
from tkinter import ttk

root = Tk()
root.title('5lab')
root.geometry('1400x550')
root.resizable(width=False, height=False)
canv = Canvas(root, width = 1400,  height = 700,bg='white')
canv.place(x = 0, y = 0)

foot1 = 0
foot2 = 0
k = 1
k1 = 1
k2 = 1
t = 0
m = 0

#информаиця
canv.create_text(800, 100, text = 'Подковыров Даниил', font = ("Times",16,"bold"))
canv.create_text(800, 120, text = 'Вариант №19', font = ("Times",16,"bold"))
canv.create_text(800, 140, text = 'Группа 18ВТ2', font = ("Times",16,"bold"))

#перекрёсток
canv.create_line(290, 0, 290, 280, width = 3)
canv.create_line(410, 0, 410, 280, width = 3)

canv.create_line(290, 280, 0, 280, width = 3)
canv.create_line(290, 400, 0, 400, width = 3)

canv.create_line(410, 280, 1400, 280, width = 3)
canv.create_line(410, 400, 1400, 400, width = 3)

canv.create_line(290, 400, 290, 700, width = 3)
canv.create_line(410, 400, 410, 700, width = 3)

canv.create_rectangle(292, 0, 408, 700, fill='grey', outline = 'grey')
canv.create_rectangle(0, 282, 1400, 398, fill='grey', outline = 'grey')

canv.create_rectangle(347, 0, 350, 700, fill='white', outline = 'white')
canv.create_rectangle(0, 339, 1400, 342, fill='white', outline = 'white')

canv.create_rectangle(300, 290, 400, 398, fill='grey', outline = 'grey')

#машинка1
car11 = canv.create_rectangle(10, 300, 30, 360, fill='red', outline = 'black')
car12 = canv.create_rectangle(30, 300, 50, 360, fill='Skyblue', outline = 'black')
car13 = canv.create_rectangle(50, 300, 100, 360, fill='red4', outline = 'black')
car14 = canv.create_rectangle(100, 300, 120, 360, fill='Skyblue', outline = 'black')
car15 = canv.create_rectangle(120, 300, 150, 360, fill='red', outline = 'black')

#машинка2
car21 = canv.create_rectangle(320, 10, 380, 30, fill= 'green', outline = 'black')
car22 = canv.create_rectangle(320, 30, 380, 50, fill='Skyblue', outline = 'black')
car23 = canv.create_rectangle(320, 50, 380, 100, fill='dark green', outline = 'black')
car24 = canv.create_rectangle(320, 100, 380, 120, fill='Skyblue', outline = 'black')
car25 = canv.create_rectangle(320, 120, 380, 150, fill= 'green', outline = 'black')

def ov():
    global m
    m +=1
    if m == 1:
        Stop()

def Stop():
	global k, k1, k2, foot2, foot1, t, m
	foot2 = 0
	foot1 = 0
	k1 = 0
	k2 = 0
	m = 0
	t = 0

def ove():
    global t, k1, k2
    t +=1
    if t == 1:
    	k1 = 1
    	k2 = 1
    	Move1()
    	Move2()

#функция движения красной машины
def Move1():
	global car11, car12, car13, car14, car15, foot1, k, k1
	canv.delete(car11,car12, car13, car14, car15)
	foot1 += 1
	if k1 == 1:
	    car11 = canv.create_rectangle(k*10+3*foot1, 300, k*30+3*foot1, 360, fill='red', outline = 'black')
	    car12 = canv.create_rectangle(k*30+3*foot1, 300, k*50+3*foot1, 360, fill='Skyblue', outline = 'black')
	    car13 = canv.create_rectangle(k*50+3*foot1, 300, k*100+3*foot1, 360, fill='red4', outline = 'black')
	    car14 = canv.create_rectangle(k*100+3*foot1, 300, k*120+3*foot1, 360, fill='Skyblue', outline = 'black')
	    car15 = canv.create_rectangle(k*120+3*foot1, 300, k*150+3*foot1, 360, fill='red', outline = 'black')
	else:
	    k1 = 1
	    canv.delete(car11,car12, car13, car14, car15)
	    car11 = canv.create_rectangle(10, 300, 30, 360, fill='red', outline = 'black')
	    car12 = canv.create_rectangle(30, 300, 50, 360, fill='Skyblue', outline = 'black')
	    car13 = canv.create_rectangle(50, 300, 100, 360, fill='red4', outline = 'black')
	    car14 = canv.create_rectangle(100, 300, 120, 360, fill='Skyblue', outline = 'black')
	    car15 = canv.create_rectangle(120, 300, 150, 360, fill='red', outline = 'black')
	    return

	if foot1 < 495:
		canv.after(10, Move1)

	if foot1 >= 495:
		foot1 = 0
		Move1()

#функция движения зеленой машины
def Move2():
	global car21, car22, car23, car24, car25, foot2, k, k2
	canv.delete(car21,car22, car23, car24, car25)
	foot2 += 1
	if k2 == 1:
	    car21 = canv.create_rectangle(320, k*10+1*foot2, 380, k*30+1*foot2, fill= 'green', outline = 'black')
	    car22 = canv.create_rectangle(320, k*30+1*foot2, 380, k*50+1*foot2, fill='Skyblue', outline = 'black')
	    car23 = canv.create_rectangle(320, k*50+1*foot2, 380, k*100+1*foot2, fill='dark green', outline = 'black')
	    car24 = canv.create_rectangle(320, k*100+1*foot2, 380, k*120+1*foot2, fill='Skyblue', outline = 'black')
	    car25 = canv.create_rectangle(320, k*120+1*foot2, 380, k*150+1*foot2, fill= 'green', outline = 'black')
	else:
		k2 = 1
		canv.delete(car21,car22, car23, car24, car25)
		car21 = canv.create_rectangle(320, 10, 380, 30, fill= 'green', outline = 'black')
		car22 = canv.create_rectangle(320, 30, 380, 50, fill='Skyblue', outline = 'black')
		car23 = canv.create_rectangle(320, 50, 380, 100, fill='dark green', outline = 'black')
		car24 = canv.create_rectangle(320, 100, 380, 120, fill='Skyblue', outline = 'black')
		car25 = canv.create_rectangle(320, 120, 380, 150, fill= 'green', outline = 'black')
		return

	if foot2 < 495:
		canv.after(10, Move2)

	if foot2 >= 495:
		foot2 = 0
		Move2()

bttnstart =  ttk.Button(root, text = "Старт", command = ove)
bttnstart.place(x = 700, y = 520)
bttnstop =  ttk.Button(root, text = "Стоп", command = ov)
bttnstop.place(x = 790, y = 520)

root.mainloop()
