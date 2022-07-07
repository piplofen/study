'''
Информационная система "Кафедра": план кафедры с указаниеме компьютерных классов.
Указание номера пары показывает, в каких классах идут занятия и в какой группе.
Два вида пользователей: администратор с возможностью редактирования и пользователь.
'''
from tkinter import*
from tkinter import messagebox as mb
from tkinter import ttk
import random
import datetime

root = Tk()
root.title("Выбор пользователя")
root.resizable(False, False)
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 125
h = h - 50
root.geometry('250x150+{}+{}'.format(w, h))

file_plan = 'plan.gif'

less1 = IntVar()
less2 = IntVar()

k = 0
check = 0

x = 0
y = 0

cab_list = ['Кабинет №1', 'Кабинет №2', 'Кабинет №3', 'Кабинет №4', 
			'Кабинет №5', 'Кабинет №6', 'Кабинет №7', 'Кабинет №8', 
			'Кабинет №9', 'Кабинет №10', 'Кабинет №11', 'Кабинет №12', 
			'Кабинет №13', 'Кабинет №14']

group_list = ['20ВТ1', '20ВТ2', '19ВТ1', '19ВТ2', '18ВТ', '17ВТ', '20ИЭ1',
			'20ИЭ2', '19ИЭ1', '19ИЭ2', '18ИЭ', '17ИЭ', '20АП1', '20АП2']

para11 = ['Кабинет №12', 'Кабинет №2', 'Кабинет №6', 'Кабинет №1']
group11 = random.sample(group_list, 4)
para12 = ['Кабинет №3', 'Кабинет №5', 'Кабинет №12', 'Кабинет №14']
group12 = random.sample(group_list, 4)
para13 = ['Кабинет №6', 'Кабинет №8', 'Кабинет №7', 'Кабинет №14']
group13 = random.sample(group_list, 4)
para14 = ['Кабинет №11', 'Кабинет №4', 'Кабинет №3', 'Кабинет №8']
group14 = random.sample(group_list, 4)
para15 = ['Кабинет №3', 'Кабинет №8', 'Кабинет №9', 'Кабинет №4']
group15 = random.sample(group_list, 4)
para16 = ['Кабинет №3', 'Кабинет №10', 'Кабинет №4', 'Кабинет №8']
group16 = random.sample(group_list, 4)

para21 = ['Кабинет №3', 'Кабинет №12', 'Кабинет №4', 'Кабинет №14']
group21 = random.sample(group_list, 4)
para22 = ['Кабинет №12', 'Кабинет №1', 'Кабинет №7', 'Кабинет №3']
group22 = random.sample(group_list, 4)
para23 = ['Кабинет №1', 'Кабинет №9', 'Кабинет №5', 'Кабинет №10']
group23 = random.sample(group_list, 4)
para24 = ['Кабинет №9', 'Кабинет №1', 'Кабинет №8', 'Кабинет №4']
group24 = random.sample(group_list, 4)
para25 = ['Кабинет №10', 'Кабинет №12', 'Кабинет №9', 'Кабинет №1']
group25 = random.sample(group_list, 4)
para26 = ['Кабинет №10', 'Кабинет №7', 'Кабинет №6', 'Кабинет №8']
group26 = random.sample(group_list, 4)

para11copy = []
para12copy = []
para13copy = []
para14copy = []
para15copy = []
para16copy = []

para21copy = []
para22copy = []
para23copy = []
para24copy = []
para25copy = []
para26copy = []

some_para = []
some_para1 = []
some_group2 = []
some_group4 = []
some_cab2 = []
cabinet = []

style = ttk.Style()
style.configure('TButton', font = "Times, 12")
style.configure('TLabel', font = "Times, 10")
style.map('TButton', background = [("active", "pink")])

#функция отслеживания мышки
def popup(event):
	global x, y
	x = event.x
	y = event.y
	menu.post(event.x_root, event.y_root)
	print(x,y)

#функция маски ввода для entry1
def mask1(event):
	global entry1
	entry1.destroy()
	entry1 = ttk.Entry(frame_for_admin, width = 25, font = "Times, 12", show = "*")
	entry1.place(x = 10, y = 2)
	entry1.focus()

#функция маски ввода для entry2
def mask2(event):
	global entry2
	entry2.destroy()
	entry2 = ttk.Entry(frame_for_admin, width = 25, font = "Times, 12", show = "*")
	entry2.place(x = 10, y = 30)
	entry2.focus()

#функция проверки ввода пароля
def verify():
	if entry1.get() == password:
		if entry2.get() == password:
			window_admin()
		else:
			mb.showerror("Ошибка", 'Пароль не совпадает')
	else:
		mb.showerror("Ошибка", 'Пароль не совпадает')

def view(cabinet):
	root5 = Toplevel()
	root5.title("Расписание для кабинета")
	w = root5.winfo_screenwidth()
	h = root5.winfo_screenheight()
	w = w//2
	h = h//2
	w = w - 770
	h = h - 325
	root5.geometry('330x340+{}+{}'.format(w, h))
	label_for_cab = ttk.Label(root5, text = "Расписание для " + cabinet + ".") 
	label_for_cab.pack(side = TOP)
	label = ttk.Label(root5)
	label.place(x = 25, y = 50)
	btttn_close = ttk.Button(root5, text = "Закрыть", command = root5.destroy)
	btttn_close.pack(side = BOTTOM)

	for i in range(len(para11)):
		if cabinet == para11[i]:
			index_for_para11 = para11.index(cabinet)
			group_for_para11 = group11[index_for_para11]
			label["text"] = para11[i] + ', ' + group11[index_for_para11] + ', 1 пара' ', 1 неделя' + "\n" + label["text"]
	for i in range(len(para12)):
		if cabinet == para12[i]:
			index_for_para12 = para12.index(cabinet)
			group_for_para12 = group12[index_for_para12]
			label["text"] = para12[i] + ', ' + group12[index_for_para12] + ', 2 пара' + ', 1 неделя' + "\n" + label["text"]
	for i in range(len(para13)):
		if cabinet == para13[i]:
			index_for_para13 = para13.index(cabinet)
			group_for_para13 = group13[index_for_para13]
			label["text"] = para13[i] + ', ' + group13[index_for_para13] + ', 3 пара' + ', 1 неделя' + "\n" + label["text"]
	for i in range(len(para14)):
		if cabinet == para14[i]:
			index_for_para14 = para14.index(cabinet)
			group_for_para14 = group14[index_for_para14]
			label["text"] = para14[i] + ', ' + group14[index_for_para14] + ', 4 пара' + ', 1 неделя' + "\n" + label["text"]
	for i in range(len(para15)):
		if cabinet == para15[i]:
			index_for_para15 = para15.index(cabinet)
			group_for_para15 = group15[index_for_para15]
			label["text"] = para15[i] + ', ' + group15[index_for_para15] + ', 5 пара' + ', 1 неделя' + "\n" + label["text"]
	for i in range(len(para16)):
		if cabinet == para16[i]:
			index_for_para16 = para16.index(cabinet)
			group_for_para16 = group16[index_for_para16]
			label["text"] = para16[i] + ', ' + group16[index_for_para16] + ', 6 пара' + ', 1 неделя' + "\n" + label["text"]

	for i in range(len(para21)):
		if cabinet == para21[i]:
			index_for_para21 = para21.index(cabinet)
			group_for_para21 = group21[index_for_para21]
			label["text"] = para21[i] + ', ' + group21[index_for_para21] + ', 1 пара' ', 2 неделя' + "\n" + label["text"]
	for i in range(len(para22)):
		if cabinet == para22[i]:
			index_for_para22 = para22.index(cabinet)
			group_for_para22 = group22[index_for_para22]
			label["text"] = para22[i] + ', ' + group22[index_for_para22] + ', 2 пара' + ', 2 неделя' + "\n" + label["text"]
	for i in range(len(para23)):
		if cabinet == para23[i]:
			index_for_para23 = para23.index(cabinet)
			group_for_para23 = group23[index_for_para23]
			label["text"] = para23[i] + ', ' + group23[index_for_para23] + ', 3 пара' + ', 2 неделя' + "\n" + label["text"]
	for i in range(len(para24)):
		if cabinet == para24[i]:
			index_for_para24 = para24.index(cabinet)
			group_for_para24 = group24[index_for_para24]
			label["text"] = para24[i] + ', ' + group24[index_for_para24] + ', 4 пара' + ', 2 неделя' + "\n" + label["text"]
	for i in range(len(para25)):
		if cabinet == para25[i]:
			index_for_para25 = para25.index(cabinet)
			group_for_para25 = group25[index_for_para25]
			label["text"] = para25[i] + ', ' + group25[index_for_para25] + ', 5 пара' + ', 2 неделя' + "\n" + label["text"]
	for i in range(len(para26)):
		if cabinet == para26[i]:
			index_for_para26 = para26.index(cabinet)
			group_for_para26 = group26[index_for_para26]
			label["text"] = para26[i] + ', ' + group26[index_for_para26] + ', 6 пара' + ', 2 неделя' + "\n" + label["text"]

