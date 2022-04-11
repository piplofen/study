from tkinter import*
from math import*

root_window=Tk()
root_window.geometry('800x750+200+50')
work_place=Canvas(root_window, bg = "white", width = 600, height = 600)
work_place.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)

def DrawCoordinatesAxes(center_point_x, center_point_y):
    long_of_coordinates=315
    work_place.create_text(center_point_x-5, center_point_y+12, text = "0", font = ("Courier New", 12), justify = CENTER)#центр координат

    axis_z = work_place.create_line(center_point_x, center_point_y, center_point_x, center_point_y-long_of_coordinates, width =1, arrow = LAST) #ось Z
    z_pointer = work_place.create_text(center_point_x, center_point_y-long_of_coordinates-15, text = "Z", font = ("Courier New", 10), justify = CENTER)

    for i in range(1, 7): #подписи ось Z
        work_place.create_line(center_point_x-5,center_point_y-i*50, center_point_x+5, center_point_y-i*50, width =1)
        work_place.create_text(center_point_x-20, center_point_y-i*50, text = str(i*50), font = ("Courier New", 10), justify = CENTER)

    angle_y = (41.25*0.01745) #ось Y
    Y_axis_x = center_point_x + (long_of_coordinates) * cos(angle_y)
    Y_axis_y = center_point_y + (long_of_coordinates) * sin(angle_y)
    axis_y = work_place.create_line(center_point_x, center_point_y, Y_axis_x, Y_axis_y, width =1, arrow = LAST) 
    y_pointer = work_place.create_text(Y_axis_x+15, Y_axis_y, text = "Y", font = ("Courier New", 10), justify = CENTER)
    
    for i in range(1, 13): #подписи ось Y
        work_place.create_line(center_point_x+0.5*i*50*cos(angle_y),(center_point_y-5+0.5*i*50*sin(angle_y)), center_point_x+0.5*i*50*cos(angle_y), (center_point_y+5+0.5*i*50*sin(angle_y)), width =1)
        work_place.create_text(center_point_x+0.5*i*50*cos(angle_y), (center_point_y+5+0.5*i*50*sin(angle_y))+15, text = str(i*50), font = ("Courier New", 9), justify = CENTER)
    
    angle_x = (172.90*0.01745) #ось X
    X_axis_x = center_point_x + (long_of_coordinates) * cos(angle_x)
    X_axis_y = center_point_y + (long_of_coordinates) * sin(angle_x)
    axis_x = work_place.create_line(center_point_x, center_point_y, X_axis_x, X_axis_y, width =1, arrow = LAST)
    x_pointer = work_place.create_text(X_axis_x-15, X_axis_y, text = "X", font = ("Courier New", 10), justify = CENTER)

    for i in range(1, 7): #подписи ось X
        work_place.create_line(center_point_x+i*50*cos(angle_x), center_point_y-5+i*50*sin(angle_x), center_point_x+i*50*cos(angle_x), center_point_y+5+i*50*sin(angle_x), width =1)
        work_place.create_text(center_point_x+i*50*cos(angle_x), center_point_y+5+i*50* sin(angle_x)+15, text = str(i*50), font = ("Courier New", 10), justify = CENTER)

#функция преобразовывает три получаемые локальные координаты в мировые
def xyz(true_x, true_y, true_z):
    global center_point_y, center_point_x
    true_y = true_y/2 #т.к. по оси Y масштаб в 2 раза меньше
    Mx2 = center_point_x + cos(41.25*pi/180) * true_y - true_x*cos(7.1*pi/180)
    My2 = center_point_y - true_z + (true_y*sin(41.25*pi/180) + true_x*sin(7.1*pi/180))
    return int(Mx2), int(My2)

