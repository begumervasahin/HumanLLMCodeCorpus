import tkinter as tk
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b1.title("Calculator")
        self.b1.geometry("500x500")
        self.b1.configure(b2 = 'powder blue')
        self.fonk2()
    def fonk2(self):
        tk.Label(self.b1, b3 = "Please Select a method from below", bg='powder blue', font=("Arial",20,'bold')).pack()
        self.fonk3("Check Prime", self.check_prime_number)
        self.fonk3("Radians to Degrees", self.radian_to_degree)
        self.fonk3("Degrees to Radian", self.degree_to_radian)
        self.fonk3("Compute Arc Length", self.compute_arc_length)
        self.fonk3("Area of Sector", self.area_of_sector)
        self.fonk3("Unknown", self.unknown)
    def fonk3(self, b3, command):
        b4 = tk.Button(self.b1, b3=b3, font=('Arial',20,'bold'), command=command)
        b4.pack()
    def fonk4(self):
        self.fonk15("Check Prime Number")
        b5 = tk.StringVar()
        b6 = tk.Entry(self.b19, b21=b5, font=('Arial', 20, 'bold'))
        b6.pack()
        self.fonk17("Calculate", lambda: self.fonk5(b6))
    def fonk5(self, b6):
        b7 = int(b6.get())
        b8 = tk.Label(self.b19, font=('Arial',20,'bold'))
        b8.pack()
        if b7 <= 1:
            b8.config(b3 = f'{b7} is not prime')
        else:
            for b9 in range(2, b7):
                if b7 % b9 = = 0:
                    b8.config(b3 = f'{b7} is not prime')
                    break
            else:
                b8.config(b3 = f'{b7} is prime')
    def fonk6(self):
        self.fonk15('Radian to Degree')
        self.fonk16("Enter Radian Value", self.convert_to_degree)
    def fonk7(self):
        b10 = float(self.b5.get())
        b11 = b10 * 180 / 3.14
        self.b8.config(b3 = f'degrees = {b11}')
    def fonk8(self):
        self.fonk15('Degree to Radian')
        self.fonk16("Enter Degree Value", self.convert_to_radian)
    def fonk9(self):
        b11 = float(self.b5.get())
        b12 = b11 * 3.14 / 180
        self.b8.config(b3 = f'b12 = {b12}')
    def fonk10(self):
        self.fonk15('Compute Arc Length of an Angle')
        self.fonk16("Enter Diameter", self.compute_arc_length_inner, "Please Enter Angle")
    def fonk11(self):
        b13 = float(self.b5.get())
        b14 = float(self.b22.get())
        b15 = 22/7
        if b14 >= 360:
            self.b8.config(b3 = "Angle not possible")
        else:
            b16 = (b15 * b13) * (b14 / 360)
            self.b8.config(b3 = f"Arc Length is: {b16}")
    def fonk12(self):
        self.fonk15('Compute Area Of Sector')
        self.fonk16("Enter Radius", self.compute_area_of_sector_inner, "Please Enter Angle")
    def fonk13(self):
        b17 = float(self.b5.get())
        b14 = float(self.b22.get())
        b18 = (1/2) * b17**2 * b14
        self.b8.config(b3 = f"Area of Sector: {b18}")
    def fonk14(self):
        self.fonk15('Unknown')
    def fonk15(self, title):
        self.b19 = tk.Toplevel(self.b1)
        self.b19.title(title)
        self.b19.geometry("400x400")
        self.b19.configure(b2 = "yellow")
    def fonk16(self, label_text, command, b20 = None):
        tk.Label(self.b19, b3 = label_text, bg='yellow', font=('Arial',15,'bold')).pack()
        self.b5 = tk.StringVar()
        tk.Entry(self.b19, b21 = self.b5, font=('Arial',15,'bold')).pack()
        if b20:
            tk.Label(self.b19, b3 = b20, bg='yellow', font=('Arial',15,'bold')).pack()
            self.b22 = tk.StringVar()
            tk.Entry(self.b19, b21 = self.b22, font=('Arial',15,'bold')).pack()
        self.fonk17("Calculate", command)
    def fonk17(self, b3, command):
        b23 = tk.Button(self.b19, b3=b3, command=command, font=('Arial',20,'bold'))
        b23.pack()
        self.b8 = tk.Label(self.b19, b3="", font=('Arial',20,'bold'))
        self.b8.pack()
def fonk18():
    b24 = tk.Tk()
    b25 = class1(b24)
    b24.mainloop()
if b26 = = "__main__":
    fonk18()