def trace():
	global x, y
	case_cab = 0
	if x >= 75 and x <= 120 and y <= 210 and y >= 165:
		case_cab = 'Кабинет №1'
		view(case_cab)
	if x >= 15 and x <= 45 and y <= 210 and y >= 165:
		case_cab = 'Кабинет №2'
		view(case_cab)
	if x >= 15 and x <= 45 and y <= 245 and y >= 210:
		case_cab = 'Кабинет №3'
		view(case_cab)
	if x >= 15 and x <= 60 and y <= 285 and y >= 245:
		case_cab = 'Кабинет №4'
		view(case_cab)
	if x >= 60 and x <= 100 and y <= 285 and y >= 245:
		case_cab = 'Кабинет №5'
		view(case_cab)
	if x >= 103 and x <= 155 and y <= 285 and y >= 245:
		case_cab = 'Кабинет №6'
		view(case_cab)
	if x >= 160 and x <= 200 and y <= 285 and y >= 245:
		case_cab = 'Кабинет №7'
		view(case_cab)
	if x >= 205 and x <= 280 and y <= 285 and y >= 245:
		case_cab = 'Кабинет №8'
		view(case_cab)
	if x >= 315 and x <= 335 and y <= 285 and y >= 245:
		case_cab = 'Кабинет №9'
		view(case_cab)
	if x >= 340 and x <= 377 and y <= 285 and y >= 245:
		case_cab = 'Кабинет №10'
		view(case_cab)
	if x >= 380 and x <= 407 and y <= 285 and y >= 245:
		case_cab = 'Кабинет №11'
		view(case_cab)
	if x >= 415 and x <= 452 and y <= 285 and y >= 245:
		case_cab = 'Кабинет №12'
		view(case_cab)
	if x >= 342 and x <= 394 and y <= 210 and y >= 165:
		case_cab = 'Кабинет №13'
		view(case_cab)
	if x >= 257 and x <= 310 and y <= 210 and y >= 165:
		case_cab = 'Кабинет №14'
		view(case_cab)