def YAxisRotation(i, lx, ly, lz, rx, ry, rz, ux, uy, uz, bx, by, bz, figure):
    description.config(text='Поворот по часовой стрелке, вокруг Y на 40°')
    second["state"] = DISABLED

    if i == 0 and figure == "first figure":
        work_place.create_line(xyz(lx, ly, lz), xyz(rx, ry, rz), width =2, fill = "cyan")
        work_place.create_line(xyz(ux, uy, uz), xyz(bx, by, bz), width =2, fill = "darkslateblue")

    alpha = -(pi/180) #1 градус в радианах
    rot_lx = lx*cos(alpha) + lz*sin(alpha)
    rot_ly = ly
    rot_lz = -lx*sin(alpha) + lz*cos(alpha)

    rot_rx = rx*cos(alpha) + rz*sin(alpha)
    rot_ry = ry
    rot_rz = -rx*sin(alpha)+rz*cos(alpha)

    rot_ux = ux*cos(alpha) + uz*sin(alpha)
    rot_uy = uy
    rot_uz = -ux*sin(alpha) + uz*cos(alpha)

    rot_bx = bx*cos(alpha) + bz*sin(alpha)
    rot_by = by
    rot_bz = -bx*sin(alpha)+bz*cos(alpha)

    if i<=40 and figure == "first figure":
        first["state"] = DISABLED
        work_place.delete('hor1')
        work_place.delete('ver1')

        horisontal = work_place.create_line(xyz(rot_lx, rot_ly, rot_lz), xyz(rot_rx, rot_ry, rot_rz), width =2, fill = "cyan", tag="hor1")
        vertical = work_place.create_line(xyz(rot_ux, rot_uy, rot_uz), xyz(rot_bx, rot_by, rot_bz), width =2, fill = "darkslateblue", tag="ver1")
        i+=1
        work_place.after(30, lambda: YAxisRotation(i,\
        rot_lx, rot_ly, rot_lz, rot_rx, rot_ry, rot_rz, rot_ux, rot_uy, rot_uz, rot_bx, rot_by, rot_bz, figure))
    
    if i<=40 and figure == "second figure":
        work_place.delete('hor2')
        work_place.delete('ver2')
        

        horisontal_2 = work_place.create_line(xyz(rot_lx, rot_ly, rot_lz), xyz(rot_rx, rot_ry, rot_rz), width =2, fill = "orange", tag="hor2")
        vertical_2 = work_place.create_line(xyz(rot_ux, rot_uy, rot_uz), xyz(rot_bx, rot_by, rot_bz), width =2, fill = "red", tag="hor2")
        i+=1
        work_place.after(30, lambda: YAxisRotation(i,\
        rot_lx, rot_ly, rot_lz, rot_rx, rot_ry, rot_rz, rot_ux, rot_uy, rot_uz, rot_bx, rot_by, rot_bz, figure))

    if i==41 and figure == "first figure":
        first.place_forget()
        second["state"] = NORMAL
    
    if i ==41 and figure == "second figure":
        second["state"] = NORMAL
        second["command"] = lambda: Move60ByY(0, int(rot_lx), int(rot_ly), int(rot_lz), int(rot_rx), int(rot_ry), int(rot_rz), int(rot_ux), int(rot_uy), int(rot_uz), int(rot_bx), int(rot_by), int(rot_bz), figure)

