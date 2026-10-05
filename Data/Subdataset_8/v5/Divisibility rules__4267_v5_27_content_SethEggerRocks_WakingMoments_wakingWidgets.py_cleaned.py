import tkinter as tk
import tkinter.ttk as ttk
from tkcolorpicker import askcolor
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.create_color_pick_button("Let's pick a color!", self.pick_color)
        self.create_color_pick_button("Let's seriously pick a color!", self.pick_color)
        self.create_quit_button()
    def create_color_pick_button(self, text, command):
        pick_color_button = tk.Button(self, text=f"\n{text}\n", command=command)
        pick_color_button.pack(side="top")
    def create_quit_button(self):
        quit_button = tk.Button(self, text="QUIT", fg="red", command=root.destroy)
        quit_button.pack(side="bottom")
    def pick_color(self):
        print(askcolor((255, 255, 0), root))
        self.destroy_and_pick_day()
    def destroy_and_pick_day(self):
        self.destroy()
        print("Bye Felicia.")
        exit()
def main():
    start = input("Would you like to begin?\n").lower()
    if start == "yes":
        root = tk.Tk()
        app = Application(master=root)
        apply_clam_theme(root)
        app.mainloop()
    else:
        print("Okay, goodbye.")
        exit()
    remaining_minutes = calculate_remaining_minutes()
    sessions, thoughtful = calculate_sessions_and_thoughtful(remaining_minutes)
    print(f"{thoughtful} Minutes available today to do something thoughtful for someone.")
    print(f"{sessions} Sessions available today for creating something!")
def apply_clam_theme(root):
    style = ttk.Style(root)
    style.theme_use('clam')
def calculate_remaining_minutes():
    today_minutes = 24 * 60
    working_minutes = get_minutes_input("work")
    sleeping_minutes = get_minutes_input("sleep")
    eating_minutes = get_minutes_input("eat")
    driving_minutes = get_minutes_input("drive")
    cleaning_minutes = get_minutes_input("clean")
    return today_minutes - (working_minutes + sleeping_minutes + eating_minutes +
                            driving_minutes + cleaning_minutes)
def get_minutes_input(activity):
    return float(input(f"How many hours will you {activity} today?\n")) * 60
def calculate_sessions_and_thoughtful(remaining_minutes):
    sessions = remaining_minutes
    thoughtful = remaining_minutes % 60
    return sessions, thoughtful
if __name__ == "__main__":
    main()