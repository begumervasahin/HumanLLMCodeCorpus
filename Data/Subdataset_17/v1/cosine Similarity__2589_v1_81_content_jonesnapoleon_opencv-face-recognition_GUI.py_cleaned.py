import tkinter as tk
from tkinter import filedialog
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
    def create_widgets(self):
        self.insert = tk.Button(self, text="Insert Photo", command=self.take_input)
        self.insert.pack(side=tk.TOP)
        self.label = tk.Label(self, text="Choose one system", pady=20)
        self.label.pack()
        self.cos = tk.Radiobutton(self, text="Cosine", padx=20, value=1)
        self.cos.pack(side=tk.LEFT)
        self.euclid = tk.Radiobutton(self, text="Euclidean distance", padx=20, value=2)
        self.euclid.pack(side=tk.LEFT)
        self.next = tk.Button(self, text="Next", fg="blue", command=self.next_step)
        self.next.pack(side=tk.BOTTOM)
        self.quit = tk.Button(self, text="Quit", fg="red", command=self.master.destroy)
        self.quit.pack(side=tk.BOTTOM)
    def next_step(self):
        print('Thank you, next')
    def take_input(self):
        file_path = filedialog.askopenfilename(title="Select a photo", filetypes=(("Image files", "*.jpg *.jpeg *.png"), ("All files", "*.*")))
        if file_path:
            print(f'Selected file: {file_path}')
        else:
            print('No file selected')
if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()