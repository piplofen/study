from tkinter import* 
root = Tk() 
canv = Canvas(root, width = 600, height = 900, bg = 'white') 
canv.pack() 
top = canv.create_arc(35, 690, 250, 878, start = 0, extent = 180, outline = 'black', fill = 'yellow', width = 2) 
mid = canv.create_rectangle(35,786,250,800, fill = 'red', outline = 'black', width = 2) 
bot = canv.create_arc(35, 895, 250, 700, start = 0, extent = -180, outline = 'black', fill = '#1f1', width =2) 
foot=0 
k=1 
def MoveBall():
    global foot, k, top, mid, bot
    canv.delete(top, mid, bot)
    foot +=1
    k -=1/440
    top = canv.create_arc(k*35+2*foot, k*690-foot, k*250+2*foot, k*878-foot, start = 0, extent = 180, outline = 'black', fill = 'yellow', width = 2)
    mid = canv.create_rectangle(k*35+2*foot, k*786-foot, k*250+2*foot, k*800-foot, fill = 'red', outline = 'black', width = 2)
    bot = canv.create_arc(k*35+2*foot, k*895-foot, k*250+2*foot, k*700-foot, start = 0, extent = -180, outline = 'black', fill = '#1f1', width =2)
    if foot < 220:
        canv.after(100, MoveBall)
        
MoveBall() 
root.mainloop()
