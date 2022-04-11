from tkinter import *
from math import *

root_window = Tk()
root_window.geometry('800x750+200+50')
work_place = Canvas(root_window, bg="white", width=600, height=600)
work_place.place(relx=0, rely=0.1, relwidth=1, relheight=0.9)


def DrawCoordinatesAxes(center_point_x, center_point_y):
    long_of_coordinates = 315
    work_place.create_text(center_point_x - 5, center_point_y + 12, text="0", font=("Courier New", 12),
                           justify=CENTER)  # центр координат

    axis_z = work_place.create_line(center_point_x, center_point_y, center_point_x,
                                    center_point_y - long_of_coordinates, width=1, arrow=LAST)  # ось Z
    z_pointer = work_place.create_text(center_point_x, center_point_y - long_of_coordinates - 15, text="Z",
                                       font=("Courier New", 10), justify=CENTER)

    for i in range(1, 7):  # подписи ось Z
        work_place.create_line(center_point_x - 5, center_point_y - i * 50, center_point_x + 5, center_point_y - i * 50,
                               width=1)
        work_place.create_text(center_point_x - 20, center_point_y - i * 50, text=str(i * 50), font=("Courier New", 10),
                               justify=CENTER)

    angle_y = (30 * 0.01745)  # ось Y
    Y_axis_x = center_point_x + (long_of_coordinates) * cos(angle_y)
    Y_axis_y = center_point_y + (long_of_coordinates) * sin(angle_y)
    axis_y = work_place.create_line(center_point_x, center_point_y, Y_axis_x, Y_axis_y, width=1, arrow=LAST)
    y_pointer = work_place.create_text(Y_axis_x + 15, Y_axis_y, text="Y", font=("Courier New", 10), justify=CENTER)

    for i in range(1, 13):  # подписи ось Y
        work_place.create_line(center_point_x + 0.5 * i * 50 * cos(angle_y),
                               (center_point_y - 5 + 0.5 * i * 50 * sin(angle_y)),
                               center_point_x + 0.5 * i * 50 * cos(angle_y),
                               (center_point_y + 5 + 0.5 * i * 50 * sin(angle_y)), width=1)
        work_place.create_text(center_point_x + 0.5 * i * 50 * cos(angle_y),
                               (center_point_y + 5 + 0.5 * i * 50 * sin(angle_y)) + 15, text=str(i * 50),
                               font=("Courier New", 9), justify=CENTER)

    angle_x = (150 * 0.01745)  # ось X
    X_axis_x = center_point_x + (long_of_coordinates) * cos(angle_x)
    X_axis_y = center_point_y + (long_of_coordinates) * sin(angle_x)
    axis_x = work_place.create_line(center_point_x, center_point_y, X_axis_x, X_axis_y, width=1, arrow=LAST)
    x_pointer = work_place.create_text(X_axis_x - 15, X_axis_y, text="X", font=("Courier New", 10), justify=CENTER)

    for i in range(1, 7):  # подписи ось X
        work_place.create_line(center_point_x + i * 50 * cos(angle_x), center_point_y - 5 + i * 50 * sin(angle_x),
                               center_point_x + i * 50 * cos(angle_x), center_point_y + 5 + i * 50 * sin(angle_x),
                               width=1)
        work_place.create_text(center_point_x + i * 50 * cos(angle_x), center_point_y + 5 + i * 50 * sin(angle_x) + 15,
                               text=str(i * 50), font=("Courier New", 10), justify=CENTER)


# функция преобразовывает три получаемые локальные координаты в мировые
def xyz(true_x, true_y, true_z):
    global center_point_y, center_point_x
    Mx2 = center_point_x + cos(30 * pi / 180) * true_y - true_x * cos(30 * pi / 180)
    My2 = center_point_y - true_z + (true_y * sin(30 * pi / 180) + true_x * sin(30 * pi / 180))
    return int(Mx2), int(My2)


