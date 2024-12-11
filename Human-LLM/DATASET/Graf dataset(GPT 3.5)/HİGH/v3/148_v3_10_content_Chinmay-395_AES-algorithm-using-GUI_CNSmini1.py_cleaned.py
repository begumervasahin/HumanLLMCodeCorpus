from tkinter import Tk, Label, Entry, Button, Text, END, WORD
import pyAesCrypt
import io
b1 = 64 * 1024
b2 = "foopassword"
b3 = 'CipherText.txt'
def fonk1():
    b15.delete('1.0', END)
    b4 = b13.get()
    b5 = b4.encode('utf-8')
    b6 = io.BytesIO()
    pyAesCrypt.encryptStream(io.BytesIO(b5), b6, b2, b1)
    b7 = b6.getvalue()
    b15.insert(END, str(b7))
    with open(b3, 'wb') as file:
        file.write(b7)
def fonk2():
    b16.delete('1.0', END)
    with open(b3, 'rb') as file:
        b7 = file.read()
    b6 = io.BytesIO(b7)
    b8 = io.BytesIO()
    pyAesCrypt.decryptStream(b6, b8, b2, b1, len(b7))
    b9 = b8.getvalue().decode('utf-8')
    b16.insert(END, b9)
def fonk3():
    b10 = Tk()
    b10.title("AES Encryption/Decryption Tool")
    b10.configure(b11 = "black")
    Label(b10, b12 = "Enter b12 to encrypt:", bg="black", fg="white", font="none 12 bold").grid(b14=0, column=0, sticky='W')
    global b13
    b13 = Entry(b10, width=50, bg='white')
    b13.grid(b14 = 1, column=0, sticky='W')
    Button(b10, b12 = "Encrypt", command=encrypt_text).grid(b14=1, column=1, padx=5)
    Label(b10, b12 = "Encrypted b12:", bg="black", fg="white", font="none 12 bold").grid(b14=2, column=0, sticky='W')
    global b15
    b15 = Text(b10, width=75, height=6, wrap=WORD, b11="white")
    b15.grid(b14 = 3, column=0, columnspan=2, sticky='W')
    Button(b10, b12 = "Decrypt", command=decrypt_text).grid(b14=4, column=1, padx=5)
    Label(b10, b12 = "Decrypted b12:", bg="black", fg="white", font="none 12 bold").grid(b14=5, column=0, sticky='W')
    global b16
    b16 = Text(b10, width=75, height=6, wrap=WORD, b11="white")
    b16.grid(b14 = 6, column=0, columnspan=2, sticky='W')
    return b10
def fonk4():
    b10 = fonk3()
    b10.mainloop()
if b17 = = "__main__":
    fonk4()