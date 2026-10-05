from tkinter import Tk, Button, Label, Entry
from main import automatic, Selection_Sort_Array
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Comparison")
        self.geometry("300x300")
        self.setup_buttons()
    def setup_buttons(self):
        self.B1 = Button(self, text="Automatic", bg="blue", command=automatic)
        self.B1.place(x=60, y=140)
        self.B2 = Button(self, text="Manual", bg="blue", command=self.open_manual)
        self.B2.place(x=180, y=140)
    def open_manual(self):
        self.top2 = Tk()
        self.top2.geometry("250x250")
        self.top2.title("Manual")
        self.setup_manual_widgets()
    def setup_manual_widgets(self):
        self.L1 = Label(self.top2, text="Size", fg="white", bd=5, bg="black")
        self.L1.place(x=50, y=90)
        self.E1 = Entry(self.top2, bd=5)
        self.E1.place(x=110, y=90)
        self.L2 = Label(self.top2, text="Inputs", fg="white", bd=5, bg="black")
        self.L2.place(x=50, y=125)
        self.E2 = Entry(self.top2, bd=5)
        self.E2.place(x=110, y=125)
        self.B3 = Button(self.top2, text="Compare", bg="blue", command=self.compare_manual)
        self.B3.place(x=110, y=160)
        self.L3 = Entry(self.top2, bd=5)
        self.L3.place(x=75, y=190)
    def compare_manual(self):
        size = int(self.E1.get())
        inputs = self.E2.get().split()
        nums = [int(num) for num in inputs]
        sorted_nums = Selection_Sort_Array(nums)
        result = " ".join(map(str, sorted_nums))
        self.L3.insert(0, result)
gui = GUI()
gui.mainloop()