def XAxisRotation(i, lx, ly, lz, rx, ry, rz, ux, uy, uz, bx, by, bz, figure):
    description.config(text='Поворот против часовой стрелки, вокруг Z на 150°')
    second["state"] = DISABLED

    if i == 0 and figure == "first figure":
        work_place.create_line(xyz(lx, ly, lz), xyz(rx, ry, rz), width =2, fill = "cyan")
        work_place.create_line(xyz(ux, uy, uz), xyz(bx, by, bz), width =2, fill = "darkslateblue")
    
    if i == 0 and figure == "second figure":
        work_place.create_line(xyz(lx, ly, lz), xyz(rx, ry, rz), width =2, fill = "orange")
        work_place.create_line(xyz(ux, uy, uz), xyz(bx, by, bz), width =2, fill = "red")
    
    alpha = (pi/180) #1 градус в радианах
    rot_lx = lx*cos(alpha) - ly*sin(alpha)
    rot_ly = cos(alpha)*ly+sin(alpha)*lx
    rot_lz = lz

    rot_rx = rx*cos(alpha) - ry*sin(alpha)
    rot_ry = cos(alpha)*ry+sin(alpha)*rx
    rot_rz = rz

    rot_ux =ux*cos(alpha) - uy*sin(alpha) 
    rot_uy = cos(alpha)*uy+sin(alpha)*ux
    rot_uz = uz

    rot_bx =bx*cos(alpha) - by*sin(alpha) 
    rot_by = cos(alpha)*by+sin(alpha)*bx
    rot_bz = bz

    if i <= 150 and figure == "first figure":
        first["state"] = DISABLED
        work_place.delete('hor1')
        work_place.delete('ver1')

        horisontal = work_place.create_line(xyz(rot_lx, rot_ly, rot_lz), xyz(rot_rx, rot_ry, rot_rz), width =2, fill = "cyan", tag="hor1")
        vertical = work_place.create_line(xyz(rot_ux, rot_uy, rot_uz), xyz(rot_bx, rot_by, rot_bz), width =2, fill = "darkslateblue", tag="ver1")
        i+=1
        work_place.after(50, lambda: XAxisRotation(i,\
        rot_lx, rot_ly, rot_lz, rot_rx, rot_ry, rot_rz, rot_ux, rot_uy, rot_uz, rot_bx, rot_by, rot_bz, figure))
    
    if i <= 150 and figure == "second figure":
        work_place.delete('hor2')
        work_place.delete('ver2')

        horisontal_2 = work_place.create_line(xyz(rot_lx, rot_ly, rot_lz), xyz(rot_rx, rot_ry, rot_rz), width =2, fill = "orange", tag="hor2")
        vertical_2 = work_place.create_line(xyz(rot_ux, rot_uy, rot_uz), xyz(rot_bx, rot_by, rot_bz), width =2, fill = "red", tag="hor2")
        i+=1
        work_place.after(25, lambda: XAxisRotation(i,\
        rot_lx, rot_ly, rot_lz, rot_rx, rot_ry, rot_rz, rot_ux, rot_uy, rot_uz, rot_bx, rot_by, rot_bz, figure))

    if i == 151 and figure == "first figure":
        first["state"] = NORMAL
        first["command"] = lambda: YAxisRotation(0, rot_lx, rot_ly, rot_lz, rot_rx, rot_ry, rot_rz, rot_ux, rot_uy, rot_uz, rot_bx, rot_by, rot_bz, figure)
    
    if i == 151 and figure == "second figure":
        second["state"] = NORMAL
        second["command"] = lambda: Move120ByZ(0, rot_lx, rot_ly, rot_lz, rot_rx, rot_ry, rot_rz, rot_ux, rot_uy, rot_uz, rot_bx, rot_by, rot_bz, figure)

def Move120ByZ(i, lx, ly, lz, rx, ry, rz, ux, uy, uz, bx, by, bz, figure):
    description.config(text='Смещение по Z на 140пиксы')
    second["state"] = DISABLED

    if i == 0 and figure == "first figure":
        work_place.create_line(xyz(lx, ly, lz), xyz(rx, ry, rz), width =2, fill = "cyan")
        work_place.create_line(xyz(ux, uy, uz), xyz(bx, by, bz), width =2, fill = "darkslateblue")
    
    if i == 0 and figure == "second figure":
        work_place.create_line(xyz(lx, ly, lz), xyz(rx, ry, rz), width =2, fill = "orange")
        work_place.create_line(xyz(ux, uy, uz), xyz(bx, by, bz), width =2, fill = "red")
    i+=1
    if i <=140 and figure == "first figure": #смещение на 140 по Z
        first["state"] = DISABLED
        work_place.delete('hor1')
        work_place.delete('ver1')
        horisontal = work_place.create_line(xyz(lx, ly, lz+1), xyz(rx, ry, rz+1), width =2, fill = "cyan", tag="hor1")
        vertical = work_place.create_line(xyz(ux, uy, uz+1), xyz(bx, by, bz+1), width =2, fill = "darkslateblue", tag="ver1")
        
        work_place.after(25, lambda: Move120ByZ(i, lx, ly, lz+1, rx, ry, rz+1, ux, uy, uz+1, bx, by, bz+1, figure))
    
    if i <=140 and figure == "second figure": #смещение на 140 по Z
        work_place.delete('hor2')
        work_place.delete('ver2')
        horisontal_2 = work_place.create_line(xyz(lx, ly, lz+1), xyz(rx, ry, rz+1), width =2, fill = "orange", tag="hor2")
        vertical_2 = work_place.create_line(xyz(ux, uy, uz+1), xyz(bx, by, bz+1), width =2, fill = "red", tag="hor2")
        work_place.after(25, lambda: Move120ByZ(i, lx, ly, lz+1, rx, ry, rz+1, ux, uy, uz+1, bx, by, bz+1, figure))
    
    if i ==141 and figure == "first figure":
        first["state"] = NORMAL
        first["command"] = lambda: XAxisRotation(0, lx, ly, lz, rx, ry, rz, ux, uy, uz, bx, by, bz, figure)
    
    if i ==141 and figure == "second figure":
        first["state"] = NORMAL
        second.place_forget()

