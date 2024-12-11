import time
from tkinter import *
from tkinter import messagebox
import functions as fn
def fonk1(b8):
    b8.tkraise()
b1 = Tk()
b1.title("BigO estimation")
b1.geometry('1049x750')
b1.resizable(False, False)
b2 = PhotoImage(file="resources/espresso2.png")
b3 = PhotoImage(file="resources/sss.png")
b4 = "Hint: Paste code in the box"
b5 = "Back"
b6 = "Calculate"
b7 = "Compare"
a1 = 1049
a2 = 750
def fonk2(parent):
    b8 = Frame(parent, bg="black")
    b8.place(b9 = 0, b17=0, relwidth=1, relheight=1)
    return b8
b10 = fonk2(b1)
b11 = fonk2(b1)
b12 = fonk2(b1)
def fonk3(parent, width, height):
    b13 = Text(parent, bg="black", b19="white", height=height, width=width)
    b13.grid(b14 = 1, row=1)
    return b13
def fonk4(parent, b18, command, b9 = 20, b17=40):
    b15 = Button(parent, b18=b18, bg="black", b19="white", command=command)
    b15.place(b9 = b9, b17=b17)
    return b15
Label(b10, b16 = b2).place(b9=0, b17=0, relwidth=1, relheight=1)
fonk4(b10, ' Single', lambda: fonk1(b11))
fonk4(b10, 'Double', lambda: fonk1(b12), b17 = 80)
Label(b10, b18 = "Hint\n"
               "Single: Estimates an algorithm b24\n"
               "Double: Compares two algorithms complexities", b19 = "white", bg="black").place(b9=20, b17=680)
Label(b11, b16 = b3).place(b9=0, b17=0, relwidth=1, relheight=1)
b20 = Label(b11, b18=b4, bg="black", b19="white")
b20.grid(b14 = 3, row=0)
b21 = fonk3(b11, width=100, height=40)
b21.insert(END, "b22 = 0\nwhile b22 < N:\n    print('*', end='')\n    b22 += 1")
def fonk5():
    b23 = b21.get("1.0", "end-1c")
    b24 = fn.equation_finder(b23)
    messagebox.showinfo("Result",
                        f"(BIG O notation): {b24[0]}\n"
                        f"Click OK to sketch the graph")
    b1.destroy()
    time.sleep(0.5)
    if b24[1] == '':
        fn.plot(1)
    elif 1 < int(b24[1]) < 10:
        fn.plot(b24[1])
    else:
        print("Not able to plot, power > 9")
fonk4(b11, b6, calc_handle, b17 = 250)
fonk4(b11, b5, lambda: fonk1(b10), b9 = 950, b17=690)
Label(b12, b16 = b3).place(b9=0, b17=0, relwidth=1, relheight=1)
b25 = fonk3(b12, width=50, height=40)
b26 = Label(b12, bg="black", b19="white", b18="")
b26.grid(b14 = 2, row=1)
b27 = fonk3(b12, width=50, height=40)
def fonk6():
    b28 = b25.get("1.0", "end-1c")
    b29 = b27.get("1.0", "end-1c")
    b30 = fn.equation_finder(b28)
    b31 = fn.equation_finder(b29)
    if b30[1] == '':
        b30[1] = "1"
    if b31[1] == '':
        b31[1] = '1'
    if b30[0] > b31[0]:
        messagebox.showinfo("Result",
                            f"It seems the 'Second' algorithm is better.\n {b30[0]} > {b31[0]}")
    elif b30[0] < b31[0]:
        messagebox.showinfo("Result",
                            f"It seems the 'First' algorithm is better.\n {b30[0]} < {b31[0]}")
    else:
        messagebox.showinfo("Result", f"It seems the order of both algorithms are equal to {b30[0]}")
    b1.destroy()
    time.sleep(0.5)
    fn.plot(b30[1], b31[1])
fonk4(b12, b7, compare_handle, b17 = 250, b9=450)
fonk4(b12, b5, lambda: fonk1(b10), b9 = 950, b17=690)
if fn.is_connected():
    fonk1(b10)
    b1.mainloop()
else:
    messagebox.showerror("No Internet Connection", "Please check your internet connection and try again.")