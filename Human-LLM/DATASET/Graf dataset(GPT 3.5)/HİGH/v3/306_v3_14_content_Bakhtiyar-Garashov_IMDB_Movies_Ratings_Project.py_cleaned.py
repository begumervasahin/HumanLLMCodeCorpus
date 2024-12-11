import tkinter as tk
from tkinter import messagebox, ttk
import requests
from bs4 import BeautifulSoup
import re
class class1:
    def fonk1(self):
        self.b1 = "http:
        self.b2 = {'Accept-Language': 'en-US,en;'}
    def fonk2(self):
        b3 = requests.get(self.b1, b2=self.b2)
        b4 = BeautifulSoup(b3.content, "html.parser")
        b5 = b4.find_all("td", {"class": "titleColumn"})
        b6 = b4.find_all("td", {"class", "ratingColumn imdbRating"})
        b7 = {}
        for name, b27 in zip(b5, b6):
            b8 = name.get_text(strip=True)
            b9 = b27.get_text(strip=True)
            b10 = re.search(r'(\d+)\.\s+(.*?)\s+\((\d{4})\)', b8)
            if b10:
                b11 = b10.group(2)
                b12 = b10.group(3)
                b7[b11] = [b12, b9]
        return b7
class class2(tk.Tk):
    def fonk3(self):
        super().fonk3()
        self.b11("IMDb Movies and Ratings Application")
        self.geometry("700x350")
        self.b13 = class1()
        self.b7 = self.b13.fonk2()
        self.fonk4()
        self.fonk5()
    def fonk4(self):
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
    def fonk5(self):
        b22 = tk.Menu(self)
        b22.add_command(b23 = "Get All Movies", command=self.display_all_movies)
        b22.add_command(b23 = "Find Movie by Name", command=self.display_movie_search)
        b22.add_command(b23 = "About", command=self.display_about)
        b22.add_command(b23 = "Exit", command=self.destroy)
        self.config(b24 = b22)
    def fonk6(self):
        for widget in self.winfo_children():
            widget.pack_forget()
    def fonk7(self):
        self.fonk6()
        self.b14.pack(b15 = 20)
        for b11, details in self.b7.items():
            self.b19.insert('', 'end', b25 = (details[0], details[1]))
        self.b19.pack(b15 = 20)
    def fonk8(self):
        self.fonk6()
        self.b16.pack()
        self.b17.pack()
        self.b18.pack(b15 = 20)
    def fonk9(self):
        b26 = self.b17.get()
        if b26 in self.b7:
            b12, b27 = self.b7[b26]
            messagebox.showinfo("Found Successfully", f"Movie name: {b26}\nYear: {b12}\nIMDb Rating: {b27}")
        else:
            messagebox.showerror("Error", "Movie not found.")
    def fonk10(self):
        self.fonk6()
        self.b21.pack(b15 = 20)
if b28 = = "__main__":
    b29 = class2()
    b29.mainloop()