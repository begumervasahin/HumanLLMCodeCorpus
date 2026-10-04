import io
import pyAesCrypt
from tkinter import *
bufferSize = 64 * 1024
password = "foopassword"
fCiph = io.BytesIO()
fDec = io.BytesIO()
def EncryptFunc(entry):
    output1.delete(0.0, END)
    pbdata = bytes(entry, encoding='utf-8')
    fIn = io.BytesIO(pbdata)
    fCiph.seek(0)
    fCiph.truncate(0)
    pyAesCrypt.encryptStream(fIn, fCiph, password, bufferSize)
    fCiph.seek(0)
    output_of_Cipher = fCiph.getvalue()
    with open('CipherText.txt', 'wb') as f:
        f.write(output_of_Cipher)
    output1.insert(END, str(output_of_Cipher))
def DecryptFunc():
    output.delete(0.0, END)
    fDec.seek(0)
    fDec.truncate(0)
    ctlen = len(fCiph.getvalue())
    fCiph.seek(0)
    pyAesCrypt.decryptStream(fCiph, fDec, password, bufferSize, ctlen)
    output_of_Decipher = fDec.getvalue().decode('utf-8')
    output.insert(END, output_of_Decipher)
window = Tk()
window.title("AES Encryption/Decryption")
window.configure(background="black")
Label(window, text="Enter the text", bg="black", fg="white", font="none 12 bold").grid(row=0, column=0, sticky='w')
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky='w')
Button(window, text="Encrypt", width=6, command=lambda: EncryptFunc(textentry.get())).grid(row=2, column=3, sticky='e')
Label(window, text="\nOutput", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky='w')
output1 = Text(window, width=75, height=6, wrap=WORD, background="white")
output1.grid(row=5, column=0, columnspan=2, sticky='w')
Button(window, text="Decrypt", width=6, command=DecryptFunc).grid(row=8, column=3, sticky='e')
Label(window, text="\nOutput", bg="black", fg="white", font="none 12 bold").grid(row=11, column=0, sticky='w')
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=14, column=0, columnspan=2, sticky='w')
window.mainloop()