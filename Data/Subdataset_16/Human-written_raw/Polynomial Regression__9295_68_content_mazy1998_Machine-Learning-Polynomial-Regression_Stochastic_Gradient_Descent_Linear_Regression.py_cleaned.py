import random
from tkinter import *
import time
class class1(Frame):
    def fonk1(self):
            Frame.fonk1(self)
            a1 = 600
            self.b1 = Canvas(width=a1,height=a1,bg="black")
            self.b1.grid()
            b2 = random.randint(-100,100)/100
            b3 = random.randint(-100,100)/100
            b4 = [b3, b2 ]
            def fonk2(b9):
              return (.5*b9+250)
            b5 = [(i,fonk2(i)+random.randint(-10,10)) for i in range(0,a1)]
            for i in b5:
               self.b1.create_line(i[0],a1-i[1],i[0]+1,a1-i[1]+1,b6 = "green")
            b7 = len(b5)
            def fonk3():
                b8 = self.b1.create_line(0,a1-b14,a1,a1-(b13*a1+b14),b6="red")
                self.b1.fonk3()
                time.sleep(.1)
                self.b1.after(10, self.b1.delete, b8)
            for z in range(120):
              b2 += (b5[0][1]-(b2))*.05
              for i in range(len(b5)):
                b9 = b5[i][0]
                b10 = b5[i][1]
                b11 = b3*b9+b2
                b12 = b10-b11
                b3 += (1/b7)*b9*b12*.001
                b13 = b3
                b14 = b2
              fonk3()
            b8 = self.b1.create_line(0,a1-b14,a1,a1-(b13*a1+b14),b6="red")
            print(b13,b14)
b15 = class1()
b15.mainloop()