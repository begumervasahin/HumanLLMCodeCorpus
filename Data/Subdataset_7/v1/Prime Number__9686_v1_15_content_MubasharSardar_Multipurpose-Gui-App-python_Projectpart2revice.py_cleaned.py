from tkinter import *
from math import pi
def fonk1():
    b1 = Tk()
    b1.title("Check Prime Number")
    b1.geometry("500x500")
    b1.configure(b2 = 'yellow')
    b3 = StringVar()
    b4 = Entry(b1, textvariable=b3, font=('Arial', 20, 'bold'))
    b4.pack()
    def fonk2():
        b5 = int(b3.get())
        if b5 <= 1:
            Label(b1, b6 = f'{b5} is not prime', font=('Arial', 20, 'bold')).pack()
        else:
            for b7 in range(2, b5):
                if b5 % b7 = = 0:
                    Label(b1, b6 = f'{b5} is not prime', font=('Arial', 20, 'bold')).pack()
                    break
            else:
                Label(b1, b6 = f'{b5} is prime', font=('Arial', 20, 'bold')).pack()
    b8 = Button(b1, b6='Calculate', command=primeNumber, font=('Arial', 20, 'bold'))
    b8.pack()
def fonk3():
    b9 = Tk()
    b9.title('Radian to Degree')
    b9.geometry("500x500")
    b9.configure(b2 = 'yellow')
    b10 = StringVar()
    b11 = Entry(b9, textvariable=b10, font=('Arial', 20, 'bold'))
    b11.pack()
    def fonk4():
        b12 = int(b10.get())
        b13 = b12 * 180 / pi
        Label(b9, b6 = f'Degrees = {b13}', font=('Arial', 20, 'bold')).pack()
    b14 = Button(b9, b6='Calculate', command=radian_to_degree, font=('Arial', 20, 'bold'))
    b14.pack()
def fonk5():
    b15 = Tk()
    b15.title('Degree to Radian')
    b15.geometry("400x400")
    b15.configure(b2 = "yellow")
    b10 = StringVar()
    b11 = Entry(b15, textvariable=b10, font=('Arial', 20, 'bold'))
    b11.pack()
    def fonk6():
        b16 = int(b10.get())
        b10 = b16 * pi / 180
        Label(b15, b6 = f'Radian = {b10}', font=('Arial', 20, 'bold')).pack()
    b14 = Button(b15, b6="Calculate", command=degrees_to_radian, font=('Arial', 20, 'bold'))
    b14.pack()
def fonk7():
    b17 = Tk()
    b17.title('Compute Arc Length of an Angle')
    b17.geometry("400x400")
    b17.configure(b2 = "yellow")
    b13 = StringVar()
    b18 = StringVar()
    Label(b17, b6 = "Please Enter Values To find Arc Length", bg='yellow', font=('Arial', 15, 'bold')).pack()
    Label(b17, b6 = "Please Enter Diameter here: ", bg='yellow', font=('Arial', 12, 'bold')).pack()
    b3 = Entry(b17, textvariable=b13, font=('Arial', 20, 'bold'))
    b3.pack()
    Label(b17, b6 = "Please Enter Angle here: ", bg='yellow', font=('Arial', 12, 'bold')).pack()
    b19 = Entry(b17, textvariable=b18, font=('Arial', 20, 'bold'))
    b19.pack()
    def fonk8():
        b20 = float(b3.get())
        b21 = float(b19.get())
        b22 = (pi * b20) * (b21 / 360)
        Label(b17, b6 = f"Arc Length is: {b22}", font=('Arial', 15, 'bold')).pack()
    b14 = Button(b17, b6="Calculate", command=b33, font=('Arial', 20, 'bold'))
    b14.pack()
def fonk9():
    b23 = Tk()
    b23.title('Compute Area Of Sector')
    b23.geometry("400x400")
    b23.configure(b2 = "yellow")
    b24 = StringVar()
    b25 = StringVar()
    Label(b23, b6 = "Please Enter Radius Here", bg='yellow', font=('Arial', 20, 'bold')).pack()
    b3 = Entry(b23, textvariable=b24, font=('Arial', 20, 'bold'))
    b3.pack()
    Label(b23, b6 = "Please Enter Angle Here", bg='yellow', font=('Arial', 20, 'bold')).pack()
    b19 = Entry(b23, textvariable=b25, font=('Arial', 20, 'bold'))
    b19.pack()
    def fonk10():
        b26 = float(b3.get())
        b21 = float(b19.get())
        b27 = (1 / 2) * b26 ** 2 * b21
        Label(b23, b6 = f"Area of Sector: {b27}", font=('Arial', 20, 'bold')).pack()
    b14 = Button(b23, b6="Calculate", command=b34, font=('Arial', 20, 'bold'))
    b14.pack()
def fonk11():
    b28 = Tk()
    b28.title('Unknown')
    b28.geometry("300x300")
b29 = Tk()
b29.title("Part B")
b29.geometry("500x500")
b29.configure(b2 = 'powder blue')
Label(b29, b6 = "Please Select b18 method from below", bg='powder blue', font=("Arial", 20, 'bold')).pack()
b30 = Button(b29, b6="Check Prime", font=('Arial', 20, 'bold'), command=Check_Prime_No)
b30.pack()
b31 = Button(b29, b6="Radians to Degrees", font=('Arial', 20, 'bold'), command=Radian_to_degree)
b31.pack()
b32 = Button(b29, b6="degrees to radian", font=('Arial', 20, 'bold'), command=Degree_to_radian)
b32.pack()
b33 = Button(b29, b6="Compute Arc Length of an b21", font=('Arial', 20, 'bold'), command=Compute_Arc_Length)
b33.pack()
b34 = Button(b29, b6="Area of Sector", font=('Arial', 20, 'bold'), command=Area_of_sector)
b34.pack()
b35 = Button(b29, b6="Unknown", font=('Arial', 20, 'bold'), command=UnKnown)
b35.pack()
b29.mainloop()