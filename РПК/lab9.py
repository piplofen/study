from math import*
from tkinter import*
from tkinter import ttk

def is_digit(n):
    try:
        int(n)
        if abs(int(n))>200:
            error_label.configure(text='Ввод координат, не входящих в диапозон')
            return  False
        else:
            return True
        
    except ValueError:
        error_label.configure(text='Ввод нечисловых координат координат')
        return  False

def read_coords():
    global figure, one_label, two_label, three_label, four_label
    graph_canvas.delete(figure, one_label, two_label, three_label, four_label)
   
    def create_trap(x1, y1, x2, y2, x3, y3, x4, y4):
        def findIntersection(x1,y1,x2,y2,x3,y3,x4,y4):
            px= ((x1*y2-y1*x2)*(x3-x4)-(x1-x2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) ) 
            py= ((x1*y2-y1*x2)*(y3-y4)-(y1-y2)*(x3*y4-y3*x4) ) / ( (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4) )
            return [px, py]

        global figure, label
        graph_canvas.delete(label)
        ox = 0
        oy = 0 
        global_square = abs(1/2*(x1*y2+x2*y3+x3*y4+x4*y1-(x2*y1+x3*y2+x4*y3+x1*y4)))

        te='Общая площадь фигуры ='+str(global_square)
        label = graph_canvas.create_text(450, 20, text=te, font = ("Courier", "10"))
            #a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300)
            #c,d = findIntersection(x1,y1,x4,y4,0,300,0,-300)
            #e,f = findIntersection(x1,y1,x2,y2,300,0,-300,0)
            #m,n = findIntersection(x1,y1,x4,y4,300,0,-300,0)
        #Odna tochka v sosednem
        #Test1
        if (x1<0 and x2>=0 and x3>=0 and x4>=0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test1')
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300)
            c,d = findIntersection(x1,y1,x4,y4,0,300,0,-300)
            s = 1/2*abs(((x1-c)*(b-d)-(a-c)*(y1-d)))
            return ['I четверть: ', abs(global_square - s), 'II четверть: ', s, 'III четверть: ', 0, 'IV четверть: ', 0]
        if (x1>=0 and x2<0 and x3<0 and x4<0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test2')
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300)
            c,d = findIntersection(x1,y1,x4,y4,0,300,0,-300)
            s = 1/2*abs(((x1-c)*(b-d)-(a-c)*(y1-d)))
            return ['I четверть: ', s, 'II четверть: ', abs(global_square - s), 'III четверть: ', 0, 'IV четверть: ', 0]
        if (x1<0 and x2>=0 and x3>=0 and x4>=0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test3')
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300)
            c,d = findIntersection(x1,y1,x4,y4,0,300,0,-300)
            s = 1/2*abs(((x1-c)*(b-d)-(a-c)*(y1-d)))
            return ['I четверть: ', 0, 'II четверть: ', 0, 'III четверть: ', s, 'IV четверть: ', abs(global_square - s)]
        if (x1>=0 and x2<0 and x3<0 and x4<0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test4')
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300)
            c,d = findIntersection(x1,y1,x4,y4,0,300,0,-300)
            s = 1/2*abs(((x1-c)*(b-d)-(a-c)*(y1-d)))
            return ['I четверть: ', 0, 'II четверть: ', 0, 'III четверть: ', abs(global_square - s), 'IV четверть: ', s]

            
        #Test2
        if (x2<0 and x1>=0 and x3>=0 and x4>=0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test5')
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300)
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            s = 1/2*abs(((x2-c)*(b-d)-(a-c)*(y2-d)))
            return ['I четверть: ', abs(global_square - s),  'II четверть: ', s, 'III четверть: ', 0, 'IV четверть: ', 0]
        if (x2>=0 and x1<0 and x3<0 and x4<0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test6')
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300)
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            s = 1/2*abs(((x2-c)*(b-d)-(a-c)*(y2-d)))
            return ['I четверть: ', s, 'II четверть: ', abs(global_square - s), 'III четверть: ', 0, 'IV четверть: ', 0]
        if (x2<0 and x1>=0 and x3>=0 and x4>=0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test7')
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300)
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            s = 1/2*abs(((x2-c)*(b-d)-(a-c)*(y2-d)))
            return ['I четверть: ', 0, 'II четверть: ', 0,'III четверть: ', s,  'IV четверть: ', abs(global_square - s)]
        if (x2>=0 and x1<0 and x3<0 and x4<0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test8')
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300)
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            s = 1/2*abs(((x2-c)*(b-d)-(a-c)*(y2-d)))
            return ['I четверть: ', 0, 'II четверть: ', 0,'III четверть: ', abs(global_square - s),  'IV четверть: ', s]
 
        #Test3
        if (x3<0 and x1>=0 and x2>=0 and x4>=0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test9')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            s = 1/2*abs(((x3-c)*(b-d)-(a-c)*(y3-d)))
            return ['I четверть: ', abs(global_square - s),  'II четверть: ', s, 'III четверть: ', 0, 'IV четверть: ', 0]
        if (x3>=0 and x1<0 and x2<0 and x4<0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test10')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            s = 1/2*abs(((x3-c)*(b-d)-(a-c)*(y3-d)))
            return ['I четверть: ', s, 'II четверть: ', abs(global_square - s), 'III четверть: ', 0, 'IV четверть: ', 0]
        if (x3<0 and x1>=0 and x2>=0 and x4>=0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test11')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            s = 1/2*abs(((x3-c)*(b-d)-(a-c)*(y3-d)))
            return ['I четверть: ', 0, 'II четверть: ', 0,'III четверть: ', s,  'IV четверть: ', abs(global_square - s)]
        if (x3>=0 and x1<0 and x2<0 and x4<0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test12')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            s = 1/2*abs(((x3-c)*(b-d)-(a-c)*(y3-d)))
            return ['I четверть: ', 0, 'II четверть: ', 0,'III четверть: ', abs(global_square - s),  'IV четверть: ', s]


        #Test7
        if (x4<0 and x1>=0 and x2>=0 and x3>=0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test13')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            c,d = findIntersection(x1,y1,x4,y4,0,300,0,-300)
            s = 1/2*abs(((x4-c)*(b-d)-(a-c)*(y4-d)))
            return ['I четверть: ', abs(global_square - s),  'II четверть: ', s, 'III четверть: ', 0, 'IV четверть: ', 0]
        if (x4>=0 and x1<0 and x2<0 and x3<0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test14')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            c,d = findIntersection(x1,y1,x4,y4,0,300,0,-300)
            s = 1/2*abs(((x4-c)*(b-d)-(a-c)*(y4-d)))
            return ['I четверть: ', s, 'II четверть: ', abs(global_square - s), 'III четверть: ', 0, 'IV четверть: ', 0]
        if (x4<0 and x1>=0 and x2>=0 and x3>=0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test15')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            c,d = findIntersection(x1,y1,x4,y4,0,300,0,-300)
            s = 1/2*abs(((x4-c)*(b-d)-(a-c)*(y4-d)))
            return ['I четверть: ', 0, 'II четверть: ', 0,'III четверть: ', s,  'IV четверть: ', abs(global_square - s)]
        if (x4>=0 and x1<0 and x2<0 and x3<0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test16')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            c,d = findIntersection(x1,y1,x4,y4,0,300,0,-300)
            s = 1/2*abs(((x4-c)*(b-d)-(a-c)*(y4-d)))
            return ['I четверть: ', 0, 'II четверть: ', 0,'III четверть: ', abs(global_square - s),  'IV четверть: ', s]

            
        #Dve tochki v sosednem
        #Test9
        if (x1>=0 and x2>=0 and x3>=0 and x4>=0 and y1<0 and y2<0 and y3>=0 and y4>=0):
            print('test17')
            e,f = findIntersection(x2,y2,x3,y3,300,0,-300,0)
            m,n = findIntersection(x1,y1,x4,y4,300,0,-300,0)
            s_4 = 1/2*abs((x1*y2+x2*f+e*n+m*y1-(y1*x2+y2*e+m*f+n*x1)))
            return ['I четверть: ', abs(global_square - s_4), 'II четверть: ',  0,\
                    'III четверть: ', 0, 'IV четверть: ', abs(s_4)]
        if (x1>=0 and x2>=0 and x3>=0 and x4>=0 and y3<0 and y4<0 and y1>=0 and y2>=0):
            print('test18')
            e,f = findIntersection(x2,y2,x3,y3,300,0,-300,0)
            m,n = findIntersection(x1,y1,x4,y4,300,0,-300,0)
            s_4 = 1/2*abs((x1*y2+x2*f+e*n+m*y1-(y1*x2+y2*e+m*f+n*x1)))
            return ['I четверть: ', abs(s_4), 'II четверть: ',  0,\
                    'III четверть: ', 0, 'IV четверть: ', abs(global_square - s_4)]
        if (x1<0 and x2<0 and x3<0 and x4<0 and y1<0 and y2<0 and y3>=0 and y4>=0):
            print('test19')
            e,f = findIntersection(x2,y2,x3,y3,300,0,-300,0)
            m,n = findIntersection(x1,y1,x4,y4,300,0,-300,0)
            s_4 = 1/2*abs((x1*y2+x2*f+e*n+m*y1-(y1*x2+y2*e+m*f+n*x1)))
            return ['I четверть: ', 0, 'II четверть: ',  abs(global_square - s_4),\
                    'III четверть: ', abs(s_4), 'IV четверть: ', 0]
        if (x1<0 and x2<0 and x3<0 and x4<0 and y3<0 and y4<0 and y1>=0 and y2>=0):
            print('test20')
            e,f = findIntersection(x2,y2,x3,y3,300,0,-300,0)
            m,n = findIntersection(x1,y1,x4,y4,300,0,-300,0)
            s_4 = 1/2*abs((x1*y2+x2*f+e*n+m*y1-(y1*x2+y2*e+m*f+n*x1)))
            return ['I четверть: ', 0, 'II четверть: ',  abs(s_4), \
                    'III четверть: ', abs(global_square - s_4), 'IV четверть: ', 0]

        #Test10
        if (x1<0 and x2<0 and x3>=0 and x4>=0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test21')
            a,b = findIntersection(x1,y1,x4,y4,0,300,0,-300)
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            print(a,b,c,d)
            s_4 = 1/2*abs((a*y1+x1*y2+x2*d+c*b-(y1*x2+y2*c+d*a+b*x1)))
            print(s_4)
            return ['I четверть: ', abs(global_square - s_4), 'II четверть: ', abs(s_4),\
                    'III четверть: ', 0, 'IV четверть: ',  0]
        if (x3<0 and x4<0 and x1>=0 and x2>=0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test22')
            a,b = findIntersection(x1,y1,x4,y4,0,300,0,-300)
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            s_4 = 1/2*abs((a*y1+x1*y2+x2*d+c*b-(y1*x2+y2*c+d*a+b*x1)))
            return ['I четверть: ', abs(global_square - s_4), 'II четверть: ', abs(s_4),\
                    'III четверть: ', 0, 'IV четверть: ',  0]
        if (x1<0 and x2<0 and x3>=0 and x4>=0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test23')
            a,b = findIntersection(x1,y1,x4,y4,0,300,0,-300)
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            s_4 = 1/2*abs((a*y1+x1*y2+x2*d+c*b-(y1*x2+y2*c+d*a+b*x1)))
            return ['I четверть: ', 0, 'II четверть: ', 0,\
                    'III четверть: ', abs(s_4), 'IV четверть: ',  abs(global_square - s_4)]
        if (x3<0 and x4<0 and x1>=0 and x2>=0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test24')
            a,b = findIntersection(x1,y1,x4,y4,0,300,0,-300)
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            s_4 = 1/2*abs((a*y1+x1*y2+x2*d+c*b-(y1*x2+y2*c+d*a+b*x1)))
            return ['I четверть: ', 0, 'II четверть: ', 0,\
                    'III четверть: ', abs(s_4), 'IV четверть: ',  abs(global_square - s_4)]
            
        #Test11
        if (x1>=0 and x2>=0 and x3>=0 and x4>=0 and y1<0 and y4<0 and y2>=0 and y3>=0):
            print('test25')
            e,f = findIntersection(x4,y4,x3,y3,300,0,-300,0)
            m,n = findIntersection(x1,y1,x2,y2,300,0,-300,0)
            s_4 = 1/2*abs((x1*y4+x4*f+e*n+m*y1-(y1*x4+y4*e+m*f+n*x1)))
            return ['I четверть: ', abs(global_square - s_4), 'II четверть: ',  0,\
                    'III четверть: ', 0, 'IV четверть: ', abs(s_4)]
        if (x1>=0 and x2>=0 and x3>=0 and x4>=0 and y2<0 and y3<0 and y1>=0 and y4>=0):
            print('test26')
            e,f = findIntersection(x4,y4,x3,y3,300,0,-300,0)
            m,n = findIntersection(x1,y1,x2,y2,300,0,-300,0)
            s_4 = 1/2*abs((x1*y4+x4*f+e*n+m*y1-(y1*x4+y4*e+m*f+n*x1)))
            return ['I четверть: ', abs(s_4), 'II четверть: ',  0,\
                    'III четверть: ', 0, 'IV четверть: ', abs(global_square - s_4)]
        if (x1<0 and x2<0 and x3<0 and x4<0 and y1<0 and y4<0 and y2>=0 and y3>=0):
            print('test27')
            e,f = findIntersection(x4,y4,x3,y3,300,0,-300,0)
            m,n = findIntersection(x1,y1,x2,y2,300,0,-300,0)
            s_4 = 1/2*abs((x1*y4+x4*f+e*n+m*y1-(y1*x4+y4*e+m*f+n*x1)))
            return ['I четверть: ', 0, 'II четверть: ',  abs(global_square - s_4),\
                    'III четверть: ', abs(s_4), 'IV четверть: ', 0]
        if (x1<0 and x2<0 and x3<0 and x4<0 and y2<0 and y3<0 and y1>=0 and y4>=0):
            print('test28')
            e,f = findIntersection(x4,y4,x3,y3,300,0,-300,0)
            m,n = findIntersection(x1,y1,x2,y2,300,0,-300,0)
            s_4 = 1/2*abs((x1*y4+x4*f+e*n+m*y1-(y1*x4+y4*e+m*f+n*x1)))
            return ['I четверть: ', 0, 'II четверть: ',  abs(s_4), \
                    'III четверть: ', abs(global_square - s_4), 'IV четверть: ', 0]

        #Test12+
        if (x1<0 and x4<0 and x2>=0 and x3>=0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test29')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            c,d = findIntersection(x2,y2,x1,y1,0,300,0,-300)
            s_4 = 1/2*abs((x1*y4+x4*b+a*d+c*y1-(y1*x4+y4*a+b*c+d*x1)))
            return ['I четверть: ', abs(global_square - s_4), 'II четверть: ', abs(s_4),\
                    'III четверть: ', 0, 'IV четверть: ', 0]
        if (x2<0 and x3<0 and x1>=0 and x4>=0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test30')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            c,d = findIntersection(x2,y2,x1,y1,0,300,0,-300)
            s_4 = 1/2*abs((x1*y4+x4*b+a*d+c*y1-(y1*x4+y4*a+b*c+d*x1)))
            return ['I четверть: ', abs(global_square - s_4), 'II четверть: ', abs(s_4),\
                    'III четверть: ', 0, 'IV четверть: ', 0]
        if (x1<0 and x4<0 and x2>=0 and x3>=0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test31')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            c,d = findIntersection(x2,y2,x1,y1,0,300,0,-300)
            s_4 = 1/2*abs((x1*y4+x4*b+a*d+c*y1-(y1*x4+y4*a+b*c+d*x1)))
            return ['I четверть: ', 0, 'II четверть: ',  0,\
                    'III четверть: ', abs(s_4), 'IV четверть: ',  abs(global_square - s_4)]
        if (x2<0 and x3<0 and x1>=0 and x4>=0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test32')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            c,d = findIntersection(x2,y2,x1,y1,0,300,0,-300)
            s_4 = 1/2*abs((x1*y4+x4*b+a*d+c*y1-(y1*x4+y4*a+b*c+d*x1)))
            return ['I четверть: ', 0, 'II четверть: ',  0,\
                    'III четверть: ', abs(s_4), 'IV четверть: ',  abs(global_square - s_4)]
        '''-------'''
        #2 точки в разных, 2 точки в одном сегменте
        if (x1<0 and x2>=0 and x3>=0 and x4>=0 and y1>=0 and y2>=0 and y3<0 and y4<0):
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300) #oy
            c,d = findIntersection(x4,y4,x1,y1,0,300,0,-300)
            e,f = findIntersection(x1,y1,x4,y4,300,0,-300,0) #ox
            m,n = findIntersection(x2,y2,x3,y3,300,0,-300,0)
            if (d<0):
                print('test33')
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x1*b+a*oy+ox*f+e*y1-(y1*a+b*ox+oy*e+f*x1)))
                s_4_2 = 1/2*abs((x2*b+a*oy+ox*n+m*y2-(y2*a+b*ox+oy*m+n*x2)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                
                return ['I четверть: ', abs(s_4_2), 'II четверть: ',  abs(s_4_1), \
                        'III четверть: ', abs(s), 'IV четверть: ', abs(global_square - s_4_1 - s_4_2 - s)]
            else:
                print('test33a')
                s = 1/2*abs(((x1-c)*(b-d)-(a-c)*(y1-d)))
                s_5 = 1/2*abs((x2*b+a*d+c*f+e*n+m*y2-(y2*a+b*c+d*e+f*m+n*x2)))
                s_4 = 1/2*abs((x3*y4+x4*f+e*n+m*y3-(y3*x4+y4*e+f*m+n*x3)))
                
                return ['I четверть: ', abs(s_5), 'II четверть: ',  abs(s), \
                            'III четверть: ', 0, 'IV четверть: ', abs(s_4)]
                

        if (x1>=0 and x2<0 and x3<0 and x4<0 and y1>=0 and y2>=0 and y3<0 and y4<0):
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300) #oy
            c,d = findIntersection(x4,y4,x1,y1,0,300,0,-300)
            e,f = findIntersection(x1,y1,x4,y4,300,0,-300,0) #ox
            m,n = findIntersection(x2,y2,x3,y3,300,0,-300,0)
            if (d<0):
                print('test34')
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x1*b+a*oy+ox*f+e*y1-(y1*a+b*ox+oy*e+f*x1)))
                s_4_2 = 1/2*abs((x2*b+a*oy+ox*n+m*y2-(y2*a+b*ox+oy*m+n*x2)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_1), 'II четверть: ',  abs(s_4_2), \
                        'III четверть: ', abs(global_square - s_4_1 - s_4_2 - s), 'IV четверть: ', abs(s)]
            else:
                print('test34a')
                s = 1/2*abs(((x1-c)*(b-d)-(a-c)*(y1-d)))
                s_5 = 1/2*abs((x2*b+a*d+c*f+e*n+m*y2-(y2*a+b*c+d*e+f*m+n*x2)))
                s_4 = 1/2*abs((x3*y4+x4*f+e*n+m*y3-(y3*x4+y4*e+f*m+n*x3)))
                print(a,b,c,d,e,f,m,n, s_4)
                return ['I четверть: ', abs(s), 'II четверть: ',  abs(s_5), \
                            'III четверть: ', abs(s_4), 'IV четверть: ', 0]
        
        if (x1<0 and x2>=0 and x3>=0 and x4>=0 and y1>=0 and y4>=0 and y3<0 and y2<0):
            
            a,b = findIntersection(x1,y1,x4,y4,0,300,0,-300) #oy
            c,d = findIntersection(x2,y2,x1,y1,0,300,0,-300)
            e,f = findIntersection(x1,y1,x2,y2,300,0,-300,0) #ox
            m,n = findIntersection(x4,y4,x3,y3,300,0,-300,0)
            if (d<0):
                print('test35')
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x1*b+a*oy+ox*f+e*y1-(y1*a+b*ox+oy*e+f*x1)))
                s_4_2 = 1/2*abs((x4*b+a*oy+ox*n+m*y4-(y4*a+b*ox+oy*m+n*x4)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_2), 'II четверть: ',  abs(s_4_1), \
                            'III четверть: ', abs(s), 'IV четверть: ', abs(global_square - s_4_1 - s_4_2 - s)]
            else:
                print('test35a')
                s = 1/2*abs(((x1-c)*(b-d)-(a-c)*(y1-d)))
                s_5 = 1/2*abs((x4*b+a*d+c*f+e*n+m*y4-(y4*a+b*c+d*e+f*m+n*x4)))
                s_4 = 1/2*abs((x3*y2+x2*f+e*n+m*y3-(y3*x2+y2*e+f*m+n*x3)))
                
                return ['I четверть: ', abs(s_5), 'II четверть: ',  abs(s), \
                            'III четверть: ', 0, 'IV четверть: ', abs(s_4)]
            
        if (x1>=0 and x2<0 and x3<0 and x4<0 and y1>=0 and y4>=0 and y3<0 and y2<0):
            
            a,b = findIntersection(x1,y1,x4,y4,0,300,0,-300) #oy
            c,d = findIntersection(x2,y2,x1,y1,0,300,0,-300)
            e,f = findIntersection(x1,y1,x2,y2,300,0,-300,0) #ox
            m,n = findIntersection(x4,y4,x3,y3,300,0,-300,0)
            if (d<0):
                print('test36')
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x1*b+a*oy+ox*f+e*y1-(y1*a+b*ox+oy*e+f*x1)))
                s_4_2 = 1/2*abs((x4*b+a*oy+ox*n+m*y4-(y4*a+b*ox+oy*m+n*x4)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_1), 'II четверть: ',  abs(s_4_2), \
                        'III четверть: ', abs(global_square - s_4_1 - s_4_2 - s), 'IV четверть: ', abs(s)]
            else:
                print('test36a')
                s = 1/2*abs(((x1-c)*(b-d)-(a-c)*(y1-d)))
                s_5 = 1/2*abs((x4*b+a*d+c*f+e*n+m*y4-(y4*a+b*c+d*e+f*m+n*x4)))
                s_4 = 1/2*abs((x3*y2+x2*f+e*n+m*y3-(y3*x2+y2*e+f*m+n*x3)))
                
                return ['I четверть: ', abs(s), 'II четверть: ',  abs(s_5), \
                            'III четверть: ', abs(s_4), 'IV четверть: ', 0]
            
        if (x2<0 and x1>=0 and x3>=0 and x4>=0 and y3>=0 and y2>=0 and y1<0 and y4<0):
            
            a,b = findIntersection(x3,y3,x2,y2,0,300,0,-300) #oy
            c,d = findIntersection(x2,y2,x1,y1,0,300,0,-300)
            e,f = findIntersection(x1,y1,x2,y2,300,0,-300,0) #ox
            m,n = findIntersection(x4,y4,x3,y3,300,0,-300,0)
            if (d<0):
                print('test37')
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x2*b+a*oy+ox*f+e*y2-(y2*a+b*ox+oy*e+f*x2)))
                s_4_2 = 1/2*abs((x3*b+a*oy+ox*n+m*y3-(y3*a+b*ox+oy*m+n*x3)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_2), 'II четверть: ',  abs(s_4_1), 'III четверть: ', abs(s), 'IV четверть: ', abs(global_square - s_4_1 - s_4_2 - s)]
            else:
                print('test37a')
                s = 1/2*abs(((x2-c)*(b-d)-(a-c)*(y2-d)))
                s_5 = 1/2*abs((x3*b+a*d+c*f+e*n+m*y3-(y3*a+b*c+d*e+f*m+n*x3)))
                s_4 = 1/2*abs((x4*y1+x1*f+e*n+m*y4-(y4*x1+y1*e+f*m+n*x4)))
                
                
                return ['I четверть: ', abs(s_5), 'II четверть: ',  abs(s), \
                            'III четверть: ', 0, 'IV четверть: ', abs(s_4)]
            
        if (x2>=0 and x1<0 and x3<0 and x4<0 and y3>=0 and y2>=0 and y1<0 and y4<0):
            
            a,b = findIntersection(x3,y3,x2,y2,0,300,0,-300) #oy
            c,d = findIntersection(x2,y2,x1,y1,0,300,0,-300)
            e,f = findIntersection(x1,y1,x2,y2,300,0,-300,0) #ox
            m,n = findIntersection(x4,y4,x3,y3,300,0,-300,0)
            if (d<0):
                print('test38')
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x2*b+a*oy+ox*f+e*y2-(y2*a+b*ox+oy*e+f*x2)))
                s_4_2 = 1/2*abs((x3*b+a*oy+ox*n+m*y3-(y3*a+b*ox+oy*m+n*x3)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_1), 'II четверть: ',  abs(s_4_2), 'III четверть: ', abs(global_square - s_4_1 - s_4_2 - s), 'IV четверть: ', abs(s)]
            else:
                print('test38a')
                s = 1/2*abs(((x2-c)*(b-d)-(a-c)*(y2-d)))
                s_5 = 1/2*abs((x3*b+a*d+c*f+e*n+m*y3-(y3*a+b*c+d*e+f*m+n*x3)))
                s_4 = 1/2*abs((x4*y1+x1*f+e*n+m*y4-(y4*x1+y1*e+f*m+n*x4)))
                
                return ['I четверть: ', abs(s), 'II четверть: ',  abs(s_5), \
                            'III четверть: ', abs(s_4), 'IV четверть: ', 0]
        if (x2<0 and x1>=0 and x3>=0 and x4>=0 and y2>=0 and y1>=0 and y3<0 and y4<0):
           
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300) #oy
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            e,f = findIntersection(x3,y3,x2,y2,300,0,-300,0) #ox
            m,n = findIntersection(x4,y4,x1,y1,300,0,-300,0)
            if (d<0):
                print('test39')
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x2*b+a*oy+ox*f+e*y1-(y2*a+b*ox+oy*e+f*x1)))
                s_4_2 = 1/2*abs((x1*b+a*oy+ox*n+m*y1-(y1*a+b*ox+oy*m+n*x1)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_2), 'II четверть: ',  abs(s_4_1), 'III четверть: ', abs(s), 'IV четверть: ', abs(global_square - s_4_1 - s_4_2 - s)]
            else:
                print('test39a')
                s = 1/2*abs(((x2-c)*(b-d)-(a-c)*(y2-d)))
                s_5 = 1/2*abs((x1*b+a*d+c*f+e*n+m*y1-(y1*a+b*c+d*e+f*m+n*x1)))
                s_4 = 1/2*abs((x4*y3+x3*f+e*n+m*y4-(y4*x3+y3*e+f*m+n*x4)))
                               
                return ['I четверть: ', abs(s_5), 'II четверть: ',  abs(s), \
                            'III четверть: ', 0, 'IV четверть: ', abs(s_4)]
            
        if (x2>=0 and x1<0 and x3<0 and x4<0 and y2>=0 and y1>=0 and y3<0 and y4<0):
            
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300) #oy
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            e,f = findIntersection(x3,y3,x2,y2,300,0,-300,0) #ox
            m,n = findIntersection(x4,y4,x1,y1,300,0,-300,0)
            if (d<0):
                print('test40')
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x2*b+a*oy+ox*f+e*y1-(y2*a+b*ox+oy*e+f*x1)))
                s_4_2 = 1/2*abs((x1*b+a*oy+ox*n+m*y1-(y1*a+b*ox+oy*m+n*x1)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_1), 'II четверть: ',  abs(s_4_2), 'III четверть: ', abs(global_square - s_4_1 - s_4_2 - s), 'IV четверть: ', abs(s)]
            else:
                print('test40a')
                s = 1/2*abs(((x2-c)*(b-d)-(a-c)*(y2-d)))
                s_5 = 1/2*abs((x1*b+a*d+c*f+e*n+m*y1-(y1*a+b*c+d*e+f*m+n*x1)))
                s_4 = 1/2*abs((x4*y3+x3*f+e*n+m*y4-(y4*x3+y3*e+f*m+n*x4)))
                print(a,b,c,d,e,f,m,n, s_4)
                return ['I четверть: ', abs(s), 'II четверть: ',  abs(s_5), \
                            'III четверть: ', abs(s_4), 'IV четверть: ', 0]

        if (x3<0 and x1>=0 and x2>=0 and x4>=0 and y3>=0 and y2>=0 and y1<0 and y4<0):
            
            a,b = findIntersection(x3,y3,x2,y2,0,300,0,-300) #oy
            c,d = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            e,f = findIntersection(x3,y3,x4,y4,300,0,-300,0) #ox
            m,n = findIntersection(x1,y1,x2,y2,300,0,-300,0)
            if (d<0):
                print('test41')
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x3*b+a*oy+ox*f+e*y3-(y3*a+b*ox+oy*e+f*x3)))
                s_4_2 = 1/2*abs((x2*b+a*oy+ox*n+m*y2-(y2*a+b*ox+oy*m+n*x2)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_2), 'II четверть: ',  abs(s_4_1), 'III четверть: ', abs(s), 'IV четверть: ', abs(global_square - s_4_1 - s_4_2 - s)]
            else:
                print('test41a')
                s = 1/2*abs(((x3-c)*(b-d)-(a-c)*(y3-d)))
                s_5 = 1/2*abs((x2*b+a*d+c*f+e*n+m*y2-(y2*a+b*c+d*e+f*m+n*x2)))
                s_4 = 1/2*abs((x1*y4+x4*f+e*n+m*y1-(y1*x4+y4*e+f*m+n*x1)))
                print(s_4, x1, y1, x4, y4)
                
                return ['I четверть: ', abs(s_5), 'II четверть: ',  abs(s), \
                            'III четверть: ', 0, 'IV четверть: ', abs(s_4)]
            
        if (x3>=0 and x1<0 and x2<0 and x4<0 and y3>=0 and y2>=0 and y1<0 and y4<0):
            print('test42')
            a,b = findIntersection(x3,y3,x2,y2,0,300,0,-300) #oy
            c,d = findIntersection(x3,y3,x4,y4,0,300,0,-300)
            e,f = findIntersection(x3,y3,x4,y4,300,0,-300,0) #ox
            m,n = findIntersection(x1,y1,x2,y2,300,0,-300,0)
            if (d<0):
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x3*b+a*oy+ox*f+e*y3-(y3*a+b*ox+oy*e+f*x3)))
                s_4_2 = 1/2*abs((x2*b+a*oy+ox*n+m*y2-(y2*a+b*ox+oy*m+n*x2)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_1), 'II четверть: ',  abs(s_4_2), 'III четверть: ', abs(global_square - s_4_1 - s_4_2 - s), 'IV четверть: ', abs(s)]
            else:
                print('test42a')
                s = 1/2*abs(((x3-c)*(b-d)-(a-c)*(y3-d)))
                s_5 = 1/2*abs((x2*b+a*d+c*f+e*n+m*y2-(y2*a+b*c+d*e+f*m+n*x2)))
                s_4 = 1/2*abs((x1*y4+x4*f+e*n+m*y1-(y1*x4+y4*e+f*m+n*x1)))
                print(a,b,c,d,e,f,m,n, s_4)
                return ['I четверть: ', abs(s), 'II четверть: ',  abs(s_5), \
                            'III четверть: ', abs(s_4), 'IV четверть: ', 0]
            
        if (x3<0 and x1>=0 and x2>=0 and x4>=0 and y3>=0 and y4>=0 and y1<0 and y2<0):
            print('test43')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300) #oy
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            e,f = findIntersection(x3,y3,x2,y2,300,0,-300,0) #ox
            m,n = findIntersection(x4,y4,x1,y1,300,0,-300,0)
            if (d<0):
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x3*b+a*oy+ox*f+e*y3-(y3*a+b*ox+oy*e+f*x3)))
                s_4_2 = 1/2*abs((x4*b+a*oy+ox*n+m*y4-(y4*a+b*ox+oy*m+n*x4)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_2), 'II четверть: ',  abs(s_4_1), 'III четверть: ', abs(s), 'IV четверть: ', abs(global_square - s_4_1 - s_4_2 - s)]
            else:
                print('test43a')
                s = 1/2*abs(((x3-c)*(b-d)-(a-c)*(y3-d)))
                s_5 = 1/2*abs((x4*b+a*d+c*f+e*n+m*y4-(y4*a+b*c+d*e+f*m+n*x4)))
                s_4 = 1/2*abs((x1*y2+x2*f+e*n+m*y1-(y1*x2+y2*e+f*m+n*x1)))
                print(s_4, x1, y1, x4, y4)
                
                return ['I четверть: ', abs(s_5), 'II четверть: ',  abs(s), \
                            'III четверть: ', 0, 'IV четверть: ', abs(s_4)]
            
        if (x3>=0 and x1<0 and x2<0 and x4<0 and y3>=0 and y4>=0 and y1<0 and y2<0):
            print('test44')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300) #oy
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            e,f = findIntersection(x3,y3,x2,y2,300,0,-300,0) #ox
            m,n = findIntersection(x4,y4,x1,y1,300,0,-300,0)
            if (d<0):
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x3*b+a*oy+ox*f+e*y3-(y3*a+b*ox+oy*e+f*x3)))
                s_4_2 = 1/2*abs((x4*b+a*oy+ox*n+m*y4-(y4*a+b*ox+oy*m+n*x4)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_1), 'II четверть: ',  abs(s_4_2), 'III четверть: ', abs(global_square - s_4_1 - s_4_2 - s), 'IV четверть: ', abs(s)]
            else:
                print('test44a')
                s = 1/2*abs(((x3-c)*(b-d)-(a-c)*(y3-d)))
                s_5 = 1/2*abs((x4*b+a*d+c*f+e*n+m*y4-(y4*a+b*c+d*e+f*m+n*x4)))
                s_4 = 1/2*abs((x1*y2+x2*f+e*n+m*y1-(y1*x2+y2*e+f*m+n*x1)))
                print(a,b,c,d,e,f,m,n, s_4)
                return ['I четверть: ', abs(s), 'II четверть: ',  abs(s_5), \
                            'III четверть: ', abs(s_4), 'IV четверть: ', 0]

        '''----'''
                    
        #Test19 x4 osn 4-1
        if (x4<0 and x1>=0 and x2>=0 and x3>=0 and y4>=0 and y1>=0 and y2<0 and y3<0):
            print('test45')
            a,b = findIntersection(x4,y4,x1,y1,0,300,0,-300) #oy
            c,d = findIntersection(x4,y4,x3,y3,0,300,0,-300)
            e,f = findIntersection(x4,y4,x3,y3,300,0,-300,0) #ox
            m,n = findIntersection(x1,y1,x2,y2,300,0,-300,0)
            if (d<0):
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x4*b+a*oy+ox*f+e*y4-(y4*a+b*ox+oy*e+f*x4)))
                s_4_2 = 1/2*abs((x1*b+a*oy+ox*n+m*y1-(y1*a+b*ox+oy*m+n*x1)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_2), 'II четверть: ',  abs(s_4_1), 'III четверть: ', abs(s), 'IV четверть: ', abs(global_square - s_4_1 - s_4_2 - s)]
            else:
                print('test45a')
                s = 1/2*abs(((x4-c)*(b-d)-(a-c)*(y4-d)))
                s_5 = 1/2*abs((x1*b+a*d+c*f+e*n+m*y1-(y1*a+b*c+d*e+f*m+n*x1)))
                s_4 = 1/2*abs((x2*y3+x3*f+e*n+m*y2-(y2*x3+y3*e+f*m+n*x2)))
                print(s_4, x1, y1, x4, y4)
                
                return ['I четверть: ', abs(s_5), 'II четверть: ',  abs(s), \
                            'III четверть: ', 0, 'IV четверть: ', abs(s_4)]
            
        if (x4>=0 and x1<0 and x2<0 and x3<0 and y4>=0 and y1>=0 and y2<0 and y3<0):
            print('test46')
            a,b = findIntersection(x4,y4,x1,y1,0,300,0,-300) #oy
            c,d = findIntersection(x4,y4,x3,y3,0,300,0,-300)
            e,f = findIntersection(x4,y4,x3,y3,300,0,-300,0) #ox
            m,n = findIntersection(x1,y1,x2,y2,300,0,-300,0)
            if (d<0):
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x4*b+a*oy+ox*f+e*y4-(y4*a+b*ox+oy*e+f*x4)))
                s_4_2 = 1/2*abs((x1*b+a*oy+ox*n+m*y1-(y1*a+b*ox+oy*m+n*x1)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_1), 'II четверть: ',  abs(s_4_2), 'III четверть: ', abs(global_square - s_4_1 - s_4_2 - s), 'IV четверть: ', abs(s)]
            else:
                print('test46a')
                s = 1/2*abs(((x4-c)*(b-d)-(a-c)*(y4-d)))
                s_5 = 1/2*abs((x1*b+a*d+c*f+e*n+m*y1-(y1*a+b*c+d*e+f*m+n*x1)))
                s_4 = 1/2*abs((x2*y3+x3*f+e*n+m*y2-(y2*x3+y3*e+f*m+n*x2)))
                print(a,b,c,d,e,f,m,n, s_4)
                return ['I четверть: ', abs(s), 'II четверть: ',  abs(s_5), \
                            'III четверть: ', abs(s_4), 'IV четверть: ', 0]

        #Test20 x4 osn 4-3

        if (x4<0 and x1>=0 and x2>=0 and x3>=0 and y3>=0 and y4>=0 and y1<0 and y2<0):
            print('test47')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300) #oy
            c,d = findIntersection(x4,y4,x1,y1,0,300,0,-300)
            e,f = findIntersection(x4,y4,x1,y1,300,0,-300,0) #ox
            m,n = findIntersection(x3,y3,x2,y2,300,0,-300,0)
            if (d<0):
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x4*b+a*oy+ox*f+e*y4-(y4*a+b*ox+oy*e+f*x4)))
                s_4_2 = 1/2*abs((x3*b+a*oy+ox*n+m*y3-(y3*a+b*ox+oy*m+n*x3)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_2), 'II четверть: ',  abs(s_4_1), 'III четверть: ', abs(s), 'IV четверть: ', abs(global_square - s_4_1 - s_4_2 - s)]
            else:
                print('test47a')
                s = 1/2*abs(((x4-c)*(b-d)-(a-c)*(y4-d)))
                s_5 = 1/2*abs((x3*b+a*d+c*f+e*n+m*y3-(y3*a+b*c+d*e+f*m+n*x3)))
                s_4 = 1/2*abs((x2*y1+x1*f+e*n+m*y2-(y2*x1+y1*e+f*m+n*x2)))
                print(s_4, x1, y1, x4, y4)
                
                return ['I четверть: ', abs(s_5), 'II четверть: ',  abs(s), \
                            'III четверть: ', 0, 'IV четверть: ', abs(s_4)]
        if (x4>=0 and x1<0 and x2<0 and x3<0 and y3>=0 and y4>=0 and y1<0 and y2<0):
            print('test48')
            a,b = findIntersection(x3,y3,x4,y4,0,300,0,-300) #oy
            c,d = findIntersection(x4,y4,x1,y1,0,300,0,-300)
            e,f = findIntersection(x4,y4,x1,y1,300,0,-300,0) #ox
            m,n = findIntersection(x3,y3,x2,y2,300,0,-300,0)
            if (d<0):
                ox = 0
                oy = 0 
                s_4_1 = 1/2*abs((x4*b+a*oy+ox*f+e*y4-(y4*a+b*ox+oy*e+f*x4)))
                s_4_2 = 1/2*abs((x3*b+a*oy+ox*n+m*y3-(y3*a+b*ox+oy*m+n*x3)))
                s = 1/2*abs(((ox-e)*(d-f)-(c-e)*(oy-f)))
                return ['I четверть: ', abs(s_4_1), 'II четверть: ',  abs(s_4_2), 'III четверть: ', abs(global_square - s_4_1 - s_4_2 - s), 'IV четверть: ', abs(s)]
            else:
                print('test48a')
                s = 1/2*abs(((x4-c)*(b-d)-(a-c)*(y4-d)))
                s_5 = 1/2*abs((x3*b+a*d+c*f+e*n+m*y3-(y3*a+b*c+d*e+f*m+n*x3)))
                s_4 = 1/2*abs((x2*y1+x1*f+e*n+m*y2-(y2*x1+y1*e+f*m+n*x2)))
                print(a,b,c,d,e,f,m,n, s_4)
                return ['I четверть: ', abs(s), 'II четверть: ',  abs(s_5), \
                            'III четверть: ', abs(s_4), 'IV четверть: ', 0]
            
        #4 точки в разных сегментах
        #Test25 
        if (x1<0 and x2<0 and x3>=0 and x4>=0 and y1<0 and y2>=0 and y3>=0 and y4<0):
            print('test49')
            a,b = findIntersection(x1,y1,x4,y4,0,300,0,-300) #oy
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            e,f = findIntersection(x1,y1,x2,y2,300,0,-300,0) #ox
            m,n = findIntersection(x4,y4,x3,y3,300,0,-300,0)
            print(a,b,c,d,e,f,m,n)
            ox = 0
            oy = 0 
            s_4_1 = 1/2*abs((x1*b+a*oy+ox*f+e*y1-(y1*a+b*ox+oy*e+f*x1)))
            s_4_2 = 1/2*abs((x2*d+c*oy+ox*f+e*y2-(y2*c+d*ox+oy*e+f*x2)))
            s_4_3 = 1/2*abs((x3*d+c*oy+ox*n+m*y3-(y3*c+d*ox+oy*m+n*x3)))
            s_4_4 = 1/2*abs((x4*b+a*oy+ox*n+m*y4-(y4*a+b*ox+oy*m+n*x4)))
            print(s_4_1, s_4_2, s_4_3, s_4_4)
            return ['I четверть: ', abs(s_4_3), 'II четверть: ', abs(s_4_2), 'III четверть: ', abs(s_4_1), 'IV четверть: ', abs(s_4_4)]

        if (x1<0 and x2>=0 and x3>=0 and x4<0 and y1>=0 and y2>=0 and y3<0 and y4<0):
            print('test50')
            a,b = findIntersection(x1,y1,x4,y4,300,0,-300,0) #ox
            c,d = findIntersection(x2,y2,x3,y3,300,0,-300,0)
            e,f = findIntersection(x1,y1,x2,y2,0,300,0,-300) #oy
            m,n = findIntersection(x4,y4,x3,y3,0,300,0,-300)
            ox = 0
            oy = 0 
            s_4_1 = 1/2*abs((x1*b+a*oy+ox*f+e*y1-(y1*a+b*ox+oy*e+f*x1)))
            s_4_2 = 1/2*abs((x2*d+c*oy+ox*f+e*y2-(y2*c+d*ox+oy*e+f*x2)))
            s_4_3 = 1/2*abs((x3*d+c*oy+ox*n+m*y3-(y3*c+d*ox+oy*m+n*x3)))
            s_4_4 = 1/2*abs((x4*b+a*oy+ox*n+m*y4-(y4*a+b*ox+oy*m+n*x4)))
            return ['I четверть: ', abs(s_4_2), 'II четверть: ', abs(s_4_1), 'III четверть: ', abs(s_4_4), 'IV четверть: ', abs(s_4_3)]
            
        if (x1>=0 and x2>=0 and x3<0 and x4<0 and y1>=0 and y2<0 and y3<0 and y4>=0):
            print('test51')
            a,b = findIntersection(x1,y1,x4,y4,0,300,0,-300) #oy
            c,d = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            e,f = findIntersection(x1,y1,x2,y2,300,0,-300,0) #ox
            m,n = findIntersection(x4,y4,x3,y3,300,0,-300,0)
            ox = 0
            oy = 0 
            s_4_1 = 1/2*abs((x1*b+a*oy+ox*f+e*y1-(y1*a+b*ox+oy*e+f*x1)))
            s_4_2 = 1/2*abs((x2*d+c*oy+ox*f+e*y2-(y2*c+d*ox+oy*e+f*x2)))
            s_4_3 = 1/2*abs((x3*d+c*oy+ox*n+m*y3-(y3*c+d*ox+oy*m+n*x3)))
            s_4_4 = 1/2*abs((x4*b+a*oy+ox*n+m*y4-(y4*a+b*ox+oy*m+n*x4)))
            return ['I четверть: ', abs(s_4_1), 'II четверть: ', abs(s_4_4), 'III четверть: ', abs(s_4_3), 'IV четверть: ', abs(s_4_2)]

        if (x1>=0 and x2<0 and x3<0 and x4>=0 and y1<0 and y2<0 and y3>=0 and y4>=0):
            print('test52')
            a,b = findIntersection(x1,y1,x4,y4,300,0,-300,0) #ox
            c,d = findIntersection(x2,y2,x3,y3,300,0,-300,0)
            e,f = findIntersection(x1,y1,x2,y2,0,300,0,-300) #oy
            m,n = findIntersection(x4,y4,x3,y3,0,300,0,-300)
            ox = 0
            oy = 0 
            s_4_1 = 1/2*abs((x1*b+a*oy+ox*f+e*y1-(y1*a+b*ox+oy*e+f*x1)))
            s_4_2 = 1/2*abs((x2*d+c*oy+ox*f+e*y2-(y2*c+d*ox+oy*e+f*x2)))
            s_4_3 = 1/2*abs((x3*d+c*oy+ox*n+m*y3-(y3*c+d*ox+oy*m+n*x3)))
            s_4_4 = 1/2*abs((x4*b+a*oy+ox*n+m*y4-(y4*a+b*ox+oy*m+n*x4)))
            return ['I четверть: ', abs(s_4_4), 'II четверть: ', abs(s_4_3), 'III четверть: ', abs(s_4_2), 'IV четверть: ', abs(s_4_1)]

        #Test25 
        if (x1<0 and x4<0 and x3>=0 and x2>=0 and y1<0 and y4>=0 and y3>=0 and y2<0):
            print('test53')
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300) #oy
            c,d = findIntersection(x4,y4,x3,y3,0,300,0,-300)
            e,f = findIntersection(x1,y1,x4,y4,300,0,-300,0) #ox
            m,n = findIntersection(x2,y2,x3,y3,300,0,-300,0)
            ox = 0
            oy = 0 
            s_4_1 = 1/2*abs((x1*b+a*oy+ox*f+e*y1-(y1*a+b*ox+oy*e+f*x1)))
            s_4_2 = 1/2*abs((x4*d+c*oy+ox*f+e*y4-(y4*c+d*ox+oy*e+f*x4)))
            s_4_3 = 1/2*abs((x3*d+c*oy+ox*n+m*y3-(y3*c+d*ox+oy*m+n*x3)))
            s_4_4 = 1/2*abs((x2*b+a*oy+ox*n+m*y2-(y2*a+b*ox+oy*m+n*x2)))
            return ['I четверть: ', abs(s_4_3), 'II четверть: ', abs(s_4_4), 'III четверть: ', abs(s_4_1), 'IV четверть: ', abs(s_4_2)]

        if (x1<0 and x4>=0 and x3>=0 and x2<0 and y1>=0 and y4>=0 and y3<0 and y2<0):
            print('test54')
            a,b = findIntersection(x1,y1,x2,y2,300,0,-300,0) #oy
            c,d = findIntersection(x4,y4,x3,y3,300,0,-300,0)
            e,f = findIntersection(x1,y1,x4,y4,0,300,0,-300) #ox
            m,n = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            ox = 0
            oy = 0
            s_4_1 = 1/2*abs((x1*b+a*oy+ox*f+e*y1-(y1*a+b*ox+oy*e+f*x1)))
            s_4_2 = 1/2*abs((x4*d+c*oy+ox*f+e*y4-(y4*c+d*ox+oy*e+f*x4)))
            s_4_3 = 1/2*abs((x3*d+c*oy+ox*n+m*y3-(y3*c+d*ox+oy*m+n*x3)))
            s_4_4 = 1/2*abs((x2*b+a*oy+ox*n+m*y2-(y2*a+b*ox+oy*m+n*x2)))
            return ['I четверть: ', abs(s_4_2), 'II четверть: ', abs(s_4_1), 'III четверть: ', abs(s_4_4), 'IV четверть: ', abs(s_4_3)]
            
        if (x1>=0 and x4>=0 and x3<0 and x2<0 and y1>=0 and y4<0 and y3<0 and y2>=0):
            print('test55')
            a,b = findIntersection(x1,y1,x2,y2,0,300,0,-300) #oy
            c,d = findIntersection(x4,y4,x3,y3,0,300,0,-300)
            e,f = findIntersection(x1,y1,x4,y4,300,0,-300,0) #ox
            m,n = findIntersection(x2,y2,x3,y3,300,0,-300,0)
            ox = 0
            oy = 0
            s_4_1 = 1/2*abs((x1*b+a*oy+ox*f+e*y1-(y1*a+b*ox+oy*e+f*x1)))
            s_4_2 = 1/2*abs((x4*d+c*oy+ox*f+e*y4-(y4*c+d*ox+oy*e+f*x4)))
            s_4_3 = 1/2*abs((x3*d+c*oy+ox*n+m*y3-(y3*c+d*ox+oy*m+n*x3)))
            s_4_4 = 1/2*abs((x2*b+a*oy+ox*n+m*y2-(y2*a+b*ox+oy*m+n*x2)))
            return ['I четверть: ', abs(s_4_1), 'II четверть: ', abs(s_4_4), 'III четверть: ', abs(s_4_3), 'IV четверть: ', abs(s_4_2)]

        if (x1>=0 and x4<0 and x3<0 and x2>=0 and y1<0 and y4<0 and y3>=0 and y2>=0):
            print('test56')
            a,b = findIntersection(x1,y1,x2,y2,300,0,-300,0) #ox
            c,d = findIntersection(x4,y4,x3,y3,300,0,-300,0)
            e,f = findIntersection(x1,y1,x4,y4,0,300,0,-300) #oy
            m,n = findIntersection(x2,y2,x3,y3,0,300,0,-300)
            ox = 0
            oy = 0
            s_4_1 = 1/2*abs((x1*b+a*oy+ox*f+e*y1-(y1*a+b*ox+oy*e+f*x1)))
            s_4_2 = 1/2*abs((x4*d+c*oy+ox*f+e*y4-(y4*c+d*ox+oy*e+f*x4)))
            s_4_3 = 1/2*abs((x3*d+c*oy+ox*n+m*y3-(y3*c+d*ox+oy*m+n*x3)))
            s_4_4 = 1/2*abs((x2*b+a*oy+ox*n+m*y2-(y2*a+b*ox+oy*m+n*x2)))
            return ['I четверть: ', abs(s_4_4), 'II четверть: ', abs(s_4_3), 'III четверть: ', abs(s_4_2), 'IV четверть: ', abs(s_4_1)]

        #Все в одном
        #Test25+
        if (x1>=0 and x2>=0 and x3>=0 and x4>=0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test57')
            return ['I четверть: ', abs(global_square), 'II четверть: ', 0, 'III четверть: ', 0, 'IV четверть: ', 0]

        if (x1>=0 and x2>=0 and x3>=0 and x4>=0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test58')
            return ['I четверть: ', 0, 'II четверть: ', 0, 'III четверть: ', 0, 'IV четверть: ', abs(global_square)]
            
        if (x1<0 and x2<0 and x3<0 and x4<0 and y1>=0 and y2>=0 and y3>=0 and y4>=0):
            print('test59')
            return ['I четверть: ', 0, 'II четверть: ', abs(global_square), 'III четверть: ', 0, 'IV четверть: ', 0]

        if (x1<0 and x2<0 and x3<0 and x4<0 and y1<0 and y2<0 and y3<0 and y4<0):
            print('test60')
            return ['I четверть: ', 0, 'II четверть: ', 0, 'III четверть: ', abs(global_square), 'IV четверть: ', 0]

        

    x1=x1_entry.get()
    x2=x2_entry.get()
    x3=x3_entry.get()
    x4=x4_entry.get()
    
    y1=y1_entry.get()
    y2=y2_entry.get()
    y3=y3_entry.get()
    y4=y4_entry.get()
    #print(x1, y1, x2, y2, x3, y3, x4, y4)
    #Проверка на целые координаты
    if (is_digit(x1) == True) and (is_digit(x2) == True) and (is_digit(x3) == True) and (is_digit(x4) == True) and \
       (is_digit(y1) == True) and (is_digit(y2) == True) and (is_digit(y3) == True) and (is_digit(y4) == True):
        x1=int(x1)
        x2=int(x2)
        x3=int(x3)
        x4=int(x4)
    
        y1=int(y1)
        y2=int(y2)
        y3=int(y3)
        y4=int(y4)
        if (x1==x2 and y1==y2) or (x1==x3 and y1==y3) or (x1==x4 and y1==y4) or (x2==x3 and y2==y3) or (x2==x4 and y2==y4) or (x3==x4 and y3==y4):
            error_label.configure(text='Ввод одинаковых координат')
        else:
            if (y1==y2 and y3==y4):
                if (abs(x4-x3)<abs(x1-x2) and (x1+x2)/2<x3 and (x1+x2)/2>x4 and y1<y3 and x1<x2)\
                   or (abs(x4-x3)<abs(x1-x2) and (x1+x2)/2<x4 and (x1+x2)/2>x3 and y1<y3 and x1>x2)\
                   or (abs(x4-x3)>abs(x1-x2) and (x4+x3)/2<x2 and (x4+x3)/2>x1 and y3<y1 and x4<x3)\
                   or (abs(x4-x3)>abs(x1-x2) and (x4+x3)/2<x1 and (x4+x3)/2>x2 and y3<y1 and x3<x4):
                    
                    if (sqrt((x1-x3)**2+(y1-y3)**2)==sqrt((x2-x4)**2+(y2-y4)**2)):
                        error_label.configure(text='')
                        figure = graph_canvas.create_line(300+int(x1)*1.25, 300-int(y1)*1.25, 300+int(x2)*1.25, 300-int(y2)*1.25,\
                                 300+int(x3)*1.25, 300-int(y3)*1.25, 300+int(x4)*1.25, 300-int(y4)*1.25, 300+int(x1)*1.25, 300-int(y1)*1.25)
                        one_label=graph_canvas.create_text(300+int(x1)*1.25,300-int(y1)*1.25, text='1', font = ("Courier", "14"), fill = "darkorchid1")
                        two_label=graph_canvas.create_text(300+int(x2)*1.25,300-int(y2)*1.25, text='2', font = ("Courier", "14"), fill = "darkorchid2")
                        three_label=graph_canvas.create_text(300+int(x3)*1.25,300-int(y3)*1.25, text='3', font = ("Courier", "14"), fill = "darkorchid3")
                        four_label=graph_canvas.create_text(300+int(x4)*1.25,300-int(y4)*1.25, text='4', font = ("Courier", "14"), fill = "darkorchid4")
                        [a, a_s, b, b_s, c, c_s, d, d_s] = create_trap(x1, y1, x2, y2, x3, y3, x4, y4)
                        I_label.configure(text = a)
                        I_label_s.configure(text = a_s)
                        II_label.configure(text = b)
                        II_label_s.configure(text = b_s)
                        III_label.configure(text = c)
                        III_label_s.configure(text = c_s)
                        IV_label.configure(text = d)
                        IV_label_s.configure(text = d_s)
                    else:
                        error_label.configure(text='Трапеция неравнобедренная')
                else:
                    error_label.configure(text='Вид трапеции не соответствует варианту')

            elif (y1==y4 and y2==y3):
                if (abs(x2-x3)<abs(x1-x4) and (x1+x4)/2<x3 and (x1+x4)/2>x2 and y1<y3 and x1<x4)\
                   or (abs(x2-x3)<abs(x1-x4) and (x1+x4)/2<x2 and (x1+x4)/2>x3 and y1<y3 and x1>x4)\
                   or (abs(x2-x3)>abs(x1-x4) and (x2+x3)/2<x4 and (x2+x3)/2>x1 and y3<y1 and x2<x3)\
                   or (abs(x2-x3)>abs(x1-x4) and (x2+x3)/2<x1 and (x2+x3)/2>x4 and y3<y1 and x3<x2):

                    if (sqrt((x1-x3)**2+(y1-y3)**2)==sqrt((x2-x4)**2+(y2-y4)**2)):
                        error_label.configure(text='')
                        figure = graph_canvas.create_line(300+int(x1)*1.25, 300-int(y1)*1.25, 300+int(x2)*1.25, 300-int(y2)*1.25,\
                                 300+int(x3)*1.25, 300-int(y3)*1.25, 300+int(x4)*1.25, 300-int(y4)*1.25, 300+int(x1)*1.25, 300-int(y1)*1.25)
                        one_label=graph_canvas.create_text(300+int(x1)*1.25,300-int(y1)*1.25, text='1', font = ("Courier", "14"), fill = "darkorchid1")
                        two_label=graph_canvas.create_text(300+int(x2)*1.25,300-int(y2)*1.25, text='2', font = ("Courier", "14"), fill = "darkorchid2")
                        three_label=graph_canvas.create_text(300+int(x3)*1.25,300-int(y3)*1.25, text='3', font = ("Courier", "14"), fill = "darkorchid3")
                        four_label=graph_canvas.create_text(300+int(x4)*1.25,300-int(y4)*1.25, text='4', font = ("Courier", "14"), fill = "darkorchid4")
                        [a, a_s, b, b_s, c, c_s, d, d_s] = create_trap(x1, y1, x2, y2, x3, y3, x4, y4)
                        I_label.configure(text = a)
                        I_label_s.configure(text = a_s)
                        II_label.configure(text = b)
                        II_label_s.configure(text = b_s)
                        III_label.configure(text = c)
                        III_label_s.configure(text = c_s)
                        IV_label.configure(text = d)
                        IV_label_s.configure(text = d_s)
                    else:
                        error_label.configure(text='Трапеция неравнобедренная')
                else:
                    error_label.configure(text='Вид трапеции не соответствует варианту')

            elif (y1==y3 and y2==y4):
                if (abs(x2-x4)<abs(x1-x3) and (x1+x3)/2<x4 and (x1+x3)/2>x2 and y1<y2 and x1<x3)\
                   or (abs(x2-x4)<abs(x1-x3) and (x1+x3)/2<x2 and (x1+x3)/2>x4 and y1<y2 and x1>x3)\
                   or (abs(x2-x4)>abs(x1-x3) and (x2+x4)/2<x3 and (x2+x4)/2>x1 and y2<y1 and x2<x4)\
                   or (abs(x2-x4)>abs(x1-x3) and (x2+x4)/2<x1 and (x2+x4)/2>x3 and y2<y1 and x4<x2):

                    if (sqrt((x1-x2)**2+(y1-y2)**2)==sqrt((x3-x4)**2+(y3-y4)**2)):
                        error_label.configure(text='')
                        figure = graph_canvas.create_line(300+int(x1)*1.25, 300-int(y1)*1.25, 300+int(x3)*1.25, 300-int(y3)*1.25,\
                                 300+int(x4)*1.25, 300-int(y4)*1.25, 300+int(x2)*1.25, 300-int(y2)*1.25, 300+int(x1)*1.25, 300-int(y1)*1.25)
                        [a, a_s, b, b_s, c, c_s, d, d_s] = create_trap(x1, y1, x2, y2, x4, y4, x3, y3)
                        one_label=graph_canvas.create_text(300+int(x1)*1.25,300-int(y1)*1.25, text='1', font = ("Courier", "14"), fill = "darkorchid1")
                        two_label=graph_canvas.create_text(300+int(x2)*1.25,300-int(y2)*1.25, text='2', font = ("Courier", "14"), fill = "darkorchid2")
                        three_label=graph_canvas.create_text(300+int(x3)*1.25,300-int(y3)*1.25, text='3', font = ("Courier", "14"), fill = "darkorchid3")
                        four_label=graph_canvas.create_text(300+int(x4)*1.25,300-int(y4)*1.25, text='4', font = ("Courier", "14"), fill = "darkorchid4")
                        I_label.configure(text = a)
                        I_label_s.configure(text = a_s)
                        II_label.configure(text = b)
                        II_label_s.configure(text = b_s)
                        III_label.configure(text = c)
                        III_label_s.configure(text = c_s)
                        IV_label.configure(text = d)
                        IV_label_s.configure(text = d_s)
                    else:
                        error_label.configure(text='Трапеция неравнобедренная')
        
                elif (abs(x2-x4)<abs(x1-x3) and (x1+x3)/2<x2 and (x1+x3)/2>x4 and y1>y2 and x1<x3)\
                   or (abs(x2-x4)<abs(x1-x3) and (x1+x3)/2<x4 and (x1+x3)/2>x2 and y1>y2 and x1>x3)\
                   or (abs(x2-x4)>abs(x1-x3) and (x2+x4)/2<x1 and (x2+x4)/2>x3 and y2>y1 and x2<x4)\
                   or (abs(x2-x4)>abs(x1-x3) and (x2+x4)/2<x3 and (x2+x4)/2>x1 and y2>y1 and x4<x2):

                    if (sqrt((x1-x2)**2+(y1-y2)**2)==sqrt((x3-x4)**2+(y3-y4)**2)):
                        error_label.configure(text='')
                        figure = graph_canvas.create_line(300+int(x1)*1.25, 300-int(y1)*1.25, 300+int(x3)*1.25, 300-int(y3)*1.25,\
                                 300+int(x2)*1.25, 300-int(y2)*1.25, 300+int(x4)*1.25, 300-int(y4)*1.25, 300+int(x1)*1.25, 300-int(y1)*1.25)

                        one_label=graph_canvas.create_text(300+int(x1)*1.25,300-int(y1)*1.25, text='1', font = ("Courier", "14"), fill = "darkorchid1")
                        two_label=graph_canvas.create_text(300+int(x2)*1.25,300-int(y2)*1.25, text='2', font = ("Courier", "14"), fill = "darkorchid2")
                        three_label=graph_canvas.create_text(300+int(x3)*1.25,300-int(y3)*1.25, text='3', font = ("Courier", "14"), fill = "darkorchid3")
                        four_label=graph_canvas.create_text(300+int(x4)*1.25,300-int(y4)*1.25, text='4', font = ("Courier", "14"), fill = "darkorchid4")

                        [a, a_s, b, b_s, c, c_s, d, d_s] = create_trap(x1, y1, x4, y4, x2, y2, x3, y3)
                        I_label.configure(text = a)
                        I_label_s.configure(text = a_s)
                        II_label.configure(text = b)
                        II_label_s.configure(text = b_s)
                        III_label.configure(text = c)
                        III_label_s.configure(text = c_s)
                        IV_label.configure(text = d)
                        IV_label_s.configure(text = d_s)
                    else:
                        error_label.configure(text='Трапеция неравнобедренная')
                else:   
                    error_label.configure(text='Вид трапеции не соответствует варианту')
                           
            else:
                    error_label.configure(text='Нет двух параллельных отрезков')
    #else:
        #error_label.configure(text='Ввод нечисловых координат')

root = Tk()
style = ttk.Style()
style.configure('TButton', font = ("Courier", "14"))
style.configure('TLabel', font = ("Courier", "10"))
style.map('TButton', background = [("active", "pink")])
style.configure('TEntry', font = ("Courier", "10"))

root.resizable(False, False)
root.title("Введите координаты")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w + 250
h = h - 120
root.geometry('300x260+{}+{}'.format(w, h))

bttn_close = ttk.Button(root, text = "Закрыть", command = root.destroy)
bttn_close.place(x = 300/2 - 55, y = 230)

#-60 -20 -20 60 20 60 60 -20

graph = Toplevel(root)
graph.title('График')
w1 = root.winfo_screenwidth()
h1 = root.winfo_screenheight()
w1 = w1//2
h1 = h1//2
w1 = w1 - 500
h1 = h1 - 350
graph.geometry('700x700+{}+{}'.format(w1, h1))
graph.resizable(False, False)

lbl_inf = ttk.Label(graph, text = "Подковыров Даниил\n   Вариант №19\n   Группа 18ВТ2").place(x = 700/2 - 50, y = 0)
 
x1_label = ttk.Label(root, text = 'X1')
x1_label.grid(row=1, column = 1)
x2_label = ttk.Label(root, text = 'X2')
x2_label.grid(row=3, column = 1)
x3_label = ttk.Label(root, text = 'X3')
x3_label.grid(row=1, column = 3)
x4_label = ttk.Label(root, text = 'X4')
x4_label.grid(row=3, column = 3)

x1_entry = ttk.Entry(root)
x1_entry.grid(row=1, column = 2)
y1_entry = ttk.Entry(root)
y1_entry.grid(row=2, column = 2)
x2_entry = ttk.Entry(root)
x2_entry.grid(row=3, column = 2)
y2_entry = ttk.Entry(root)
y2_entry.grid(row=4, column = 2)
x3_entry = ttk.Entry(root)
x3_entry.grid(row=1, column = 4)
y3_entry = ttk.Entry(root)
y3_entry.grid(row=2, column = 4)
x4_entry = ttk.Entry(root)
x4_entry.grid(row=3, column = 4)
y4_entry = ttk.Entry(root)
y4_entry.grid(row=4, column = 4)

y1_label = ttk.Label(root, text = 'Y1')
y1_label.grid(row=2, column = 1)
y2_label = ttk.Label(root, text = 'Y2')
y2_label.grid(row=4, column = 1)
y3_label = ttk.Label(root, text = 'Y3')
y3_label.grid(row=2, column = 3)
y4_label = ttk.Label(root, text = 'Y4')
y4_label.grid(row=4, column = 3)

I_label = ttk.Label(root)
I_label.grid(row=6, column = 1)
II_label = ttk.Label(root)
II_label.grid(row=7, column = 1)
III_label = ttk.Label(root)
III_label.grid(row=8, column = 1)
IV_label = ttk.Label(root)
IV_label.grid(row=9, column = 1)

I_label_s = ttk.Label(root)
I_label_s.grid(row=6, column = 2)
II_label_s = ttk.Label(root)
II_label_s.grid(row=7, column = 2)
III_label_s = ttk.Label(root)
III_label_s.grid(row=8, column = 2)
IV_label_s = ttk.Label(root)
IV_label_s.grid(row=9, column = 2)

error_label = ttk.Label(root)
error_label.grid(row=10, column = 1, columnspan=4)

graph_canvas = Canvas(graph, width=600, height=600, bg='lightpink')
graph_canvas.pack(expand=1)
graph_canvas.create_line(300, 45, 300, 555, fill = "maroon1", width = 1) #Oy
graph_canvas.create_line(45, 300, 555, 300, fill = "maroon1", width = 1) #Ox
figure = graph_canvas.create_line(-1000, -1000, -500, -500)
label = graph_canvas.create_text(450, 20, text='', font = ("Courier", "10"))
one_label=graph_canvas.create_text(-1000, -1000, text='1', fill="red", font = ("Courier", "10"))
two_label=graph_canvas.create_text(-1000, -1000, text='2', fill="red", font = ("Courier", "10"))
three_label=graph_canvas.create_text(-1000, -1000, text='3', fill="red", font = ("Courier", "10"))
four_label=graph_canvas.create_text(-1000, -1000, text='4', fill="red", font = ("Courier", "10"))
for i in range(21):
    graph_canvas.create_line(295, 50+25*i, 305, 50+25*i, fill = "slateblue4", width = 2) #Oy
    graph_canvas.create_text(308, 308, text = 0, font = ("Courier", "8"), fill = "mediumvioletred") #O
    graph_canvas.create_line(50+25*i, 295, 50+25*i, 305, fill = "slateblue4", width = 2) #Ox
    
for i in range(10):
    graph_canvas.create_text(285, 50+25*i, text = 200 - 20*i, font = ("Courier", "8"), fill = "mediumvioletred") #Oy
    graph_canvas.create_text(285, 325+25*i, text = -20 - 20*i, font = ("Courier", "8"), fill = "mediumvioletred") #Oy
    graph_canvas.create_text(275-25*i, 285, text = -20 - 20*i, font = ("Courier", "8"), fill = "mediumvioletred") #Ox
    graph_canvas.create_text(325+25*i, 285, text = 20 + 20*i, font = ("Courier", "8"), fill = "mediumvioletred") #Ox

But_go = ttk.Button(root, text = 'Прочитать данные', command = read_coords)
But_go.grid(row=5, column = 1, columnspan=4)
root.mainloop()
