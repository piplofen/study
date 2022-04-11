from tkinter import*

root = Tk()
root.title("Lab1")
root.geometry("430x440")

def cal_func1(event):
	insert1(object)
	insertLabel1(object)

def cal_func2(event):
	insert2(object)
	insertLabel2(object)

def cal_func3(event):
	insert3(object)
	insertLabel3(object)

def cal_func4(event):
	insert4(object)
	insertLabel4(object)

def cal_func5(event):
	insert5(object)
	insertLabel5(object)

def cal_func6(event):
	insert6(object)
	insertLabel6(object)

def cal_func7(event):
	insert7(object)
	insertLabel7(object)

def insert1(object):
	global entry1,entry2,entry3,entry4,entry5,entry6,entry7
	entry1.delete(0, END)
	entry2.delete(0, END)
	entry3.delete(0, END)
	entry4.delete(0, END)
	entry5.delete(0, END)
	entry6.delete(0, END)
	entry7.delete(0, END)
	entry1.insert(0,"Monday")

def insert2(object):
	global entry1,entry2,entry3,entry4,entry5,entry6,entry7
	entry2.delete(0, END)
	entry1.delete(0, END)
	entry3.delete(0, END)
	entry4.delete(0, END)
	entry5.delete(0, END)
	entry6.delete(0, END)
	entry7.delete(0, END)
	entry2.insert(0,"Tuesday")

def insert3(object):
	global entry1,entry2,entry3,entry4,entry5,entry6,entry7
	entry3.delete(0, END)
	entry2.delete(0, END)
	entry1.delete(0, END)
	entry4.delete(0, END)
	entry5.delete(0, END)
	entry6.delete(0, END)
	entry7.delete(0, END)
	entry3.insert(0,"Wednesday")

def insert4(object):
	global entry1,entry2,entry3,entry4,entry5,entry6,entry7
	entry4.delete(0, END)
	entry2.delete(0, END)
	entry3.delete(0, END)
	entry1.delete(0, END)
	entry5.delete(0, END)
	entry6.delete(0, END)
	entry7.delete(0, END)
	entry4.insert(0,"Thursday")

def insert5(object):
	global entry1,entry2,entry3,entry4,entry5,entry6,entry7
	entry5.delete(0, END)
	entry2.delete(0, END)
	entry3.delete(0, END)
	entry4.delete(0, END)
	entry1.delete(0, END)
	entry6.delete(0, END)
	entry7.delete(0, END)
	entry5.insert(0,"Friday")

def insert6(object):
	global entry1,entry2,entry3,entry4,entry5,entry6,entry7
	entry6.delete(0, END)
	entry2.delete(0, END)
	entry3.delete(0, END)
	entry4.delete(0, END)
	entry5.delete(0, END)
	entry1.delete(0, END)
	entry7.delete(0, END)
	entry6.insert(0,"Saturday")

def insert7(object):
	global entry1,entry2,entry3,entry4,entry5,entry6,entry7
	entry7.delete(0, END)
	entry2.delete(0, END)
	entry3.delete(0, END)
	entry4.delete(0, END)
	entry5.delete(0, END)
	entry6.delete(0, END)
	entry1.delete(0, END)
	entry7.insert(0,"Sunday")

def insertLabel1(object):
	label1['text'] = ''
	label1['text'] = "Monday"
	label2['text'] = ''
	label3['text'] = ''
	label4['text'] = ''
	label5['text'] = ''
	label6['text'] = ''
	label7['text'] = ''

def insertLabel2(object):
	label2['text'] = ''
	label2['text'] = "Tuesday"
	label1['text'] = ''
	label3['text'] = ''
	label4['text'] = ''
	label5['text'] = ''
	label6['text'] = ''
	label7['text'] = ''	

def insertLabel3(object):
	label3['text'] = ''
	label3['text'] = "Wednesday"
	label2['text'] = ''
	label1['text'] = ''
	label4['text'] = ''
	label5['text'] = ''
	label6['text'] = ''
	label7['text'] = ''

def insertLabel4(object):
	label4['text'] = ''
	label4['text'] = "Thursday"
	label2['text'] = ''
	label3['text'] = ''
	label1['text'] = ''
	label5['text'] = ''
	label6['text'] = ''
	label7['text'] = ''

def insertLabel5(object):
	label5['text'] = ''
	label5['text'] = "Friday"
	label2['text'] = ''
	label3['text'] = ''
	label4['text'] = ''
	label1['text'] = ''
	label6['text'] = ''
	label7['text'] = ''

def insertLabel6(object):
	label6['text'] = ''
	label6['text'] = "Saturday"
	label2['text'] = ''
	label3['text'] = ''
	label4['text'] = ''
	label5['text'] = ''
	label1['text'] = ''
	label7['text'] = ''

