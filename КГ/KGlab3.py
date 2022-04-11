from tkinter import*
root = Tk()

canv = Canvas(root, width = 300, height = 900, bg = 'white')
canv.pack()
top = canv.create_arc(35, 690, 250, 878, start = 0, extent = 180, outline = 'black', fill = 'yellow', width = 2)
mid = canv.create_rectangle(35,786,250,800, fill = 'red', outline = 'black', width = 2)
bot = canv.create_arc(35, 895, 250, 700, start = 0, extent = -180, outline = 'black', fill = '#1f1', width =2)