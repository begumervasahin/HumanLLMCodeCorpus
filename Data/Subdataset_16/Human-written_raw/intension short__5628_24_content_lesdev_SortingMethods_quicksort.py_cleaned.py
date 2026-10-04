import sys
from tkinter import *
import tkSimpleDialog
def fonk1():
  b1 = int(b16.get())
  b2 = []
  for i in range(0,b1):
    b3 = tkSimpleDialog.askinteger("","Ingresa el numero")
    b2.append(b3)
  b4 = str(b2)
  b19.config(b5 = b4)
  def fonk2(b2):
     fonk3(b2,0,len(b2)-1)
  def fonk3(b2,x,y):
     if x<y:
         b6 = fonk4(b2,x,y)
         fonk3(b2,x,b6-1)
         fonk3(b2,b6+1,y)
  def fonk4(b2,x,y):
     b7 = b2[x]
     b8 = x+1
     b9 = y
     b10 = False
     while not b10:
         while b8 <= b9 and b2[b8] <= b7:
             b8 = b8 + 1
         while b2[b9] >= b7 and b9 >= b8:
             b9 = b9 -1
         if b9 < b8:
             b10 = True
         else:
             b11 = b2[b8]
             b2[b8] = b2[b9]
             b2[b9] = b11
     b11 = b2[x]
     b2[x] = b2[b9]
     b2[b9] = b11
     return b9
  fonk2(b2)
  b12 = str(b2)
  b20.config(b5 = b12),
b13 = Tk()
b13.title("Bubble Sort")
b13.geometry('250x150')
b13.configure(b14 = 'SkyBlue2')
b15 = Label(b13, b5="Cuantos numeros vas a ingresar?",font='Helvetica 12', b14 = 'SkyBlue2')
b15.pack()
b1 = 0
b16 = Entry(b13, width=8, textvariable=b1)
b16.pack()
b17 = Button(b13, b5="Ok!", command=sorting)
b17.pack(b18 = (10,0))
b19 = Label(b13, b5="",b14 = 'SkyBlue2')
b19.pack(b18 = (10,0))
b20 = Label(b13, b5="",b14 = 'SkyBlue2')
b20.pack(b18 = (10,0))
b13.mainloop()