def insertLabel7(object):
	label7['text'] = ''
	label7['text'] = "Sunday"
	label2['text'] = ''
	label3['text'] = ''
	label4['text'] = ''
	label5['text'] = ''
	label6['text'] = ''
	label1['text'] = ''

def Opr(event):
	global entry1, entry2, entry3, entry4, entry5, entry6, entry7, label1, label2, label3, label4, label5, label6, label7, r_v
	a = colors_listbox.get("active")
	if r_v.get() == 0:
		if a == "Red":
			entry1 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			entry2 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			entry3 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			entry4 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			entry5 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			entry6 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			entry7 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			entry1.place(x = 75, y = 16)
			entry2.place(x = 75, y = 66)
			entry3.place(x = 75, y = 116)
			entry4.place(x = 75, y = 166)
			entry5.place(x = 75, y = 216)
			entry6.place(x = 75, y = 266)
			entry7.place(x = 75, y = 316)
		if a == "Yellow":
			entry1 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			entry2 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			entry3 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			entry4 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			entry5 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			entry6 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			entry7 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			entry1.place(x = 75, y = 16)
			entry2.place(x = 75, y = 66)
			entry3.place(x = 75, y = 116)
			entry4.place(x = 75, y = 166)
			entry5.place(x = 75, y = 216)
			entry6.place(x = 75, y = 266)
			entry7.place(x = 75, y = 316)	
		if a == "Green":
			entry1 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			entry2 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			entry3 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			entry4 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			entry5 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			entry6 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			entry7 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			entry1.place(x = 75, y = 16)
			entry2.place(x = 75, y = 66)
			entry3.place(x = 75, y = 116)
			entry4.place(x = 75, y = 166)
			entry5.place(x = 75, y = 216)
			entry6.place(x = 75, y = 266)
			entry7.place(x = 75, y = 316)
		if a == "Grey":
			entry1 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			entry2 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			entry3 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			entry4 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			entry5 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			entry6 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			entry7 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			entry1.place(x = 75, y = 16)
			entry2.place(x = 75, y = 66)
			entry3.place(x = 75, y = 116)
			entry4.place(x = 75, y = 166)
			entry5.place(x = 75, y = 216)
			entry6.place(x = 75, y = 266)
			entry7.place(x = 75, y = 316)
		if a == "Purple":
			entry1 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			entry2 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			entry3 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			entry4 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			entry5 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			entry6 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			entry7 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			entry1.place(x = 75, y = 16)
			entry2.place(x = 75, y = 66)
			entry3.place(x = 75, y = 116)
			entry4.place(x = 75, y = 166)
			entry5.place(x = 75, y = 216)
			entry6.place(x = 75, y = 266)
			entry7.place(x = 75, y = 316)
		if a == "Orange":
			entry1 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			entry2 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			entry3 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			entry4 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			entry5 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			entry6 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			entry7 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			entry1.place(x = 75, y = 16)
			entry2.place(x = 75, y = 66)
			entry3.place(x = 75, y = 116)
			entry4.place(x = 75, y = 166)
			entry5.place(x = 75, y = 216)
			entry6.place(x = 75, y = 266)
			entry7.place(x = 75, y = 316)
		if a == "Navy":
			entry1 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			entry2 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			entry3 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			entry4 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			entry5 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			entry6 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			entry7 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			entry1.place(x = 75, y = 16)
			entry2.place(x = 75, y = 66)
			entry3.place(x = 75, y = 116)
			entry4.place(x = 75, y = 166)
			entry5.place(x = 75, y = 216)
			entry6.place(x = 75, y = 266)
			entry7.place(x = 75, y = 316)
		if a == "Pink":
			entry1 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			entry2 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			entry3 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			entry4 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			entry5 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			entry6 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			entry7 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			entry1.place(x = 75, y = 16)
			entry2.place(x = 75, y = 66)
			entry3.place(x = 75, y = 116)
			entry4.place(x = 75, y = 166)
			entry5.place(x = 75, y = 216)
			entry6.place(x = 75, y = 266)
			entry7.place(x = 75, y = 316)
		if a == "Violet":
			entry1 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			entry2 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			entry3 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			entry4 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			entry5 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			entry6 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			entry7 = Entry(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			entry1.place(x = 75, y = 16)
			entry2.place(x = 75, y = 66)
			entry3.place(x = 75, y = 116)
			entry4.place(x = 75, y = 166)
			entry5.place(x = 75, y = 216)
			entry6.place(x = 75, y = 266)
			entry7.place(x = 75, y = 316)
	elif r_v.get() == 1:
		if a == "Red":
			label1 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			label2 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			label3 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			label4 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			label5 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			label6 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			label7 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "red")
			label1.place(x = 75, y = 16)
			label2.place(x = 75, y = 66)
			label3.place(x = 75, y = 116)
			label4.place(x = 75, y = 166)
			label5.place(x = 75, y = 216)
			label6.place(x = 75, y = 266)
			label7.place(x = 75, y = 316)
		if a == "Yellow":
			label1 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			label2 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			label3 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			label4 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			label5 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			label6 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			label7 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "yellow")
			label1.place(x = 75, y = 16)
			label2.place(x = 75, y = 66)
			label3.place(x = 75, y = 116)
			label4.place(x = 75, y = 166)
			label5.place(x = 75, y = 216)
			label6.place(x = 75, y = 266)
			label7.place(x = 75, y = 316)	
		if a == "Green":
			label1 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			label2 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			label3 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			label4 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			label5 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			label6 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			label7 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "green")
			label1.place(x = 75, y = 16)
			label2.place(x = 75, y = 66)
			label3.place(x = 75, y = 116)
			label4.place(x = 75, y = 166)
			label5.place(x = 75, y = 216)
			label6.place(x = 75, y = 266)
			label7.place(x = 75, y = 316)
		if a == "Grey":
			label1 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			label2 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			label3 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			label4 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			label5 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			label6 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			label7 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "grey")
			label1.place(x = 75, y = 16)
			label2.place(x = 75, y = 66)
			label3.place(x = 75, y = 116)
			label4.place(x = 75, y = 166)
			label5.place(x = 75, y = 216)
			label6.place(x = 75, y = 266)
			label7.place(x = 75, y = 316)
		if a == "Purple":
			label1 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			label2 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			label3 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			label4 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			label5 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			label6 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			label7 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "purple")
			label1.place(x = 75, y = 16)
			label2.place(x = 75, y = 66)
			label3.place(x = 75, y = 116)
			label4.place(x = 75, y = 166)
			label5.place(x = 75, y = 216)
			label6.place(x = 75, y = 266)
			label7.place(x = 75, y = 316)
		if a == "Orange":
			label1 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			label2 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			label3 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			label4 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			label5 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			label6 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			label7 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "orange")
			label1.place(x = 75, y = 16)
			label2.place(x = 75, y = 66)
			label3.place(x = 75, y = 116)
			label4.place(x = 75, y = 166)
			label5.place(x = 75, y = 216)
			label6.place(x = 75, y = 266)
			label7.place(x = 75, y = 316)
		if a == "Navy":
			label1 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			label2 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			label3 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			label4 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			label5 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			label6 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			label7 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "navy")
			label1.place(x = 75, y = 16)
			label2.place(x = 75, y = 66)
			label3.place(x = 75, y = 116)
			label4.place(x = 75, y = 166)
			label5.place(x = 75, y = 216)
			label6.place(x = 75, y = 266)
			label7.place(x = 75, y = 316)
		if a == "Pink":
			label1 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			label2 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			label3 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			label4 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			label5 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			label6 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			label7 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "pink")
			label1.place(x = 75, y = 16)
			label2.place(x = 75, y = 66)
			label3.place(x = 75, y = 116)
			label4.place(x = 75, y = 166)
			label5.place(x = 75, y = 216)
			label6.place(x = 75, y = 266)
			label7.place(x = 75, y = 316)
		if a == "Violet":
			label1 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			label2 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			label3 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			label4 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			label5 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			label6 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			label7 = Label(root, font = ("Times",16,"bold"), width = 10, fg = "violet")
			label1.place(x = 75, y = 16)
			label2.place(x = 75, y = 66)
			label3.place(x = 75, y = 116)
			label4.place(x = 75, y = 166)
			label5.place(x = 75, y = 216)
			label6.place(x = 75, y = 266)
			label7.place(x = 75, y = 316)
