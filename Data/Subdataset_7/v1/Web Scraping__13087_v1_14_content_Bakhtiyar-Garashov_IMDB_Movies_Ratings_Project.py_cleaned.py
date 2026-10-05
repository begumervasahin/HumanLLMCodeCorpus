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
    for name, b25 in zip(b6, b7):
        b9 = name.get_text(strip=True)
        b10 = b25.get_text(strip=True)
        b11 = re.search(r'(\d+)\.\s+(.*?)\s+\((\d{4})\)', b9)
        if b11:
            b8[b11.group(2)] = [b11.group(3), b10]
    return b8
class class1(tk.Tk):
    def fonk2(self):
        super().fonk2()
        self.title("IMDb Movies and Ratings Application")
        self.geometry("700x350")
        self.b8 = fonk1()
        self.fonk3()
        self.fonk4()
    def fonk3(self):
        self.b12 = tk.Label(self, b18="Welcome to IMDb Movies and Ratings Application!")
        self.b12.pack(b13 = 20)
        self.b14 = tk.Label(self, b18="Enter movie name to find:")
        self.b15 = tk.Entry(self, width=30)
        self.b16 = tk.Button(self, b18="Find Movie", command=self.find_movie)
        self.b17 = ttk.Treeview(self, columns=("Year", "Rating"), show="headings")
        self.b17.heading("Year", b18 = "Year")
        self.b17.heading("Rating", b18 = "IMDb Rating")
        self.b19 = tk.Label(self, b18="This application is developed for a course project.\n"
                                               "Contact: example@example.com\nVersion 1.0")
    def fonk4(self):
        b20 = tk.Menu(self)
        b20.add_command(b21 = "Get All Movies", command=self.display_all_movies)
        b20.add_command(b21 = "Find Movie by Name", command=self.display_movie_search)
        b20.add_command(b21 = "About", command=self.display_about)
        b20.add_command(b21 = "Exit", command=self.destroy)
        self.config(b22 = b20)
    def fonk5(self):
        for widget in self.winfo_children():
            widget.pack_forget()
    def fonk6(self):
        self.fonk5()
        self.b12.pack(b13 = 20)
        for name, details in self.b8.items():
            self.b17.insert('', 'end', b23 = (details[0], details[1]))
        self.b17.pack(b13 = 20)
    def fonk7(self):
        self.fonk5()
        self.b14.pack()
        self.b15.pack()
        self.b16.pack(b13 = 20)
    def fonk8(self):
        b24 = self.b15.get()
        if b24 in self.b8:
            year, b25 = self.b8[b24]
            messagebox.showinfo("Found Successfully", f"Movie name: {b24}\nYear: {year}\nIMDb Rating: {b25}")
        else:
            messagebox.showerror("Error", "Movie not found.")
    def fonk9(self):
        self.fonk5()
        self.b19.pack(b13 = 20)
if b26 = = "__main__":
    b27 = class1()
    b27.mainloop()