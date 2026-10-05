import tkinter as tk
import time
b1 = True
def fonk1(event):
    global b1
    b1 = False
b2 = tk.Tk()
b2.overrideredirect(True)
b2.wm_attributes("-transparentcolor", "gray99")
b3 = b2.winfo_screenwidth()
b4 = b2.winfo_screenheight()
b5 = tk.Frame(b2, width=b3, height=b4, bg="gray99")
b5.grid(b6 = 0, column=0)
b7 = tk.StringVar()
b8 = tk.Label(b5, textvariable=b7, fg="white", bg="gray99", font=("NovaMono", 40))
b8.place(b9 = b4/2 - 60, x=b3/2, anchor="center")
b10 = tk.StringVar()
b11 = tk.Label(b5, textvariable=b10, fg="white", bg="gray99", font=("Bahnschrift", 15))
b11.place(b9 = b4/2 + 60, x=b3/2, anchor="center")
b2.bind('<Escape>', close)
while b1:
    b7.set(b12 = time.strftime("%H:%M:%S"))
    b10.set(b12 = time.strftime("%A, %e %B"))
    b2.update_idletasks()
    b2.update()
    time.sleep(1)
b2.destroy()