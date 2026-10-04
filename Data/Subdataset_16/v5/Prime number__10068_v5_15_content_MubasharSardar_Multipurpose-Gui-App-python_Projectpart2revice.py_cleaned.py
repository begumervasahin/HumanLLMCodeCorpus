import math
from tkinter import *
from tkinter import messagebox
def fonk1():
    b1 = Tk()
    b1.title("Check Prime Number")
    b1.geometry("500x500")
    b1.configure(b2 = 'yellow')
    b3 = StringVar()
    b4 = Entry(b1, textvariable=b3, font=('Arial', 20, 'bold'))
    b4.pack()
    def fonk2():
        try:
            b5 = int(b4.get())
            if b5 <= 1:
                b6 = f'{b5} is not a prime b5'
            else:
                for b7 in range(2, b5):
                    if b5 % b7 = = 0:
                        b6 = f'{b5} is not a prime b5'
                        break
                else:
                    b6 = f'{b5} is a prime b5'
            Label(b1, b8 = b6, font=('Arial', 15)).pack()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid b5")
    Button(b1, b8 = 'Calculate', command=prime_number, font=('Arial', 20, 'bold')).pack()
def fonk3():
    b9 = Tk()
    b9.title('Radian to Degree')
    b9.geometry("500x500")
    b9.configure(b2 = 'yellow')
    Label(b9, b8 = "Enter Radian value to convert into degrees", bg='yellow', font=('Arial', 15, 'bold')).pack()
    b10 = StringVar()
    b4 = Entry(b9, textvariable=b10, font=('Arial', 15, 'bold'))
    b4.pack()
    def fonk4():
        try:
            b11 = float(b4.get())
            b12 = b11 * 180 / math.pi
            Label(b9, b8 = f"Degrees = {b12}", font=('Arial', 15)).pack()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid b11 value")
    Button(b9, b8 = 'Calculate', font=('Arial', 20, 'bold'), command=convert_radian_to_degree).pack()
def fonk5():
    b13 = Tk()
    b13.title('Degree to Radian')
    b13.geometry("500x500")
    b13.configure(b2 = "yellow")
    Label(b13, b8 = "Enter Degrees value to convert into radians", bg='yellow', font=('Arial', 15, 'bold')).pack()
    b14 = StringVar()
    b4 = Entry(b13, textvariable=b14, font=('Arial', 15, 'bold'))
    b4.pack()
    def fonk6():
        try:
            b12 = float(b4.get())
            b11 = b12 * math.pi / 180
            Label(b13, b8 = f"Radians = {b11}", font=('Arial', 15)).pack()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid b12 value")
    Button(b13, b8 = "Calculate", font=('Arial', 20, 'bold'), command=convert_degree_to_radian).pack()
def fonk7():
    b15 = Tk()
    b15.title('Compute Arc Length of an Angle')
    b15.geometry("500x500")
    b15.configure(b2 = "yellow")
    Label(b15, b8 = "Please Enter Values To Find Arc Length", bg='yellow', font=('Arial', 15, 'bold')).pack()
    b16 = StringVar()
    b17 = StringVar()
    Label(b15, b8 = "Please Enter Diameter here: ", bg='yellow', font=('Arial', 12, 'bold')).pack()
    b18 = Entry(b15, textvariable=b16, font=('Arial', 20, 'bold'))
    b18.pack()
    Label(b15, b8 = "Please Enter Angle here: ", bg='yellow', font=('Arial', 12, 'bold')).pack()
    b19 = Entry(b15, textvariable=b17, font=('Arial', 20, 'bold'))
    b19.pack()
    def fonk8():
        try:
            b20 = float(b18.get())
            b21 = float(b19.get())
            if b21 >= 360:
                messagebox.showerror("Invalid input", "Angle not possible")
            else:
                b22 = (math.pi * b20) * (b21 / 360)
                Label(b15, b8 = f"Arc Length is: {b22}", font=('Arial', 15, 'bold')).pack()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numerical values")
    Button(b15, b8 = "Calculate", font=('Arial', 20, 'bold'), command=calculate_arc_length).pack()
def fonk9():
    b23 = Tk()
    b23.title('Compute Area Of Sector')
    b23.geometry("500x500")
    b23.configure(b2 = "yellow")
    Label(b23, b8 = "Please Enter Radius Here", bg='yellow', font=('Arial', 20, 'bold')).pack()
    b24 = StringVar()
    b17 = StringVar()
    b25 = Entry(b23, textvariable=b24, font=('Arial', 20, 'bold'))
    b25.pack()
    Label(b23, b8 = "Please Enter Angle Here", bg='yellow', font=('Arial', 20, 'bold')).pack()
    b19 = Entry(b23, textvariable=b17, font=('Arial', 20, 'bold'))
    b19.pack()
    def fonk10():
        try:
            b26 = float(b25.get())
            b21 = float(b19.get())
            b27 = 0.5 * b26 ** 2 * (b21 * math.pi / 180)
            Label(b23, b8 = f"Area of Sector: {b27}", font=('Arial', 15, 'bold')).pack()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numerical values")
    Button(b23, b8 = "Calculate", font=('Arial', 20, 'bold'), command=calculate_area_of_sector).pack()
def fonk11():
    b28 = Tk()
    b28.title('Unknown')
    b28.geometry("300x300")
def fonk12():
    b29 = Tk()
    b29.title("Part B")
    b29.geometry("500x500")
    b29.configure(b2 = 'powder blue')
    Label(b29, b8 = "Please Select a method from below", bg='powder blue', font=("Arial", 20, 'bold')).pack()
    Button(b29, b8 = "Check Prime", font=('Arial', 20, 'bold'), command=check_prime_number).pack()
    Button(b29, b8 = "Radians to Degrees", font=('Arial', 20, 'bold'), command=radian_to_degree).pack()
    Button(b29, b8 = "Degrees to Radians", font=('Arial', 20, 'bold'), command=degree_to_radian).pack()
    Button(b29, b8 = "Compute Arc Length of an Angle", font=('Arial', 20, 'bold'), command=compute_arc_length).pack()
    Button(b29, b8 = "Area of Sector", font=('Arial', 20, 'bold'), command=area_of_sector).pack()
    Button(b29, b8 = "Unknown", font=('Arial', 20, 'bold'), command=unknown).pack()
    b29.mainloop()
if b30 = = "__main__":
    fonk12()