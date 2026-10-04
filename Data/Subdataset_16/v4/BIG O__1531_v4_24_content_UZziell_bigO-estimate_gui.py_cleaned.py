import time
from tkinter import *
from tkinter import messagebox
import functions as fn
def fonk1(frame):
    frame.tkraise()
def fonk2():
    b1 = b16.get("1.0", "end-1c")
    b2 = fn.equation_finder(b1)
    messagebox.showinfo("Result", f"(BIG O notation): {b2[0]}\nClick OK to sketch the graph")
    b7.destroy()
    time.sleep(0.5)
    if b2[1] == '':
        fn.plot(1)
    elif 1 < int(b2[1]) < 10:
        fn.plot(b2[1])
    else:
        print("Not able to plot, power > 9")
def fonk3():
    b3 = b19.get("1.0", "end-1c")
    b4 = b21.get("1.0", "end-1c")
    b5 = fn.equation_finder(b3)
    b6 = fn.equation_finder(b4)
    if b5[1] == '':
        b5[1] = "1"
    if b6[1] == '':
        b6[1] = "1"
    if b5[0] > b6[0]:
        messagebox.showinfo("Comparison Result", f"The 'Second' algorithm is better.\n{b5[0]} > {b6[0]}")
    elif b5[0] < b6[0]:
        messagebox.showinfo("Comparison Result", f"The 'First' algorithm is better.\n{b5[0]} < {b6[0]}")
    else:
        messagebox.showinfo("Comparison Result", f"The b2 of both algorithms is equal: {b5[0]}")
    b7.destroy()
    time.sleep(0.5)
    fn.plot(b5[1], b6[1])
b7 = Tk()
b7.title("BigO Estimation")
b7.geometry('1049x750')
b7.resizable(False, False)
b8 = Frame(b7)
b9 = Frame(b7)
b10 = Frame(b7)
for frame in (b8, b9, b10):
    frame.grid(b11 = 0, b17=0, sticky='news')
b12 = PhotoImage(file="resources/espresso2.png")
Label(b8, b13 = b12).place(x=0, y=0, relwidth=1, relheight=1)
Button(b8, b14 = 'Single', b20="black", fg="white", command=lambda: fonk1(b9)).place(x=20, y=40)
Button(b8, b14 = 'Double', b20="black", fg="white", command=lambda: fonk1(b10)).place(x=20, y=80)
Label(b8, b14 = "Hint\nSingle: Estimates an algorithm b2\nDouble: Compares two algorithms complexities", fg="white", b20="black").place(x=20, y=680)
b15 = PhotoImage(file="resources/sss.png")
Label(b9, b13 = b15).place(x=0, y=0, relwidth=1, relheight=1)
Label(b9, b14 = "Hint: Paste code in the box", b20="black", fg="white").grid(b17=3, b11=0)
b16 = Text(b9, b20="black", fg="white", height=40, width=100)
b16.grid(b17 = 1, b11=1)
b16.insert(END, "\n\b18 = 0\nwhile i < N:\n    print(\"*\", end='')\n    i += 1")
Button(b9, b14 = "Calculate", b20="black", fg="white", command=calculate_handle).grid(b17=1, b11=3)
Button(b9, b14 = 'Back', b20="black", fg="white", command=lambda: fonk1(b8)).grid(b11=3, b17=4)
Label(b10, b13 = b15).place(x=0, y=0, relwidth=1, relheight=1)
b19 = Text(b10, b20="black", fg="white", height=40, width=50)
b19.grid(b17 = 1, b11=1)
b19.insert(END, "\n\b18 = 0\nwhile i < N:\n    print(\"*\", end='')\n    i += 1")
Label(b10, b20 = "black", fg="white", b14="").grid(b17=2, b11=1)
b21 = Text(b10, b20="black", fg="white", height=40, width=50)
b21.grid(b17 = 3, b11=1)
Button(b10, b14 = "Compare", b20="black", fg="white", command=compare_handle).grid(b11=3, columnspan=4)
Button(b10, b14 = 'Back', b20="black", fg="white", command=lambda: fonk1(b8)).place(x=970, y=690)
if fn.is_connected():
    fonk1(b8)
    b7.mainloop()
else:
    messagebox.showerror("No Internet Connection", "Please check your internet connection and try again.")