import time
from tkinter import *
from tkinter import messagebox
import functions as fn
def fonk1(f):
    f.tkraise()
b1 = Tk()
b1.title("BigO Estimation")
b1.geometry('1049x750')
b1.resizable(False, False)
b2 = Frame(b1)
b3 = Frame(b1)
b4 = Frame(b1)
for frame in (b2, b3, b4):
    frame.grid(b5 = 0, b12=0, sticky='news')
b6 = PhotoImage(file="resources/espresso2.png")
b7 = PhotoImage(file="resources/sss.png")
Label(b2, b8 = b6).place(x=0, y=0, relwidth=1, relheight=1)
Button(b2, b9 = 'Single', b17="black", b10="white", command=lambda: fonk1(b3)).place(x=20, y=40)
Button(b2, b9 = 'Double', b17="black", b10="white", command=lambda: fonk1(b4)).place(x=20, y=80)
Label(b2, b9 = "Hint\nSingle: Estimates an algorithm b15\nDouble: Compares two algorithms complexities",
      b10 = "white", b17="black").place(x=20, y=680)
Label(b3, b8 = b7).place(x=0, y=0, relwidth=1, relheight=1)
Label(b3, b9 = "Hint: Paste code in the box", b17="black", b10="white").grid(b12=3, b5=0)
b11 = Text(b3, b17="black", b10="white", height=40, width=100)
b11.grid(b12 = 1, b5=1)
b11.insert(END, """\n\b13 = 0\nwhile i < N:\n    print("*", end='')\n    i += 1""")
def fonk2():
    b14 = b11.get("1.0", "end-1c")
    b15 = fn.equation_finder(b14)
    messagebox.showinfo("TADAAA", f"(BIG O notation): {b15[0]}\nclick OK to sketch the graph")
    b1.destroy()
    time.sleep(0.5)
    if b15[1] == '':
        fn.plot(1)
    elif 1 < int(b15[1]) < 10:
        fn.plot(b15[1])
    else:
        print("Not able to plot, power > 9")
Button(b3, b9 = "Calculate", b17="black", b10="white", command=calc_handle).grid(b12=1, b5=3)
Button(b3, b9 = 'Back', b17="black", b10="white", command=lambda: fonk1(b2)).grid(b5=3, b12=4)
Label(b4, b8 = b7).place(x=0, y=0, relwidth=1, relheight=1)
b16 = Text(b4, b17="black", b10="white", height=40, width=50)
b16.grid(b12 = 1, b5=1)
b16.insert(END, """\n\b13 = 0\nwhile i < N:\n    print("*", end='')\n    i += 1""")
Label(b4, b17 = "black", b10="white", b9="").grid(b12=2, b5=1)
b18 = Text(b4, b17="black", b10="white", height=40, width=50)
b18.grid(b12 = 3, b5=1)
def fonk3():
    b19 = b16.get("1.0", "end-1c")
    b20 = b18.get("1.0", "end-1c")
    b21 = fn.equation_finder(b19)
    b22 = fn.equation_finder(b20)
    if b21[1] == '':
        b21[1] = "1"
    if b22[1] == '':
        b22[1] = '1'
    if b21[0] > b22[0]:
        messagebox.showinfo("Result", f"It seems 'Second' algorithm is better.\n {b21[0]} > {b22[0]}")
    elif b21[0] < b22[0]:
        messagebox.showinfo("Result", f"It seems 'First' algorithm is better.\n {b21[0]} < {b22[0]}")
    else:
        messagebox.showinfo("Result", f"Both algorithms have equal b15: {b21[0]}")
    b1.destroy()
    time.sleep(0.5)
    fn.plot(b21[1], b22[1])
Button(b4, b9 = "Compare", b17="black", b10="white", command=compare_handle).grid(b5=3, columnspan=4)
Button(b4, b9 = 'Back', b17="black", b10="white", command=lambda: fonk1(b2)).place(x=970, y=690)
if fn.is_connected():
    fonk1(b2)
    b1.mainloop()
else:
    messagebox.showerror("No Internet Connection", "Please check your internet connection and try again.")