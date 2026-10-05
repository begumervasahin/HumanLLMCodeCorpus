import sys
from tkinter import *
import tkSimpleDialog
def sorting():
  datos = int(entrynumeros.get())
  vector = []
  for i in range(0,datos):
    dialog = tkSimpleDialog.askinteger("","Ingresa el numero")
    vector.append(dialog)
  aux_impresion1 = str(vector)
  Label2.config(text=aux_impresion1)
  def quickSort(vector):
     sort(vector,0,len(vector)-1)
  def sort(vector,x,y):
     if x<y:
         punto = particion(vector,x,y)
         sort(vector,x,punto-1)
         sort(vector,punto+1,y)
  def particion(vector,x,y):
     pivote = vector[x]
     izquierda = x+1
     derecha = y
     done = False
     while not done:
         while izquierda <= derecha and vector[izquierda] <= pivote:
             izquierda = izquierda + 1
         while vector[derecha] >= pivote and derecha >= izquierda:
             derecha = derecha -1
         if derecha < izquierda:
             done = True
         else:
             aux = vector[izquierda]
             vector[izquierda] = vector[derecha]
             vector[derecha] = aux
     aux = vector[x]
     vector[x] = vector[derecha]
     vector[derecha] = aux
     return derecha
  quickSort(vector)
  aux_impresion2 = str(vector)
  label3.config(text=aux_impresion2),
app = Tk()
app.title("Bubble Sort")
app.geometry('250x150')
app.configure(bg = 'SkyBlue2')
Label1 = Label(app, text="Cuantos numeros vas a ingresar?",font='Helvetica 12', bg = 'SkyBlue2')
Label1.pack()
datos = 0
entrynumeros = Entry(app, width=8, textvariable=datos)
entrynumeros.pack()
button1 = Button(app, text="Ok!", command=sorting)
button1.pack(pady=(10,0))
Label2 = Label(app, text="",bg = 'SkyBlue2')
Label2.pack(pady=(10,0))
label3 = Label(app, text="",bg = 'SkyBlue2')
label3.pack(pady=(10,0))
app.mainloop()