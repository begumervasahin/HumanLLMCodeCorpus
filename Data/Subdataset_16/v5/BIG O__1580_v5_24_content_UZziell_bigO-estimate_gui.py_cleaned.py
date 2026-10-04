import time
from tkinter import *
from tkinter import messagebox
import functions as fn
def fonk1(frame):
    frame.tkraise()
def fonk2():
    b1 = b21.get("1.0", "end-1c")
    b2 = fn.equation_finder(b1)
    messagebox.showinfo("Result", f"(BIG O notation): {b2[0]}\nClick OK to sketch the graph")
    b12.destroy()
    time.sleep(0.5)
    b3 = b2[1] if b2[1] else '1'
    b4 = int(b3)
    if 1 <= b4 < 10:
        fn.plot(b4)
    else:
        print("Not able to plot, b3 > 9")
def fonk3():
    b5 = b24.get("1.0", "end-1c")
    b6 = b26.get("1.0", "end-1c")
    b7 = fn.equation_finder(b5)
    b8 = fn.equation_finder(b6)
    b9 = b7[1] if b7[1] else "1"
    b10 = b8[1] if b8[1] else "1"
    if b7[0] > b8[0]:
        b11 = f"The 'Second' algorithm is better.\n{b7[0]} > {b8[0]}"
    elif b7[0] < b8[0]:
        b11 = f"The 'First' algorithm is better.\n{b7[0]} < {b8[0]}"
    else:
        b11 = f"The b2 of both algorithms is equal: {b7[0]}"
    messagebox.showinfo("Comparison Result", b11)
    b12.destroy()
    time.sleep(0.5)
    fn.plot(b9, b10)
b12 = Tk()
b12.title("BigO Estimation")
b12.geometry('1049x750')
b12.resizable(False, False)
b13 = Frame(b12)
b14 = Frame(b12)
b15 = Frame(b12)
for frame in (b13, b14, b15):
    frame.grid(b16 = 0, b22=0, sticky='news')
b17 = PhotoImage(file="resources/espresso2.png")
Label(b13, b18 = b17).place(x=0, y=0, relwidth=1, relheight=1)
Button(b13, b19 = 'Single', b25="black", fg="white", command=lambda: fonk1(b14)).place(x=20, y=40)
Button(b13, b19 = 'Double', b25="black", fg="white", command=lambda: fonk1(b15)).place(x=20, y=80)
Label(b13, b19 = "Hint\nSingle: Estimates an algorithm b2\nDouble: Compares two algorithms complexities", fg="white", b25="black").place(x=20, y=680)
b20 = PhotoImage(file="resources/sss.png")
Label(b14, b18 = b20).place(x=0, y=0, relwidth=1, relheight=1)
Label(b14, b19 = "Hint: Paste code in the box", b25="black", fg="white").grid(b22=3, b16=0)
b21 = Text(b14, b25="black", fg="white", height=40, width=100)
b21.grid(b22 = 1, b16=1)
b21.insert(END, "\n\b23 = 0\nwhile i < N:\n    print(\"*\", end='')\n    i += 1")
Button(b14, b19 = "Calculate", b25="black", fg="white", command=calculate_handle).grid(b22=1, b16=3)
Button(b14, b19 = 'Back', b25="black", fg="white", command=lambda: fonk1(b13)).grid(b16=3, b22=4)
Label(b15, b18 = b20).place(x=0, y=0, relwidth=1, relheight=1)
b24 = Text(b15, b25="black", fg="white", height=40, width=50)
b24.grid(b22 = 1, b16=1)
b24.insert(END, "\n\b23 = 0\nwhile i < N:\n    print(\"*\", end='')\n    i += 1")
Label(b15, b25 = "black", fg="white", b19="").grid(b22=2, b16=1)
b26 = Text(b15, b25="black", fg="white", height=40, width=50)
b26.grid(b22 = 3, b16=1)
Button(b15, b19 = "Compare", b25="black", fg="white", command=compare_handle).grid(b16=3, columnspan=4)
Button(b15, b19 = 'Back', b25="black", fg="white", command=lambda: fonk1(b13)).place(x=970, y=690)
if fn.is_connected():
    fonk1(b13)
    b12.mainloop()
else:
    messagebox.showerror("No Internet Connection", "Please check your internet connection and try again.")