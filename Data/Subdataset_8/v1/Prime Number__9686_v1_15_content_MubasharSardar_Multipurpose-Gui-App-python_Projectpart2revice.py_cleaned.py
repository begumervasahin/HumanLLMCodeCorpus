from tkinter import *
from math import pi
def Check_Prime_No():
    Cp = Tk()
    Cp.title("Check Prime Number")
    Cp.geometry("500x500")
    Cp.configure(background='yellow')
    entry1 = StringVar()
    EntryBox = Entry(Cp, textvariable=entry1, font=('Arial', 20, 'bold'))
    EntryBox.pack()
    def primeNumber():
        no = int(entry1.get())
        if no <= 1:
            Label(Cp, text=f'{no} is not prime', font=('Arial', 20, 'bold')).pack()
        else:
            for i in range(2, no):
                if no % i == 0:
                    Label(Cp, text=f'{no} is not prime', font=('Arial', 20, 'bold')).pack()
                    break
            else:
                Label(Cp, text=f'{no} is prime', font=('Arial', 20, 'bold')).pack()
    Btn = Button(Cp, text='Calculate', command=primeNumber, font=('Arial', 20, 'bold'))
    Btn.pack()
def Radian_to_degree():
    Rd = Tk()
    Rd.title('Radian to Degree')
    Rd.geometry("500x500")
    Rd.configure(background='yellow')
    r = StringVar()
    take_input = Entry(Rd, textvariable=r, font=('Arial', 20, 'bold'))
    take_input.pack()
    def radian_to_degree():
        r_value = int(r.get())
        d = r_value * 180 / pi
        Label(Rd, text=f'Degrees = {d}', font=('Arial', 20, 'bold')).pack()
    btn = Button(Rd, text='Calculate', command=radian_to_degree, font=('Arial', 20, 'bold'))
    btn.pack()
def Degree_to_radian():
    Dr = Tk()
    Dr.title('Degree to Radian')
    Dr.geometry("400x400")
    Dr.configure(background="yellow")
    r = StringVar()
    take_input = Entry(Dr, textvariable=r, font=('Arial', 20, 'bold'))
    take_input.pack()
    def degrees_to_radian():
        d_value = int(r.get())
        r = d_value * pi / 180
        Label(Dr, text=f'Radian = {r}', font=('Arial', 20, 'bold')).pack()
    btn = Button(Dr, text="Calculate", command=degrees_to_radian, font=('Arial', 20, 'bold'))
    btn.pack()
def Compute_Arc_Length():
    Cal = Tk()
    Cal.title('Compute Arc Length of an Angle')
    Cal.geometry("400x400")
    Cal.configure(background="yellow")
    d = StringVar()
    a = StringVar()
    Label(Cal, text="Please Enter Values To find Arc Length", bg='yellow', font=('Arial', 15, 'bold')).pack()
    Label(Cal, text="Please Enter Diameter here: ", bg='yellow', font=('Arial', 12, 'bold')).pack()
    entry1 = Entry(Cal, textvariable=d, font=('Arial', 20, 'bold'))
    entry1.pack()
    Label(Cal, text="Please Enter Angle here: ", bg='yellow', font=('Arial', 12, 'bold')).pack()
    entry2 = Entry(Cal, textvariable=a, font=('Arial', 20, 'bold'))
    entry2.pack()
    def arc_length():
        diameter = float(entry1.get())
        angle = float(entry2.get())
        arc_len = (pi * diameter) * (angle / 360)
        Label(Cal, text=f"Arc Length is: {arc_len}", font=('Arial', 15, 'bold')).pack()
    btn = Button(Cal, text="Calculate", command=arc_length, font=('Arial', 20, 'bold'))
    btn.pack()
def Area_of_sector():
    Aos = Tk()
    Aos.title('Compute Area Of Sector')
    Aos.geometry("400x400")
    Aos.configure(background="yellow")
    Aos1 = StringVar()
    Aos2 = StringVar()
    Label(Aos, text="Please Enter Radius Here", bg='yellow', font=('Arial', 20, 'bold')).pack()
    entry1 = Entry(Aos, textvariable=Aos1, font=('Arial', 20, 'bold'))
    entry1.pack()
    Label(Aos, text="Please Enter Angle Here", bg='yellow', font=('Arial', 20, 'bold')).pack()
    entry2 = Entry(Aos, textvariable=Aos2, font=('Arial', 20, 'bold'))
    entry2.pack()
    def area_of_sector():
        radius = float(entry1.get())
        angle = float(entry2.get())
        area = (1 / 2) * radius ** 2 * angle
        Label(Aos, text=f"Area of Sector: {area}", font=('Arial', 20, 'bold')).pack()
    btn = Button(Aos, text="Calculate", command=area_of_sector, font=('Arial', 20, 'bold'))
    btn.pack()
def UnKnown():
    UK = Tk()
    UK.title('Unknown')
    UK.geometry("300x300")
win = Tk()
win.title("Part B")
win.geometry("500x500")
win.configure(background='powder blue')
Label(win, text="Please Select a method from below", bg='powder blue', font=("Arial", 20, 'bold')).pack()
checkprimeno = Button(win, text="Check Prime", font=('Arial', 20, 'bold'), command=Check_Prime_No)
checkprimeno.pack()
radiantodegree = Button(win, text="Radians to Degrees", font=('Arial', 20, 'bold'), command=Radian_to_degree)
radiantodegree.pack()
degreestoradian = Button(win, text="degrees to radian", font=('Arial', 20, 'bold'), command=Degree_to_radian)
degreestoradian.pack()
arc_length = Button(win, text="Compute Arc Length of an angle", font=('Arial', 20, 'bold'), command=Compute_Arc_Length)
arc_length.pack()
area_of_sector = Button(win, text="Area of Sector", font=('Arial', 20, 'bold'), command=Area_of_sector)
area_of_sector.pack()
unknown = Button(win, text="Unknown", font=('Arial', 20, 'bold'), command=UnKnown)
unknown.pack()
win.mainloop()