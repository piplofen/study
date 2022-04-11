from tkinter import*

root = Tk()
root.iconbitmap('2.ico')
root.title("Lab2")
root.geometry('950x650')
root.resizable(width=False, height=False)
root.title('Учебные заведения')

v0 = IntVar() #Переменные переключения "флажков"
fontValue = IntVar() 
v1 = BooleanVar()
v2 = BooleanVar()

MyFont='Times 14'

def TNR_22():
    global MyFont
    MyFont='Times 24'
    My_Surname()
    
def TNR_20():
    global MyFont
    MyFont='Times 22'
    My_Surname()

def TNR_18():
    global MyFont
    MyFont='Times 20'
    My_Surname()
    
def TNR_16():
    global MyFont
    MyFont='Times 18'
    My_Surname()

def TNR_14():
    global MyFont
    MyFont='Times 14'
    My_Surname()

def inf_inst():
	panelFrame = Frame(root, height = 10000,width=10000)
	panelFrame.place(x = 0, y = 50)
	inf = ('В программе записаны учебные заведения, имеющиеся в Калиниградской области: \n1)КГТУ \n2)БФУ \n3)МФЮА \n4)КМРК \n5)КБК \n6)РУК \n7)Колледж предпринимательства \n8)РАНХиГС \n9)Лицей №23 \n10)КИУ \n11)Гимназия №40')
	inf_label = Label(text = inf,font = ("Times",16,"bold"))
	inf_label.place(x = 100, y = 100)

def inf_KGTU():
    global KGTU_image
    panelFrame = Frame(root, height = 10000,width=10000)
    panelFrame.place(x=0, y=50)
    Name_gull = Label(text = "КГТУ", font="Times 36")
    Name_gull.place(x=50, y=50)
    KGTU = 'В настоящее время КГТУ является одним из крупнейших высших учебных заведений отрасли рыбного хозяйства России. В университете осуществляется подготовка специалистов по 42 специальностям и направлениям высшего профессионального образования.'
    Info_bird_gull = Label(text = KGTU, wraplength = 250, justify = LEFT, font = 'Times 14')
    Info_bird_gull.place(x=50, y=100)
    KGTU_image = PhotoImage(file = "KGTU.gif")
    Image_KGTU = Label(root, image=KGTU_image , width=350, height=350)
    Image_KGTU.place(x=370, y=50)

def inf_BFU():
    global BFU_image
    panelFrame = Frame(root, height = 10000,width=10000)
    panelFrame.place(x=0, y=50)
    Name_gull = Label(text = "БФУ", font="Times 36")
    Name_gull.place(x=50, y=50)
    BFU = 'Один из ведущих вузов Калининградской области, один из девяти федеральных университетов России. До 2005 года назывался Калининградским государственным университетом (КГУ), затем, до 2011 года — Российским государственным университетом имени Иммануила Канта (РГУ им. И. Канта).'
    Info_bird_gull = Label(text = BFU, wraplength = 250, justify = LEFT, font = 'Times 14')
    Info_bird_gull.place(x=50, y=100)
    BFU_image = PhotoImage(file = "BFU.gif")
    Image_BFU = Label(root, image=BFU_image , width=350, height=350)
    Image_BFU.place(x=370, y=50)

def inf_MFUA():
    global MFUA_image
    panelFrame = Frame(root, height = 10000,width=10000)
    panelFrame.place(x=0, y=50)
    Name_gull = Label(text = "МФЮА", font="Times 36")
    Name_gull.place(x=50, y=50)
    MFUA = 'Московская финансово-юридическая академия (МФЮА) создана в 1995 году при поддержке правительства Москвы и Ассоциации международного образования. В 2010 году приказом Федеральной службы по надзору в сфере образования и науки МФЮА получила статус университета, подтверждающий значительные достижения в образовательной деятельности.'
    Info_bird_gull = Label(text =  MFUA, wraplength = 250, justify = LEFT, font = 'Times 14')
    Info_bird_gull.place(x=50, y=100)
    MFUA_image = PhotoImage(file = "MFUA.gif")
    Image_MFUA = Label(root, image=MFUA_image , width=550, height=500)
    Image_MFUA.place(x=370, y=50)

