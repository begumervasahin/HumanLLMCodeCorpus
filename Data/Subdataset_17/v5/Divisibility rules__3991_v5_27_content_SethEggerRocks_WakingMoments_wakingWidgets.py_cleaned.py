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
        self.quit_button = tk.Button(self, text="QUIT", fg="red", command=self.quit_app)
        self.quit_button.pack(side="bottom")
    def create_color_picker_widgets(self):
        self.color_picker_button = tk.Button(self)
        self.color_picker_button["text"] = "\n Let's seriously pick a color!\n"
        self.color_picker_button["command"] = self.say_hi
        self.color_picker_button.pack(side="top")
    def say_hi(self):
        print(askcolor((255, 255, 0), root))
        self.quit_app()
    def quit_app(self):
        root.destroy()
        self.print_farewell()
    @staticmethod
    def print_farewell():
        print("Bye Felicia.")
        exit()
def main():
    start_application()
    today_minutes = 24 * 60
    activity_minutes = collect_activity_minutes()
    remaining_minutes = today_minutes - sum(activity_minutes.values())
    calculate_and_print_time(remaining_minutes)
def start_application():
    color_or_not = input("Would you like to begin? (yes/no)\n").strip().lower()
    if color_or_not == "yes":
        global root
        root = tk.Tk()
        app = Application(master=root)
        style = ttk.Style(root)
        style.theme_use('clam')
        app.mainloop()
    else:
        print("Okay, goodbye.")
        exit()
def collect_activity_minutes():
    activities = ["work", "sleep", "eat", "drive", "clean"]
    activity_minutes = {}
    for activity in activities:
        hours = float(input(f"How many hours will you spend {activity} today?\n"))
        activity_minutes[activity] = hours * 60
    return activity_minutes
def calculate_and_print_time(remaining_minutes):
    session_length = 60
    sessions = remaining_minutes
    thoughtful_minutes = remaining_minutes % session_length
    print(f"{thoughtful_minutes} minutes available today to do something thoughtful for someone.")
    print(f"{sessions} sessions available today for creating something!")
if __name__ == "__main__":
    main()