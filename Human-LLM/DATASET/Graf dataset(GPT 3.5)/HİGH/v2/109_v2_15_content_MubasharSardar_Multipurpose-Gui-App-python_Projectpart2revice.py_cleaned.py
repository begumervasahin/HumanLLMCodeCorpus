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
            b7["b20"] = f'{b5} is not prime'
        else:
            for b6 in range(2, b5):
                if b5 % b6 = = 0:
                    b7["b20"] = f'{b5} is not prime'
                    break
            else:
                b7["b20"] = f'{b5} is prime'
    b7 = tk.Label(b1, font=('Arial', 20, 'bold'))
    b7.pack()
    b8 = tk.Button(b1, b20='Calculate', command=prime_number, font=('Arial', 20, 'bold'))
    b8.pack()
def fonk3():
    b9 = tk.Tk()
    b9.title('b17 to Degree')
    b9.geometry("500x500")
    b9.configure(b2 = 'yellow')
    b10 = tk.StringVar()
    b4 = tk.Entry(b9, textvariable=b10, font=('Arial', 20, 'bold'))
    b4.pack()
    def fonk4():
        b11 = float(b10.get())
        b12 = b11 * 180 / pi
        b7["b20"] = f'b13 = {b12}'
    b7 = tk.Label(b9, font=('Arial', 20, 'bold'))
    b7.pack()
    b8 = tk.Button(b9, b20='Calculate', command=convert, font=('Arial', 20, 'bold'))
    b8.pack()
def fonk5():
    b14 = tk.Tk()
    b14.title('Degree to b17')
    b14.geometry("400x400")
    b14.configure(b2 = "yellow")
    b15 = tk.StringVar()
    b4 = tk.Entry(b14, textvariable=b15, font=('Arial', 20, 'bold'))
    b4.pack()
    def fonk6():
        b12 = float(b15.get())
        b16 = b12 * pi / 180
        b7["b20"] = f'b17 = {b16}'
    b7 = tk.Label(b14, font=('Arial', 20, 'bold'))
    b7.pack()
    b8 = tk.Button(b14, b20="Calculate", command=convert, font=('Arial', 20, 'bold'))
    b8.pack()
def fonk7():
    b18 = tk.Tk()
    b18.title('Compute Arc Length of an Angle')
    b18.geometry("400x400")
    b18.configure(b2 = "yellow")
    b15 = tk.StringVar()
    b19 = tk.StringVar()
    tk.Label(b18, b20 = "Please Enter Values To find Arc Length", bg='yellow', font=('Arial', 15, 'bold')).pack()
    tk.Label(b18, b20 = "Please Enter Diameter here: ", bg='yellow', font=('Arial', 12, 'bold')).pack()
    b21 = tk.Entry(b18, textvariable=b15, font=('Arial', 20, 'bold'))
    b21.pack()
    tk.Label(b18, b20 = "Please Enter Angle here: ", bg='yellow', font=('Arial', 12, 'bold')).pack()
    b22 = tk.Entry(b18, textvariable=b19, font=('Arial', 20, 'bold'))
    b22.pack()
    def fonk8():
        b23 = float(b21.get())
        b24 = float(b22.get())
        b25 = (pi * b23) * (b24 / 360)
        b7["b20"] = f"Arc Length is: {b25}"
    b7 = tk.Label(b18, font=('Arial', 15, 'bold'))
    b7.pack()
    b8 = tk.Button(b18, b20="Calculate", command=arc_length, font=('Arial', 20, 'bold'))
    b8.pack()
def fonk9():
    b26 = tk.Tk()
    b26.title('Compute Area Of Sector')
    b26.geometry("400x400")
    b26.configure(b2 = "yellow")
    b27 = tk.StringVar()
    b28 = tk.StringVar()
    tk.Label(b26, b20 = "Please Enter Radius Here", bg='yellow', font=('Arial', 20, 'bold')).pack()
    b21 = tk.Entry(b26, textvariable=b27, font=('Arial', 20, 'bold'))
    b21.pack()
    tk.Label(b26, b20 = "Please Enter Angle Here", bg='yellow', font=('Arial', 20, 'bold')).pack()
    b22 = tk.Entry(b26, textvariable=b28, font=('Arial', 20, 'bold'))
    b22.pack()
    def fonk10():
        b29 = float(b21.get())
        b24 = float(b22.get())
        b30 = (1 / 2) * b29 ** 2 * b24
        b7["b20"] = f"Area of Sector: {b30}"
    b7 = tk.Label(b26, font=('Arial', 20, 'bold'))
    b7.pack()
    b8 = tk.Button(b26, b20="Calculate", command=calculate_area, font=('Arial', 20, 'bold'))
    b8.pack()
def fonk11():
    b31 = tk.Tk()
    b31.title('Unknown')
    b31.geometry("300x300")
def fonk12():
    b32 = tk.Tk()
    b32.title("Part B")
    b32.geometry("500x500")
    b32.configure(b2 = 'powder blue')
    tk.Label(b32, b20 = "Please Select a method from below", bg='powder blue', font=("Arial", 20, 'bold')).pack()
    tk.Button(b32, b20 = "Check Prime", font=('Arial', 20, 'bold'), command=check_prime_number).pack()
    tk.Button(b32, b20 = "Radians to b13", font=('Arial', 20, 'bold'), command=radian_to_degree).pack()
    tk.Button(b32, b20 = "b13 to b17", font=('Arial', 20, 'bold'), command=degree_to_radian).pack()
    tk.Button(b32, b20 = "Compute Arc Length of an b24", font=('Arial', 20, 'bold'), command=compute_arc_length).pack()
    tk.Button(b32, b20 = "Area of Sector", font=('Arial', 20, 'bold'), command=area_of_sector).pack()
    tk.Button(b32, b20 = "Unknown", font=('Arial', 20, 'bold'), command=unknown).pack()
    b32.mainloop()
if b33 = = "__main__":
    fonk12()