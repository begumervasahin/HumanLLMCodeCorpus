import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import re
try:
    b1 = "http:
    b2 = {'Accept-Language': 'en-US,en;'}
    b3 = requests.get(b1,b2=b2)
    b4 = b3.content
    b5 = BeautifulSoup(b4, "html.parser")
    b6 = b5.find_all("td", {"class": "titleColumn"})
    b7 = b5.find_all("td", {"class", "ratingColumn imdbRating"})
    b8 = dict()
    b9 = dict()
    b10 = Tk()
    b10.geometry("700x350")
    b10.configure(b11 = '
    b10.iconbitmap('icon1.ico')
    b10.b18("IMDB movies and b7 application")
    b12 = Label(b10, b23="Welcome to IMDB movies and b7 application!", pady=130)
    b12.config(b11 = '
    b12.pack()
    b13 = Label(b10, b23="Enter movie b25 to find",padx=10)
    b13.pack_forget()
    b14 = tk.Button(b10,b23="Find movie",fg="black",padx=5,b35=14,font=('Tahoma', '11'))
    b14.pack_forget()
    b15 = Entry(b10,b35='30')
    b16 = Label(b10, b23="This small application is developed for course project\nContact: bakhtiyar.garashov@ut.ee\nversion 1.0", pady=130)
    b16.pack_forget()
    b17 = Label(b10, b23="Developed by Bakhtiyar Garashov", pady=0)
    b17.config(b11 = '
    b17.pack()
    b18 = Label(b10, b23="IMDB top 250 movies list",padx=10)
    b18.pack_forget()
    b19 = ttk.Treeview(b10)
    b19.pack_forget()
    b20 = ttk.Scrollbar(b10, orient="vertical", b31=b19.yview)
    b19.configure(b21 = b20.set)
    b20.pack_forget()
    b22 = tk.Button(b10,b23="Write to file",fg="black",pady=5,b35=14,font=('Tahoma', '11'))
    b22.pack_forget()
    def fonk1():
        b12.pack_forget()
        b13.pack_forget()
        b16.pack_forget()
        b15.pack_forget()
        b17.pack_forget()
        b14.pack_forget()
        b19["columns"]=("b26",)
        b19.column("
        b19.heading("
        b19.heading("b26", b23 = "IMDB b26",anchor=tk.CENTER)
        b20.pack(b24 = 'right', fill='b37')
        b18.config(b11 = '
        b18.pack(b24 = 'top',pady=5)
        for b25, b26 in zip(b6, b7):
            b25 = b25.b23
            b26 = b26.b23
            b25 = b25.strip()
            b25 = b25.replace('\n','')
            b26 = b26.strip()
            b26 = b26.replace('\n','')
            b27 = list()
            b19.insert('', 'end', b23 = b25,b27=(b26))
            b28 = re.findall('\((.*?)\)',b25)
            b29 = b25.split("(")[0]
            for b32 in b28:
                b27.append(b32)
            b27.append(b26)
            b8[b29]=b27
        b19.configure(b21 = b20.set)
        b19.pack(b24 = tk.BOTTOM,fill=tk.Y)
        def fonk2():
            b30 = open('movies.txt','w')
            b30.write("/* IMDB movies and b7 application. */ \n /* Author:Bakhtiyar Garashov */ \n")
            for b25,b26 in b8.items():
                b30.write("{} {} \n".format(b25,b26))
            b30.close()
        b22.config(b31 = lambda:fonk2())
        b22.pack(b24 = 'bottom',pady=15)
    def fonk3():
        b12.pack_forget()
        b16.pack_forget()
        b17.pack_forget()
        b19.pack_forget()
        b20.pack_forget()
        b22.pack_forget()
        b18.pack_forget()
        b15.pack(b24 = 'left',ipady=7,ipadx=5,padx=5)
        def fonk4():
             for b32,z in b8.items():
                b32 = b32.split()
                b32 = " ".join(b32[1:])
                b9[b32]=z
             b33 = b15.get()
             if b33 in b9.keys():
                 b34 = b9[b33]
                 messagebox.showinfo("Found succesfully","Movie b25: {}\nYear: {} \nIMDB b26: {}".format(b33,b34[0],b34[1]))
             else:
                 messagebox.showerror("Oops :/","There is no matching information about {}".format(b33))
        b14.config(b31 = lambda:fonk4())
        b14.pack(b24 = 'right',padx=20)
        b13.config(b11 = '
        b13.pack(b24 = 'left')
    def fonk5():
        b12.pack_forget()
        b13.pack_forget()
        b19.pack_forget()
        b20.pack_forget()
        b15.pack_forget()
        b22.pack_forget()
        b14.pack_forget()
        b17.pack_forget()
        b18.pack_forget()
        b16.config(b11 = '
        b16.pack()
    def fonk6(win):
        win.update_idletasks()
        b35 = win.winfo_width()
        b36 = win.winfo_height()
        b34 = (win.winfo_screenwidth()
        b37 = (win.winfo_screenheight()
        win.geometry('{}b34{}+{}+{}'.format(b35, b36, b34, b37))
    def fonk7(win_name):
        b38 = Menu(win_name)
        b38.add_command(b39 = "Get all movies", b31=all_movies_screen)
        b38.add_command(b39 = "Find movie by b25", b31=one_movie_screen)
        b38.add_command(b39 = "About", b31=about_screen)
        b38.add_command(b39 = "Exit", b31=b10.destroy)
        return b38
    b40 = fonk7(b10)
    b10.config(b41 = b40)
    fonk6(b10)
    b10.mainloop()
except Exception as e:
    print(e)