from tkinter import *
from tkinter import messagebox
b1 = Tk()
b1.title("Part B")
b1.geometry("500x500")
b1.configure(b2 = 'powder blue')
Label(b1, b3 = "Please Select b17 method from below",bg='powder blue',font=("Arial",20,'bold')).pack()
def fonk1():
  b4 = Tk()
  b4.title("Check prime Number")
  b4.geometry("500x500")
  b4.configure(b2 = 'yellow')
  b5 = StringVar()
  b6 = Entry(b4,textvariable=b5,font=('Arial', 20, 'bold'))
  b6.pack()
  def fonk2():
    b7 = b6.get()
    b7 = int(b7)
    if b7 <=1:
      return False
    else:
      for b8 in range(2, b7):
        if b7 % b8 = = 0:
          return False
        else:
          return True
      if fonk2() == True:
        Label(b4, b3 = f'{b7} is prime').pack()
      else:
        Label(b4, b3 = f'{b7} is not prime').pack()
  b9 = Button(b4, b3='Calculate',command=primeNumber,font=('Arial',20,'bold'))
  b9.pack()
def fonk3():
    b10 = Tk()
    b10.title('Radian to Degree')
    b10.geometry("500x500")
    b10.configure(b2 = 'yellow')
    Label(b10, b3 = "Enter Radian value to convert into degrees", bg='yellow',font=('Arial',15,'bold')).pack()
    b11 = StringVar()
    b12 = Entry(b10, textvariable=b11,font=('Arial',15,'bold'))
    b12.pack()
    def fonk4():
      b11 = b12.get()
      b11 = int(b11)
      b13 = b11*3.14/180
      Label(b10, b3 = "degrees = "+str(b13)).pack()
    b14 = Button(b10, b3='Calculate',font=('Arial',20,'bold'),command=radian_to_degree)
    b14.pack()
def fonk5():
    b15 = Tk()
    b15.title('Degree to Radian')
    b15.geometry("400x400")
    b15.configure(b2 = "yellow")
    b11 = StringVar()
    Label(b15, b3 = "Enter Degrees value to convert into radian", bg='yellow', font=('Arial',15,'bold')).pack()
    b12 = Entry(b15, textvariable=b11,font=('Arial',15,'bold'))
    b12.pack()
    def fonk6():
      b11 = b12.get()
      b11 = int(b11)
      b13 = b11*180/3.14
      Label(b15, b3 = "degrees = "+str(b13)).pack()
    b14 = Button(b15, b3="calculate", command=degrees_to_radian,font=('Arial',20, 'bold'))
    b14.pack()
def fonk7():
    b16 = Tk()
    b16.title('Compute Arc Length of an Angle')
    b16.geometry("400x400")
    b16.configure(b2 = "yellow")
    Label(b16, b3 = "Please Enter Values To find Arc Length", bg='yellow', font=('Arial',15,'bold')).pack()
    b13 = StringVar()
    b17 = StringVar()
    Label(b16, b3 = "Please Enter Diameter here: ",bg='yellow', font=('Arial',12,'bold')).pack()
    b5 = Entry(b16, textvariable=b13, font=('Arial',20,'bold'))
    b5.pack()
    Label(b16, b3 = "Please Enter Angle here: ", bg='yellow', font=('Arial',12,'bold')).pack()
    b18 = Entry(b16, textvariable=b17, font=('Arial',20,'bold'))
    b18.pack()
    def fonk8():
      b19 = b5.get()
      b19 = float(b19)
      b20 = b18.get()
      b20 = float(b20)
      b21 = 22/7
      if b20 >= 360:
        Label(b16, b3 = "Angle not possible",font=('Arial',20,'bold')).pack()
        return
      b22 = (b21*b19) * (b20/360)
      Label(b16, b3 = "Arc Length is: "+str(b22), font=('Arial',15, 'bold')).pack()
    b14 = Button(b16, b3="Calculate", command=b22)
    b14.pack()
def fonk9():
    b23 = Tk()
    b23.title('Compute Area Of Sector')
    b23.geometry("400x400")
    b23.configure(b2 = "yellow")
    b24 = StringVar()
    b25 = StringVar()
    Label(b23, b3 = "Please Enter Radius Here",bg='yellow',font=('Arial',20,'bold')).pack()
    b5 = Entry(b23, textvariable=b24,font=('Arial',20,'bold'))
    b5.pack()
    Label(b23, b3 = "Please Enter Angle Here",bg='yellow',font=('Arial',20,'bold')).pack()
    b18 = Entry(b23, textvariable=b25,font=('Arial',20,'bold'))
    b18.pack()
    def fonk10():
      b17 = b5.get()
      b17 = float(b17)
      b26 = b18.get()
      b26 = float(b26)
      b27 = (1/2)*b17**2*b26
      Label(b23, b3 = "Area of Sector: "+str(b27),font=('Arial',20,'bold')).pack()
    b14 = Button(b23, b3="Calculate",command=b32,font=('Arial',20,'bold'))
    b14.pack()
def fonk11():
    b28 = Tk()
    b28.title('Unknown')
    b28.geometry("300x300")
b29 = Button(b1, b3="Check Prime",font=('Arial',20,'bold'),command=Check_Prime_No)
b29.pack()
b30 = Button(b1, b3="Radians to Degrees",font=('Arial',20,'bold'),command=Radian_to_degree)
b30.pack()
b31 = Button(b1, b3="degrees to radian",font=('Arial',20,'bold'),command=Degree_to_radian)
b31.pack()
b22 = Button(b1, b3="Compute Arc Length of an b20",font=('Arial',20,'bold'),command=Compute_Arc_Length)
b22.pack()
b32 = Button(b1, b3="Area of Sector",font=('Arial',20,'bold'),command=Area_of_sector)
b32.pack()
b33 = Button(b1, b3="Unknown",font=('Arial',20,'bold'),command=UnKnown)
b33.pack()
b1.mainloop()