#функция просмотра кабинетов
def cab(*args):
	global canv
	lbl_inf = Label(frame2, justify = LEFT)
	lbl_inf.place(x = 0, y = 0)
	lbl_inf['text'] = ' '
	choice_cab = []
	canv.delete('cab1','cab2','cab3','cab4','cab5','cab6','cab7','cab8','cab9','cab10','cab11','cab12','cab13','cab14')
	
	if combobox_for_week.get() == "1 неделя":
		if less1.get() == 1:
			choice_cab = para11
			choice_group = group11
		elif less1.get() == 2:
			choice_cab = para12
			choice_group = group12
		elif less1.get() == 3:
			choice_cab = para13
			choice_group = group13
		elif less1.get() == 4:
			choice_cab = para14
			choice_group = group14
		elif less1.get() == 5:
			choice_cab = para15
			choice_group = group15
		elif less1.get() == 6:
			choice_cab = para16
			choice_group = group16

	if combobox_for_week.get() == "2 неделя":
		if less2.get() == 1:
			choice_cab = para21
			choice_group = group21
		elif less2.get() == 2:
			choice_cab = para22
			choice_group = group22
		elif less2.get() == 3:
			choice_cab = para23
			choice_group = group23
		elif less2.get() == 4:
			choice_cab = para24
			choice_group = group24
		elif less2.get() == 5:
			choice_cab = para25
			choice_group = group25
		elif less2.get() == 6:
			choice_cab = para26
			choice_group = group26

	for i in range(len(choice_cab)):
		if choice_cab[i] == 'Кабинет №1':
			canv.delete('cab1text')
			canv.create_rectangle(77, 169, 116, 207, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab1')
			canv.create_text(97, 188, text = 'Кабинет\n    №1', font = 'Times 7', tag = 'cab1text')
			lbl_inf['text'] = 'Кабинет №1 группа: ' + choice_group[i] + "\n" + lbl_inf['text']
		if choice_cab[i] == 'Кабинет №2':
			canv.delete('cab2text')
			canv.create_rectangle(15, 169, 42, 207, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab2')
			canv.create_text(28, 188, text = 'Кабинет\n    №2', font = 'Times 7', tag = 'cab2text')
			lbl_inf['text'] = 'Кабинет №2 группа: ' + choice_group[i] + "\n" + lbl_inf['text']
		if choice_cab[i] == 'Кабинет №3':
			canv.delete('cab3text')
			canv.create_rectangle(15, 211, 42, 241, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab3')
			canv.create_text(28, 228, text = 'Кабинет\n    №3', font = 'Times 7', tag = 'cab3text')
			lbl_inf['text'] = 'Кабинет №3 группа: ' + choice_group[i] + "\n" + lbl_inf['text']
		if choice_cab[i] == 'Кабинет №4':
			canv.delete('cab4text')
			canv.create_rectangle(15, 245, 56, 282, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab4')
			canv.create_text(35, 265, text = 'Кабинет\n    №4', font = 'Times 7', tag = 'cab4text')
			lbl_inf['text'] = 'Кабинет №4 группа: ' + choice_group[i] + "\n" + lbl_inf['text']
		if choice_cab[i] == 'Кабинет №5':
			canv.delete('cab5text')
			canv.create_rectangle(63, 245, 98, 282, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab5')
			canv.create_text(82, 265, text = 'Кабинет\n    №5', font = 'Times 7', tag = 'cab5text')
			lbl_inf['text'] = 'Кабинет №5 группа: ' + choice_group[i] + "\n" + lbl_inf['text']
		if choice_cab[i] == 'Кабинет №6':
			canv.delete('cab6text')
			canv.create_rectangle(105, 245, 153, 282, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab6')
			canv.create_text(128, 265, text = 'Кабинет\n    №6', font = 'Times 7', tag = 'cab6text')
			lbl_inf['text'] = 'Кабинет №6 группа: ' + choice_group[i] + "\n" + lbl_inf['text']
		if choice_cab[i] == 'Кабинет №7':
			canv.delete('cab7text')
			canv.create_rectangle(160, 245, 196, 282, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab7')
			canv.create_text(178, 265, text = 'Кабинет\n    №7', font = 'Times 7', tag = 'cab7text')
			lbl_inf['text'] = 'Кабинет №7 группа: ' + choice_group[i] + "\n" + lbl_inf['text']
		if choice_cab[i] == 'Кабинет №8':
			canv.delete('cab8text')
			canv.create_rectangle(202, 245, 281, 282, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab8')
			canv.create_text(240, 265, text = 'Кабинет\n    №8', font = 'Times 7', tag = 'cab8text')
			lbl_inf['text'] = 'Кабинет №8 группа: ' + choice_group[i] + "\n" + lbl_inf['text']
		if choice_cab[i] == 'Кабинет №9':
			canv.delete('cab9text')
			canv.create_rectangle(316, 245, 334, 282, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab9')
			canv.create_text(326, 265, text = 'Кабинет\n    №9', font = 'Times 7', tag = 'cab9text')
			lbl_inf['text'] = 'Кабинет №9 группа: ' + choice_group[i] + "\n" + lbl_inf['text']
		if choice_cab[i] == 'Кабинет №10':
			canv.delete('cab10text')
			canv.create_rectangle(342, 245, 372, 282, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab10')
			canv.create_text(356, 265, text = 'Кабинет\n    №10', font = 'Times 7', tag = 'cab10text')
			lbl_inf['text'] = 'Кабинет №10 группа: ' + choice_group[i] + "\n" + lbl_inf['text']
		if choice_cab[i] == 'Кабинет №11':
			canv.delete('cab11text')
			canv.create_rectangle(379, 245, 406, 282, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab11')
			canv.create_text(394, 265, text = 'Кабинет\n    №11', font = 'Times 7', tag = 'cab11text')
			lbl_inf['text'] = 'Кабинет №11 группа: ' + choice_group[i] + "\n" + lbl_inf['text']
		if choice_cab[i] == 'Кабинет №12':
			canv.delete('cab12text')
			canv.create_rectangle(415, 245, 451, 282, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab12')
			canv.create_text(433, 265, text = 'Кабинет\n    №12', font = 'Times 7', tag = 'cab12text')
			lbl_inf['text'] = 'Кабинет №12 группа: ' + choice_group[i] + "\n" + lbl_inf['text']
		if choice_cab[i] == 'Кабинет №13':
			canv.delete('cab13text')
			canv.create_rectangle(342, 169, 390, 210, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab13')
			canv.create_text(368, 188, text = 'Кабинет\n    №13', font = 'Times 7', tag = 'cab13text')
			lbl_inf['text'] = 'Кабинет №13 группа: ' + choice_group[i] + "\n" + lbl_inf['text']
		if choice_cab[i] == 'Кабинет №14':
			canv.delete('cab14text')
			canv.create_rectangle(259, 169, 307, 210, width = 3, fill = 'coral1', outline = 'coral3', tag = 'cab14')
			canv.create_text(282, 188, text = 'Кабинет\n    №14', font = 'Times 7', tag = 'cab14text')
			lbl_inf['text'] = 'Кабинет №14 группа: ' + choice_group[i] + "\n" + lbl_inf['text']

#функция для разделения расписания на 1 и 2 недели
def week(event):
	if combobox_for_week.get() == "1 неделя":
		rb1 = ttk.Radiobutton(frame1, text = '1 пара', value = 1, variable = less1)
		rb1.place(x = 5, y = 10)
		rb1.bind('<Double-Button-1>', cab)
		rb2 = ttk.Radiobutton(frame1, text = '2 пара', value = 2, variable = less1)
		rb2.place(x = 85, y = 10)
		rb2.bind('<Double-Button-1>', cab)
		rb3 = ttk.Radiobutton(frame1, text = '3 пара', value = 3, variable = less1)
		rb3.place(x = 165, y = 10)
		rb3.bind('<Double-Button-1>', cab)
		rb4 = ttk.Radiobutton(frame1, text = '4 пара', value = 4, variable = less1)
		rb4.place(x = 5, y = 45)
		rb4.bind('<Double-Button-1>', cab)
		rb5 = ttk.Radiobutton(frame1, text = '5 пара', value = 5, variable = less1)
		rb5.place(x = 85, y = 45)
		rb5.bind('<Double-Button-1>', cab)
		rb6 = ttk.Radiobutton(frame1, text = '6 пара', value = 6, variable = less1)
		rb6.place(x = 165, y = 45)
		rb6.bind('<Double-Button-1>', cab)
	elif combobox_for_week.get() == "2 неделя":
		rb1 = ttk.Radiobutton(frame1, text = '1 пара', value = 1, variable = less2)
		rb1.place(x = 5, y = 10)
		rb1.bind('<Double-Button-1>', cab)
		rb2 = ttk.Radiobutton(frame1, text = '2 пара', value = 2, variable = less2)
		rb2.place(x = 85, y = 10)
		rb2.bind('<Double-Button-1>', cab)
		rb3 = ttk.Radiobutton(frame1, text = '3 пара', value = 3, variable = less2)
		rb3.place(x = 165, y = 10)
		rb3.bind('<Double-Button-1>', cab)
		rb4 = ttk.Radiobutton(frame1, text = '4 пара', value = 4, variable = less2)
		rb4.place(x = 5, y = 45)
		rb4.bind('<Double-Button-1>', cab)
		rb5 = ttk.Radiobutton(frame1, text = '5 пара', value = 5, variable = less2)
		rb5.place(x = 85, y = 45)
		rb5.bind('<Double-Button-1>', cab)
		rb6 = ttk.Radiobutton(frame1, text = '6 пара', value = 6, variable = less2)
		rb6.place(x = 165, y = 45)
		rb6.bind('<Double-Button-1>', cab)

#функция изменения кабинета и группы
def switch(event):
	global label_inf_pick_less2
	oldCab = cb1.get()
	newCab = cb2.get()
	newGroup = cb3.get()

	if newGroup == "Группа, на которую меняем":
		indexcab = some_para.index(oldCab)
		if newCab in some_para:
			mb.showerror("Ошибка!", "Попробуйте еще раз")
		elif (newCab not in some_para and newGroup not in some_group2):
			indexcab = some_para.index(oldCab)
			some_para.pop(indexcab)
			some_para.insert(indexcab, newCab)
			mb.showinfo("Успех!", 'Запись успешно изменена!')
			for x in range(len(some_para)):
				label_inf_pick_less2["text"] = some_para[x] + ", " + some_group2[x] + "\n" + label_inf_pick_less2["text"]
		cab()
	else:
		if newCab in some_para:
			mb.showerror("Ошибка!", "Попробуйте еще раз")
		elif (newCab not in some_para and newGroup not in some_group2):
			indexcab = some_para.index(oldCab)
			some_group2.pop(indexcab)
			some_para.pop(indexcab)
			some_group2.insert(indexcab, newGroup)
			some_para.insert(indexcab, newCab)
			mb.showinfo("Успех!", 'Запись успешно изменена!')
			for x in range(len(some_para)):
				label_inf_pick_less2["text"] = some_para[x] + ", " + some_group2[x] + "\n" + label_inf_pick_less2["text"]
		else:
			mb.showerror("Ошибка!", "Попробуйте еще раз")
		cab()

#функция построения окна изменения
def convert(some_less, some_group):
	global label_inf_pick_less1, root1, cb1, cb2, some_para, label_inf_pick_less2, some_group2, cb3
	label_inf_pick_less1["text"] = " "
	label_inf_pick_less2["text"] = " "
	for x in range(len(some_less)):
		label_inf_pick_less1["text"] = some_less[x] + ", " + some_group[x] + "\n" + label_inf_pick_less1["text"]
	cb1 = ttk.Combobox(root1, value = some_less)
	cb1.place(x = 330/2 - 150, y = 190)
	cb1.set("Кабинет, который нужно заменить")
	cb2 = ttk.Combobox(root1, value = cab_list)
	cb2.place(x = 330/2, y = 190)
	cb2.set("Кабинет, на который меняем")
	cb3 = ttk.Combobox(root1, value = group_list)
	cb3.place(x = 330/2 - 70, y = 220)
	cb3.set("Группа, на которую меняем")
	bttn_accept1 = ttk.Button(root1, text = "Подтвердить")
	bttn_accept1.place(x = 330/2 - 50, y = 250)
	bttn_accept1.bind("<Button-1>", switch)
	some_para = some_less
	some_group2 = some_group

#функция для распределения выбранной пары с текущей
def output_less(event):
	global label_inf_pick_less1
	if rbweek.get() == 1:
		if combobox_for_pick_less.get() == "1 пара":
			para11copy = para11
			convert(para11copy, group11)
		elif combobox_for_pick_less.get() == "2 пара":
			para12copy = para12
			convert(para12copy, group12)
		elif combobox_for_pick_less.get() == "3 пара":
			para13copy = para13
			convert(para13copy, group13)
		elif combobox_for_pick_less.get() == "4 пара":
			para14copy = para14
			convert(para14copy, group14)
		elif combobox_for_pick_less.get() == "5 пара":
			para15copy = para15
			convert(para15copy, group15)
		elif combobox_for_pick_less.get() == "6 пара":
			para16copy = para16
			convert(para16copy, group16)
	if rbweek.get() == 2:
		if combobox_for_pick_less.get() == "1 пара":
			para21copy = para21
			convert(para21copy, group21)
		elif combobox_for_pick_less.get() == "2 пара":
			para22copy = para22
			convert(para22copy, group22)
		elif combobox_for_pick_less.get() == "3 пара":
			para23copy = para23
			convert(para23copy, group23)
		elif combobox_for_pick_less.get() == "4 пара":
			para24copy = para24
			convert(para24copy, group24)
		elif combobox_for_pick_less.get() == "5 пара":
			para25copy = para25
			convert(para25copy, group25)
		elif combobox_for_pick_less.get() == "6 пара":
			para26copy = para26
			convert(para26copy, group26)

def root1_inf(event):
	mb.showinfo("Справочная информация", "Вы вошли в режим изменения кабинета и группы.\nДля того чтобы изменить запись вам нужно:\n   1) Выбрать неделю(двойным щелчком левой кнопки мыши).\n   2) Выбрать пару в выпадающем меню.\nПосле чего, указать какой кабинет меняем, на какой меняем и группу.\nСохранить изменения нажатием кнопки \"Подтвердить\".")

#функция построения окна изменения
def change_cab():
	global rbweek, combobox_for_pick_less, label_inf_pick_less1, root1, label_inf_pick_less2
	rbweek = IntVar()
	root1 = Toplevel()
	root1.title("Изменить кабинет")
	root1.resizable(False, False)
	oldframe = ttk.LabelFrame(root1, text = "Старый вариант", width = 150, height = 150)
	newframe = ttk.LabelFrame(root1, text = "Новый вариант", width = 150, height = 150)
	oldframe. place(x = 10, y = 30)
	newframe.place(x = 170, y = 30)
	w = root1.winfo_screenwidth()
	h = root1.winfo_screenheight()
	w = w//2
	h = h//2
	w = w - 465
	h = h - 52
	root1.geometry('330x355+{}+{}'.format(w, h))
	rb_for_week1 = ttk.Radiobutton(root1, text = "1 неделя", value = 1, variable = rbweek)
	rb_for_week1.place(x = 265/2 - 50, y = 10)
	rb_for_week2 = ttk.Radiobutton(root1, text = "2 неделя", value = 2, variable = rbweek)
	rb_for_week2.place(x = 265/2 + 50, y = 10)
	label_inf_pick_less1 = ttk.Label(oldframe)
	label_inf_pick_less1.place(x = 5, y = 5)
	label_inf_pick_less2 = ttk.Label(newframe)
	label_inf_pick_less2.place(x = 5, y = 5)
	combobox_for_pick_less = ttk.Combobox(root1, values = ["1 пара", "2 пара", "3 пара", "4 пара", "5 пара", "6 пара"], width = 18)
	combobox_for_pick_less.place(x = 330/2 - 55, y = 300)
	combobox_for_pick_less.set("Выберите пару")
	combobox_for_pick_less.bind("<<ComboboxSelected>>", output_less)
	btttn_inf = ttk.Button(root1, text = "Справочная информация")
	btttn_inf.place(x = 75, y = 323)
	btttn_inf.bind("<Button-1>", root1_inf)

#функция для добавления кабинета и группы
def add(event):
	global group11, label_inf_pick_less1, label_inf_pick_less2
	newCab = cb2.get()
	newGroup = cb1.get()
	label_inf_pick_less2["text"] = " "
	if newGroup == "Выберите группу":
		mb.showerror("Ошибка!", "Выберите группу!")
		return newGroup
	if newCab in some_para1 or newGroup in some_group1:
		mb.showerror("Ошибка!", "Попробуйте еще раз!")
	elif newCab not in some_para1 and newGroup not in some_group1:
		some_para1.append(newCab)
		some_group1.append(newGroup)
		for x in range(len(some_para1)):
			label_inf_pick_less2["text"] = some_para1[x] + ", " + some_group1[x] + "\n" + label_inf_pick_less2["text"]
		mb.showinfo("Успех!", 'Запись успешно добавлена!')
	#elif newGroup in 
		cab()

#функция построения окна добавления
def choice_cab_add1(some_cab, some_group):
	global some_para1, cb2, cb1, label_inf_pick_less1, label_inf_pick_less2, some_group1
	label_inf_pick_less1["text"] = " "
	label_inf_pick_less2["text"] = " "
	print(some_group)
	for x in range(len(some_cab)):
		label_inf_pick_less1["text"] = some_cab[x] + ", " + some_group[x] + "\n" + label_inf_pick_less1["text"]
	cb2 = ttk.Combobox(root2, value = cab_list)
	cb2.place(x = 330/2 - 150, y = 220)
	cb2.set("Выберите кабинет")
	cb1 = ttk.Combobox(root2, value = group_list)
	cb1.place(x = 330/2, y = 220)
	cb1.set("Выберите группу")
	bttn_accept2 = ttk.Button(root2, text = "Добавить")
	bttn_accept2.place(x = 330/2 - 50, y = 250)
	bttn_accept2.bind("<Button-1>", add)
	some_para1 = some_cab
	some_group1 = some_group

#функция для распределения выбранной пары с текущей
def choice_cab_add(event):
	if rbweek1.get() == 1:
		if cb_para.get() == "1 пара":
			para11copy = para11
			choice_cab_add1(para11copy, group11)
		elif cb_para.get() == "2 пара":
			para12copy = para12
			choice_cab_add1(para12copy, group12)
		elif cb_para.get() == "3 пара":
			para13copy = para13
			choice_cab_add1(para13copy, group13)
		elif cb_para.get() == "4 пара":
			para14copy = para14
			choice_cab_add1(para14copy, group14)
		elif cb_para.get() == "5 пара":
			para15copy = para15
			choice_cab_add1(para15copy, group15)
		elif cb_para.get() == "6 пара":
			para16copy = para16
			choice_cab_add1(para16copy, group16)
	elif rbweek1.get() == 2:
		if cb_para.get() == "1 пара":
			para21copy = para21
			choice_cab_add1(para21copy, group21)
		elif cb_para.get() == "2 пара":
			para22copy = para22
			choice_cab_add1(para22copy, group22)
		elif cb_para.get() == "3 пара":
			para23copy = para23
			choice_cab_add1(para23copy, group23)
		elif cb_para.get() == "4 пара":
			para24copy = para24
			choice_cab_add1(para24copy, group24)
		elif cb_para.get() == "5 пара":
			para25copy = para25
			choice_cab_add1(para25copy, group25)
		elif cb_para.get() == "6 пара":
			para26copy = para26
			choice_cab_add1(para26copy, group26)

def root2_inf(event):
	mb.showinfo("Справочная информация", "Вы вошли в режим добавления кабинета и группы!\nДля того чтобы добавить запись вам нужно:\n   1) Выбрать неделю(двойным щелчком левой кнопки мыши)\n   2) Выбрать пару в выпадающем меню\nПосле чего, указать кабинет и группу, которую хотите добавить и нажать на кнопку \"Добавить\".")

#функция построения окна добавления
def add_cab():
	global cb_para, rbweek1, label_inf_pick_less1, label_inf_pick_less2, root2
	rbweek1 = IntVar()
	root2 = Toplevel()
	root2.title("Добавить кабинет")
	root2.resizable(False, False)
	oldframe = ttk.LabelFrame(root2, text = "Старый вариант", width = 150, height = 175)
	newframe = ttk.LabelFrame(root2, text = "Новый вариант", width = 150, height = 175)
	oldframe. place(x = 10, y = 30)
	newframe.place(x = 170, y = 30)
	w = root2.winfo_screenwidth()
	h = root2.winfo_screenheight()
	w = w//2
	h = h//2
	w = w - 465
	h = h - 52
	root2.geometry('330x355+{}+{}'.format(w, h))
	label_inf_pick_less1 = ttk.Label(oldframe)
	label_inf_pick_less1.place(x = 5, y = 5)
	label_inf_pick_less2 = ttk.Label(newframe)
	label_inf_pick_less2.place(x = 5, y = 5)
	rb_for_week1 = ttk.Radiobutton(root2, text = "1 неделя", value = 1, variable = rbweek1)
	rb_for_week1.place(x = 265/2 - 50, y = 10)
	rb_for_week2 = ttk.Radiobutton(root2, text = "2 неделя", value = 2, variable = rbweek1)
	rb_for_week2.place(x = 265/2 + 50, y = 10)
	cb_para = ttk.Combobox(root2, values = ["1 пара", "2 пара", "3 пара", "4 пара", "5 пара", "6 пара"], width = 18)
	cb_para.set("Выберите пару")
	cb_para.place(x = 330/2 - 55, y = 300)
	cb_para.bind("<<ComboboxSelected>>", choice_cab_add)
	btttn_inf = ttk.Button(root2, text = "Справочная информация")
	btttn_inf.place(x = 75, y = 323)
	btttn_inf.bind("<Button-1>", root2_inf)

#функция для удаления кабинета и группы
def delete(event):
	global label_inf_pick_less2
	delCab = cb2.get()
	label_inf_pick_less2["text"] = " "
	if delCab in some_cab2:
		indexdelcab = some_cab2.index(delCab)
		some_cab2.pop(indexdelcab)
		some_group4.pop(indexdelcab)
		mb.showinfo("Успех!", 'Кабинет успешно удален!')
		cab()
	for i in range(len(some_cab2)):
		label_inf_pick_less2["text"] = some_cab2[i] + ", " + some_group4[i] + "\n" + label_inf_pick_less2["text"]

#функция построения окна удаления
def choice_cab_del1(some_cab1, some_group3):
	global some_cab2, cb2, label_inf_pick_less1, label_inf_pick_less2, some_group4
	label_inf_pick_less1["text"] = " "
	label_inf_pick_less2["text"] = " "
	print(some_group3)
	print(some_cab1)
	for x in range(len(some_cab1)):
		label_inf_pick_less1["text"] = some_cab1[x] + ", " + some_group3[x] + "\n" + label_inf_pick_less1["text"]
	cb2 = ttk.Combobox(root3, value = some_cab1)
	cb2.place(x = 350/2 - 150, y = 220)
	cb2.set("Выберите кабинет")
	bttn_accept2 = ttk.Button(root3, text = "Удалить")
	bttn_accept2.place(x = 350/2 + 10, y = 216)
	bttn_accept2.bind("<Button-1>", delete)
	some_group4 = some_group3
	some_cab2 = some_cab1

#функция для распределения выбранной пары с текущей
def choice_cab_del(event):
	if rbweek2.get() == 1:
		print("1 неделя")
		if cb_para.get() == "1 пара":
			print("1 пара")
			para11copy = para11
			choice_cab_del1(para11copy, group16)
		elif cb_para.get() == "2 пара":
			print("2 пара")
			para12copy = para12
			choice_cab_del1(para12copy, group12)
		elif cb_para.get() == "3 пара":
			print("3 пара")
			para13copy = para13
			choice_cab_del1(para13copy, group13)
		elif cb_para.get() == "4 пара":
			print("4 пара")
			para14copy = para14
			choice_cab_del1(para14copy, group14)
		elif cb_para.get() == "5 пара":
			print("5 пара")
			para15copy = para15
			choice_cab_del1(para15copy, group15)
		elif cb_para.get() == "6 пара":
			print("6 пара")
			para16copy = para16
			choice_cab_del1(para16copy, group16)
	elif rbweek2.get() == 2:
		print("2 неделя")
		if cb_para.get() == "1 пара":
			print("1 пара")
			para21copy = para21
			choice_cab_del1(para21copy, group21)
		elif cb_para.get() == "2 пара":
			print("2 пара")
			para22copy = para22
			choice_cab_del1(para22copy, group22)
		elif cb_para.get() == "3 пара":
			print("3 пара")
			para23copy = para23
			choice_cab_del1(para23copy, group23)
		elif cb_para.get() == "4 пара":
			print("4 пара")
			para24copy = para24
			choice_cab_del1(para24copy, group24)
		elif cb_para.get() == "5 пара":
			print("5 пара")
			para25copy = para25
			choice_cab_del1(para25copy, group25)
		elif cb_para.get() == "6 пара":
			print("6 пара")
			para26copy = para26
			choice_cab_del1(para26copy, group26)

def root5_inf(event):
	mb.showinfo("Справочная информация", "Вы вошли в режим удаления кабинета и группы!\nДля того чтобы удалить запись вам нужно:\n   1) Выбрать неделю(двойным щелчком левой кнопки мыши)\n   2) Выбрать пару в выпадающем меню\nПосле чего, указать кабинет, который хотите удалить и нажать на кнопку \"Удалить\".")

#функция построения окна удаления
def del_cab():
	global cb_para, rbweek2, label_inf_pick_less1, label_inf_pick_less2, root3
	rbweek2 = IntVar()
	root3 = Toplevel()
	root3.title("Удалить кабинет")
	root3.resizable(False, False)
	oldframe = ttk.LabelFrame(root3, text = "Старый вариант", width = 150, height = 175)
	newframe = ttk.LabelFrame(root3, text = "Новый вариант", width = 150, height = 175)
	oldframe. place(x = 10, y = 30)
	newframe.place(x = 170, y = 30)
	w = root3.winfo_screenwidth()
	h = root3.winfo_screenheight()
	w = w//2
	h = h//2
	w = w - 465
	h = h - 52
	root3.geometry('330x355+{}+{}'.format(w, h))
	label_inf_pick_less1 = ttk.Label(oldframe)
	label_inf_pick_less1.place(x = 5, y = 5)
	label_inf_pick_less2 = ttk.Label(newframe)
	label_inf_pick_less2.place(x = 5, y = 5)
	rb_for_week1 = ttk.Radiobutton(root3, text = "1 неделя", value = 1, variable = rbweek2)
	rb_for_week1.place(x = 265/2 - 50, y = 10)
	rb_for_week2 = ttk.Radiobutton(root3, text = "2 неделя", value = 2, variable = rbweek2)
	rb_for_week2.place(x = 265/2 + 50, y = 10)
	cb_para = ttk.Combobox(root3, values = ["1 пара", "2 пара", "3 пара", "4 пара", "5 пара", "6 пара"], width = 18)
	cb_para.set("Выберите пару")
	cb_para.place(x = 330/2 - 55, y = 300)
	cb_para.bind("<<ComboboxSelected>>", choice_cab_del)
	btttn_inf = ttk.Button(root3, text = "Справочная информация")
	btttn_inf.place(x = 75, y = 323)
	btttn_inf.bind("<Button-1>", root5_inf)

#функция для переноса кабинета и группы
def switchtc(event):
	global para11, group11, para12, group12, para13, group13, para14, group14, para15, group15, para16, group16, para21, group21, para22, group22, para23, group23, para24, group24, para25, group25, para26, group26
	if rbweek4.get() == 1:
		print("1 неделя")
		if cb_para.get() == "1 пара":
			para11 = para21
			group11 = group21
			para21 = some_cab4
			group21 = some_group6
			print(para21, group21)
			for i in range(len(para11)):
				label_inf_pick_less2["text"] = para11[i] + ", " + group11[i] + "\n" + label_inf_pick_less2["text"]
			cab()
		elif cb_para.get() == "2 пара":
			para12 = para22
			group12 = group22
			para22 = some_cab4
			group22 = some_group6
			for i in range(len(para12)):
				label_inf_pick_less2["text"] = para12[i] + ", " + group12[i] + "\n" + label_inf_pick_less2["text"]
			cab()
		elif cb_para.get() == "3 пара":
			para13 = para23
			group13 = group23
			para23 = some_cab4
			group23 = some_group6
			for i in range(len(para13)):
				label_inf_pick_less2["text"] = para13[i] + ", " + group13[i] + "\n" + label_inf_pick_less2["text"]
			cab()
		elif cb_para.get() == "4 пара":
			para14 = para24
			group14 = group24
			para24 = some_cab4
			group24 = some_group6
			for i in range(len(para14)):
				label_inf_pick_less2["text"] = para14[i] + ", " + group14[i] + "\n" + label_inf_pick_less2["text"]
			cab()
		elif cb_para.get() == "5 пара":
			para15 = para25
			group15 = group25
			para25 = some_cab4
			group25 = some_group6
			for i in range(len(para15)):
				label_inf_pick_less2["text"] = para15[i] + ", " + group15[i] + "\n" + label_inf_pick_less2["text"]
			cab()
		elif cb_para.get() == "6 пара":
			para16 = para26
			group16 = group26
			para26 = some_cab4
			group26 = some_group6
			for i in range(len(para16)):
				label_inf_pick_less2["text"] = para16[i] + ", " + group16[i] + "\n" + label_inf_pick_less2["text"]
			cab()
	elif rbweek4.get() == 2:
		print("2 неделя")
		if cb_para.get() == "1 пара":
			para21 = para11
			group21 = group11
			para11 = some_cab4
			group11 = some_group6
			for i in range(len(para21)):
				label_inf_pick_less2["text"] = para21[i] + ", " + group21[i] + "\n" + label_inf_pick_less2["text"]
			cab()
		elif cb_para.get() == "2 пара":
			para22 = para12
			group22 = group12
			para12 = some_cab4
			group12 = some_group6
			for i in range(len(para22)):
				label_inf_pick_less2["text"] = para22[i] + ", " + group22[i] + "\n" + label_inf_pick_less2["text"]
			cab()
		elif cb_para.get() == "3 пара":
			para23 = para13
			group23 = group13
			para13 = some_cab4
			group13 = some_group6
			for i in range(len(para23)):
				label_inf_pick_less2["text"] = para23[i] + ", " + group23[i] + "\n" + label_inf_pick_less2["text"]
			cab()
		elif cb_para.get() == "4 пара":
			para24 = para14
			group24 = group14
			para14 = some_cab4
			group14 = some_group6
			for i in range(len(para24)):
				label_inf_pick_less2["text"] = para24[i] + ", " + group24[i] + "\n" + label_inf_pick_less2["text"]
			cab()
		elif cb_para.get() == "5 пара":
			para25 = para15
			group25 = group15
			para15 = some_cab4
			group15 = some_group6
			for i in range(len(para25)):
				label_inf_pick_less2["text"] = para25[i] + ", " + group25[i] + "\n" + label_inf_pick_less2["text"]
			cab()
		elif cb_para.get() == "6 пара":
			para26 = para16
			group26 = group16
			para16 = some_cab4
			group16 = some_group6
			for i in range(len(para26)):
				label_inf_pick_less2["text"] = para26[i] + ", " + group26[i] + "\n" + label_inf_pick_less2["text"]
			cab()

#функция построения окна переноса пары
def choice_cab_switch(some_cab3, some_group5):
	global label_inf_pick_less1, label_inf_pick_less2, some_group6, some_cab4
	label_inf_pick_less1["text"] = " "
	label_inf_pick_less2["text"] = " "
	for x in range(len(some_cab3)):
		label_inf_pick_less1["text"] = some_cab3[x] + ", " + some_group5[x] + "\n" + label_inf_pick_less1["text"]
	bttn_accept3 = ttk.Button(root4, text = "Поменять")
	bttn_accept3.place(x = 350/2 - 60, y = 216)
	bttn_accept3.bind("<Button-1>", switchtc)
	some_group6 = some_group5
	some_cab4 = some_cab3

#функция для распределения выбранной пары с текущей
def choice_switch_del(event):
	if rbweek4.get() == 1:
		print("1 неделя")
		if cb_para.get() == "1 пара":
			print("1 пара")
			para11copy = para11
			choice_cab_switch(para11copy, group11)
		elif cb_para.get() == "2 пара":
			print("2 пара")
			para12copy = para12
			choice_cab_switch(para12copy, group12)
		elif cb_para.get() == "3 пара":
			print("3 пара")
			para13copy = para13
			choice_cab_switch(para13copy, group13)
		elif cb_para.get() == "4 пара":
			print("4 пара")
			para14copy = para14
			choice_cab_switch(para14copy, group14)
		elif cb_para.get() == "5 пара":
			print("5 пара")
			para15copy = para15
			choice_cab_switch(para15copy, group15)
		elif cb_para.get() == "6 пара":
			print("6 пара")
			para16copy = para16
			choice_cab_switch(para16copy, group16)
	elif rbweek4.get() == 2:
		print("2 неделя")
		if cb_para.get() == "1 пара":
			print("1 пара")
			para21copy = para21
			choice_cab_switch(para21copy, group21)
		elif cb_para.get() == "2 пара":
			print("2 пара")
			para22copy = para22
			choice_cab_switch(para22copy, group22)
		elif cb_para.get() == "3 пара":
			print("3 пара")
			para23copy = para23
			choice_cab_switch(para23copy, group23)
		elif cb_para.get() == "4 пара":
			print("4 пара")
			para24copy = para24
			choice_cab_switch(para24copy, group24)
		elif cb_para.get() == "5 пара":
			print("5 пара")
			para25copy = para25
			choice_cab_switch(para25copy, group25)
		elif cb_para.get() == "6 пара":
			print("6 пара")
			para26copy = para26
			choice_cab_switch(para26copy, group26)

def root4_inf(event):
	mb.showinfo("Справочная информация", "Вы вошли в режим переноса пар!\nДля того чтобы перенести запись вам нужно:\n   1) Выбрать с какой пары на какую неодходимо перенести пару(двойным щелчком левой кнопки мыши)\n   2) Выбрать пару в выпадающем меню\nПосле чего, нажимаем на кнопку \"Поменять\".")

#функция построения окна переноса пары
def switch_cab():
	global cb_para, rbweek4, label_inf_pick_less1, label_inf_pick_less2, root4
	rbweek4 = IntVar()
	root4 = Toplevel()
	root4.title("Перенести кабинет")
	root4.resizable(False, False)
	oldframe = ttk.LabelFrame(root4, text = "Старый вариант", width = 150, height = 175)
	newframe = ttk.LabelFrame(root4, text = "Новый вариант", width = 150, height = 175)
	oldframe. place(x = 10, y = 30)
	newframe.place(x = 170, y = 30)
	w = root4.winfo_screenwidth()
	h = root4.winfo_screenheight()
	w = w//2
	h = h//2
	w = w - 465
	h = h - 52
	root4.geometry('330x355+{}+{}'.format(w, h))
	label_inf_pick_less1 = ttk.Label(oldframe)
	label_inf_pick_less1.place(x = 5, y = 5)
	label_inf_pick_less2 = ttk.Label(newframe)
	label_inf_pick_less2.place(x = 5, y = 5)
	rb_for_week1 = ttk.Radiobutton(root4, text = "С 1 недели на 2", value = 1, variable = rbweek4)
	rb_for_week1.place(x = 265/2 - 90, y = 10)
	rb_for_week2 = ttk.Radiobutton(root4, text = "С 2 недели на 1", value = 2, variable = rbweek4)
	rb_for_week2.place(x = 265/2 + 60, y = 10)
	cb_para = ttk.Combobox(root4, values = ["1 пара", "2 пара", "3 пара", "4 пара", "5 пара", "6 пара"], width = 18)
	cb_para.set("Выберите пару")
	cb_para.place(x = 330/2 - 55, y = 300)
	cb_para.bind("<<ComboboxSelected>>", choice_switch_del)
	btttn_inf = ttk.Button(root4, text = "Справочная информация")
	btttn_inf.place(x = 75, y = 323)
	btttn_inf.bind("<Button-1>", root4_inf)

def group(event):
	global label_for_group
	label_for_group["text"] = ""
	print(combobox_for_group.get())

	for i in range(len(group11)):
		if combobox_for_group.get() == group11[i]:
			index_for_group11 = group11.index(combobox_for_group.get())
			para_for_group11 = para11[index_for_group11]
			print(para_for_group11)
			label_for_group["text"] = para_for_group11 + ", 1 пара" + ", 1 неделя" + "\n" + label_for_group["text"]
	for i in range(len(group12)):
		if combobox_for_group.get() == group12[i]:
			index_for_group12 = group12.index(combobox_for_group.get())
			para_for_group12 = para12[index_for_group12]
			print(para_for_group12)
			label_for_group["text"] = para_for_group12 + ", 2 пара" + ", 1 неделя" + "\n" + label_for_group["text"]
	for i in range(len(group13)):
		if combobox_for_group.get() == group13[i]:
			index_for_group13 = group13.index(combobox_for_group.get())
			para_for_group13 = para13[index_for_group13]
			print(para_for_group13)
			label_for_group["text"] = para_for_group13 + ", 3 пара" + ", 1 неделя" + "\n" + label_for_group["text"]
	for i in range(len(group14)):
		if combobox_for_group.get() == group14[i]:
			index_for_group14 = group14.index(combobox_for_group.get())
			para_for_group14 = para14[index_for_group14]
			print(para_for_group14)
			label_for_group["text"] = para_for_group14 + ", 4 пара" + ", 1 неделя" + "\n" + label_for_group["text"]
	for i in range(len(group15)):
		if combobox_for_group.get() == group15[i]:
			index_for_group15 = group15.index(combobox_for_group.get())
			para_for_group15 = para15[index_for_group15]
			print(para_for_group15)
			label_for_group["text"] = para_for_group15 + ", 5 пара" + ", 1 неделя" + "\n" + label_for_group["text"]
	for i in range(len(group16)):
		if combobox_for_group.get() == group16[i]:
			index_for_group16 = group16.index(combobox_for_group.get())
			para_for_group16 = para16[index_for_group16]
			print(para_for_group16)
			label_for_group["text"] = para_for_group16 + ", 6 пара" + ", 1 неделя" + "\n" + label_for_group["text"]

	for i in range(len(group21)):
		if combobox_for_group.get() == group21[i]:
			index_for_group21 = group21.index(combobox_for_group.get())
			para_for_group21 = para21[index_for_group21]
			print(para_for_group21)
			label_for_group["text"] = para_for_group21 + ", 1 пара" + ", 2 неделя" + "\n" + label_for_group["text"]
	for i in range(len(group22)):
		if combobox_for_group.get() == group22[i]:
			index_for_group22 = group22.index(combobox_for_group.get())
			para_for_group22 = para22[index_for_group22]
			print(para_for_group22)
			label_for_group["text"] = para_for_group22 + ", 2 пара" + ", 2 неделя" + "\n" + label_for_group["text"]
	for i in range(len(group23)):
		if combobox_for_group.get() == group23[i]:
			index_for_group23 = group23.index(combobox_for_group.get())
			para_for_group23 = para23[index_for_group23]
			print(para_for_group23)
			label_for_group["text"] = para_for_group23 + ", 3 пара" + ", 2 неделя" + "\n" + label_for_group["text"]
	for i in range(len(group24)):
		if combobox_for_group.get() == group24[i]:
			index_for_group24 = group24.index(combobox_for_group.get())
			para_for_group24 = para24[index_for_group24]
			print(para_for_group24)
			label_for_group["text"] = para_for_group24 + ", 4 пара" + ", 2 неделя" + "\n" + label_for_group["text"]
	for i in range(len(group25)):
		if combobox_for_group.get() == group25[i]:
			index_for_group25 = group25.index(combobox_for_group.get())
			para_for_group25 = para25[index_for_group25]
			print(para_for_group25)
			label_for_group["text"] = para_for_group25 + ", 5 пара" + ", 2 неделя" + "\n" + label_for_group["text"]
	for i in range(len(group26)):
		if combobox_for_group.get() == group26[i]:
			index_for_group26 = group26.index(combobox_for_group.get())
			para_for_group26 = para26[index_for_group26]
			print(para_for_group26)
			label_for_group["text"] = para_for_group26 + ", 6 пара" + ", 2 неделя" + "\n" + label_for_group["text"]

#функция для справочной информации
def root_inf3():
	mb.showinfo("Справочная информация", "Вы вошли в качестве администратора!\nВы можете просматривать и редактировать расписание на кафедре.\nПриятного использования!")

#функция окна администратора
def window_admin():
	global plan, combobox_for_week, frame1, canv, frame2, mainmenu, check, label_for_group, combobox_for_group, menu
	frame = Frame(root, height = 308, width = 472)
	frame.place(x = 0, y = 0)
	frame1 = LabelFrame(root, height = 100, width = 235, text = 'Выберите пару')
	frame1.place(x = 480, y = 0)
	frame2 = LabelFrame(root, height = 200, width = 200, text = 'Информация')
	frame2.place(x = 480, y = 105)	
	frame3 = LabelFrame(root, height = 200, width = 210, text = 'Группы')
	frame3.place(x = 690, y = 105)
	label_for_group = ttk.Label(frame3)
	label_for_group.place(x = 5, y = 30)
	check = 2
	root.title('Расписание пар(Администратор)')
	w = root.winfo_screenwidth()
	h = root.winfo_screenheight()
	w = w//2
	h = h//2
	w = w - 435
	h = h - 325
	root.geometry('910x355+{}+{}'.format(w, h))
	canv = Canvas(frame, width = 464, height = 300, bg = "white")
	canv.place(x = 0, y = 0)
	plan = PhotoImage(file = file_plan)
	image = canv.create_image(233, 145, image = plan)
	mainmenu = Menu(root)
	root.config(menu = mainmenu)
	mainmenu.add_command(label = "Добавить", command = add_cab)
	mainmenu.add_command(label = "Удалить", command = del_cab)
	mainmenu.add_command(label = "Изменить", command = change_cab)
	mainmenu.add_command(label = "Перенести пару", command = switch_cab)
	menu = Menu(tearoff = 0)
	menu.add_command(label = "Показать всё расписание", command = trace)
	combobox_for_week = ttk.Combobox(root, values = ["1 неделя", "2 неделя"])
	combobox_for_week.place(x = 720, y = 10)
	combobox_for_week.set("Выберите неделю")
	combobox_for_week.bind("<<ComboboxSelected>>", week)
	combobox_for_group = ttk.Combobox(frame3, values = ['20ВТ1', '20ВТ2', '19ВТ1', '19ВТ2', '18ВТ', '17ВТ', '20ИЭ1',
														'20ИЭ2', '19ИЭ1', '19ИЭ2', '18ИЭ', '17ИЭ', '20АП1', '20АП2'],
														width = 17)
	combobox_for_group.place(x = 5, y = 5)
	combobox_for_group.set("Выберите группу")
	combobox_for_group.bind("<<ComboboxSelected>>", group)
	canv.create_text(97, 188, text = 'Кабинет\n    №1', font = 'Times 7', tag = 'cab1text')
	canv.create_text(28, 188, text = 'Кабинет\n    №2', font = 'Times 7', tag = 'cab2text')
	canv.create_text(28, 228, text = 'Кабинет\n    №3', font = 'Times 7', tag = 'cab3text')
	canv.create_text(35, 265, text = 'Кабинет\n    №4', font = 'Times 7', tag = 'cab4text')
	canv.create_text(82, 265, text = 'Кабинет\n    №5', font = 'Times 7', tag = 'cab5text')
	canv.create_text(128, 265, text = 'Кабинет\n    №6', font = 'Times 7', tag = 'cab6text')
	canv.create_text(178, 265, text = 'Кабинет\n    №7', font = 'Times 7', tag = 'cab7text')
	canv.create_text(240, 265, text = 'Кабинет\n    №8', font = 'Times 7', tag = 'cab8text')
	canv.create_text(326, 265, text = 'Кабинет\n    №9', font = 'Times 7', tag = 'cab9text')
	canv.create_text(356, 265, text = 'Кабинет\n    №10', font = 'Times 7', tag = 'cab10text')
	canv.create_text(394, 265, text = 'Кабинет\n    №11', font = 'Times 7', tag = 'cab11text')
	canv.create_text(433, 265, text = 'Кабинет\n    №12', font = 'Times 7', tag = 'cab12text')
	canv.create_text(368, 188, text = 'Кабинет\n    №13', font = 'Times 7', tag = 'cab13text')
	canv.create_text(282, 188, text = 'Кабинет\n    №14', font = 'Times 7', tag = 'cab14text')
	bttn_back1 = ttk.Button(root, text = "Назад", command = main).place(x = 760, y = 305)
	bttn_close1 = ttk.Button(root, text = "Выйти", command = root.destroy).place(x = 640, y = 305)
	bttn_inf2 = ttk.Button(root, text = "Справочная информация", command = root_inf3).place(x = 435, y = 305)
	canv.bind("<Button-3>", popup)

#функция окна ввода пароля
def admin_verify():
	global entry1, entry2, frame_for_admin
	root.title("Введите логин и пароль")
	frame_for_admin = Frame(root, height = 100, width = 250).place(x = 0, y = 0)

	w = root.winfo_screenwidth()
	h = root.winfo_screenheight()
	w = w//2
	h = h//2
	w = w - 125
	h = h - 50
	root.geometry('250x100+{}+{}'.format(w, h))
	entry1 = ttk.Entry(frame_for_admin, width = 25, font = "Times, 12")
	entry1.place(x = 10, y = 2)
	entry1.insert(0, "Введите пароль")
	entry1.bind("<Button-1>", mask1)
	entry2 = ttk.Entry(frame_for_admin, width = 25, font = "Times, 12")
	entry2.place(x = 10, y = 30)
	entry2.insert(0, "Введите пароль еще раз")
	entry2.bind("<Button-1>", mask2)

	bttn_accept = ttk.Button(frame_for_admin, text = "Ок", command = verify).place(x = 5, y = 65)
	bttn_back = ttk.Button(frame_for_admin, text = "Назад", command = main).place(x = 135, y = 65)

#функция для справочной информации
def root_inf2():
	mb.showinfo("Справочная информация", "Вы вошли в качестве пользователя!\nВы можете просмотреть:\n   1)Полное расписание на кафедре.\n   2)Расписание для конкретного кабинета(нажатием правой клавиши мыши по кабинету).\n   3)Расписание для конкретной группы(в окне \"Группы\").\nПриятного использования!")

#функция окна пользователя
def window_user():
	global plan, combobox_for_week, frame1, canv, frame2, check, menu, label_for_group, combobox_for_group
	frame = Frame(root, height = 308, width = 472)
	frame.place(x = 0, y = 0)
	frame1 = LabelFrame(root, height = 100, width = 235, text = 'Выберите пару')
	frame1.place(x = 480, y = 0)
	frame2 = LabelFrame(root, height = 200, width = 200, text = 'Информация')
	frame2.place(x = 480, y = 105)
	frame3 = LabelFrame(root, height = 200, width = 210, text = 'Группы')
	frame3.place(x = 690, y = 105)
	label_for_group = ttk.Label(frame3)
	label_for_group.place(x = 5, y = 30)
	check = 1
	root.title('Расписание пар')
	w = root.winfo_screenwidth()
	h = root.winfo_screenheight()
	w = w//2
	h = h//2
	w = w - 435
	h = h - 325
	root.geometry('910x335+{}+{}'.format(w, h))
	canv = Canvas(frame, width = 464, height = 300, bg = "white")
	canv.place(x = 0, y = 0)
	plan = PhotoImage(file = file_plan)
	image = canv.create_image(233, 145, image = plan)
	combobox_for_week = ttk.Combobox(root, values = ["1 неделя", "2 неделя"])
	combobox_for_week.place(x = 720, y = 10)
	combobox_for_week.set("Выберите неделю")
	combobox_for_week.bind("<<ComboboxSelected>>", week)
	menu = Menu(tearoff = 0)
	menu.add_command(label = "Показать всё расписание", command = trace)
	combobox_for_group = ttk.Combobox(frame3, values = ['20ВТ1', '20ВТ2', '19ВТ1', '19ВТ2', '18ВТ', '17ВТ', '20ИЭ1',
														'20ИЭ2', '19ИЭ1', '19ИЭ2', '18ИЭ', '17ИЭ', '20АП1', '20АП2'],
														width = 17)
	combobox_for_group.place(x = 5, y = 5)
	combobox_for_group.set("Выберите группу")
	combobox_for_group.bind("<<ComboboxSelected>>", group)

	canv.create_text(97, 188, text = 'Кабинет\n    №1', font = 'Times 7', tag = 'cab1text')
	canv.create_text(28, 188, text = 'Кабинет\n    №2', font = 'Times 7', tag = 'cab2text')
	canv.create_text(28, 228, text = 'Кабинет\n    №3', font = 'Times 7', tag = 'cab3text')
	canv.create_text(35, 265, text = 'Кабинет\n    №4', font = 'Times 7', tag = 'cab4text')
	canv.create_text(82, 265, text = 'Кабинет\n    №5', font = 'Times 7', tag = 'cab5text')
	canv.create_text(128, 265, text = 'Кабинет\n    №6', font = 'Times 7', tag = 'cab6text')
	canv.create_text(178, 265, text = 'Кабинет\n    №7', font = 'Times 7', tag = 'cab7text')
	canv.create_text(240, 265, text = 'Кабинет\n    №8', font = 'Times 7', tag = 'cab8text')
	canv.create_text(326, 265, text = 'Кабинет\n    №9', font = 'Times 7', tag = 'cab9text')
	canv.create_text(356, 265, text = 'Кабинет\n    №10', font = 'Times 7', tag = 'cab10text')
	canv.create_text(394, 265, text = 'Кабинет\n    №11', font = 'Times 7', tag = 'cab11text')
	canv.create_text(433, 265, text = 'Кабинет\n    №12', font = 'Times 7', tag = 'cab12text')
	canv.create_text(368, 188, text = 'Кабинет\n    №13', font = 'Times 7', tag = 'cab13text')
	canv.create_text(282, 188, text = 'Кабинет\n    №14', font = 'Times 7', tag = 'cab14text')
	bttn_back1 = ttk.Button(root, text = "Назад", command = main).place(x = 760, y = 305)
	bttn_close1 = ttk.Button(root, text = "Выйти", command = root.destroy).place(x = 640, y = 305)
	bttn_inf1 = ttk.Button(root, text = "Справочная информация", command = root_inf2).place(x = 435, y = 305)
	canv.bind("<Button-3>", popup)

#функция для информации об авторе
def root_inf():
	mb.showinfo("Информация об авторе", "ФИО: Подковыров Даниил\nКем является: студент\nМесто: Калининградская область\n")

#функция для справочной информации
def root_inf1():
	mb.showinfo("Справочная информация", "Добро пожаловать в ПС \"Кафедра\"!\nВы можете выбрать интересуемый вас режим входа:\n   1. Режим пользователя(Просмотр информации)\n   2.Режим администратора через пароль(Просмотр и редактирование информации)")

#функция режима входа в систему
def main():
	global root, mainmenu, menu
	if check == 2:
		mainmenu.delete("Добавить")
		mainmenu.delete("Изменить")
		mainmenu.delete("Удалить")
		mainmenu.delete("Перенести пару")
		menu.delete("Показать всё расписание")
	root.title("Выбор пользователя")
	root.resizable(False, False)
	w = root.winfo_screenwidth()
	h = root.winfo_screenheight()
	w = w//2
	h = h//2
	w = w - 125
	h = h - 50
	root.geometry('250x150+{}+{}'.format(w, h))
	frame21 = Frame(root, width = 250, height = 150)
	frame21.place(x = 0, y = 0)
	label_choice = ttk.Label(frame21, text = 'Выберите пользователя', font = 'Times 14').place(x = 30, y = 10)
	bttn_admin = ttk.Button(frame21, text = 'Администратор', command = admin_verify).place(x = 0, y = 50)
	bttn_user = ttk.Button(frame21, text = 'Пользователь', command = window_user).place(x = 135, y = 50)

	bttn_inf_avtor = ttk.Button(frame21, text = "Об авторе", command = root_inf).place(x = 75, y = 110)
	bttn_inf = ttk.Button(frame21, text = "Справочная информация", command = root_inf1).place(x = 25, y = 80)

main()

'''
#функция изменения пароля через каждын 10 дней
def root_change_password():
    global root
    root1 = Tk()
    root1.geometry('310x220')
    root1.title("Cмена пароля")
    print(123)

    style = ttk.Style()
    style.configure('TButton', font = "Times, 12")
    style.configure('TLabel', font = "Times, 10")
    style.configure('TEntry', font = "Times, 10")
    style.map('TButton', background = [("active", "pink")])

    main_label = ttk.Label(root1, text = "Необходимо поменять пароль")
    main_label.place(x = 155, y = 30, anchor = CENTER)

    password_label = ttk.Label(root1, text = "Введите новый пароль:", justify = LEFT)
    password_entry = ttk.Entry(root1, width = 12, show = "•")
    password_label_help = ttk.Label(root1, text = "Минимум 6 символов")
    password_label_help.place(x = 220, y = 105  , anchor  =CENTER)
    password_label.place(x = 80, y = 80, anchor = CENTER)
    password_entry.place(x = 225, y = 80, anchor = CENTER)

    password_label1 = ttk.Label(root1, text = "Повторите ещё раз:", justify = LEFT)
    password_entry1 = ttk.Entry(root1, width = 12, show = "•")
    password_label1.place(x = 80, y = 135, anchor = CENTER)
    password_entry1.place(x = 225, y = 135, anchor = CENTER)
    def change_password():
        global password
        if (password_entry.get() == password_entry1.get()):
            if (len(password_entry.get()) >= 6 and password_entry.get() != password):
                password = password_entry.get()
                password_day = datetime.date.today()
                f = open('secret.txt', 'r')
                lines = f.readlines()
                lines[0] = password + '\n'
                lines[1] = str(password_day) + '\n'
                f.close()
                save_changes = open('secret.txt', 'w')
                save_changes.writelines(lines)
                save_changes.close()
                main()

            elif(len(password_entry.get()) < 6):
                mb.showerror("Ошибка!", "Пароль должен состоять минимум из 6 символов")

            elif(password_entry.get() == password):
                mb.showerror("Ошибка!", "Новый пароль должен отличаться от предыдущего")
        else:
            mb.showerror("Ошибка!", "Пароли не совпадают")

    button = ttk.Button(root1, text = "Готово")
    button.place(x = 155, y = 185, anchor = CENTER)
'''
f = open('secret.txt', 'r')
lines = f.readlines()
password = lines[0].rstrip()
password_day = datetime.datetime.strptime(lines[1].rstrip(), "%Y-%m-%d").date()
f.close()

today = datetime.date.today()
difference_password_day = 1 - int((today - password_day).days)

if (difference_password_day < 1):
   pass
else:
    main()

root.mainloop()