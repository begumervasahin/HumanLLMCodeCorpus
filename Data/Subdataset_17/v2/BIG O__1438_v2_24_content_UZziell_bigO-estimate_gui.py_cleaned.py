import time
from tkinter import *
from tkinter import messagebox
import functions as fn
def raise_frame(frame):
    frame.tkraise()
def setup_main_window(root):
    root.title("BigO Estimation")
    root.geometry('1049x750')
    root.resizable(False, False)
def create_frames(root):
    frames = {}
    frames['home'] = Frame(root)
    frames['single'] = Frame(root)
    frames['comparison'] = Frame(root)
    for frame in frames.values():
        frame.grid(row=0, column=0, sticky='news')
    return frames
def setup_home_frame(frame, photo, raise_frame_func):
    Label(frame, image=photo).place(x=0, y=0, relwidth=1, relheight=1)
    Button(frame, text='Single', bg="black", fg="white", command=lambda: raise_frame_func('single')).place(x=20, y=40)
    Button(frame, text='Double', bg="black", fg="white", command=lambda: raise_frame_func('comparison')).place(x=20, y=80)
    Label(frame, text="Hint\nSingle: Estimates an algorithm complexity\nDouble: Compares two algorithms complexities",
          fg="white", bg="black").place(x=20, y=680)
def setup_single_frame(frame, photo_earth, handle_calculate, raise_frame_func):
    Label(frame, image=photo_earth).place(x=0, y=0, relwidth=1, relheight=1)
    Label(frame, text="Hint: Paste code in the box", bg="black", fg="white").grid(column=3, row=0)
    text_entry = Text(frame, bg="black", fg="white", height=40, width=100)
    text_entry.grid(column=1, row=1)
    text_entry.insert(END, """\n\ni = 0\nwhile i < N:\n    print("*", end='')\n    i += 1""")
    Button(frame, text="Calculate", bg="black", fg="white", command=handle_calculate).grid(column=1, row=3)
    Button(frame, text='Back', bg="black", fg="white", command=lambda: raise_frame_func('home')).grid(row=3, column=4)
    return text_entry
def setup_comparison_frame(frame, photo_earth, handle_compare, raise_frame_func):
    Label(frame, image=photo_earth).place(x=0, y=0, relwidth=1, relheight=1)
    text_entry1 = Text(frame, bg="black", fg="white", height=40, width=50)
    text_entry1.grid(column=1, row=1)
    text_entry1.insert(END, """\n\ni = 0\nwhile i < N:\n    print("*", end='')\n    i += 1""")
    Label(frame, bg="black", fg="white", text="").grid(column=2, row=1)
    text_entry2 = Text(frame, bg="black", fg="white", height=40, width=50)
    text_entry2.grid(column=3, row=1)
    Button(frame, text="Compare", bg="black", fg="white", command=handle_compare).grid(row=3, columnspan=4)
    Button(frame, text='Back', bg="black", fg="white", command=lambda: raise_frame_func('home')).place(x=970, y=690)
    return text_entry1, text_entry2
def handle_calculate_single():
    user_input = single_text_entry.get("1.0", "end-1c")
    complexity = fn.equation_finder(user_input)
    messagebox.showinfo("Result", f"(BIG O notation): {complexity[0]}\nClick OK to sketch the graph")
    root.destroy()
    time.sleep(0.5)
    fn.plot(complexity[1] if 1 < int(complexity[1]) < 10 else 1)
def handle_compare_algorithms():
    src1 = comparison_text_entry1.get("1.0", "end-1c")
    src2 = comparison_text_entry2.get("1.0", "end-1c")
    left_complex = fn.equation_finder(src1)
    right_complex = fn.equation_finder(src2)
    left_complex[1] = left_complex[1] or "1"
    right_complex[1] = right_complex[1] or "1"
    if left_complex[0] > right_complex[0]:
        messagebox.showinfo("Result", f"The second algorithm is better.\n {left_complex[0]} > {right_complex[0]}")
    elif left_complex[0] < right_complex[0]:
        messagebox.showinfo("Result", f"The first algorithm is better.\n {left_complex[0]} < {right_complex[0]}")
    else:
        messagebox.showinfo("Result", f"Both algorithms have equal complexity: {left_complex[0]}")
    root.destroy()
    time.sleep(0.5)
    fn.plot(left_complex[1], right_complex[1])
if __name__ == "__main__":
    root = Tk()
    setup_main_window(root)
    frames = create_frames(root)
    photo = PhotoImage(file="resources/espresso2.png")
    photo_earth = PhotoImage(file="resources/sss.png")
    setup_home_frame(frames['home'], photo, raise_frame)
    single_text_entry = setup_single_frame(frames['single'], photo_earth, handle_calculate_single, raise_frame)
    comparison_text_entry1, comparison_text_entry2 = setup_comparison_frame(frames['comparison'], photo_earth, handle_compare_algorithms, raise_frame)
    if fn.is_connected():
        raise_frame(frames['home'])
        root.mainloop()
    else:
        messagebox.showerror("No Internet Connection", "Please check your internet connection and try again.")