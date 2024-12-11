import time
from tkinter import *
from tkinter import messagebox
import functions as fn
def fonk1(frame):
    frame.tkraise()
b1 = Tk()
b1.title("BigO estimation")
b1.geometry('1049x750')
b1.resizable(False, False)
b2 = Frame(b1)
b3 = Frame(b1)
b4 = Frame(b1)
for frame in (b2, b3, b4):
    frame.grid(b5 = 0, b12=0, sticky='news')
b6 = PhotoImage(file="resources/espresso2.png")
Label(b2, b7 = b6).place(x=0, y=0, relwidth=1, relheight=1)
Button(b2, b8 = ' Single', bg="black", b9="white", command=lambda: fonk1(b3)).place(x=20, y=40)
Button(b2, b8 = 'Double', bg="black", b9="white", command=lambda: fonk1(b4)).place(x=20, y=80)
Label(b2, b8 = "Hint\n"
               "Single: Estimates an algorithm b16\n"
               "Double: Compares two algorithms complexities", b9 = "white", bg="black").place(x=20, y=680)
b10 = PhotoImage(file="resources/sss.png")
Label(b3, b7 = b10).place(x=0, y=0, relwidth=1, relheight=1)
b11 = Label(b3, b8="Hint: Paste code in the box", bg="black", b9="white")
b11.grid(b12 = 3, b5=0)
b13 = Text(b3, bg="black", b9="white", height=40, width=100)
b13.grid(b12 = 1, b5=1)
b13.insert(END, """
a1 = 0
while a1 < N:
    print("*", b14 = '')
    a1 += 1
""")
def fonk2():
    b15 = b13.get("1.0", "b14-1c")
    b16 = fn.equation_finder(b15)
    messagebox.showinfo("TADDDDDAAAAAAAAAAAAA",
                        f"(BIG O notation): {b16[0]}\n"
                        f"click OK to sketch the graph")
    b1.destroy()
    time.sleep(0.5)
    if b16[1] == '':
        fn.plot(1)
    elif 1 < int(b16[1]) < 10:
        fn.plot(b16[1])
    else:
        print("Not able to plot, power > 9")
b17 = Button(b3, b8="Calculate", bg="black", b9="white", command=calc_handle)
b17.grid(b12 = 1, b5=3)
Button(b3, b8 = 'Back', bg="black", b9="white", command=lambda: fonk1(b2)).grid(b5=3, b12=4)
Label(b3, b8 = "", bg="black", b9="white").grid(b5=10, b12=10)
Label(b4, b7 = b10).place(x=0, y=0, relwidth=1, relheight=1)
b18 = Text(b4, bg="black", b9="white", height=40, width=50)
b18.grid(b12 = 1, b5=1)
b18.insert(END, """
a1 = 0
while a1 < N:
    print("*", b14 = '')
    a1 += 1
""")
b19 = Label(b4, bg="black", b9="white", b8="")
b19.grid(b12 = 2, b5=1)
b20 = Text(b4, bg="black", b9="white", height=40, width=50)
b20.grid(b12 = 3, b5=1)
def fonk3():
    b21 = b18.get("1.0", "b14-1c")
    b22 = b20.get("1.0", "b14-1c")
    b23 = fn.equation_finder(b21)
    b24 = fn.equation_finder(b22)
    if b23[1] == '':
        b23[1] = "1"
    if b24[1] == '':
        b24[1] = '1'
    if b23[0] > b24[0]:
        messagebox.showinfo("Well WEll WELL...",
                            f"It seems 'Second' algorithm is better.\n {b23[0]} > {b24[0]}")
    elif b23[0] < b24[0]:
        messagebox.showinfo("Well WEll WELL...",
                            f"It seems 'First' algorithm is better.\n {b23[0]} < {b24[0]}")
    else:
        messagebox.showinfo("Well WEll WELL...", f"It seems order of both algorithms are equal to {b23[0]}")
    b1.destroy()
    time.sleep(0.5)
    fn.plot(b23[1], b24[1])
b25 = Button(b4, b8="Compare", bg="black", b9="white", command=compare_handle)
b25.grid(b5 = 3, columnspan=4)
Button(b4, b8 = 'back', bg="black", b9="white", command=lambda: fonk1(b2)).place(x=970, y=690)
if fn.is_connected():
    fonk1(b2)
    b1.mainloop()
else:
    messagebox.showerror("No Internet Connection", "Please check your internet connection and try again.")