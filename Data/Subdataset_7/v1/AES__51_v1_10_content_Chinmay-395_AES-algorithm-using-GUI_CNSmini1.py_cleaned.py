from tkinter import *
import pyAesCrypt
import io
b1 = 64 * 1024
b2 = "foopassword"
def fonk1(entry):
    b15.delete(0.0, END)
    b3 = bytes(entry, encoding='utf-8')
    b4 = io.BytesIO()
    pyAesCrypt.encryptStream(io.BytesIO(b3), b4, b2, b1)
    b5 = b4.getvalue()
    print("This is the ciphertext:\n" + str(b5))
    b6 = str(b5)
    with open('CipherText.txt', 'w') as f:
        f.write(b6)
    b15.insert(END, b6)
def fonk2():
    b16.delete(0.0, END)
    b4.seek(0)
    b7 = io.BytesIO()
    b8 = len(b4.getvalue())
    pyAesCrypt.decryptStream(b4, b7, b2, b1, b8)
    b9 = b7.getvalue().decode('utf-8')
    print("Decrypted data:\n" + b9)
    b16.insert(END, b9)
b10 = Tk()
b10.title("AES Encryption/Decryption")
b10.configure(b11 = "black")
Label(b10, b12 = "Enter the b12", bg="black", fg="white", font="none 12 bold").grid(b14=0, column=0, sticky='w')
b13 = Entry(b10, width=20, bg='white')
b13.grid(b14 = 2, column=0, sticky='w')
Button(b10, b12 = "Encrypt", width=6, command=lambda: fonk1(b13.get())).grid(b14=2, column=3, sticky='e')
Label(b10, b12 = "\nEncrypted Output", bg="black", fg="white", font="none 12 bold").grid(b14=4, column=0, sticky='w')
b15 = Text(b10, width=75, height=6, wrap=WORD, b11="White")
b15.grid(b14 = 5, column=0, columnspan=2, sticky='w')
Button(b10, b12 = "Decrypt", width=6, command=DecryptFunc).grid(b14=8, column=3, sticky='e')
Label(b10, b12 = "\nDecrypted Output", bg="black", fg="white", font="none 12 bold").grid(b14=11, column=0, sticky='w')
b16 = Text(b10, width=75, height=6, wrap=WORD, b11="White")
b16.grid(b14 = 14, column=0, columnspan=2, sticky='w')
b10.mainloop()