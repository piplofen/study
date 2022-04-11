from tkinter import*

root = Tk()
root.title('4lab')

#canv = Canvas(root, width = 700, height = 700, bg = 'white')
#canv.focus_set()
#canv.grid(row = 0, column = 0)

labelList = [
    "ПН", "ВТ","СР","ЧТ","ПТ", "СБ", "ВС",
    " ", " ","1","2","3", "4", "5",
    "6", "7","8","9","10", "11", "12",
    "13", "14","15","16","17", "18", "19",
    "20", "21","22","23","24", "25", "26",
    "27", "28","29","30","31", " ", " "
    ]

r = 1
c = 0
k = 0

for i in labelList:
    x = Label(root, text=i,  width = 7, height = 3, font = ("Times",16,"bold"))
    x.grid(row = r, column = c)
    c += 1
    if c>6:
        c=0
        r += 1

    if k <= 6:
        x['bg'] = 'lightgrey'
        k += 1

    if (i == '4' or i == '5' or i == '11' or i == '12' or i == '18' or i == '19' or i == '25' or i == '26'):
        x['bg'] = "goldenrod1"

MonthName = Label(root, text = 'ИЮЛЬ',  width = 7, height = 3, font = ("Times",16,"bold"))
MonthName.grid(row = 0, column = 3)

#im = PhotoImage(file = 'square1.gif')
#labelsquare = Label(root, image = im)
#labelsquare.grid(row = 0, column = 0)

#canv.bind('<Right>', lambda event: canv.move(else1, 10, 0))
#canv.bind('<Down>', lambda event: canv.move(else1, 0, 10))
#canv.bind('<Up>', lambda event: canv.move(else1, 0, -10))
#canv.bind('<Left>', lambda event: canv.move(else1, -10, 0))

root.mainloop()