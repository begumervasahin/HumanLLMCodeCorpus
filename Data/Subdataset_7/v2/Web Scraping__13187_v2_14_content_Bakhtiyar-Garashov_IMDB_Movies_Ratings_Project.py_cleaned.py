import tkinter as tk
from tkinter import messagebox, ttk
import requests
from bs4 import BeautifulSoup
import re
def fonk1():
    b1 = "http:
    b2 = {'Accept-Language': 'en-US,en;'}
    b3 = requests.get(b1, b2=b2)
    b4 = b3.content
    b5 = BeautifulSoup(b4, "html.parser")
    b6 = b5.find_all("td", {"class": "titleColumn"})
    b7 = b5.find_all("td", {"class", "ratingColumn imdbRating"})
    b8 = {}
    for name, b27 in zip(b6, b7):
        b9 = name.get_text(strip=True)
        b10 = b27.get_text(strip=True)
        b11 = re.search(r'(\d+)\.\s+(.*?)\s+\((\d{4})\)', b9)
        if b11:
            b12 = b11.group(2)
            b13 = b11.group(3)
            b8[b12] = [b13, b10]
    return b8
class class1(tk.Tk):
    def fonk2(self):
        super().fonk2()
        self.b12("IMDb Movies and Ratings Application")
        self.geometry("700x350")
        self.b8 = fonk1()
        self.fonk3()
        self.fonk4()
    def fonk3(self):
        self.b14 = tk.Label(self, b20="Welcome to IMDb Movies and Ratings Application!")
        self.b14.pack(b15 = 20)
        self.b16 = tk.Label(self, b20="Enter movie name to find:")
        self.b17 = tk.Entry(self, width=30)
        self.b18 = tk.Button(self, b20="Find Movie", command=self.find_movie)
        self.b19 = ttk.Treeview(self, columns=("Year", "Rating"), show="headings")
        self.b19.heading("Year", b20 = "Year")
        self.b19.heading("Rating", b20 = "IMDb Rating")
        self.b21 = tk.Label(self, b20="This application is developed for a course project.\n"
                                               "Contact: example@example.com\nVersion 1.0")
    def fonk4(self):
        b22 = tk.Menu(self)
        b22.add_command(b23 = "Get All Movies", command=self.display_all_movies)
        b22.add_command(b23 = "Find Movie by Name", command=self.display_movie_search)
        b22.add_command(b23 = "About", command=self.display_about)
        b22.add_command(b23 = "Exit", command=self.destroy)
        self.config(b24 = b22)
    def fonk5(self):
        for widget in self.winfo_children():
            widget.pack_forget()
    def fonk6(self):
        self.fonk5()
        self.b14.pack(b15 = 20)
        for b12, details in self.b8.items():
            self.b19.insert('', 'end', b25 = (details[0], details[1]))
        self.b19.pack(b15 = 20)
    def fonk7(self):
        self.fonk5()
        self.b16.pack()
        self.b17.pack()
        self.b18.pack(b15 = 20)
    def fonk8(self):
        b26 = self.b17.get()
        if b26 in self.b8:
            b13, b27 = self.b8[b26]
            messagebox.showinfo("Found Successfully", f"Movie name: {b26}\nYear: {b13}\nIMDb Rating: {b27}")
        else:
            messagebox.showerror("Error", "Movie not found.")
    def fonk9(self):
        self.fonk5()
        self.b21.pack(b15 = 20)
if b28 = = "__main__":
    b29 = class1()
    b29.mainloop()