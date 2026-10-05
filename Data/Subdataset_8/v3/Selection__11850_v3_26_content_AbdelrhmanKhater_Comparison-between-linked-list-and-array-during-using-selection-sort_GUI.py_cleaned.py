from tkinter import Tk, Button, Label, Entry
from main import automatic, Selection_Sort_Array, Linkedlist
class ComparisonGUI(Tk):
    def __init__(self):
        super().__init__()
        self.setup_main_window()
    def setup_main_window(self):
        self.title("Comparison")
        self.geometry("300x300")
        self.setup_automatic_button()
        self.setup_manual_button()
    def setup_automatic_button(self):
        self.automatic_button = Button(self, text="Automatic", bg="blue", command=automatic)
        self.automatic_button.place(x=60, y=140)
    def setup_manual_button(self):
        self.manual_button = Button(self, text="Manual", bg="blue", command=self.open_manual_input)
        self.manual_button.place(x=180, y=140)
    def open_manual_input(self):
        self.manual_window = Tk()
        self.setup_manual_window()
    def setup_manual_window(self):
        self.manual_window.geometry("250x250")
        self.manual_window.title("Manual Input")
        self.setup_size_input()
        self.setup_numbers_input()
        self.setup_compare_button()
        self.setup_result_entry()
        self.manual_window.mainloop()
    def setup_size_input(self):
        self.size_label = Label(self.manual_window, text="Size", fg="white", bd=5, bg="black")
        self.size_label.place(x=50, y=90)
        self.size_entry = Entry(self.manual_window, bd=5)
        self.size_entry.place(x=110, y=90)
    def setup_numbers_input(self):
        self.numbers_label = Label(self.manual_window, text="Inputs", fg="white", bd=5, bg="black")
        self.numbers_label.place(x=50, y=125)
        self.numbers_entry = Entry(self.manual_window, bd=5)
        self.numbers_entry.place(x=110, y=125)
    def setup_compare_button(self):
        self.compare_button = Button(self.manual_window, text="Compare", bg="blue", command=self.compare_manual_input)
        self.compare_button.place(x=110, y=160)
    def setup_result_entry(self):
        self.result_entry = Entry(self.manual_window, bd=5)
        self.result_entry.place(x=75, y=190)
    def compare_manual_input(self):
        size = int(self.size_entry.get())
        numbers_str = self.numbers_entry.get()
        numbers_list = [int(num) for num in numbers_str.split()]
        sorted_array = Selection_Sort_Array(numbers_list)
        sorted_array_str = " ".join(map(str, sorted_array))
        self.result_entry.delete(0, 'end')
        self.result_entry.insert(0, sorted_array_str)
if __name__ == "__main__":
    gui = ComparisonGUI()
    gui.mainloop()