def change():
	global entry1, entry2, entry3, entry4, entry5, entry6, entry7, label1, label2, label3, label4, label5, label6, label7
	print(r_v.get())
	if r_v.get() == 0:
		entry1 = Entry(root, font = ("Times",16,"bold"), width = 10)
		entry2 = Entry(root, font = ("Times",16,"bold"), width = 10)
		entry3 = Entry(root, font = ("Times",16,"bold"), width = 10)
		entry4 = Entry(root, font = ("Times",16,"bold"), width = 10)
		entry5 = Entry(root, font = ("Times",16,"bold"), width = 10)
		entry6 = Entry(root, font = ("Times",16,"bold"), width = 10)
		entry7 = Entry(root, font = ("Times",16,"bold"), width = 10)
		entry1.place(x = 75, y = 16)
		entry2.place(x = 75, y = 66)
		entry3.place(x = 75, y = 116)
		entry4.place(x = 75, y = 166)
		entry5.place(x = 75, y = 216)
		entry6.place(x = 75, y = 266)
		entry7.place(x = 75, y = 316)
	else:
		label1 = Label(root, font = ("Times",16,"bold"), width = 10)
		label2 = Label(root, font = ("Times",16,"bold"), width = 10)
		label3 = Label(root, font = ("Times",16,"bold"), width = 10)
		label4 = Label(root, font = ("Times",16,"bold"), width = 10)
		label5 = Label(root, font = ("Times",16,"bold"), width = 10)
		label6 = Label(root, font = ("Times",16,"bold"), width = 10)
		label7 = Label(root, font = ("Times",16,"bold"), width = 10)
		label1.place(x = 75, y = 16)
		label2.place(x = 75, y = 66)
		label3.place(x = 75, y = 116)
		label4.place(x = 75, y = 166)
		label5.place(x = 75, y = 216)
		label6.place(x = 75, y = 266)
		label7.place(x = 75, y = 316)

