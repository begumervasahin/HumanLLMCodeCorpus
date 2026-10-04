import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.color_button = tk.Button(self, text="\n Let's pick a color!\n", command=self.pick_color)
        self.color_button.pack(side="top")
        self.quit_button = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit_button.pack(side="bottom")
    def pick_color(self):
        print(askcolor((255, 255, 0), self.master))
        self.master.destroy()
        self.exit_message()
    def exit_message(self):
        print("Bye Felicia.")
        exit()
def get_minutes_from_user(prompt):
    hours = float(input(prompt))
    return hours * 60
def calculate_remaining_minutes():
    TOTAL_MINUTES_IN_DAY = 24 * 60
    prompts = [
        "How many hours will you work today?\n",
        "How many hours will you sleep today?\n",
        "How many hours will you spend eating today?\n",
        "How many hours will you spend driving today?\n",
        "How many hours will you spend cleaning today?\n"
    ]
    total_used_minutes = sum(get_minutes_from_user(prompt) for prompt in prompts)
    remaining_minutes = TOTAL_MINUTES_IN_DAY - total_used_minutes
    sessions = remaining_minutes
    thoughtful_minutes = remaining_minutes % 60
    print(f"{thoughtful_minutes} minutes available today to do something thoughtful for someone.")
    print(f"{sessions} sessions available today for creating something!")
def main():
    color_or_not = input("Would you like to begin?\n").strip().lower()
    if color_or_not == "yes":
        root = tk.Tk()
        app = Application(master=root)
        style = ttk.Style(root)
        style.theme_use('clam')
        app.mainloop()
    else:
        print("Okay, goodbye.")
        exit()
    calculate_remaining_minutes()
if __name__ == "__main__":
    main()