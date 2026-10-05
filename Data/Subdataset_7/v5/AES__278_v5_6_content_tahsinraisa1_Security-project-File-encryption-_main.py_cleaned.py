import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from random import randrange
import sqlite3
import os
b24 = ""
b25 = ""
b3 = ""
b4 = ""
b5 = {}
def fonk1(base, exponent, modulus):
    ...
def fonk2(p, s):
    ...
def fonk3(b6 = 16):
    ...
def fonk4(ra, rb):
    ...
def fonk5(y, d, p, q):
    ...
def fonk6(b6 = 1024):
    ...
def fonk7(msg):
    ...
def fonk8(i):
    ...
def fonk9(msg, e, n):
    ...
def fonk10(msg, d, p, q):
    ...
def fonk11(key, b25):
    ...
def fonk12(key, b25):
    ...
def fonk13(key, b25):
    ...
def fonk14(key, b25):
    ...
def fonk15(b4):
    ...
def fonk16(choice):
    ...
def fonk17():
    ...
def fonk18():
    ...
def fonk19():
    ...
def fonk20():
    ...
def fonk21():
    ...
def fonk22():
    ...
def fonk23():
    ...
def fonk24():
    ...
def fonk25():
    ...
b7 = tk.Tk()
b7.title("File Encryption System")
b7.geometry("400x300")
b8 = tk.Label(b7, text="Login or Register", font=("bold", 15))
b8.grid(b9 = 0, column=1)
b10 = tk.Label(b7, text="Login", font=("bold", 13))
b10.grid(b9 = 2, column=1)
b11 = tk.Label(b7, text="Username")
b11.grid(b9 = 3, column=0)
b12 = tk.Label(b7, text="Password")
b12.grid(b9 = 4, column=0)
b13 = tk.StringVar()
b14 = tk.Entry(b7, textvariable=b13)
b14.grid(b9 = 3, column=1)
b15 = tk.StringVar()
b16 = tk.Entry(b7, textvariable=b15)
b16.grid(b9 = 4, column=1)
b17 = tk.Label(b7, text="Register", font=("bold", 13))
b17.grid(b9 = 6, column=1)
b18 = tk.Label(b7, text="Username")
b18.grid(b9 = 7, column=0)
b19 = tk.Label(b7, text="Password")
b19.grid(b9 = 8, column=0)
b20 = tk.StringVar()
b21 = tk.Entry(b7, textvariable=b20)
b21.grid(b9 = 7, column=1)
b22 = tk.StringVar()
b23 = tk.Entry(b7, textvariable=b22)
b23.grid(b9 = 8, column=1)
b24 = tk.Button(b7, text="Login", width=10, background='grey', command=loginbutton)
b24.grid(b9 = 5, column=1)
b25 = tk.Button(b7, text="Register", width=10, background='grey', command=registerbutton)
b25.grid(b9 = 9, column=1)
b7.mainloop()