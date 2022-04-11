from tkinter import *
root = Tk()
c = Canvas(root, width=150, height=100, bg="white")
c.place(x=30, y=30)
ball = c.create_text(0, 65, text="P", fill = "pink")
x=0
y=0
z=0
def motion():
    global x
    c.move(ball, 1, 0)
    if c.coords(ball)[0] < 56:
        c.after(50, motion)
        x+=1
    if x==55:
        c2 = Canvas(root, width=150, height=100, bg="white")
        c2.place(x=30, y=30)
        ball2 = c2.create_text(56, 60, text="P", fill = "blue")
        x2=0
        y2=0
        def motion2():
            global y
            c2.move(ball, 0, -1)
            if c2.coords(ball)[1] < 100:
                c2.after(50, motion2)
                y+=1
                if y==83:
                    c3 = Canvas(root, width=150, height=100, bg="white")
                    c3.place(x=30, y=30)
                    ball3 = c3.create_text(57, 14, text="P", fill = "green")
                    x3=0
                    y3=0
                    def motion3():
                        global z
                        c3.move(ball, 1, 0)
                        if c3.coords(ball)[0] < 100:
                            c3.after(50, motion3)
                            z+=1
                            if z==13:
                                c4 = Canvas(root, width=150, height=100, bg="white")
                                c4.place(x=30, y=30)
                                ball4 = c4.create_text(66, 14, text="P", fill = "cyan")
                                def motion4():
                                    c4.move(ball, 0, -1)
                                    if c4.coords(ball)[1] > 1:
                                        c4.after(50, motion4)
                                c4.create_text(80,10,text=chr(0x2501) + chr(0x2565) + chr(0x2568) + chr(0x2574) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551))
                                c4.create_text(80,22,text=chr(0x2556) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2559) + chr(0x2562) + chr(0x2551) + chr(0x2559) + chr(0x2562) + chr(0x2551))
                                c4.create_text(80,34,text=chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2559) + chr(0x2556) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551))
                                c4.create_text(80,46,text=chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2553) + chr(0x255C) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551))
                                c4.create_text(80,58,text=chr(0x2559) + chr(0x2501) + chr(0x255C) + chr(0x2551) + chr(0x2576) + chr(0x255C) + chr(0x2559) + chr(0x255C) + chr(0x2551) + chr(0x2551))
                                c4.create_text(80,70,text=chr(0x2501) + chr(0x2501) + chr(0x2501) + chr(0x2568) + chr(0x2501) + chr(0x2501) + chr(0x2501) + chr(0x2556) + chr(0x2551) + chr(0x255F))
                                motion4() 
                    c3.create_text(80,10,text=chr(0x2501) + chr(0x2565) + chr(0x2568) + chr(0x2574) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551))
                    c3.create_text(80,22,text=chr(0x2556) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2559) + chr(0x2562) + chr(0x2551) + chr(0x2559) + chr(0x2562) + chr(0x2551))
                    c3.create_text(80,34,text=chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2559) + chr(0x2556) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551))
                    c3.create_text(80,46,text=chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2553) + chr(0x255C) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551))
                    c3.create_text(80,58,text=chr(0x2559) + chr(0x2501) + chr(0x255C) + chr(0x2551) + chr(0x2576) + chr(0x255C) + chr(0x2559) + chr(0x255C) + chr(0x2551) + chr(0x2551))
                    c3.create_text(80,70,text=chr(0x2501) + chr(0x2501) + chr(0x2501) + chr(0x2568) + chr(0x2501) + chr(0x2501) + chr(0x2501) + chr(0x2556) + chr(0x2551) + chr(0x255F))
                    motion3()    
        c2.create_text(80,10,text=chr(0x2501) + chr(0x2565) + chr(0x2568) + chr(0x2574) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551))
        c2.create_text(80,22,text=chr(0x2556) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2559) + chr(0x2562) + chr(0x2551) + chr(0x2559) + chr(0x2562) + chr(0x2551))
        c2.create_text(80,34,text=chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2559) + chr(0x2556) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551))
        c2.create_text(80,46,text=chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2553) + chr(0x255C) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551))
        c2.create_text(80,58,text=chr(0x2559) + chr(0x2501) + chr(0x255C) + chr(0x2551) + chr(0x2576) + chr(0x255C) + chr(0x2559) + chr(0x255C) + chr(0x2551) + chr(0x2551))
        c2.create_text(80,70,text=chr(0x2501) + chr(0x2501) + chr(0x2501) + chr(0x2568) + chr(0x2501) + chr(0x2501) + chr(0x2501) + chr(0x2556) + chr(0x2551) + chr(0x255F))
        motion2()  
motion()
c.create_text(80,10,text=chr(0x2501) + chr(0x2565) + chr(0x2568) + chr(0x2574) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551))
c.create_text(80,22,text=chr(0x2556) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2559) + chr(0x2562) + chr(0x2551) + chr(0x2559) + chr(0x2562) + chr(0x2551))
c.create_text(80,34,text=chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2559) + chr(0x2556) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551))
c.create_text(80,46,text=chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2553) + chr(0x255C) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551) + chr(0x2551))
c.create_text(80,58,text=chr(0x2559) + chr(0x2501) + chr(0x255C) + chr(0x2551) + chr(0x2576) + chr(0x255C) + chr(0x2559) + chr(0x255C) + chr(0x2551) + chr(0x2551))
c.create_text(80,70,text=chr(0x2501) + chr(0x2501) + chr(0x2501) + chr(0x2568) + chr(0x2501) + chr(0x2501) + chr(0x2501) + chr(0x2556) + chr(0x2551) + chr(0x255F))
root.mainloop()
