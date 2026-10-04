import io
import pyAesCrypt
from tkinter import *
BUFFER_SIZE = 64 * 1024
PASSWORD = "foopassword"
fCiph = io.BytesIO()
def encrypt_text(entry):
    encryption_output.delete(0.0, END)
    plaintext_bytes = bytes(entry, encoding='utf-8')
    plaintext_stream = io.BytesIO(plaintext_bytes)
    fCiph.seek(0)
    fCiph.truncate(0)
    pyAesCrypt.encryptStream(plaintext_stream, fCiph, PASSWORD, BUFFER_SIZE)
    fCiph.seek(0)
    encrypted_bytes = fCiph.getvalue()
    with open('CipherText.txt', 'wb') as f:
        f.write(encrypted_bytes)
    encryption_output.insert(END, str(encrypted_bytes))
def decrypt_text():
    decryption_output.delete(0.0, END)
    decrypted_data = io.BytesIO()
    encrypted_length = len(fCiph.getvalue())
    fCiph.seek(0)
    pyAesCrypt.decryptStream(fCiph, decrypted_data, PASSWORD, BUFFER_SIZE, encrypted_length)
    decrypted_text = decrypted_data.getvalue().decode('utf-8')
    decryption_output.insert(END, decrypted_text)
window = Tk()
window.title("AES Encryption/Decryption")
window.configure(background="black")
Label(window, text="Enter the text", bg="black", fg="white", font="none 12 bold").grid(row=0, column=0, sticky='w')
text_entry = Entry(window, width=20, bg='white')
text_entry.grid(row=2, column=0, sticky='w')
Button(window, text="Encrypt", width=6, command=lambda: encrypt_text(text_entry.get())).grid(row=2, column=3, sticky='e')
Label(window, text="\nEncrypted Output", bg="black", fg="white", font="none 12 bold").grid(row=4, column=0, sticky='w')
encryption_output = Text(window, width=75, height=6, wrap=WORD, background="white")
encryption_output.grid(row=5, column=0, columnspan=2, sticky='w')
Button(window, text="Decrypt", width=6, command=decrypt_text).grid(row=8, column=3, sticky='e')
Label(window, text="\nDecrypted Output", bg="black", fg="white", font="none 12 bold").grid(row=11, column=0, sticky='w')
decryption_output = Text(window, width=75, height=6, wrap=WORD, background="white")
decryption_output.grid(row=14, column=0, columnspan=2, sticky='w')
window.mainloop()