def Move60ByY(i, lx, ly, lz, rx, ry, rz, ux, uy, uz, bx, by, bz, dz):
    global center_point_x, center_point_y
    i += 1

    if i <= 360:  # смещение на -120 по Y
        first["state"] = DISABLED
        work_place.delete("all")
        if bz >= 0:
            DrawCoordinatesAxes(center_point_x, center_point_y)

        lz += 1/2
        rz += 1/2
        uz += 1/2
        bz += 1/2

        #if i >= 180:
            #dz -= 1/2

        alpha = -(pi / 180)
        rot_bx = cos(alpha)*bx - sin(alpha)*by
        rot_by = sin(alpha)*bx +cos(alpha)*by
        rot_bz = bz
        #rot_by = (cos(alpha) * (y) - sin(alpha) * (bz))
        #rot_bz = (by) * sin(alpha) + (bz) * cos(alpha)

        rot_rx = cos(alpha)*rx - sin(alpha)*ry
        rot_ry = sin(alpha)*rx +cos(alpha)*ry
        rot_rz = rz

        #rot_rx = rx
        #rot_ry = (cos(alpha) * (ry) - sin(alpha) * (rz))
        #rot_rz = (ry) * sin(alpha) + (rz) * cos(alpha)


        true_z = rot_bz - dz
        tr_z = rz - dz
        Mx2 = center_point_x + cos(30 * pi / 180) * rot_by - rot_bx * cos(30 * pi / 180)
        My2 = center_point_y - true_z + (rot_by * sin(30 * pi / 180) + rot_bx * sin(30 * pi / 180))

        Mx3 = center_point_x + cos(30 * pi / 180) * rot_ry - rot_rx * cos(30 * pi / 180)
        My3 = center_point_y - true_z + (rot_ry * sin(30 * pi / 180) + rot_rx * sin(30 * pi / 180))
        x, y = xyz(rx, ry, tr_z)
        if My2 >= y - 20 and My2 <= y + 20:
            vertical = work_place.create_line(xyz(ux, uy, uz), Mx2, My2, width=5, fill="red", tag="ver1")
            horisontal = work_place.create_line(xyz(lx, ly, lz), Mx3, My3, width=5, fill="cyan", tag="hor1")
        else:
            horisontal = work_place.create_line(xyz(lx, ly, lz), Mx3, My3, width=5, fill="cyan", tag="hor1")
            vertical = work_place.create_line(xyz(ux, uy, uz), Mx2, My2, width=5, fill="red", tag="ver1")

        if bz < 0:
            DrawCoordinatesAxes(center_point_x, center_point_y)

        work_place.after(25, lambda: Move60ByY(i, lx, ly, lz, rot_rx, rot_ry, rot_rz, ux, uy, uz, rot_bx, rot_by, rot_bz, dz))
    if i == 361:
        first["state"] = NORMAL

def FirstConversion():
    global lx, ly, lz, rx, ry, rz, ux, uy, uz, bx, by, bz
    Move60ByY(0, lx, ly, lz, rx, ry, rz, ux, uy, uz, bx, by, bz, 0)


center_point_x = 400
center_point_y = 400
DrawCoordinatesAxes(center_point_x, center_point_y)

description = Label(root_window,
                    text='\nВторая линия совершает полный оборот вокруг оси X\nВсе изображение сдвигается по оси Y на -120px\n', \
                    bg="lightgray", fg="black", font=("Courier New, bold", 12), justify=CENTER, bd=3)
description.place(relx=0.25, rely=0.01, relheight=0.08)

first = Button(root_window, text='Начать\nпреобразование', font=("Courier New, bold", 14), bd=3,
               command=FirstConversion)
first.place(relx=0.01, rely=0.01, relwidth=0.2, relheight=0.08)

lx = 0
lz = 0
ly = 0

rx = 100
rz = 0
ry = 0

ux = 0
uz = 0
uy = 0

bx = 0
bz = 0
by = 90

horisontal = work_place.create_line(xyz(lx, ly, lz), xyz(rx, ry, rz), width=5, fill="cyan", tag="hor1")
vertical = work_place.create_line(xyz(ux, uy, uz), xyz(bx, by, bz), width=5, fill="red", tag="ver1")
root_window.mainloop()
