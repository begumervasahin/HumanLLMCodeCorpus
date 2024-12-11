from tkinter import *
import time
def fonk1(event):
    global b1
    b1 = False
b2 = Tk()
b2.overrideredirect(True)
b2.wm_attributes("-transparentcolor", "gray99")
b3 = b2.winfo_screenwidth()
b4 = b2.winfo_screenheight()
b5 = Frame(b2, width=b3, height=b4, b10="gray99")
b5.grid(b6 = 0, column=0)
b7 = Label(
    b5,
    b8 = tkintertime,
    b9 = "white",
    b10 = "gray99",
    b11 = ("NovaMono", 40)
)
b7.place(b12 = b4/2 - 60, x=b3/2, anchor="center")
b13 = Label(
    b5,
    b8 = tkinterdate,
    b9 = "white",
    b10 = "gray99",
    b11 = ("Bahnschrift", 15)
)
b13.place(b12 = b4/2 + 60, x=b3/2, anchor="center")
b2.bind('<Escape>', close)
b1 = True
while b1:
    b14 = time.strftime("%H:%M:%S")
    b15 = time.strftime("%A, %e %B")
    tkintertime.set(b16 = b14)
    tkinterdate.set(b16 = b15)
    b2.update_idletasks()
    b2.update()
    time.sleep(1)