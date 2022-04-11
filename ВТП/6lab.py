from tkinter import *
from tkinter import ttk
import math
root = Tk()
root.geometry('700x300+400+100')
root.resizable (False, False)
tab_control = ttk.Notebook(root)
tab1 = Frame(tab_control)
tab2 = Frame(tab_control)
tab3 = Frame(tab_control)

tab_control.add(tab1, text='Первая')
tab_control.add(tab2, text='Вторая')
tab_control.add(tab3, text='Третья')

tab_control.pack(expand=1, fill='both')

c = Canvas(tab1, width=650, height=300, bg="white")
c.place(x = 20, y = 20)

c2 = Canvas(tab2, width=650, height=300, bg="white")
c2.place(x = 20, y = 20)

c3 = Canvas(tab3, width=650, height=300, bg="white")
c3.place(x = 20, y = 20)

Hx = 500
Hy = 500
xmin = -5
xmax = 11
ymin = 5
ymax = -5
Rx = xmax-xmin
Ry = ymax-ymin
mx = Hx/Rx
my = Hy/Ry
x=xmin

while x <= xmax:
    y = (8 * (x - 4)/(x * x + 26))
    if y<ymin:
        ymin = y
    if y>ymax:
        ymax = y
    x += 1

print(ymin, ymax)

dx = 230
dy = 200

c.create_line(200, 0, 200, 600)
c.create_line(0, 200, 1000, 200)

x=xmin

foot_x = 0.5
points=int(Rx/foot_x)

point_x = []
point_y = []
i = 0
while x <= xmax:
    i += 25
    y = (8 * (x - 4)/(x * x + 26))
    xt = mx*x+dx
    yt = dy - my*y
    c.create_line(0, dy-i, 600, dy-i, fill='grey')
    c.create_text(210, 200-i, text=i)
    c.create_line(xt, 0, xt, 200, fill='grey')
    c.create_text(xt, 210, text=x)
    c2.create_line(0, dy-i, 600, dy-i, fill='grey')
    c2.create_text(210, 200-i, text=i)
    c2.create_line(xt, 0, xt, 200, fill='grey')
    c2.create_text(xt, 210, text=x)
    c3.create_line(0, dy-i, 600, dy-i, fill='grey')
    c3.create_text(210, 200-i, text=i)
    c3.create_line(xt, 0, xt, 200, fill='grey')
    c3.create_text(xt, 210, text=x)
    point_x.append(xt)
    point_y.append(yt)
    print('1:',i,xt, yt, x, y)
    x += foot_x

for i in range(points):

    x1=point_x[i]
    y1=point_y[i]
    x2=point_x[i+1]
    y2=point_y[i+1]
    c.create_line(x1, y1, x2, y2, width=3, fill="black")

c2.create_line(200, 0, 200, 600)
c2.create_line(0, 200, 1000, 200)

x2 = xmin
foot_x2 = Rx/Hx
points2=int(Rx/foot_x2)

point_x2 = []
point_y2 = []

while x2 <= xmax:
    y2 = (8 * (x2 - 4)/(x2 * x2 + 26))
    xt2 = mx*x2+dx
    yt2 = dy - my*y2
    point_x2.append(xt2)
    point_y2.append(yt2)
    x2 += foot_x2

for i in range(points2-1):
    x12=point_x2[i]
    y12=point_y2[i]
    x22=point_x2[i+1]
    y22=point_y2[i+1]
    c2.create_line(x12, y12, x22, y22, width=3, fill="black")

c3.create_line(200, 0, 200, 600)
c3.create_line(0, 200, 1000, 200)

x3 = xmin
foot_x3 = 0.5
points3=int(Rx/foot_x3)

point_x3 = []
point_y3 = []

while x3 <= xmax:

    y3 = (8 * (x3 - 4)/(x3 * x3 + 26))
    xt3 = mx*x3+dx
    yt3 = dy - my*y3
    point_x3.append(xt3)
    point_y3.append(yt3)
    print('3:',xt3, yt3)
    x3 += foot_x3

x31 = point_x3[0]
y31 = point_y3[0]
x32 = point_x3[1]
y32 = point_y3[1]
x33 = point_x3[2]
y33 = point_y3[2]
x34 = point_x3[3]
y34 = point_y3[3]
x35 = point_x3[4]
y35 = point_y3[4]
x36 = point_x3[5]
y36 = point_y3[5]
x37 = point_x3[6]
y37 = point_y3[6]
x38 = point_x3[7]
y38 = point_y3[7]
x39 = point_x3[8]
y39 = point_y3[8]
x310 = point_x3[9]
y310 = point_y3[9]
x311 = point_x3[10]
y311 = point_y3[10]
x312 = point_x3[11]
y312 = point_y3[11]
x313 = point_x3[12]
y313 = point_y3[12]
x314 = point_x3[13]
y314 = point_y3[13]
x315 = point_x3[14]
y315 = point_y3[14]
x316 = point_x3[15]
y316 = point_y3[15]
c3.create_line(x31, y31, x32, y32, x33, y33, x34, y34, x35, y35, x36, y36, x37, y37, x38, y38, x39, y39, x310, y310, x311, y311, x312, y312, x313, y313, x314, y314, x315, y315, x316, y316, smooth = 1, width=3, fill="black")

root.mainloop()