def inf_KMRK():
    global KMRK_image
    panelFrame = Frame(root, height = 10000,width=10000)
    panelFrame.place(x=0, y=50)
    Name_gull = Label(text = "КМРК", font="Times 36")
    Name_gull.place(x=50, y=50)
    KMRK = 'Калининградское высшее мореходное училище создано в 1966 году на основании Постановления Совета Министров СССР 30 апреля 1966 года № 330. Ректором университета назначен Волкогон Владимир Алексеевич. Приказом ректора университета начальником академии назначен Карпович Сергей Михайлович.'
    Info_bird_gull = Label(text = KMRK, wraplength = 250, justify = LEFT, font = 'Times 14')
    Info_bird_gull.place(x=50, y=100)
    KMRK_image = PhotoImage(file = "KMRK.gif")
    Image_KMRK = Label(root, image=KMRK_image , width=550, height=550)
    Image_KMRK.place(x=370, y=50)

def inf_KBK():
    global KBK_image
    panelFrame = Frame(root, height = 10000,width=10000)
    panelFrame.place(x=0, y=50)
    Name_gull = Label(text = "КБК", font="Times 36")
    Name_gull.place(x=50, y=50)
    KBK = 'Калининградский бизнес-колледж уже почти 20 лет готовит высококлассных специалистов по более чем 10 направлениям. С 2005 года образовательное учреждение выдаёт дипломы государственного образца. Колледж первым в Калининграде начал подготовку специалистов в области рекламы, земельно-имущественных отношений и дизайна. Многие выпускники колледжа сделали успешную карьеру и трудятся в различных отраслях экономики и культуры Калининградской области.'
    Info_bird_gull = Label(text = KBK, wraplength = 250, justify = LEFT, font = 'Times 14')
    Info_bird_gull.place(x=50, y=100)
    KBK_image = PhotoImage(file = "KBK.gif")
    Image_KBK = Label(root, image=KBK_image , width=550, height=550)
    Image_KBK.place(x=370, y=50)

def inf_RUK():
    global RUK_image
    panelFrame = Frame(root, height = 10000,width=10000)
    panelFrame.place(x=0, y=50)
    Name_gull = Label(text = "РУК", font="Times 36")
    Name_gull.place(x=50, y=50)
    RUK = 'Сегодня Российский университет кооперации, согласно рейтингу Министерства образования, входит в топ-10 экономических вузов России. Инновационные образовательные практики базируются на лучших традициях кооперативного образования, которое мы основали в 1918 году. Вуз пережил революцию, Великую отечественную войну, изменения экономического и политического режимов, реформы в образовании – и все это время был крупнейшим центром развития системы потребительской кооперации и отраслей экономики России.'
    Info_bird_gull = Label(text = RUK, wraplength = 250, justify = LEFT, font = 'Times 14')
    Info_bird_gull.place(x=50, y=100)
    RUK_image = PhotoImage(file = "919.gif")
    Image_RUK = Label(root, image=RUK_image , width=550, height=550)
    Image_RUK.place(x=370, y=50)

def inf_KP():
    global KP_image
    panelFrame = Frame(root, height = 10000,width=10000)
    panelFrame.place(x=0, y=50)
    Name_gull = Label(text = "Колледж предпринимательства", font="Times 36")
    Name_gull.place(x=50, y=50)
    KP = 'В соответствии с постановлением Совета министров РСФСР от 4 марта 1953 года № 272 на базе учебно-курсового комбината Управления местными торгами Калининградской области была создана школа торгово-кулинарного ученичества. 31 августа 1953 года утверждено Положение о школе, где указывалось, что во главе школы стоит директор, штат составляет преподавательский и инструкторский персонал. В школу принимались учащиеся после окончания 7 классов общеобразовательной школы со сдачей экзаменов и после окончания 8 и 9 классов – без экзаменов.'
    Info_bird_gull = Label(text = KP, wraplength = 250, justify = LEFT, font = 'Times 14')
    Info_bird_gull.place(x=50, y=100)
    KP_image = PhotoImage(file = "XXL.gif")
    Image_KP = Label(root, image=KP_image , width=550, height=450)
    Image_KP.place(x=370, y=150)

def inf_RANG():
    global RANG_image
    panelFrame = Frame(root, height = 10000,width=10000)
    panelFrame.place(x=0, y=50)
    Name_gull = Label(text = "РАНХиГС", font="Times 36")
    Name_gull.place(x=50, y=50)
    RANG = 'В Калининграде, столице самого западного края Российской Федерации, многие годы успешно работает ровесник области - наш Филиал. Образовательную деятельность Западный филиал РАНХиГС ведет еще с 1946 года. В год основания Калининградской области, в соответствии с Приказом Министерства торговли СССР от 01 ноября 1946 г. № 437, наше учебное заведение получило официальное название Калининградский техникум советской торговли, которое до 1992 года оставалось неизменным.'
    Info_bird_gull = Label(text = RANG, wraplength = 250, justify = LEFT, font = 'Times 14')
    Info_bird_gull.place(x=50, y=100)
    RANG_image = PhotoImage(file = "RANG.gif")
    Image_RANG = Label(root, image=RANG_image , width=550, height=550)
    Image_RANG.place(x=370, y=50)

