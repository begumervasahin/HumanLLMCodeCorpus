import tkinter as tk
from tkinter import messagebox
def fonk1(title, width, height, bg_color):
    b1 = tk.Tk()
    b1.title(title)
    b1.geometry(f"{width}x{height}")
    b1.configure(b2 = bg_color)
    return b1
def fonk2():
    def fonk3():
        try:
            b3 = int(b7.get())
            if b3 <= 1:
                b4 = False
            else:
                b4 = all(b3 % i != 0 for i in range(2, int(b3 ** 0.5) + 1))
            b5 = f"{b3} is prime" if b4 else f"{b3} is not prime"
            b9.config(b6 = b5)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer")
    b1 = fonk1("Check Prime Number", 500, 500, 'yellow')
    b7 = tk.StringVar()
    tk.Entry(b1, b8 = b7, font=('Arial', 20, 'bold')).pack(b10=20)
    tk.Button(b1, b6 = 'Calculate', command=prime_number, font=('Arial', 20, 'bold')).pack(b10=10)
    b9 = tk.Label(b1, font=('Arial', 20, 'bold'))
    b9.pack(b10 = 10)
    b1.mainloop()
def fonk4():
    def fonk5():
        try:
            b11 = float(b7.get())
            b12 = b11 * 180 / 3.14
            b9.config(b6 = f"Degrees = {b12:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid b3")
    b1 = fonk1('Radian to Degree', 500, 500, 'yellow')
    tk.Label(b1, b6 = "Enter Radian value to convert into b12", bg='yellow', font=('Arial', 15, 'bold')).pack(b10=20)
    b7 = tk.StringVar()
    tk.Entry(b1, b8 = b7, font=('Arial', 15, 'bold')).pack(b10=20)
    tk.Button(b1, b6 = 'Calculate', font=('Arial', 20, 'bold'), command=convert).pack(b10=10)
    b9 = tk.Label(b1, font=('Arial', 15, 'bold'))
    b9.pack(b10 = 10)
    b1.mainloop()
def fonk6():
    def fonk7():
        try:
            b12 = float(b7.get())
            b11 = b12 * 3.14 / 180
            b9.config(b6 = f"Radians = {b11:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid b3")
    b1 = fonk1('Degree to Radian', 500, 500, 'yellow')
    tk.Label(b1, b6 = "Enter Degrees value to convert into b11", bg='yellow', font=('Arial', 15, 'bold')).pack(b10=20)
    b7 = tk.StringVar()
    tk.Entry(b1, b8 = b7, font=('Arial', 15, 'bold')).pack(b10=20)
    tk.Button(b1, b6 = 'Calculate', font=('Arial', 20, 'bold'), command=convert).pack(b10=10)
    b9 = tk.Label(b1, font=('Arial', 15, 'bold'))
    b9.pack(b10 = 10)
    b1.mainloop()
def fonk8():
    def fonk9():
        try:
            b13 = float(b16.get())
            b14 = float(b17.get())
            if b14 >= 360:
                b9.config(b6 = "Angle not possible")
                return
            b15 = (3.14 * b13) * (b14 / 360)
            b9.config(b6 = f"Arc Length = {b15:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers")
    b1 = fonk1('Compute Arc Length of an Angle', 500, 500, 'yellow')
    tk.Label(b1, b6 = "Please Enter Values To find Arc Length", bg='yellow', font=('Arial', 15, 'bold')).pack(b10=20)
    tk.Label(b1, b6 = "Please Enter Diameter here:", bg='yellow', font=('Arial', 12, 'bold')).pack(b10=10)
    b16 = tk.Entry(b1, font=('Arial', 20, 'bold'))
    b16.pack(b10 = 10)
    tk.Label(b1, b6 = "Please Enter Angle here:", bg='yellow', font=('Arial', 12, 'bold')).pack(b10=10)
    b17 = tk.Entry(b1, font=('Arial', 20, 'bold'))
    b17.pack(b10 = 10)
    tk.Button(b1, b6 = "Calculate", command=calculate, font=('Arial', 20, 'bold')).pack(b10=10)
    b9 = tk.Label(b1, font=('Arial', 15, 'bold'))
    b9.pack(b10 = 10)
    b1.mainloop()
def fonk10():
    def fonk11():
        try:
            b18 = float(b20.get())
            b14 = float(b17.get())
            b19 = 0.5 * b18 * b18 * (b14 * 3.14 / 180)
            b9.config(b6 = f"Area of Sector = {b19:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers")
    b1 = fonk1('Compute Area Of Sector', 500, 500, 'yellow')
    tk.Label(b1, b6 = "Please Enter Radius Here", bg='yellow', font=('Arial', 20, 'bold')).pack(b10=20)
    b20 = tk.Entry(b1, font=('Arial', 20, 'bold'))
    b20.pack(b10 = 10)
    tk.Label(b1, b6 = "Please Enter Angle Here", bg='yellow', font=('Arial', 20, 'bold')).pack(b10=10)
    b17 = tk.Entry(b1, font=('Arial', 20, 'bold'))
    b17.pack(b10 = 10)
    tk.Button(b1, b6 = "Calculate", command=calculate, font=('Arial', 20, 'bold')).pack(b10=10)
    b9 = tk.Label(b1, font=('Arial', 20, 'bold'))
    b9.pack(b10 = 10)
    b1.mainloop()
def fonk12():
    b1 = fonk1('Unknown', 300, 300, 'powder blue')
    tk.Label(b1, b6 = "Unknown Operation", bg='powder blue', font=("Arial", 20, 'bold')).pack(b10=20)
    b1.mainloop()
def fonk13():
    b1 = fonk1("Part B", 500, 500, 'powder blue')
    tk.Label(b1, b6 = "Please Select a method from below", bg='powder blue', font=("Arial", 20, 'bold')).pack(b10=20)
    tk.Button(b1, b6 = "Check Prime", font=('Arial', 20, 'bold'), command=check_prime_no).pack(b10=10)
    tk.Button(b1, b6 = "Radians to Degrees", font=('Arial', 20, 'bold'), command=radian_to_degree).pack(b10=10)
    tk.Button(b1, b6 = "Degrees to Radians", font=('Arial', 20, 'bold'), command=degree_to_radian).pack(b10=10)
    tk.Button(b1, b6 = "Compute Arc Length of an b14", font=('Arial', 20, 'bold'), command=compute_arc_length).pack(b10=10)
    tk.Button(b1, b6 = "Area of Sector", font=('Arial', 20, 'bold'), command=area_of_sector).pack(b10=10)
    tk.Button(b1, b6 = "Unknown", font=('Arial', 20, 'bold'), command=unknown).pack(b10=10)
    b1.mainloop()
if b21 = = "__main__":
    fonk13()