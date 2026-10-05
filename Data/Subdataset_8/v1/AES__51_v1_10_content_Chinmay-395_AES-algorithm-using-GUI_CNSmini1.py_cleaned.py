from tkinter import *
import pyAesCrypt
import io
bufferSize = 64 * 1024
password = "foopassword"
def EncryptFunc(entry):
    output1.delete(0.0, END)
    pbdata = bytes(entry, encoding='utf-8')
    fCiph = io.BytesIO()
    pyAesCrypt.encryptStream(io.BytesIO(pbdata), fCiph, password, bufferSize)
    encrypted_data = fCiph.getvalue()
    print("This is the ciphertext:\n" + str(encrypted_data))
    output_of_Cipher = str(encrypted_data)
    with open('CipherText.txt', 'w') as f:
        f.write(output_of_Cipher)
    output1.insert(END, output_of_Cipher)
def DecryptFunc():
    output.delete(0.0, END)
    fCiph.seek(0)
    fDec = io.BytesIO()
    ctlen = len(fCiph.getvalue())
    pyAesCrypt.decryptStream(fCiph, fDec, password, bufferSize, ctlen)
    decrypted_data = fDec.getvalue().decode('utf-8')
    print("Decrypted data:\n" + decrypted_data)
    output.insert(END, decrypted_data)
window = Tk()
window.title("AES Encryption/Decryption")
window.configure(background="black")
Label(window, text="Enter the text", bg="black", fg="white", font="none 12 bold").grid(row=0, column=0, sticky='w')
textentry = Entry(window, width=20, bg='white')
textentry.grid(row=2, column=0, sticky='w')
Button(window, text="Encrypt", width=6, command=lambda: EncryptFunc(textentry.get())).grid(row=2, column=3, sticky='e')
Label(window, text="\nEncrypted Output", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky='w')
output1 = Text(window, width=75, height=6, wrap=WORD, background="White")
output1.grid(row=5, column=0, columnspan=2, sticky='w')
Button(window, text="Decrypt", width=6, command=DecryptFunc).grid(row=8, column=3, sticky='e')
Label(window, text="\nDecrypted Output", bg="black", fg="white", font="none 12 bold").grid(row=11, column=0, sticky='w')
output = Text(window, width=75, height=6, wrap=WORD, background="White")
output.grid(row=14, column=0, columnspan=2, sticky='w')
window.mainloop()