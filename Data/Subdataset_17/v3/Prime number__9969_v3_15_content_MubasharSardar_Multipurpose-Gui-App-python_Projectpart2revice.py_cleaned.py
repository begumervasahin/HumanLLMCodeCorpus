import tkinter as tk
from tkinter import messagebox
def create_window(title, width, height, bg_color):
    window = tk.Tk()
    window.title(title)
    window.geometry(f"{width}x{height}")
    window.configure(background=bg_color)
    return window
def check_prime_no():
    def prime_number():
        try:
            number = int(entry.get())
            if number <= 1:
                result = False
            else:
                result = all(number % i != 0 for i in range(2, int(number ** 0.5) + 1))
            result_text = f"{number} is prime" if result else f"{number} is not prime"
            result_label.config(text=result_text)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer")
    window = create_window("Check Prime Number", 500, 500, 'yellow')
    entry = tk.StringVar()
    tk.Entry(window, textvariable=entry, font=('Arial', 20, 'bold')).pack(pady=20)
    tk.Button(window, text='Calculate', command=prime_number, font=('Arial', 20, 'bold')).pack(pady=10)
    result_label = tk.Label(window, font=('Arial', 20, 'bold'))
    result_label.pack(pady=10)
    window.mainloop()
def radian_to_degree():
    def convert():
        try:
            radians = float(entry.get())
            degrees = radians * 180 / 3.14
            result_label.config(text=f"Degrees = {degrees:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
    window = create_window('Radian to Degree', 500, 500, 'yellow')
    tk.Label(window, text="Enter Radian value to convert into degrees", bg='yellow', font=('Arial', 15, 'bold')).pack(pady=20)
    entry = tk.StringVar()
    tk.Entry(window, textvariable=entry, font=('Arial', 15, 'bold')).pack(pady=20)
    tk.Button(window, text='Calculate', font=('Arial', 20, 'bold'), command=convert).pack(pady=10)
    result_label = tk.Label(window, font=('Arial', 15, 'bold'))
    result_label.pack(pady=10)
    window.mainloop()
def degree_to_radian():
    def convert():
        try:
            degrees = float(entry.get())
            radians = degrees * 3.14 / 180
            result_label.config(text=f"Radians = {radians:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")
    window = create_window('Degree to Radian', 500, 500, 'yellow')
    tk.Label(window, text="Enter Degrees value to convert into radians", bg='yellow', font=('Arial', 15, 'bold')).pack(pady=20)
    entry = tk.StringVar()
    tk.Entry(window, textvariable=entry, font=('Arial', 15, 'bold')).pack(pady=20)
    tk.Button(window, text='Calculate', font=('Arial', 20, 'bold'), command=convert).pack(pady=10)
    result_label = tk.Label(window, font=('Arial', 15, 'bold'))
    result_label.pack(pady=10)
    window.mainloop()
def compute_arc_length():
    def calculate():
        try:
            diameter = float(diameter_entry.get())
            angle = float(angle_entry.get())
            if angle >= 360:
                result_label.config(text="Angle not possible")
                return
            arc_length = (3.14 * diameter) * (angle / 360)
            result_label.config(text=f"Arc Length = {arc_length:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers")
    window = create_window('Compute Arc Length of an Angle', 500, 500, 'yellow')
    tk.Label(window, text="Please Enter Values To find Arc Length", bg='yellow', font=('Arial', 15, 'bold')).pack(pady=20)
    tk.Label(window, text="Please Enter Diameter here:", bg='yellow', font=('Arial', 12, 'bold')).pack(pady=10)
    diameter_entry = tk.Entry(window, font=('Arial', 20, 'bold'))
    diameter_entry.pack(pady=10)
    tk.Label(window, text="Please Enter Angle here:", bg='yellow', font=('Arial', 12, 'bold')).pack(pady=10)
    angle_entry = tk.Entry(window, font=('Arial', 20, 'bold'))
    angle_entry.pack(pady=10)
    tk.Button(window, text="Calculate", command=calculate, font=('Arial', 20, 'bold')).pack(pady=10)
    result_label = tk.Label(window, font=('Arial', 15, 'bold'))
    result_label.pack(pady=10)
    window.mainloop()
def area_of_sector():
    def calculate():
        try:
            radius = float(radius_entry.get())
            angle = float(angle_entry.get())
            area = 0.5 * radius * radius * (angle * 3.14 / 180)
            result_label.config(text=f"Area of Sector = {area:.2f}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers")
    window = create_window('Compute Area Of Sector', 500, 500, 'yellow')
    tk.Label(window, text="Please Enter Radius Here", bg='yellow', font=('Arial', 20, 'bold')).pack(pady=20)
    radius_entry = tk.Entry(window, font=('Arial', 20, 'bold'))
    radius_entry.pack(pady=10)
    tk.Label(window, text="Please Enter Angle Here", bg='yellow', font=('Arial', 20, 'bold')).pack(pady=10)
    angle_entry = tk.Entry(window, font=('Arial', 20, 'bold'))
    angle_entry.pack(pady=10)
    tk.Button(window, text="Calculate", command=calculate, font=('Arial', 20, 'bold')).pack(pady=10)
    result_label = tk.Label(window, font=('Arial', 20, 'bold'))
    result_label.pack(pady=10)
    window.mainloop()
def unknown():
    window = create_window('Unknown', 300, 300, 'powder blue')
    tk.Label(window, text="Unknown Operation", bg='powder blue', font=("Arial", 20, 'bold')).pack(pady=20)
    window.mainloop()
def main_window():
    window = create_window("Part B", 500, 500, 'powder blue')
    tk.Label(window, text="Please Select a method from below", bg='powder blue', font=("Arial", 20, 'bold')).pack(pady=20)
    tk.Button(window, text="Check Prime", font=('Arial', 20, 'bold'), command=check_prime_no).pack(pady=10)
    tk.Button(window, text="Radians to Degrees", font=('Arial', 20, 'bold'), command=radian_to_degree).pack(pady=10)
    tk.Button(window, text="Degrees to Radians", font=('Arial', 20, 'bold'), command=degree_to_radian).pack(pady=10)
    tk.Button(window, text="Compute Arc Length of an angle", font=('Arial', 20, 'bold'), command=compute_arc_length).pack(pady=10)
    tk.Button(window, text="Area of Sector", font=('Arial', 20, 'bold'), command=area_of_sector).pack(pady=10)
    tk.Button(window, text="Unknown", font=('Arial', 20, 'bold'), command=unknown).pack(pady=10)
    window.mainloop()
if __name__ == "__main__":
    main_window()