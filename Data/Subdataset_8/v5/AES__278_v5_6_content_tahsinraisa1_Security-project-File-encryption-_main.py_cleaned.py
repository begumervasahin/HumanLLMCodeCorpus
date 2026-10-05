import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from random import randrange
import sqlite3
import os
filetype = ""
filename = ""
username = ""
password = ""
RSAparams = {}
def modular_pow(base, exponent, modulus):
    ...
def miller_rabin(p, s):
    ...
def get_rand_prime(nbits=16):
    ...
def inverse(ra, rb):
    ...
def CRT(y, d, p, q):
    ...
def RSA_Init(nbits=1024):
    ...
def msg_to_int(msg):
    ...
def int_to_msg(i):
    ...
def encryption(msg, e, n):
    ...
def decryption(msg, d, p, q):
    ...
def iencrypt(key, filename):
    ...
def idecrypt(key, filename):
    ...
def tencrypt(key, filename):
    ...
def tdecrypt(key, filename):
    ...
def getKey(password):
    ...
def Main(choice):
    ...
def ienbutton():
    ...
def idebutton():
    ...
def tenbutton():
    ...
def tdebutton():
    ...
def iwin():
    ...
def twin():
    ...
def fd():
    ...
def loginbutton():
    ...
def registerbutton():
    ...
window = tk.Tk()
window.title("File Encryption System")
window.geometry("400x300")
label_login_or_register = tk.Label(window, text="Login or Register", font=("bold", 15))
label_login_or_register.grid(row=0, column=1)
label_login = tk.Label(window, text="Login", font=("bold", 13))
label_login.grid(row=2, column=1)
label_username = tk.Label(window, text="Username")
label_username.grid(row=3, column=0)
label_password = tk.Label(window, text="Password")
label_password.grid(row=4, column=0)
Text1 = tk.StringVar()
t1 = tk.Entry(window, textvariable=Text1)
t1.grid(row=3, column=1)
Text2 = tk.StringVar()
t2 = tk.Entry(window, textvariable=Text2)
t2.grid(row=4, column=1)
label_register = tk.Label(window, text="Register", font=("bold", 13))
label_register.grid(row=6, column=1)
label_register_username = tk.Label(window, text="Username")
label_register_username.grid(row=7, column=0)
label_register_password = tk.Label(window, text="Password")
label_register_password.grid(row=8, column=0)
Text3 = tk.StringVar()
t3 = tk.Entry(window, textvariable=Text3)
t3.grid(row=7, column=1)
Text4 = tk.StringVar()
t4 = tk.Entry(window, textvariable=Text4)
t4.grid(row=8, column=1)
b1 = tk.Button(window, text="Login", width=10, background='grey', command=loginbutton)
b1.grid(row=5, column=1)
b2 = tk.Button(window, text="Register", width=10, background='grey', command=registerbutton)
b2.grid(row=9, column=1)
window.mainloop()