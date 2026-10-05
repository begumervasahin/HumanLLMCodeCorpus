import time
from tkinter import *
from tkinter import messagebox
import functions as fn
def fonk1(frame):
    frame.tkraise()
def fonk2():
    b1 = b15.get("1.0", "end-1c")
    b2 = fn.equation_finder(b1)
    messagebox.showinfo("Big O Notation", f"(BIG O notation): {b2[0]}\nClick OK to sketch the graph")
    b7.destroy()
    time.sleep(0.5)
    if b2[1] == '':
        fn.plot(1)
    elif 1 < int(b2[1]) < 10:
        fn.plot(b2[1])
    else:
        print("Not able to plot, power > 9")
def fonk3():
    b3 = b17.get("1.0", "end-1c")
    b4 = b19.get("1.0", "end-1c")
    b5 = fn.equation_finder(b3)
    b6 = fn.equation_finder(b4)
    if b5[1] == '':
        b5[1] = "1"
    if b6[1] == '':
        b6[1] = '1'
    if b5[0] > b6[0]:
        messagebox.showinfo("Comparison Result",
                            f"'Second' algorithm is better.\n{b5[0]} > {b6[0]}")
    elif b5[0] < b6[0]:
        messagebox.showinfo("Comparison Result",
                            f"'First' algorithm is better.\n{b5[0]} < {b6[0]}")
    else:
        messagebox.showinfo("Comparison Result", f"Both algorithms have equal b2: {b5[0]}")
    b7.destroy()
    time.sleep(0.5)
    fn.plot(b5[1], b6[1])
b7 = Tk()
b7.title("Big O estimation")
b7.geometry('1049x750')
b7.resizable(False, False)
b8 = Frame(b7)
b9 = Frame(b7)
b10 = Frame(b7)
for frame in (b8, b9, b10):
    frame.grid(b11 = 0, b16=0, sticky='news')
Label(b8, b12 = fn.photo).place(x=0, y=0, relwidth=1, relheight=1)
Button(b8, b13 = ' Single', b18="black", b14="white", command=lambda: fonk1(b9)).place(x=20, y=40)
Button(b8, b13 = 'Double', b18="black", b14="white", command=lambda: fonk1(b10)).place(x=20, y=80)
Label(b8, b13 = "Hint\n"
               "Single: Estimates an algorithm b2\n"
               "Double: Compares two algorithms complexities", b14 = "white", b18="black").place(x=20, y=680)
Label(b9, b12 = fn.photo_earth).place(x=0, y=0, relwidth=1, relheight=1)
Label(b9, b13 = "Hint: Paste code in the box", b18="black", b14="white").grid(b16=3, b11=0)
b15 = Text(b9, b18="black", b14="white", height=40, width=100)
b15.grid(b16 = 1, b11=1)
b15.insert(END, fn.default_code)
Button(b9, b13 = "Calculate", b18="black", b14="white", command=calculate_complexity).grid(b16=1, b11=3)
Button(b9, b13 = 'Back', b18="black", b14="white", command=lambda: fonk1(b8)).grid(b11=3, b16=4)
Label(b10, b12 = fn.photo_earth).place(x=0, y=0, relwidth=1, relheight=1)
b17 = Text(b10, b18="black", b14="white", height=40, width=50)
b17.grid(b16 = 1, b11=1)
b17.insert(END, fn.default_code)
Label(b10, b18 = "black", b14="white", b13="").grid(b11=10, b16=10)
b19 = Text(b10, b18="black", b14="white", height=40, width=50)
b19.grid(b16 = 3, b11=1)
Button(b10, b13 = "Compare", b18="black", b14="white", command=compare_complexities).grid(b11=3, columnspan=4)
Button(b10, b13 = 'back', b18="black", b14="white", command=lambda: fonk1(b8)).place(x=970, y=690)
if fn.is_connected():
    fonk1(b8)
    b7.mainloop()
else:
    messagebox.showerror("No Internet Connection", "Please check your internet connection and try again.")