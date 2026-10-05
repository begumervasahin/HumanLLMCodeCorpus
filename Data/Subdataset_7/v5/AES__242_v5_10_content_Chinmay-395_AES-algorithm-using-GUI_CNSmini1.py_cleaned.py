from tkinter import Tk, Label, Entry, Button, Text, END, WORD
import pyAesCrypt
import io
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b1.title("AES Encryption/Decryption")
        self.b1.configure(b2 = "black")
        self.fonk2()
    def fonk2(self):
        Label(self.b1, b3 = "Enter the b3", bg="black", fg="white", font="none 12 bold").grid(b5=0, column=0, sticky='W')
        self.b4 = Entry(self.b1, width=20, bg='white')
        self.b4.grid(b5 = 1, column=0, sticky='W')
        Button(self.b1, b3 = "Encrypt", command=self.encrypt_text).grid(b5=1, column=1)
        Label(self.b1, b3 = "\nEncrypted Output", bg="black", fg="white", font="none 12 bold").grid(b5=2, column=0, sticky='W')
        self.b6 = Text(self.b1, width=75, height=6, wrap=WORD, b2="white")
        self.b6.grid(b5 = 3, column=0, columnspan=2, sticky='W')
        Button(self.b1, b3 = "Decrypt", command=self.decrypt_text).grid(b5=4, column=1)
        Label(self.b1, b3 = "\nDecrypted Output", bg="black", fg="white", font="none 12 bold").grid(b5=5, column=0, sticky='W')
        self.b7 = Text(self.b1, width=75, height=6, wrap=WORD, b2="white")
        self.b7.grid(b5 = 6, column=0, columnspan=2, sticky='W')
    def fonk3(self):
        b8 = self.b4.get()
        b9 = b8.encode('utf-8')
        b10 = io.BytesIO(b9)
        b11 = io.BytesIO()
        pyAesCrypt.encryptStream(b10, b11, b15, b14)
        b12 = b11.getvalue()
        self.b6.delete('1.0', END)
        self.b6.insert(END, str(b12))
        with open('CipherText.txt', 'wb') as file:
            file.write(b12)
    def fonk4(self):
        try:
            with open('CipherText.txt', 'rb') as file:
                b12 = file.read()
            b11 = io.BytesIO(b12)
            b13 = io.BytesIO()
            pyAesCrypt.decryptStream(b11, b13, b15, b14, len(b12))
            self.b7.delete('1.0', END)
            self.b7.insert(END, b13.getvalue().decode('utf-8'))
        except FileNotFoundError:
            self.b7.delete('1.0', END)
            self.b7.insert(END, "Encrypted file not found. Please encrypt some b3 first.")
b14 = 64 * 1024
b15 = "foopassword"
if b16 = = "__main__":
    b1 = Tk()
    b17 = class1(b1)
    b1.mainloop()