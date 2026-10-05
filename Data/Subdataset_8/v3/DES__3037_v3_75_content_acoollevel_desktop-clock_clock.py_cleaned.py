import tkinter as tk
import time
def close(event):
    global running
    running = False
def create_root_window():
    root = tk.Tk()
    root.overrideredirect(True)
    root.wm_attributes("-transparentcolor", "gray99")
    return root
def get_screen_dimensions(root):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    return screen_width, screen_height
def create_time_frame(root, screen_width, screen_height):
    timeframe = tk.Frame(root, width=screen_width, height=screen_height, bg="gray99")
    timeframe.grid(row=0, column=0)
    return timeframe
def create_time_labels(timeframe, screen_width, screen_height):
    tkintertime = tk.StringVar()
    timelabel = tk.Label(timeframe, textvariable=tkintertime, fg="white", bg="gray99", font=("NovaMono", 40))
    timelabel.place(y=screen_height/2 - 60, x=screen_width/2, anchor="center")
    tkinterdate = tk.StringVar()
    datelabel = tk.Label(timeframe, textvariable=tkinterdate, fg="white", bg="gray99", font=("Bahnschrift", 15))
    datelabel.place(y=screen_height/2 + 60, x=screen_width/2, anchor="center")
    return tkintertime, tkinterdate
def update_time_and_date(tkintertime, tkinterdate):
    while running:
        tkintertime.set(value=time.strftime("%H:%M:%S"))
        tkinterdate.set(value=time.strftime("%A, %e %B"))
        root.update_idletasks()
        root.update()
        time.sleep(1)
def main():
    global running
    running = True
    root = create_root_window()
    screen_width, screen_height = get_screen_dimensions(root)
    timeframe = create_time_frame(root, screen_width, screen_height)
    tkintertime, tkinterdate = create_time_labels(timeframe, screen_width, screen_height)
    root.bind('<Escape>', close)
    update_time_and_date(tkintertime, tkinterdate)
    root.destroy()
if __name__ == "__main__":
    main()