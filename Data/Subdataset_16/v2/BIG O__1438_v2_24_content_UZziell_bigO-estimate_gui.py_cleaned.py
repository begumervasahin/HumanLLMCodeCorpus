import time
from tkinter import *
from tkinter import messagebox
import functions as fn
def fonk1(frame):
    frame.tkraise()
def fonk2(b19):
    b19.title("BigO Estimation")
    b19.geometry('1049x750')
    b19.resizable(False, False)
def fonk3(b19):
    b1 = {}
    b1['home'] = Frame(b19)
    b1['single'] = Frame(b19)
    b1['comparison'] = Frame(b19)
    for frame in b1.values():
        frame.grid(b2 = 0, b7=0, sticky='news')
    return b1
def fonk4(frame, b20, raise_frame_func):
    Label(frame, b3 = b20).place(x=0, y=0, relwidth=1, relheight=1)
    Button(frame, b4 = 'Single', b10="black", b5="white", command=lambda: raise_frame_func('single')).place(x=20, y=40)
    Button(frame, b4 = 'Double', b10="black", b5="white", command=lambda: raise_frame_func('comparison')).place(x=20, y=80)
    Label(frame, b4 = "Hint\nSingle: Estimates an algorithm b13\nDouble: Compares two algorithms complexities",
          b5 = "white", b10="black").place(x=20, y=680)
def fonk5(frame, b21, handle_calculate, raise_frame_func):
    Label(frame, b3 = b21).place(x=0, y=0, relwidth=1, relheight=1)
    Label(frame, b4 = "Hint: Paste code in the box", b10="black", b5="white").grid(b7=3, b2=0)
    b6 = Text(frame, b10="black", b5="white", height=40, width=100)
    b6.grid(b7 = 1, b2=1)
    b6.insert(END, """\n\b8 = 0\nwhile i < N:\n    print("*", end='')\n    i += 1""")
    Button(frame, b4 = "Calculate", b10="black", b5="white", command=handle_calculate).grid(b7=1, b2=3)
    Button(frame, b4 = 'Back', b10="black", b5="white", command=lambda: raise_frame_func('home')).grid(b2=3, b7=4)
    return b6
def fonk6(frame, b21, handle_compare, raise_frame_func):
    Label(frame, b3 = b21).place(x=0, y=0, relwidth=1, relheight=1)
    b9 = Text(frame, b10="black", b5="white", height=40, width=50)
    b9.grid(b7 = 1, b2=1)
    b9.insert(END, """\n\b8 = 0\nwhile i < N:\n    print("*", end='')\n    i += 1""")
    Label(frame, b10 = "black", b5="white", b4="").grid(b7=2, b2=1)
    b11 = Text(frame, b10="black", b5="white", height=40, width=50)
    b11.grid(b7 = 3, b2=1)
    Button(frame, b4 = "Compare", b10="black", b5="white", command=handle_compare).grid(b2=3, columnspan=4)
    Button(frame, b4 = 'Back', b10="black", b5="white", command=lambda: raise_frame_func('home')).place(x=970, y=690)
    return b9, b11
def fonk7():
    b12 = b22.get("1.0", "end-1c")
    b13 = fn.equation_finder(b12)
    messagebox.showinfo("Result", f"(BIG O notation): {b13[0]}\nClick OK to sketch the graph")
    b19.destroy()
    time.sleep(0.5)
    fn.plot(b13[1] if 1 < int(b13[1]) < 10 else 1)
def fonk8():
    b14 = comparison_text_entry1.get("1.0", "end-1c")
    b15 = b23.get("1.0", "end-1c")
    b16 = fn.equation_finder(b14)
    b17 = fn.equation_finder(b15)
    b16[1] = b16[1] or "1"
    b17[1] = b17[1] or "1"
    if b16[0] > b17[0]:
        messagebox.showinfo("Result", f"The second algorithm is better.\n {b16[0]} > {b17[0]}")
    elif b16[0] < b17[0]:
        messagebox.showinfo("Result", f"The first algorithm is better.\n {b16[0]} < {b17[0]}")
    else:
        messagebox.showinfo("Result", f"Both algorithms have equal b13: {b16[0]}")
    b19.destroy()
    time.sleep(0.5)
    fn.plot(b16[1], b17[1])
if b18 = = "__main__":
    b19 = Tk()
    fonk2(b19)
    b1 = fonk3(b19)
    b20 = PhotoImage(file="resources/espresso2.png")
    b21 = PhotoImage(file="resources/sss.png")
    fonk4(b1['home'], b20, raise_frame)
    b22 = fonk5(b1['single'], b21, handle_calculate_single, raise_frame)
    comparison_text_entry1, b23 = fonk6(b1['comparison'], b21, handle_compare_algorithms, raise_frame)
    if fn.is_connected():
        fonk1(b1['home'])
        b19.mainloop()
    else:
        messagebox.showerror("No Internet Connection", "Please check your internet connection and try again.")