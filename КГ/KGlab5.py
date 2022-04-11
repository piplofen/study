from tkinter import *
from math import *
root = Tk()
root.geometry('1000x600+200+100')
c = Canvas(root, width=600, height=400,bg='white')
c.place(x=200, y=100)
c.create_text(40, 10, text='Вариант - 19')
c.create_line(450, 0, 450, 400)
c.create_line(0, 300, 600, 300)
dx=0
dy=0
alfa=0
dx2=0
dy2=0
alfa2=0
dx3=0
dy3=0
alfa3=0
z=0
x0 = 450
y0 = 300

def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point
    qx = ox + cos(angle) * (px - ox) - sin(angle) * (py - oy)
    qy = oy + sin(angle) * (px - ox) + cos(angle) * (py - oy)
    return qx, qy
def MoveLine():
    global dx,dy,alfa
    c.delete("all")
    c.create_line(450, 0, 450, 400)
    c.create_line(0, 300, 600, 300)
    dx +=1
    dy += 30/180
    alfa += 60/180
    x1=x0+30
    y1=y0-60
    x2=x0+30
    y2=y0
    x3 = x0+60
    y3 = y0-60
    x4 = x0+60
    y4 = y0
    point=(x1, y1)
    origin = (x0, y0)
    x1, y1 = rotate(origin, point, radians(alfa))
    point=(x2, y2)
    x2, y2 = rotate(origin, point, radians(alfa))
    point=(x3, y3)
    x3, y3 = rotate(origin, point, radians(alfa))
    point=(x4, y4)
    x4, y4 = rotate(origin, point, radians(alfa))

    Line1=c.create_line(x1-dx, y1-dy, x2-dx, y2-dy, fill="blue", width=2)
    Line2=c.create_line(x2-dx, y2-dy, x4-dx, y4-dy, fill="green", width=2)
    Line3=c.create_line(x1-dx, y1-dy, x4-dx, y4-dy, fill="reD", width=2)
    if dx < 120:
            c.after(50, MoveLine)
MoveLine()

root.mainloop()
