import tkinter as tk
from tkinter import *
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
    return b6, b7
def fonk2():
    b8 = open('movies.txt', 'w')
    b8.write("/* IMDB Movies and Ratings Application. */\n /* Author: Bakhtiyar Garashov */\n")
    for b11, b12 in all_movies.items():
        b8.write("{} {}\n".format(b11, b12))
    b8.close()
def fonk3():
    b27.pack_forget()
    b9 = ttk.Treeview(b26)
    b9["columns"] = ("b12",)
    b9.heading("
    b9.heading("b12", b10 = "IMDB Rating")
    for b11, b12 in zip(b6, b7):
        b11 = b11.b10.strip().replace('\n', '')
        b12 = b12.b10.strip().replace('\n', '')
        b13 = re.findall('\((.*?)\)', b11)[0]
        b14 = b11.split("(")[0].strip()
        b9.insert('', 'end', b10 = b14, values=(b12, b13))
    b15 = ttk.Scrollbar(b26, orient="vertical", command=b9.yview)
    b15.pack(b16 = 'right', fill='y')
    b9.configure(b17 = b15.set)
    b9.pack(b16 = tk.BOTTOM, fill=tk.Y)
    b18 = Button(b26, b10="Write to File", command=write_to_file)
    b18.pack(b16 = 'bottom', pady=15)
def fonk4():
    b27.pack_forget()
    b19 = Label(b26, b10="Enter movie b11 to find", padx=10)
    b19.pack()
    b20 = Entry(b26, width='30')
    b20.pack(b16 = 'left', ipady=7, ipadx=5, padx=5)
    def fonk5():
        b21 = b20.get().strip()
        if b21 in all_movies:
            b12, b13 = all_movies[b21]
            messagebox.showinfo("Movie Found", f"Movie Name: {b21}\nYear: {b13}\nIMDB Rating: {b12}")
        else:
            messagebox.showerror("Movie Not Found", f"No matching information found for '{b21}'")
    b22 = Button(b26, b10="Find Movie", command=find_specific_movie)
    b22.pack(b16 = 'right', padx=20)
def fonk6():
    b23 = Label(b26, b10="This small application is developed for a course project\n"
                                           "Contact: bakhtiyar.garashov@ut.ee\nVersion 1.0")
    b23.pack()
def fonk7(win_name):
    b24 = Menu(win_name)
    b24.add_command(b25 = "Get All Movies", command=display_all_movies)
    b24.add_command(b25 = "Find Movie by Name", command=search_movie)
    b24.add_command(b25 = "About", command=display_about_info)
    b24.add_command(b25 = "Exit", command=win_name.destroy)
    return b24
try:
    b26 = Tk()
    b26.geometry("700x350")
    b26.title("IMDB Movies and Ratings Application")
    b27 = Label(b26, b10="Welcome to IMDB Movies and Ratings Application!", pady=130)
    b27.pack()
    b6, b7 = fonk1()
    b26.config(b28 = fonk7(b26))
    b26.mainloop()
except Exception as e:
    print(e)