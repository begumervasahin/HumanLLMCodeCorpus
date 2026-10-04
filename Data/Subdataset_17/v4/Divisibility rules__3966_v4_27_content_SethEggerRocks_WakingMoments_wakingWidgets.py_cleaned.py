import math
import random
import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.create_color_picker_widgets()
    def create_widgets(self):
        self.hi_button = tk.Button(self)
        self.hi_button["text"] = "\n Let's pick a color!\n"
        self.hi_button["command"] = self.say_hi
        self.hi_button.pack(side="top")
        self.quit_button = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit_button.pack(side="bottom")
    def create_color_picker_widgets(self):
        self.color_picker_button = tk.Button(self)
        self.color_picker_button["text"] = "\n Let's seriously pick a color!\n"
        self.color_picker_button["command"] = self.say_hi
        self.color_picker_button.pack(side="top")
    def say_hi(self):
        print(askcolor((255, 255, 0), root))
        app.destroy()
        self.pick_day()
    def pick_day(self):
        print("Bye Felicia.")
        exit()
def main():
    colorOrNot = input("Would you like to begin? (yes/no)\n").strip().lower()
    if colorOrNot == "yes":
        root = tk.Tk()
        app = Application(master=root)
        style = ttk.Style(root)
        style.theme_use('clam')
        app.mainloop()
    else:
        print("Okay, goodbye.")
        exit()
    today_minutes = 24 * 60
    working_minutes = float(input("How many hours will you work today?\n")) * 60
    sleeping_minutes = float(input("How many hours will you sleep today?\n")) * 60
    eating_minutes = float(input("How many hours will you spend eating today?\n")) * 60
    driving_minutes = float(input("How many hours will you spend driving today?\n")) * 60
    cleaning_minutes = float(input("How many hours will you spend cleaning today?\n")) * 60
    total_used_minutes = working_minutes + sleeping_minutes + eating_minutes + driving_minutes + cleaning_minutes
    remaining_minutes = today_minutes - total_used_minutes
    artistic_windows = 45
    artistic_breaks = 15
    session_length = 60
    sessions = remaining_minutes
    thoughtful_minutes = remaining_minutes % session_length
    print(f"{thoughtful_minutes} minutes available today to do something thoughtful for someone.")
    print(f"{sessions} sessions available today for creating something!")
if __name__ == "__main__":
    main()