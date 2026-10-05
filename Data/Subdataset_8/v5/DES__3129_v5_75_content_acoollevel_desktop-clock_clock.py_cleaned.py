from tkinter import *
import time
def close(event):
    global running
    running = False
root = Tk()
root.overrideredirect(True)
root.wm_attributes("-transparentcolor", "gray99")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
timeframe = Frame(root, width=screen_width, height=screen_height, bg="gray99")
timeframe.grid(row=0, column=0)
time_label = Label(
    timeframe,
    textvariable=tkintertime,
    fg="white",
    bg="gray99",
    font=("NovaMono", 40)
)
time_label.place(y=screen_height/2 - 60, x=screen_width/2, anchor="center")
date_label = Label(
    timeframe,
    textvariable=tkinterdate,
    fg="white",
    bg="gray99",
    font=("Bahnschrift", 15)
)
date_label.place(y=screen_height/2 + 60, x=screen_width/2, anchor="center")
root.bind('<Escape>', close)
running = True
while running:
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%A, %e %B")
    tkintertime.set(value=current_time)
    tkinterdate.set(value=current_date)
    root.update_idletasks()
    root.update()
    time.sleep(1)