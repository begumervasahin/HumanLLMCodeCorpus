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
                b6 = f'{b5} is not a prime number'
            else:
                for b7 in range(2, b5):
                    if b5 % b7 = = 0:
                        b6 = f'{b5} is not a prime number'
                        break
                else:
                    b6 = f'{b5} is a prime number'
            Label(b1, b8 = b6, font=('Arial', 15)).pack()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number")
    b9 = Button(b1, b8='Calculate', command=prime_number, font=('Arial', 20, 'bold'))
    b9.pack()
def fonk3():
    b10 = Tk()
    b10.title('Radian to Degree')
    b10.geometry("500x500")
    b10.configure(b2 = 'yellow')
    Label(b10, b8 = "Enter Radian value to convert into degrees", bg='yellow', font=('Arial', 15, 'bold')).pack()
    b11 = StringVar()
    b12 = Entry(b10, textvariable=b11, font=('Arial', 15, 'bold'))
    b12.pack()
    def fonk4():
        try:
            b13 = float(b12.get())
            b14 = b13 * 180 / math.pi
            Label(b10, b8 = f"Degrees = {b14}", font=('Arial', 15)).pack()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid b13 value")
    b9 = Button(b10, b8='Calculate', font=('Arial', 20, 'bold'), command=convert_radian_to_degree)
    b9.pack()
def fonk5():
    b15 = Tk()
    b15.title('Degree to Radian')
    b15.geometry("500x500")
    b15.configure(b2 = "yellow")
    Label(b15, b8 = "Enter Degrees value to convert into radians", bg='yellow', font=('Arial', 15, 'bold')).pack()
    b11 = StringVar()
    b12 = Entry(b15, textvariable=b11, font=('Arial', 15, 'bold'))
    b12.pack()
    def fonk6():
        try:
            b14 = float(b12.get())
            b13 = b14 * math.pi / 180
            Label(b15, b8 = f"Radians = {b13}", font=('Arial', 15)).pack()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid b14 value")
    b9 = Button(b15, b8="Calculate", font=('Arial', 20, 'bold'), command=convert_degree_to_radian)
    b9.pack()
def fonk7():
    b16 = Tk()
    b16.title('Compute Arc Length of an Angle')
    b16.geometry("500x500")
    b16.configure(b2 = "yellow")
    Label(b16, b8 = "Please Enter Values To Find Arc Length", bg='yellow', font=('Arial', 15, 'bold')).pack()
    b17 = StringVar()
    b18 = StringVar()
    Label(b16, b8 = "Please Enter Diameter here: ", bg='yellow', font=('Arial', 12, 'bold')).pack()
    b19 = Entry(b16, textvariable=b17, font=('Arial', 20, 'bold'))
    b19.pack()
    Label(b16, b8 = "Please Enter Angle here: ", bg='yellow', font=('Arial', 12, 'bold')).pack()
    b20 = Entry(b16, textvariable=b18, font=('Arial', 20, 'bold'))
    b20.pack()
    def fonk8():
        try:
            b21 = float(b19.get())
            b22 = float(b20.get())
            if b22 >= 360:
                messagebox.showerror("Invalid input", "Angle not possible")
            else:
                b23 = (math.pi * b21) * (b22 / 360)
                Label(b16, b8 = f"Arc Length is: {b23}", font=('Arial', 15, 'bold')).pack()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numerical values")
    b9 = Button(b16, b8="Calculate", font=('Arial', 20, 'bold'), command=calculate_arc_length)
    b9.pack()
def fonk9():
    b24 = Tk()
    b24.title('Compute Area Of Sector')
    b24.geometry("500x500")
    b24.configure(b2 = "yellow")
    Label(b24, b8 = "Please Enter Radius Here", bg='yellow', font=('Arial', 20, 'bold')).pack()
    b25 = StringVar()
    b18 = StringVar()
    b26 = Entry(b24, textvariable=b25, font=('Arial', 20, 'bold'))
    b26.pack()
    Label(b24, b8 = "Please Enter Angle Here", bg='yellow', font=('Arial', 20, 'bold')).pack()
    b20 = Entry(b24, textvariable=b18, font=('Arial', 20, 'bold'))
    b20.pack()
    def fonk10():
        try:
            b27 = float(b26.get())
            b22 = float(b20.get())
            b28 = 0.5 * b27 ** 2 * (b22 * math.pi / 180)
            Label(b24, b8 = f"Area of Sector: {b28}", font=('Arial', 15, 'bold')).pack()
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numerical values")
    b9 = Button(b24, b8="Calculate", font=('Arial', 20, 'bold'), command=calculate_area_of_sector)
    b9.pack()
def fonk11():
    b29 = Tk()
    b29.title('Unknown')
    b29.geometry("300x300")
b30 = Tk()
b30.title("Part B")
b30.geometry("500x500")
b30.configure(b2 = 'powder blue')
Label(b30, b8 = "Please Select a method from below", bg='powder blue', font=("Arial", 20, 'bold')).pack()
Button(b30, b8 = "Check Prime", font=('Arial', 20, 'bold'), command=check_prime_number).pack()
Button(b30, b8 = "Radians to Degrees", font=('Arial', 20, 'bold'), command=radian_to_degree).pack()
Button(b30, b8 = "Degrees to Radians", font=('Arial', 20, 'bold'), command=degree_to_radian).pack()
Button(b30, b8 = "Compute Arc Length of an Angle", font=('Arial', 20, 'bold'), command=compute_arc_length).pack()
Button(b30, b8 = "Area of Sector", font=('Arial', 20, 'bold'), command=area_of_sector).pack()
Button(b30, b8 = "Unknown", font=('Arial', 20, 'bold'), command=unknown).pack()
b30.mainloop()