def inf_u23():
    global u23_image
    panelFrame = Frame(root, height = 10000,width=10000)
    panelFrame.place(x=0, y=50)
    Name_gull = Label(text = "Лицей №23", font="Times 36")
    Name_gull.place(x=50, y=50)
    u23 = 'Семилетняя школа #23 открыта в 1949 году в здании бывшего анатомического музея Кенигсбергского университета на ул. Каменный Вал (ныне ул. генерала Галицкого). В 1949 году школа приняла первых 400 учеников. В 1952/1953 учебном году переименована в среднюю школу. В 1974 году в марте месяце школа переехала в новое здание по ул. Вагнера, 51. За истекшие 55 лет в школе получили образование более 4 тысяч выпускников, среди которых Дважды Герой Советского Союза, летчик-космонавт СССР Романенко Ю.В.; Заслуженная артистка России, солистка Калининградской филармонии Галина Мосолова'
    Info_bird_gull = Label(text = u23, wraplength = 250, justify = LEFT, font = 'Times 14')
    Info_bird_gull.place(x=50, y=100)
    u23_image = PhotoImage(file = "23.gif")
    Image_u23 = Label(root, image=u23_image , width=550, height=550)
    Image_u23.place(x=370, y=15)

def inf_KIU():
    global KIU_image
    panelFrame = Frame(root, height = 10000,width=10000)
    panelFrame.place(x=0, y=50)
    Name_gull = Label(text = "КИУ", font="Times 36")
    Name_gull.place(x=50, y=50)
    KIU = 'Дата создания образовательного учреждения - 25 мая 1989 года.Свидетельство о государственная регистрация образовательного учреждения от 08 августа 1996 года.В феврале 2010 года институт уже в третий раз успешно прошел государственную аккредитацию по специальностям высшего и среднего профессионального образования.'
    Info_bird_gull = Label(text = KIU, wraplength = 250, justify = LEFT, font = 'Times 14')
    Info_bird_gull.place(x=50, y=100)
    KIU_image = PhotoImage(file = "263.gif")
    Image_KIU = Label(root, image=KIU_image , width=550, height=550)
    Image_KIU.place(x=370, y=50)

def inf_u40():
    global u40_image
    panelFrame = Frame(root, height = 10000,width=10000)
    panelFrame.place(x=0, y=50)
    Name_gull = Label(text = "Гимназия №40", font="Times 36")
    Name_gull.place(x=50, y=50)
    u40 = 'МАОУ гимназия № 40 им. Ю. А. Гагарина появилась на карте образовательного пространства Калининградской области в 2005 г. Общеобразовательное учреждение обрело новый статус в год своего 45-летия (школа № 40 распахнула свои двери для первых учеников 1 сентября 1960 года).'
    Info_bird_gull = Label(text = u40, wraplength = 250, justify = LEFT, font = 'Times 14')
    Info_bird_gull.place(x=50, y=100)
    u40_image = PhotoImage(file = "40.gif")
    Image_u40 = Label(root, image=u40_image , width=550, height=550)
    Image_u40.place(x=370, y=50)

def inf_prog():
    panelFrame = Frame(root, height = 10000,width=10000)
    panelFrame.place(x=0, y=50)
    inf = Label(text = "В программе записаны учебные заведения Калининградской области. \nПрограмма может предоставить информацию о каждом заведении \nВывести(стрелочка вверх) или убрать(стрелочка вниз) фамилию разработчика.", font="Times 14", justify=CENTER)
    inf.place(x=200, y=150)

def My_Surname_Fire(event):
    global MyFont, v1, v2
    v1.set(True)
    v2.set(False)
    Info_student = 'Подковыров Даниил'
    Information_student = Entry(font = 'Times 14')
    Information_student.insert(0,Info_student)
    Information_student.bind("<Button-3>", popup)
    Information_student.place(x=500, y=20)

def Del_My_Surname_Fire(event):
    global v1, v2
    v1.set(False)
    v2.set(True)
    panelFrame = Frame(root, height = 37,width=500)
    panelFrame.place(x=500, y=20)

