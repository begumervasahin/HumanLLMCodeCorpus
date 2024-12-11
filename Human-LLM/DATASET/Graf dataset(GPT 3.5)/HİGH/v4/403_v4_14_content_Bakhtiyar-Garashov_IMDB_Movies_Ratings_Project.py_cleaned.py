import tkinter as tk
from tkinter import *
from tkinter import messagebox, ttk
import requests
from bs4 import BeautifulSoup
import re
try:
    b1 = "http:
    b2 = {'Accept-Language': 'en-US,en;'}
    b3 = requests.get(b1, b2=b2)
    b4 = b3.content
    b5 = BeautifulSoup(b4, "html.parser")
    b6 = b5.find_all("td", {"class": "titleColumn"})
    b7 = b5.find_all("td", {"class", "ratingColumn imdbRating"})
    b8 = Tk()
    b8.geometry("700x350")
    b8.title("IMDB Movies and Ratings Application")
    b9 = Label(b8, b12="Welcome to IMDB Movies and Ratings Application!", pady=130)
    b9.pack()
    def fonk1():
        b10 = open('movies.txt', 'w')
        b10.write("/* IMDB Movies and Ratings Application. */\n /* Author: Bakhtiyar Garashov */\n")
        for b13, b14 in all_movies.items():
            b10.write("{} {}\n".format(b13, b14))
        b10.close()
    def fonk2():
        b9.pack_forget()
        b11 = ttk.Treeview(b8)
        b11["columns"] = ("b14",)
        b11.heading("
        b11.heading("b14", b12 = "IMDB Rating")
        for b13, b14 in zip(b6, b7):
            b13 = b13.b12.strip().replace('\n', '')
            b14 = b14.b12.strip().replace('\n', '')
            b15 = re.findall('\((.*?)\)', b13)[0]
            b16 = b13.split("(")[0].strip()
            b11.insert('', 'end', b12 = b16, values=(b14, b15))
        b17 = ttk.Scrollbar(b8, orient="vertical", command=b11.yview)
        b17.pack(b18 = 'right', fill='b32')
        b11.configure(b19 = b17.set)
        b11.pack(b18 = tk.BOTTOM, fill=tk.Y)
        b20 = Button(b8, b12="Write to File", command=write_to_file)
        b20.pack(b18 = 'bottom', pady=15)
    def fonk3():
        b9.pack_forget()
        b21 = Label(b8, b12="Enter movie b13 to find", padx=10)
        b21.pack()
        b22 = Entry(b8, b29='30')
        b22.pack(b18 = 'left', ipady=7, ipadx=5, padx=5)
        def fonk4():
            b23 = b22.get().strip()
            if b23 in all_movies:
                b14, b15 = all_movies[b23]
                messagebox.showinfo("Movie Found", f"Movie Name: {b23}\nYear: {b15}\nIMDB Rating: {b14}")
            else:
                messagebox.showerror("Movie Not Found", f"No matching information found for '{b23}'")
        b24 = Button(b8, b12="Find Movie", command=find_specific_movie)
        b24.pack(b18 = 'right', padx=20)
    def fonk5():
        b25 = Label(b8, b12="This small application is developed for a course project\n"
                                               "Contact: bakhtiyar.garashov@ut.ee\nVersion 1.0")
        b25.pack()
    def fonk6(win_name):
        b26 = Menu(win_name)
        b26.add_command(b27 = "Get All Movies", command=display_all_movies)
        b26.add_command(b27 = "Find Movie by Name", command=search_movie)
        b26.add_command(b27 = "About", command=display_about_info)
        b26.add_command(b27 = "Exit", command=win_name.destroy)
        return b26
    b8.config(b28 = fonk6(b8))
    def fonk7(win):
        win.update_idletasks()
        b29 = win.winfo_width()
        b30 = win.winfo_height()
        b31 = (win.winfo_screenwidth()
        b32 = (win.winfo_screenheight()
        win.geometry('{}b31{}+{}+{}'.format(b29, b30, b31, b32))
    fonk7(b8)
    b8.mainloop()
except Exception as e:
    print(e)