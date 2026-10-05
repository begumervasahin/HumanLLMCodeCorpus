import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.pick_color_button = tk.Button(self, text="\n Let's pick a color!\n", command=self.pick_color)
        self.pick_color_button.pack(side="top")
        self.pick_color_button2 = tk.Button(self, text="\n Let's seriously pick a color!\n", command=self.pick_color)
        self.pick_color_button2.pack(side="top")
        self.quit_button = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        self.quit_button.pack(side="bottom")
    def pick_color(self):
        print(askcolor((255, 255, 0), root))
        app.destroy()
        self.pick_day()
    def pick_day(self):
        print("Bye Felicia.")
        exit()
def main():
    color_or_not = input("Would you like to begin?\n")
    if color_or_not.lower() == "yes":
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
    what_is_left = today_minutes - (working_minutes + sleeping_minutes + eating_minutes +
                                    driving_minutes + cleaning_minutes)
    sessions = what_is_left
    thoughtful = what_is_left % 60
    print(f"{thoughtful} Minutes available today to do something thoughtful for someone.")
    print(f"{sessions} Sessions available today for creating something!")
if __name__ == "__main__":
    main()