def Move60ByY(i, lx, ly, lz, rx, ry, rz, ux, uy, uz, bx, by, bz, figure):
    description.config(text='Смещение по X на 40 px')
    second["state"] = DISABLED

    if i == 0 and figure == "second figure":
        work_place.create_line(xyz(lx, ly, lz), xyz(rx, ry, rz), width =2, fill = "orange")
        work_place.create_line(xyz(ux, uy, uz), xyz(bx, by, bz), width =2, fill = "red")
    i+=1
    if i <=40 and figure == "first figure": 
        work_place.delete('hor1')
        work_place.delete('ver1')
        horisontal = work_place.create_line(xyz(lx+1, ly, lz), xyz(rx+1, ry, rz), width =2, fill = "cyan", tag="hor1")
        vertical = work_place.create_line(xyz(ux+1, uy, uz), xyz(bx+1, by, bz), width =2, fill = "darkslateblue", tag="ver1")
        work_place.after(25, lambda: Move60ByY(i, lx+1, ly, lz, rx+1, ry, rz, ux+1, uy, uz, bx+1, by, bz, figure))
    
    if i <=40 and figure == "second figure":
        work_place.delete('hor2')
        work_place.delete('ver2')
        horisontal_2 = work_place.create_line(xyz(lx+1, ly, lz), xyz(rx+1, ry, rz), width =2, fill = "orange", tag="hor2")
        vertical_2 = work_place.create_line(xyz(ux+1, uy, uz), xyz(bx+1, by, bz), width =2, fill = "red", tag="hor2")
        work_place.after(25, lambda: Move60ByY(i, lx+1, ly, lz, rx+1, ry, rz, ux+1, uy, uz, bx+1, by, bz, figure))

    if i==41 and figure == "first figure":
        first["state"] = NORMAL
        first["command"] = lambda: Move120ByZ(0, lx, ly, lz, rx, ry, rz, ux, uy, uz, bx, by, bz, figure)
    
    if i==41 and figure == "second figure":
        second["state"] = NORMAL
        second["command"] = lambda: XAxisRotation(0, int(lx), int(ly), int(lz), int(rx), int(ry), int(rz), int(ux), int(uy), int(uz), int(bx), int(by), int(bz), figure)

def FirstConversion():
    global lx, ly, lz, rx, ry, rz, ux, uy, uz, bx, by, bz
    second["state"] = DISABLED
    first["state"] = DISABLED
    first["text"] = "Далее"
    figure = "first figure"
    Move60ByY(0, lx, ly, lz, rx, ry, rz, ux, uy, uz, bx, by, bz, figure)

def SecondConversion():
    global lx, ly, lz, rx, ry, rz, ux, uy, uz, bx, by, bz
    second["state"] = DISABLED
    second["text"] = "Далее"
    first["state"] = DISABLED
    figure = "second figure"
    YAxisRotation(0, lx, ly, lz, rx, ry, rz, ux, uy, uz, bx, by, bz, figure)

center_point_x=400
center_point_y=400
DrawCoordinatesAxes(center_point_x, center_point_y)

description=Label(root_window, text='\nНАЧАЛЬНОЕ ПОЛОЖЕНИЕ\n',\
bg="lightgray", fg="black",font=("Courier New, bold", 12), justify = CENTER, bd=3)
description.place(relx=0.45, rely=0.01, relheight=0.08)

first = Button(root_window, text='Первый вариант', font=("Courier New, bold", 14), bd=3, command=FirstConversion)
first.place(relx=0.01, rely=0.01, relwidth=0.2, relheight=0.08)
second = Button(root_window, text='Второй вариант', font=("Courier New, bold", 14), bd=3, command=SecondConversion)
second.place(relx=0.21, rely=0.01, relwidth=0.2, relheight=0.08)

lx =250
lz =150
ly =0

rx =50
rz =150
ry =0

ux =150
uz =150
uy =0

bx =150
bz =50
by =0

work_place.create_line(xyz(lx, ly, lz), xyz(rx, ry, rz), width =3, fill = "lightgray")
work_place.create_line(xyz(ux, uy, uz), xyz(bx, by, bz), width =3, fill = "gray")
root_window.mainloop()
