from tkinter import Tk, Label, Entry, Button, Text, END, WORD
import pyAesCrypt
import io
b1 = 64 * 1024
b2 = "foopassword"
def fonk1():
    b15.delete('1.0', END)
    b3 = b13.get()
    b4 = b3.encode('utf-8')
    b5 = io.BytesIO()
    pyAesCrypt.encryptStream(io.BytesIO(b4), b5, b2, b1)
    b6 = b5.getvalue()
    b7 = str(b6)
    b15.insert(END, b7)
    with open('CipherText.txt', 'w') as file:
        file.write(b7)
def fonk2():
    b16.delete('1.0', END)
    b5.seek(0)
    b8 = io.BytesIO()
    pyAesCrypt.decryptStream(b5, b8, b2, b1, len(b5.getvalue()))
    b9 = b8.getvalue().decode('utf-8')
    b16.insert(END, b9)
b10 = Tk()
b10.title("AES Encryption/Decryption")
b10.configure(b11 = "black")
Label(b10, b12 = "Enter the b12", bg="black", fg="white", font="none 12 bold").grid(b14=0, column=0, sticky='w')
b13 = Entry(b10, width=20, bg='white')
b13.grid(b14 = 1, column=0, sticky='w')
Button(b10, b12 = "Encrypt", command=encrypt_text).grid(b14=1, column=1)
Label(b10, b12 = "\nEncrypted Output", bg="black", fg="white", font="none 12 bold").grid(b14=2, column=0, sticky='w')
b15 = Text(b10, width=75, height=6, wrap=WORD, b11="White")
b15.grid(b14 = 3, column=0, columnspan=2, sticky='w')
Button(b10, b12 = "Decrypt", command=decrypt_text).grid(b14=4, column=1)
Label(b10, b12 = "\nDecrypted Output", bg="black", fg="white", font="none 12 bold").grid(b14=5, column=0, sticky='w')
b16 = Text(b10, width=75, height=6, wrap=WORD, b11="White")
b16.grid(b14 = 6, column=0, columnspan=2, sticky='w')
b10.mainloop()