import encrypt
from tkinter import *
class ButtonWidget:
    def __init__(self, window, text, column, row, command):
        self.button = Button(window, text=text, command=command)
        self.button.grid(column=column, row=row)
class InputField:
    def __init__(self, window, column, row):
        self.entry = Entry(window)
        self.entry.grid(column=column, row=row)
class DropDownMenu:
    def __init__(self, window, options, column, row):
        self.var = StringVar(window)
        self.var.set(options[0])
        self.dropdown = OptionMenu(window, self.var, *options)
        self.dropdown.grid(column=column, row=row)
def main():
    root = Tk()
    root.title("Simple GUI")
    input_field = InputField(root, column=1, row=1)
    submit_button = ButtonWidget(root, text="Submit", column=2, row=1, command=lambda: print("Button clicked!"))
    dropdown_menu = DropDownMenu(root, options=["Option 1", "Option 2", "Option 3"], column=1, row=2)
    root.mainloop()
if __name__ == "__main__":
    main()