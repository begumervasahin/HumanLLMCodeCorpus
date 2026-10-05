import tkinter as tk
from math import pi
def fonk1():
    b1 = tk.Tk()
    b1.title("Check Prime Number")
    b1.geometry("500x500")
    b1.configure(b2 = 'yellow')
    b3 = tk.StringVar()
    b4 = tk.Entry(b1, textvariable=b3, font=('Arial', 20, 'bold'))
    b4.pack()
    def fonk2():
        b5 = int(b3.get())
        if b5 <= 1:
            b7["b17"] = f'{b5} is not prime'
        else:
            for b6 in range(2, b5):
                if b5 % b6 = = 0:
                    b7["b17"] = f'{b5} is not prime'
                    break
            else:
                b7["b17"] = f'{b5} is prime'
    b7 = tk.Label(b1, font=('Arial', 20, 'bold'))
    b7.pack()
    b8 = tk.Button(b1, b17='Calculate', command=prime_number, font=('Arial', 20, 'bold'))
    b8.pack()
def fonk3():
    b1 = tk.Tk()
    b1.title('b15 to Degree')
    b1.geometry("500x500")
    b1.configure(b2 = 'yellow')
    b9 = tk.StringVar()
    b4 = tk.Entry(b1, textvariable=b9, font=('Arial', 20, 'bold'))
    b4.pack()
    def fonk4():
        b10 = float(b9.get())
        b11 = b10 * 180 / pi
        b7["b17"] = f'b12 = {b11}'
    b7 = tk.Label(b1, font=('Arial', 20, 'bold'))
    b7.pack()
    b8 = tk.Button(b1, b17='Calculate', command=convert, font=('Arial', 20, 'bold'))
    b8.pack()
def fonk5():
    b1 = tk.Tk()
    b1.title('Degree to b15')
    b1.geometry("400x400")
    b1.configure(b2 = "yellow")
    b13 = tk.StringVar()
    b4 = tk.Entry(b1, textvariable=b13, font=('Arial', 20, 'bold'))
    b4.pack()
    def fonk6():
        b11 = float(b13.get())
        b14 = b11 * pi / 180
        b7["b17"] = f'b15 = {b14}'
    b7 = tk.Label(b1, font=('Arial', 20, 'bold'))
    b7.pack()
    b8 = tk.Button(b1, b17="Calculate", command=convert, font=('Arial', 20, 'bold'))
    b8.pack()
def fonk7():
    b1 = tk.Tk()
    b1.title('Compute Arc Length of an Angle')
    b1.geometry("400x400")
    b1.configure(b2 = "yellow")
    b13 = tk.StringVar()
    b16 = tk.StringVar()
    tk.Label(b1, b17 = "Please Enter Values To find Arc Length", bg='yellow', font=('Arial', 15, 'bold')).pack()
    tk.Label(b1, b17 = "Please Enter Diameter here: ", bg='yellow', font=('Arial', 12, 'bold')).pack()
    b18 = tk.Entry(b1, textvariable=b13, font=('Arial', 20, 'bold'))
    b18.pack()
    tk.Label(b1, b17 = "Please Enter Angle here: ", bg='yellow', font=('Arial', 12, 'bold')).pack()
    b19 = tk.Entry(b1, textvariable=b16, font=('Arial', 20, 'bold'))
    b19.pack()
    def fonk8():
        b20 = float(b18.get())
        b21 = float(b19.get())
        b22 = (pi * b20) * (b21 / 360)
        b7["b17"] = f"Arc Length is: {b22}"
    b7 = tk.Label(b1, font=('Arial', 15, 'bold'))
    b7.pack()
    b8 = tk.Button(b1, b17="Calculate", command=arc_length, font=('Arial', 20, 'bold'))
    b8.pack()
def fonk9():
    b1 = tk.Tk()
    b1.title('Compute Area Of Sector')
    b1.geometry("400x400")
    b1.configure(b2 = "yellow")
    b23 = tk.StringVar()
    b24 = tk.StringVar()
    tk.Label(b1, b17 = "Please Enter Radius Here", bg='yellow', font=('Arial', 20, 'bold')).pack()
    b18 = tk.Entry(b1, textvariable=b23, font=('Arial', 20, 'bold'))
    b18.pack()
    tk.Label(b1, b17 = "Please Enter Angle Here", bg='yellow', font=('Arial', 20, 'bold')).pack()
    b19 = tk.Entry(b1, textvariable=b24, font=('Arial', 20, 'bold'))
    b19.pack()
    def fonk10():
        b25 = float(b18.get())
        b21 = float(b19.get())
        b26 = (1 / 2) * b25 ** 2 * b21
        b7["b17"] = f"Area of Sector: {b26}"
    b7 = tk.Label(b1, font=('Arial', 20, 'bold'))
    b7.pack()
    b8 = tk.Button(b1, b17="Calculate", command=calculate_area, font=('Arial', 20, 'bold'))
    b8.pack()
def fonk11():
    b1 = tk.Tk()
    b1.title('Unknown')
    b1.geometry("300x300")
def fonk12():
    b27 = tk.Tk()
    b27.title("Part B")
    b27.geometry("500x500")
    b27.configure(b2 = 'powder blue')
    tk.Label(b27, b17 = "Please Select a method from below", bg='powder blue', font=("Arial", 20, 'bold')).pack()
    tk.Button(b27, b17 = "Check Prime", font=('Arial', 20, 'bold'), command=check_prime_number).pack()
    tk.Button(b27, b17 = "Radians to b12", font=('Arial', 20, 'bold'), command=radian_to_degree).pack()
    tk.Button(b27, b17 = "b12 to b15", font=('Arial', 20, 'bold'), command=degree_to_radian).pack()
    tk.Button(b27, b17 = "Compute Arc Length of an b21", font=('Arial', 20, 'bold'), command=compute_arc_length).pack()
    tk.Button(b27, b17 = "Area of Sector", font=('Arial', 20, 'bold'), command=area_of_sector).pack()
    tk.Button(b27, b17 = "Unknown", font=('Arial', 20, 'bold'), command=unknown).pack()
    b27.mainloop()
if b28 = = "__main__":
    fonk12()