colors = ["Red","Yellow","Green","Grey","Purple","Orange","Navy","Pink","Violet"]

colors_listbox = Listbox(bg = "lightgray", font = ("Times",16,"bold"), selectmode=EXTENDED, selectbackground = "green", highlightcolor = "violet", background = "pink" , bd = 5)
colors_listbox.bind('<Double-Button-1>', Opr)

for color in colors:
	colors_listbox.insert(END, color)

bttn1 = Button(root, text = "1", font = ("Times",16,"bold"), width = 3, height = 1)
bttn2 = Button(root, text = "2", font = ("Times",16,"bold"), width = 3, height = 1)
bttn3 = Button(root, text = "3", font = ("Times",16,"bold"), width = 3, height = 1)
bttn4 = Button(root, text = "4", font = ("Times",16,"bold"), width = 3, height = 1)
bttn5 = Button(root, text = "5", font = ("Times",16,"bold"), width = 3, height = 1)
bttn6 = Button(root, text = "6", font = ("Times",16,"bold"), width = 3, height = 1)
bttn7 = Button(root, text = "7", font = ("Times",16,"bold"), width = 3, height = 1)
bttnClose  = Button(root, text = "Close", font = ("Times",16,"bold"), width = 5, height = 1, command = root.destroy)

entry1 = Entry(root, font = ("Times",16,"bold"), width = 10)
entry2 = Entry(root, font = ("Times",16,"bold"), width = 10)
entry3 = Entry(root, font = ("Times",16,"bold"), width = 10)
entry4 = Entry(root, font = ("Times",16,"bold"), width = 10)
entry5 = Entry(root, font = ("Times",16,"bold"), width = 10)
entry6 = Entry(root, font = ("Times",16,"bold"), width = 10)
entry7 = Entry(root, font = ("Times",16,"bold"), width = 10)

bttn1.place(x = 20, y = 10)
bttn2.place(x = 20, y = 60)
bttn3.place(x = 20, y = 110)
bttn4.place(x = 20, y = 160)
bttn5.place(x = 20, y = 210)
bttn6.place(x = 20, y = 260)
bttn7.place(x = 20, y = 310)
bttnClose.place(x = 180, y = 390)

entry1.place(x = 75, y = 16)
entry2.place(x = 75, y = 66)
entry3.place(x = 75, y = 116)
entry4.place(x = 75, y = 166)
entry5.place(x = 75, y = 216)
entry6.place(x = 75, y = 266)
entry7.place(x = 75, y = 316)

colors_listbox.place(x = 200, y = 10)

bttn1.bind('<Button-1>', cal_func1)
bttn2.bind('<Button-1>', cal_func2)
bttn3.bind('<Button-1>', cal_func3)
bttn4.bind('<Button-1>', cal_func4)
bttn5.bind('<Button-1>', cal_func5)
bttn6.bind('<Button-1>', cal_func6)
bttn7.bind('<Button-1>', cal_func7)

r_v = IntVar()
r_v.set(0)
radio_bttn_accept = Button(root, text = "Выбрать", font = ("Times",16,"bold"), width = 7, height = 1, command = change)
radio_bttn1 = Radiobutton(root, text = "Подсказка с помощью Entry", variable = r_v, value = 0)
radio_bttn2 = Radiobutton(root, text = "Подсказка с помощью Label", variable = r_v, value = 1)
radio_bttn_accept.place(x =240, y = 320)
radio_bttn1.place(x = 200, y = 270)
radio_bttn2.place(x = 200, y = 290)
root.mainloop()