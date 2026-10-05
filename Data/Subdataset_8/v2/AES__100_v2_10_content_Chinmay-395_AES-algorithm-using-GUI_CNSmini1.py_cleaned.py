from tkinter import Tk, Label, Entry, Button, Text, END, WORD
import pyAesCrypt
import io
BUFFER_SIZE = 64 * 1024
PASSWORD = "foopassword"
def encrypt_text():
    encrypted_text_display.delete('1.0', END)
    plain_text = user_input_entry.get()
    plain_text_bytes = plain_text.encode('utf-8')
    encrypted_bytes_io = io.BytesIO()
    pyAesCrypt.encryptStream(io.BytesIO(plain_text_bytes), encrypted_bytes_io, PASSWORD, BUFFER_SIZE)
    encrypted_data = encrypted_bytes_io.getvalue()
    encrypted_data_str = str(encrypted_data)
    encrypted_text_display.insert(END, encrypted_data_str)
    with open('CipherText.txt', 'w') as file:
        file.write(encrypted_data_str)
def decrypt_text():
    decrypted_text_display.delete('1.0', END)
    encrypted_bytes_io.seek(0)
    decrypted_bytes_io = io.BytesIO()
    pyAesCrypt.decryptStream(encrypted_bytes_io, decrypted_bytes_io, PASSWORD, BUFFER_SIZE, len(encrypted_bytes_io.getvalue()))
    decrypted_data = decrypted_bytes_io.getvalue().decode('utf-8')
    decrypted_text_display.insert(END, decrypted_data)
window = Tk()
window.title("AES Encryption/Decryption")
window.configure(background="black")
Label(window, text="Enter the text", bg="black", fg="white", font="none 12 bold").grid(row=0, column=0, sticky='w')
user_input_entry = Entry(window, width=20, bg='white')
user_input_entry.grid(row=1, column=0, sticky='w')
Button(window, text="Encrypt", command=encrypt_text).grid(row=1, column=1)
Label(window, text="\nEncrypted Output", bg="black", fg="white", font="none 12 bold").grid(row=2, column=0, sticky='w')
encrypted_text_display = Text(window, width=75, height=6, wrap=WORD, background="White")
encrypted_text_display.grid(row=3, column=0, columnspan=2, sticky='w')
Button(window, text="Decrypt", command=decrypt_text).grid(row=4, column=1)
Label(window, text="\nDecrypted Output", bg="black", fg="white", font="none 12 bold").grid(row=5, column=0, sticky='w')
decrypted_text_display = Text(window, width=75, height=6, wrap=WORD, background="White")
decrypted_text_display.grid(row=6, column=0, columnspan=2, sticky='w')
window.mainloop()