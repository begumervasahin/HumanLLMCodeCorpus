import io
import pyAesCrypt
from tkinter import *
b1 = 64 * 1024
b2 = "foopassword"
b3 = io.BytesIO()
b4 = io.BytesIO()
def fonk1(entry):
    b15.delete(0.0, END)
    b5 = bytes(entry, encoding='utf-8')
    b6 = io.BytesIO(b5)
    b3.seek(0)
    b3.truncate(0)
    pyAesCrypt.encryptStream(b6, b3, b2, b1)
    b3.seek(0)
    b7 = b3.getvalue()
    with open('CipherText.txt', 'wb') as f:
        f.write(b7)
    b15.insert(END, str(b7))
def fonk2():
    b16.delete(0.0, END)
    b4.seek(0)
    b4.truncate(0)
    b8 = len(b3.getvalue())
    b3.seek(0)
    pyAesCrypt.decryptStream(b3, b4, b2, b1, b8)
    b9 = b4.getvalue().decode('utf-8')
    b16.insert(END, b9)
b10 = Tk()
b10.title("AES Encryption/Decryption")
b10.configure(b11 = "black")
Label(b10, b12 = "Enter the b12", bg="black", fg="white", font="none 12 bold").grid(b14=0, column=0, sticky='w')
b13 = Entry(b10, width=20, bg='white')
b13.grid(b14 = 2, column=0, sticky='w')
Button(b10, b12 = "Encrypt", width=6, command=lambda: fonk1(b13.get())).grid(b14=2, column=3, sticky='e')
Label(b10, b12 = "\nEncrypted Output", bg="black", fg="white", font="none 12 bold").grid(b14=4, column=0, sticky='w')
b15 = Text(b10, width=75, height=6, wrap=WORD, b11="white")
b15.grid(b14 = 5, column=0, columnspan=2, sticky='w')
Button(b10, b12 = "Decrypt", width=6, command=decrypt_text).grid(b14=8, column=3, sticky='e')
Label(b10, b12 = "\nDecrypted Output", bg="black", fg="white", font="none 12 bold").grid(b14=11, column=0, sticky='w')
b16 = Text(b10, width=75, height=6, wrap=WORD, b11="white")
b16.grid(b14 = 14, column=0, columnspan=2, sticky='w')
b10.mainloop()