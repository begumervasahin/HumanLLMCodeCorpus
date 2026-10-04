import time
from tkinter import *
from tkinter import messagebox
import functions as fn
def raise_frame(frame):
    frame.tkraise()
def calculate_handle():
    user_input = f2_entry.get("1.0", "end-1c")
    complexity = fn.equation_finder(user_input)
    messagebox.showinfo("Result", f"(BIG O notation): {complexity[0]}\nClick OK to sketch the graph")
    root.destroy()
    time.sleep(0.5)
    power = complexity[1] if complexity[1] else '1'
    power_int = int(power)
    if 1 <= power_int < 10:
        fn.plot(power_int)
    else:
        print("Not able to plot, power > 9")
def compare_handle():
    src1 = f3_entry1.get("1.0", "end-1c")
    src2 = f3_entry2.get("1.0", "end-1c")
    left_complex = fn.equation_finder(src1)
    right_complex = fn.equation_finder(src2)
    left_power = left_complex[1] if left_complex[1] else "1"
    right_power = right_complex[1] if right_complex[1] else "1"
    if left_complex[0] > right_complex[0]:
        message = f"The 'Second' algorithm is better.\n{left_complex[0]} > {right_complex[0]}"
    elif left_complex[0] < right_complex[0]:
        message = f"The 'First' algorithm is better.\n{left_complex[0]} < {right_complex[0]}"
    else:
        message = f"The complexity of both algorithms is equal: {left_complex[0]}"
    messagebox.showinfo("Comparison Result", message)
    root.destroy()
    time.sleep(0.5)
    fn.plot(left_power, right_power)
root = Tk()
root.title("BigO Estimation")
root.geometry('1049x750')
root.resizable(False, False)
f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)
for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky='news')
photo = PhotoImage(file="resources/espresso2.png")
Label(f1, image=photo).place(x=0, y=0, relwidth=1, relheight=1)
Button(f1, text='Single', bg="black", fg="white", command=lambda: raise_frame(f2)).place(x=20, y=40)
Button(f1, text='Double', bg="black", fg="white", command=lambda: raise_frame(f3)).place(x=20, y=80)
Label(f1, text="Hint\nSingle: Estimates an algorithm complexity\nDouble: Compares two algorithms complexities", fg="white", bg="black").place(x=20, y=680)
photo_earth = PhotoImage(file="resources/sss.png")
Label(f2, image=photo_earth).place(x=0, y=0, relwidth=1, relheight=1)
Label(f2, text="Hint: Paste code in the box", bg="black", fg="white").grid(column=3, row=0)
f2_entry = Text(f2, bg="black", fg="white", height=40, width=100)
f2_entry.grid(column=1, row=1)
f2_entry.insert(END, "\n\ni = 0\nwhile i < N:\n    print(\"*\", end='')\n    i += 1")
Button(f2, text="Calculate", bg="black", fg="white", command=calculate_handle).grid(column=1, row=3)
Button(f2, text='Back', bg="black", fg="white", command=lambda: raise_frame(f1)).grid(row=3, column=4)
Label(f3, image=photo_earth).place(x=0, y=0, relwidth=1, relheight=1)
f3_entry1 = Text(f3, bg="black", fg="white", height=40, width=50)
f3_entry1.grid(column=1, row=1)
f3_entry1.insert(END, "\n\ni = 0\nwhile i < N:\n    print(\"*\", end='')\n    i += 1")
Label(f3, bg="black", fg="white", text="").grid(column=2, row=1)
f3_entry2 = Text(f3, bg="black", fg="white", height=40, width=50)
f3_entry2.grid(column=3, row=1)
Button(f3, text="Compare", bg="black", fg="white", command=compare_handle).grid(row=3, columnspan=4)
Button(f3, text='Back', bg="black", fg="white", command=lambda: raise_frame(f1)).place(x=970, y=690)
if fn.is_connected():
    raise_frame(f1)
    root.mainloop()
else:
    messagebox.showerror("No Internet Connection", "Please check your internet connection and try again.")