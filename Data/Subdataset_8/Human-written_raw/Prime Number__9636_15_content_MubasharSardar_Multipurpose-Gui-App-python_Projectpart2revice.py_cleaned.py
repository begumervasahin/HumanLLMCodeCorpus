from tkinter import *
from tkinter import messagebox
win = Tk()
win.title("Part B")
win.geometry("500x500")
win.configure(background='powder blue')
Label(win, text="Please Select a method from below",bg='powder blue',font=("Arial",20,'bold')).pack()
def Check_Prime_No():
  Cp = Tk()
  Cp.title("Check prime Number")
  Cp.geometry("500x500")
  Cp.configure(background='yellow')
  entry1= StringVar()
  EntryBox=Entry(Cp,textvariable=entry1,font=('Arial', 20, 'bold'))
  EntryBox.pack()
  def primeNumber():
    no = EntryBox.get()
    no = int(no)
    if no <=1:
      return False
    else:
      for i in range(2, no):
        if no % i == 0:
          return False
        else:
          return True
      if primeNumber() == True:
        Label(Cp, text=f'{no} is prime').pack()
      else:
        Label(Cp, text=f'{no} is not prime').pack()
  Btn = Button(Cp, text='Calculate',command=primeNumber,font=('Arial',20,'bold'))
  Btn.pack()
def Radian_to_degree():
    Rd = Tk()
    Rd.title('Radian to Degree')
    Rd.geometry("500x500")
    Rd.configure(background='yellow')
    Label(Rd, text="Enter Radian value to convert into degrees", bg='yellow',font=('Arial',15,'bold')).pack()
    r = StringVar()
    take_input = Entry(Rd, textvariable=r,font=('Arial',15,'bold'))
    take_input.pack()
    def radian_to_degree():
      r = take_input.get()
      r = int(r)
      d = r*3.14/180
      Label(Rd, text="degrees = "+str(d)).pack()
    btn= Button(Rd, text='Calculate',font=('Arial',20,'bold'),command=radian_to_degree)
    btn.pack()
def Degree_to_radian():
    Dr = Tk()
    Dr.title('Degree to Radian')
    Dr.geometry("400x400")
    Dr.configure(background="yellow")
    r = StringVar()
    Label(Dr, text="Enter Degrees value to convert into radian", bg='yellow', font=('Arial',15,'bold')).pack()
    take_input = Entry(Dr, textvariable=r,font=('Arial',15,'bold'))
    take_input.pack()
    def degrees_to_radian():
      r = take_input.get()
      r = int(r)
      d = r*180/3.14
      Label(Dr, text="degrees = "+str(d)).pack()
    btn = Button(Dr, text="calculate", command=degrees_to_radian,font=('Arial',20, 'bold'))
    btn.pack()
def Compute_Arc_Length():
    Cal = Tk()
    Cal.title('Compute Arc Length of an Angle')
    Cal.geometry("400x400")
    Cal.configure(background="yellow")
    Label(Cal, text="Please Enter Values To find Arc Length", bg='yellow', font=('Arial',15,'bold')).pack()
    d = StringVar()
    a = StringVar()
    Label(Cal, text="Please Enter Diameter here: ",bg='yellow', font=('Arial',12,'bold')).pack()
    entry1=Entry(Cal, textvariable=d, font=('Arial',20,'bold'))
    entry1.pack()
    Label(Cal, text="Please Enter Angle here: ", bg='yellow', font=('Arial',12,'bold')).pack()
    entry2=Entry(Cal, textvariable=a, font=('Arial',20,'bold'))
    entry2.pack()
    def arc_length():
      diameter= entry1.get()
      diameter = float(diameter)
      angle= entry2.get()
      angle = float(angle)
      pi=22/7
      if angle >= 360:
        Label(Cal, text="Angle not possible",font=('Arial',20,'bold')).pack()
        return
      arc_length = (pi*diameter) * (angle/360)
      Label(Cal, text="Arc Length is: "+str(arc_length), font=('Arial',15, 'bold')).pack()
    btn = Button(Cal, text="Calculate", command=arc_length)
    btn.pack()
def Area_of_sector():
    Aos = Tk()
    Aos.title('Compute Area Of Sector')
    Aos.geometry("400x400")
    Aos.configure(background="yellow")
    Aos1 = StringVar()
    Aos2 = StringVar()
    Label(Aos, text="Please Enter Radius Here",bg='yellow',font=('Arial',20,'bold')).pack()
    entry1 = Entry(Aos, textvariable=Aos1,font=('Arial',20,'bold'))
    entry1.pack()
    Label(Aos, text="Please Enter Angle Here",bg='yellow',font=('Arial',20,'bold')).pack()
    entry2 = Entry(Aos, textvariable=Aos2,font=('Arial',20,'bold'))
    entry2.pack()
    def area_of_sector():
      a = entry1.get()
      a = float(a)
      b = entry2.get()
      b = float(b)
      aoa = (1/2)*a**2*b
      Label(Aos, text="Area of Sector: "+str(aoa),font=('Arial',20,'bold')).pack()
    btn = Button(Aos, text="Calculate",command=area_of_sector,font=('Arial',20,'bold'))
    btn.pack()
def UnKnown():
    UK = Tk()
    UK.title('Unknown')
    UK.geometry("300x300")
checkprimeno = Button(win, text="Check Prime",font=('Arial',20,'bold'),command=Check_Prime_No)
checkprimeno.pack()
radiantodegree = Button(win, text="Radians to Degrees",font=('Arial',20,'bold'),command=Radian_to_degree)
radiantodegree.pack()
degreestoradian = Button(win, text="degrees to radian",font=('Arial',20,'bold'),command=Degree_to_radian)
degreestoradian.pack()
arc_length = Button(win, text="Compute Arc Length of an angle",font=('Arial',20,'bold'),command=Compute_Arc_Length)
arc_length.pack()
area_of_sector = Button(win, text="Area of Sector",font=('Arial',20,'bold'),command=Area_of_sector)
area_of_sector.pack()
unknown = Button(win, text="Unknown",font=('Arial',20,'bold'),command=UnKnown)
unknown.pack()
win.mainloop()