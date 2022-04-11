from tkinter import *
from math import *
root = Tk()
root.geometry('600x400')
c = Canvas(root, width = 600, height = 400)
c.place(x=0, y=0)

dx=0
dy=0
x0=92.5
y0=305
alfa=0
z=0



def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point
    qx = ox - cos(angle) * (px - ox) + sin(angle) * (py - oy)
    qy = oy + sin(angle) * (px - ox) + cos(angle) * (py - oy)
    return qx, qy

def MoveLine():
    global dx, dy, alfa, x0, y0, z
    c.delete("all")
    c.create_line(60, 340, 220, 340, width = 5)
    c.create_line(60, 340, 60, 370, width = 5)
    c.create_line(0, 340, 600, 340)#x
    c.create_line(60, 0, 60, 400)#y
    z += 1
    dx = -1
    dy = 150/300
    alfa -= 41/300
    x0 = x0-dx
    y0 = y0+dy
    x1 = x0-12.5
    y1 = y0-25
    x2 = x0-12.5
    y2 = y0+25
    x3 = x0+12.5
    y3 = y0-25
    x4 = x0+12.5
    y4 = y0+25
    point=(x1, y1)
    origin = (x0, y0)
    x1, y1 = rotate(origin, point, radians(alfa))
    point=(x2, y2)
    x2, y2 = rotate(origin, point, radians(alfa))
    point=(x3, y3)
    x3, y3 = rotate(origin, point, radians(alfa))
    point=(x4, y4)
    x4, y4 = rotate(origin, point, radians(alfa))
    Line1=c.create_line(x1, y1, x2, y2, fill = "red", width = 2)
    Line2=c.create_line(x2, y2, x4, y4, fill = "green", width = 2)
    Line3=c.create_line(x1, y1, x4, y4, fill = "blue", width = 2)
    if z < 301:
            c.after(50, MoveLine)

MoveLine()
root.mainloop()