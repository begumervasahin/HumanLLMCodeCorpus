import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import sqlite3
import os
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from random import randrange
def initialize_rsa_params(nbits=1024):
    p = get_random_prime(nbits)
    q = get_random_prime(nbits)
    while p == q:
        q = get_random_prime(nbits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e, d = generate_rsa_keys(phi)
    return {
        "p": p,
        "q": q,
        "n": n,
        "phi": phi,
        "e": e,
        "d": d
    }
def get_random_prime(nbits=16):
    while True:
        p = randrange(2 ** nbits, 2 * 2 ** nbits)
        if miller_rabin_primality_test(p, 100):
            return p
def miller_rabin_primality_test(p, s):
    if p == 2:
        return True
    if p % 2 == 0:
        return False
    u, r = calculate_ur(p)
    for i in range(s):
        a = randrange(2, p - 1)
        z = modular_pow(a, r, p)
        if z != 1 and z != (p - 1):
            for j in range(u):
                z = modular_pow(z, 2, p)
                if z == p - 1:
                    break
                else:
                    return False
    return True
def calculate_ur(num):
    u = 0
    num -= 1
    while True:
        u += 1
        num
        if u != 0 and num % 2 != 0:
            break
    return (u, num)
def generate_rsa_keys(phi):
    e = randrange(2 ** 16, 2 ** 17)
    d = modular_multiplicative_inverse(phi, e)
    while d == -1:
        e = randrange(2 ** 16, 2 ** 17)
        d = modular_multiplicative_inverse(phi, e)
    return e, d
def modular_multiplicative_inverse(ra, rb):
    if rb > ra:
        ra, rb = rb, ra
    modulos = ra
    mult = [(1, 0), (0, 1)]
    i = 2
    while True:
        mod = ra % rb
        q = (ra - mod)
        ra = rb
        rb = mod
        mult = [
            (mult[1][0], mult[1][1]),
            ((-q * mult[1][0]) + mult[0][0], (-q * mult[1][1]) + mult[0][1])
        ]
        if mod == 0:
            if ra == 1:
                return mult[0][1] % modulos
            else:
                return -1
def main(choice):
    global passw, filetypee, filenamee
    if choice.lower() == 'e':
        if filetypee == 't':
            encrypt_text(get_key(passw), filenamee)
        elif filetypee == 'i':
            encrypt_image(get_key(passw), filenamee)
    elif choice.lower() == 'd':
        if filetypee == 't':
            decrypt_text(get_key(passw), filenamee)
        elif filetypee == 'i':
            decrypt_image(get_key(passw), filenamee)
    else:
        print("No Option selected, closing...")
def encrypt_text(key, filename):
    pass
def decrypt_text(key, filename):
    pass
def encrypt_image(key, filename):
    pass
def decrypt_image(key, filename):
    pass
def get_key(password):
    hasher = SHA256.new(password.encode('utf-8'))
    return hasher.digest()
def create_image_window():
    pass
def create_text_window():
    pass
def file_dialog():
    pass
def login_button():
    pass
def register_button():
    pass
def create_main_window():
    pass
if __name__ == "__main__":
    create_main_window()