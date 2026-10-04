import tkinter as tk
from tkinter import messagebox
def fonk1():
    def fonk2():
        try:
            b1 = int(b7.get())
            if b1 <= 1:
                b2 = False
            else:
                b2 = all(b1 % i != 0 for i in range(2, int(b1 ** 0.5) + 1))
            b3 = f"{b1} is prime" if b2 else f"{b1} is not prime"
            b9.config(b4 = b3)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer")
    b5 = tk.Tk()
    b5.title("Check Prime Number")
    b5.geometry("500x500")
    b5.configure(b6 = 'yellow')
    b7 = tk.StringVar()
    tk.Entry(b5, b8 = b7, font=('Arial', 20, 'bold')).pack(b10=20)
    tk.Button(b5, b4 = 'Calculate', command=prime_number, font=('Arial', 20, 'bold')).pack(b10=10)
    b9 = tk.Label(b5, font=('Arial', 20, 'bold'))
    b9.pack(b10 = 10)
def fonk3():
    def fonk4():
        try:
            b11 = float(b7.get())
            b12 = b11 * 180 / 3.14
            b9.config(b4 = f"Degrees = {b12:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid b1")
    b5 = tk.Tk()
    b5.title('Radian to Degree')
    b5.geometry("500x500")
    b5.configure(b6 = 'yellow')
    tk.Label(b5, b4 = "Enter Radian value to convert into b12", bg='yellow', font=('Arial', 15, 'bold')).pack(b10=20)
    b7 = tk.StringVar()
    tk.Entry(b5, b8 = b7, font=('Arial', 15, 'bold')).pack(b10=20)
    tk.Button(b5, b4 = 'Calculate', font=('Arial', 20, 'bold'), command=convert).pack(b10=10)
    b9 = tk.Label(b5, font=('Arial', 15, 'bold'))
    b9.pack(b10 = 10)
def fonk5():
    def fonk6():
        try:
            b12 = float(b7.get())
            b11 = b12 * 3.14 / 180
            b9.config(b4 = f"Radians = {b11:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid b1")
    b5 = tk.Tk()
    b5.title('Degree to Radian')
    b5.geometry("500x500")
    b5.configure(b6 = 'yellow')
    tk.Label(b5, b4 = "Enter Degrees value to convert into b11", bg='yellow', font=('Arial', 15, 'bold')).pack(b10=20)
    b7 = tk.StringVar()
    tk.Entry(b5, b8 = b7, font=('Arial', 15, 'bold')).pack(b10=20)
    tk.Button(b5, b4 = 'Calculate', font=('Arial', 20, 'bold'), command=convert).pack(b10=10)
    b9 = tk.Label(b5, font=('Arial', 15, 'bold'))
    b9.pack(b10 = 10)
def fonk7():
    def fonk8():
        try:
            b13 = float(b16.get())
            b14 = float(b17.get())
            if b14 >= 360:
                b9.config(b4 = "Angle not possible")
                return
            b15 = (3.14 * b13) * (b14 / 360)
            b9.config(b4 = f"Arc Length = {b15:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers")
    b5 = tk.Tk()
    b5.title('Compute Arc Length of an Angle')
    b5.geometry("500x500")
    b5.configure(b6 = 'yellow')
    tk.Label(b5, b4 = "Please Enter Values To find Arc Length", bg='yellow', font=('Arial', 15, 'bold')).pack(b10=20)
    tk.Label(b5, b4 = "Please Enter Diameter here:", bg='yellow', font=('Arial', 12, 'bold')).pack(b10=10)
    b16 = tk.Entry(b5, font=('Arial', 20, 'bold'))
    b16.pack(b10 = 10)
    tk.Label(b5, b4 = "Please Enter Angle here:", bg='yellow', font=('Arial', 12, 'bold')).pack(b10=10)
    b17 = tk.Entry(b5, font=('Arial', 20, 'bold'))
    b17.pack(b10 = 10)
    tk.Button(b5, b4 = "Calculate", command=calculate, font=('Arial', 20, 'bold')).pack(b10=10)
    b9 = tk.Label(b5, font=('Arial', 15, 'bold'))
    b9.pack(b10 = 10)
def fonk9():
    def fonk10():
        try:
            b18 = float(b20.get())
            b14 = float(b17.get())
            b19 = 0.5 * b18 * b18 * (b14 * 3.14 / 180)
            b9.config(b4 = f"Area of Sector = {b19:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers")
    b5 = tk.Tk()
    b5.title('Compute Area Of Sector')
    b5.geometry("500x500")
    b5.configure(b6 = 'yellow')
    tk.Label(b5, b4 = "Please Enter Radius Here", bg='yellow', font=('Arial', 20, 'bold')).pack(b10=20)
    b20 = tk.Entry(b5, font=('Arial', 20, 'bold'))
    b20.pack(b10 = 10)
    tk.Label(b5, b4 = "Please Enter Angle Here", bg='yellow', font=('Arial', 20, 'bold')).pack(b10=10)
    b17 = tk.Entry(b5, font=('Arial', 20, 'bold'))
    b17.pack(b10 = 10)
    tk.Button(b5, b4 = "Calculate", command=calculate, font=('Arial', 20, 'bold')).pack(b10=10)
    b9 = tk.Label(b5, font=('Arial', 20, 'bold'))
    b9.pack(b10 = 10)
def fonk11():
    b5 = tk.Tk()
    b5.title('Unknown')
    b5.geometry("300x300")
def fonk12():
    b5 = tk.Tk()
    b5.title("Part B")
    b5.geometry("500x500")
    b5.configure(b6 = 'powder blue')
    tk.Label(b5, b4 = "Please Select a method from below", bg='powder blue', font=("Arial", 20, 'bold')).pack(b10=20)
    tk.Button(b5, b4 = "Check Prime", font=('Arial', 20, 'bold'), command=check_prime_no).pack(b10=10)
    tk.Button(b5, b4 = "Radians to Degrees", font=('Arial', 20, 'bold'), command=radian_to_degree).pack(b10=10)
    tk.Button(b5, b4 = "Degrees to Radians", font=('Arial', 20, 'bold'), command=degree_to_radian).pack(b10=10)
    tk.Button(b5, b4 = "Compute Arc Length of an b14", font=('Arial', 20, 'bold'), command=compute_arc_length).pack(b10=10)
    tk.Button(b5, b4 = "Area of Sector", font=('Arial', 20, 'bold'), command=area_of_sector).pack(b10=10)
    tk.Button(b5, b4 = "Unknown", font=('Arial', 20, 'bold'), command=unknown).pack(b10=10)
    b5.mainloop()
if b21 = = "__main__":
    fonk12()