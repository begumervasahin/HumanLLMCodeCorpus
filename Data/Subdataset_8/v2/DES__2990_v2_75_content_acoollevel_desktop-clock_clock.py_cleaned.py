import tkinter as tk
import time
def close(event):
    global running
    running = False
root = tk.Tk()
root.overrideredirect(True)
root.wm_attributes("-transparentcolor", "gray99")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
timeframe = tk.Frame(root, width=screen_width, height=screen_height, bg="gray99")
timeframe.grid(row=0, column=0)
tkintertime = tk.StringVar()
timelabel = tk.Label(timeframe, textvariable=tkintertime, fg="white", bg="gray99", font=("NovaMono", 40))
timelabel.place(y=screen_height/2 - 60, x=screen_width/2, anchor="center")
tkinterdate = tk.StringVar()
datelabel = tk.Label(timeframe, textvariable=tkinterdate, fg="white", bg="gray99", font=("Bahnschrift", 15))
datelabel.place(y=screen_height/2 + 60, x=screen_width/2, anchor="center")
root.bind('<Escape>', close)
running = True
while running:
    tkintertime.set(value=time.strftime("%H:%M:%S"))
    tkinterdate.set(value=time.strftime("%A, %e %B"))
    root.update_idletasks()
    root.update()
    time.sleep(1)
root.destroy()