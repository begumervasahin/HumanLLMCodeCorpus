from tkinter import *
import time, datetime
from time import gmtime, strftime
b1 = Tk()
b1.overrideredirect(1)
b1.wm_attributes("-transparentcolor", "gray99")
b2 = True
def fonk1(event):
    global b2
    b2 = False
b1.bind('<Escape>', close)
b3 = b1.winfo_screenwidth()
b4 = b1.winfo_screenheight()
b5 = Frame(b1, width=b3, height=b4, bg="gray99")
b5.grid(b6 = 0,column=0)
b7 = StringVar()
b8 = Label(b5, textvariable=b7, fg="white", bg="gray99", font=("NovaMono", 40))
b8.place(b9 = b4/2 - 60, x=b3/2, anchor="center")
b10 = StringVar()
b11 = Label(b5, textvariable=b10, fg="white", bg="gray99", font=("Bahnschrift", 15))
b11.place(b9 = b4/2 + 60, x=b3/2, anchor="center")
while b2:
    b7.set(b12 = strftime("%H:%M:%S"))
    b10.set(b12 = strftime("%A, %e %B"))
    b1.update_idletasks()
    b1.update()
    time.sleep(1)