def My_Surname():
    global v1, v2
    v1.set(True)
    v2.set(False)
    panelFrame = Frame(root, height = 36,width=500)
    panelFrame.place(x=500, y=20)
    Info_student = 'Подковыров Даниил'
    Information_student = Entry(font = MyFont)
    Information_student.insert(0,Info_student)
    Information_student.bind("<Button-3>", popup)
    Information_student.place(x=500, y=20)

def Del_My_Surname():
    global v1, v2
    v1.set(False)
    v2.set(True)
    panelFrame = Frame(root, height = 37,width=500)
    panelFrame.place(x=500, y=20)

def popup(event):
    global x, y
    x = event.x
    y = event.y
    helpmenu2.post(event.x_root, event.y_root)

im0 = PhotoImage(file = 'asf.gif')
im1 = PhotoImage(file = 'asf1.gif')

mainmenu = Menu(root)
root.config(menu=mainmenu)

helpmenu = Menu(mainmenu, tearoff=0)
filemenu = Menu(mainmenu, tearoff=0)
helpmenu1 = Menu(mainmenu, tearoff=0)
helpmenu2 = Menu(mainmenu, tearoff=0)

filemenu.add_command(label="Список всех заведений", command = inf_inst)
filemenu.add_cascade(label="Информация по каждому заведению", menu = helpmenu)
filemenu.add_command(label="Выход", command = root.destroy)
mainmenu.add_cascade(label="Информация о заведениях", menu=filemenu)
mainmenu.add_cascade(label="Общая информация", menu=helpmenu1)

helpmenu.add_checkbutton(label="КГТУ", compound="left", command = inf_KGTU, variable = v0, onvalue=1, offvalue=0, image = im0)
helpmenu.add_checkbutton(label="БФУ", compound="left", command = inf_BFU, variable = v0, onvalue=2, offvalue=0, image = im1)
helpmenu.add_checkbutton(label="МФЮА", compound="left", command = inf_MFUA, variable = v0, onvalue=3, offvalue=0, image = im0)
helpmenu.add_checkbutton(label="КМРК", compound="left", command = inf_KMRK, variable = v0, onvalue=4, offvalue=0, image = im1)
helpmenu.add_checkbutton(label="КБК", compound="left", command = inf_KBK, variable = v0, onvalue=5, offvalue=0, image = im0)
helpmenu.add_checkbutton(label="РУК", compound="left", command = inf_RUK, variable = v0, onvalue=6, offvalue=0, image = im1)
helpmenu.add_checkbutton(label="Колледж предпринимательства", compound="left", command = inf_KP, variable = v0, onvalue=7, offvalue=0, image = im0)
helpmenu.add_checkbutton(label="РАНХиГС", compound="left", command = inf_RANG, variable = v0, onvalue=8, offvalue=0, image = im1)
helpmenu.add_checkbutton(label="Лицей №23", compound="left", command = inf_u23, variable = v0, onvalue=9, offvalue=0, image = im0)
helpmenu.add_checkbutton(label="КИУ", compound="left", command = inf_KIU, variable = v0, onvalue=1, offvalue=10, image = im1)
helpmenu.add_checkbutton(label="Гимназия №40", compound="left", command = inf_u40, variable = v0, onvalue=11, offvalue=0, image = im0)

helpmenu1.add_command(label = 'Информация о программе', command = inf_prog)
helpmenu1.add_checkbutton(label = 'Вывести фамилию(Стрелочка вверх)', variable = v1, command=My_Surname)
helpmenu1.add_checkbutton(label = 'Убрать фамилию(Стрелочка вниз)', variable = v2, command=Del_My_Surname)
helpmenu2.add_checkbutton(label="Times New Roman 24", variable = fontValue, onvalue = 1, offvalue=0, command=TNR_22)
helpmenu2.add_checkbutton(label="Times New Roman 22", variable = fontValue, onvalue = 2, offvalue=0, command=TNR_20)
helpmenu2.add_checkbutton(label="Times New Roman 20", variable = fontValue, onvalue = 3, offvalue=0, command=TNR_18)
helpmenu2.add_checkbutton(label="Times New Roman 18", variable = fontValue, onvalue = 4, offvalue=0, command=TNR_16)
helpmenu2.add_checkbutton(label="Times New Roman 14", variable = fontValue, onvalue = 0, offvalue=0, command=TNR_14)

root.bind("<Up>", My_Surname_Fire)
root.bind("<Down>", Del_My_Surname_Fire)

root.mainloop()