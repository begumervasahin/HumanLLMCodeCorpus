import time
from tkinter import *
from tkinter import messagebox
import functions as fn
def raise_frame(frame):
    frame.tkraise()
root = Tk()
root.title("BigO estimation")
root.geometry('1049x750')
root.resizable(False, False)
photo = PhotoImage(file="resources/espresso2.png")
photo_earth = PhotoImage(file="resources/sss.png")
HINT_TEXT = "Hint: Paste code in the box"
BTN_TEXT_BACK = "Back"
BTN_TEXT_CALCULATE = "Calculate"
BTN_TEXT_COMPARE = "Compare"
FRAME_WIDTH = 1049
FRAME_HEIGHT = 750
def create_frame(parent):
    frame = Frame(parent, bg="black")
    frame.place(x=0, y=0, relwidth=1, relheight=1)
    return frame
f1 = create_frame(root)
f2 = create_frame(root)
f3 = create_frame(root)
def create_text_entry(parent, width, height):
    entry = Text(parent, bg="black", fg="white", height=height, width=width)
    entry.grid(column=1, row=1)
    return entry
def create_button(parent, text, command, x=20, y=40):
    button = Button(parent, text=text, bg="black", fg="white", command=command)
    button.place(x=x, y=y)
    return button
Label(f1, image=photo).place(x=0, y=0, relwidth=1, relheight=1)
create_button(f1, ' Single', lambda: raise_frame(f2))
create_button(f1, 'Double', lambda: raise_frame(f3), y=80)
Label(f1, text="Hint\n"
               "Single: Estimates an algorithm complexity\n"
               "Double: Compares two algorithms complexities", fg="white", bg="black").place(x=20, y=680)
Label(f2, image=photo_earth).place(x=0, y=0, relwidth=1, relheight=1)
hint_lbl = Label(f2, text=HINT_TEXT, bg="black", fg="white")
hint_lbl.grid(column=3, row=0)
f2entry = create_text_entry(f2, width=100, height=40)
f2entry.insert(END, "i = 0\nwhile i < N:\n    print('*', end='')\n    i += 1")
def calc_handle():
    user_input = f2entry.get("1.0", "end-1c")
    complexity = fn.equation_finder(user_input)
    messagebox.showinfo("Result",
                        f"(BIG O notation): {complexity[0]}\n"
                        f"Click OK to sketch the graph")
    root.destroy()
    time.sleep(0.5)
    if complexity[1] == '':
        fn.plot(1)
    elif 1 < int(complexity[1]) < 10:
        fn.plot(complexity[1])
    else:
        print("Not able to plot, power > 9")
create_button(f2, BTN_TEXT_CALCULATE, calc_handle, y=250)
create_button(f2, BTN_TEXT_BACK, lambda: raise_frame(f1), x=950, y=690)
Label(f3, image=photo_earth).place(x=0, y=0, relwidth=1, relheight=1)
f3entry = create_text_entry(f3, width=50, height=40)
lbl = Label(f3, bg="black", fg="white", text="")
lbl.grid(column=2, row=1)
f3entry2 = create_text_entry(f3, width=50, height=40)
def compare_handle():
    src1 = f3entry.get("1.0", "end-1c")
    src2 = f3entry2.get("1.0", "end-1c")
    left_complex = fn.equation_finder(src1)
    right_complex = fn.equation_finder(src2)
    if left_complex[1] == '':
        left_complex[1] = "1"
    if right_complex[1] == '':
        right_complex[1] = '1'
    if left_complex[0] > right_complex[0]:
        messagebox.showinfo("Result",
                            f"It seems the 'Second' algorithm is better.\n {left_complex[0]} > {right_complex[0]}")
    elif left_complex[0] < right_complex[0]:
        messagebox.showinfo("Result",
                            f"It seems the 'First' algorithm is better.\n {left_complex[0]} < {right_complex[0]}")
    else:
        messagebox.showinfo("Result", f"It seems the order of both algorithms are equal to {left_complex[0]}")
    root.destroy()
    time.sleep(0.5)
    fn.plot(left_complex[1], right_complex[1])
create_button(f3, BTN_TEXT_COMPARE, compare_handle, y=250, x=450)
create_button(f3, BTN_TEXT_BACK, lambda: raise_frame(f1), x=950, y=690)
if fn.is_connected():
    raise_frame(f1)
    root.mainloop()
else:
    messagebox.showerror("No Internet Connection", "Please check your internet connection and try again.")