from tkinter import Tk, Label, Entry, Button, Text, END, WORD
import pyAesCrypt
import io
class AESApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AES Encryption/Decryption")
        self.root.configure(background="black")
        self.setup_ui()
    def setup_ui(self):
        Label(self.root, text="Enter the text", bg="black", fg="white", font="none 12 bold").grid(row=0, column=0, sticky='W')
        self.text_entry = Entry(self.root, width=20, bg='white')
        self.text_entry.grid(row=1, column=0, sticky='W')
        Button(self.root, text="Encrypt", command=self.encrypt_text).grid(row=1, column=1)
        Label(self.root, text="\nEncrypted Output", bg="black", fg="white", font="none 12 bold").grid(row=2, column=0, sticky='W')
        self.encrypted_output = Text(self.root, width=75, height=6, wrap=WORD, background="white")
        self.encrypted_output.grid(row=3, column=0, columnspan=2, sticky='W')
        Button(self.root, text="Decrypt", command=self.decrypt_text).grid(row=4, column=1)
        Label(self.root, text="\nDecrypted Output", bg="black", fg="white", font="none 12 bold").grid(row=5, column=0, sticky='W')
        self.decrypted_output = Text(self.root, width=75, height=6, wrap=WORD, background="white")
        self.decrypted_output.grid(row=6, column=0, columnspan=2, sticky='W')
    def encrypt_text(self):
        user_input = self.text_entry.get()
        input_bytes = user_input.encode('utf-8')
        input_stream = io.BytesIO(input_bytes)
        encrypted_stream = io.BytesIO()
        pyAesCrypt.encryptStream(input_stream, encrypted_stream, PASSWORD, BUFFER_SIZE)
        encrypted_data = encrypted_stream.getvalue()
        self.encrypted_output.delete('1.0', END)
        self.encrypted_output.insert(END, str(encrypted_data))
        with open('CipherText.txt', 'wb') as file:
            file.write(encrypted_data)
    def decrypt_text(self):
        try:
            with open('CipherText.txt', 'rb') as file:
                encrypted_data = file.read()
            encrypted_stream = io.BytesIO(encrypted_data)
            decrypted_stream = io.BytesIO()
            pyAesCrypt.decryptStream(encrypted_stream, decrypted_stream, PASSWORD, BUFFER_SIZE, len(encrypted_data))
            self.decrypted_output.delete('1.0', END)
            self.decrypted_output.insert(END, decrypted_stream.getvalue().decode('utf-8'))
        except FileNotFoundError:
            self.decrypted_output.delete('1.0', END)
            self.decrypted_output.insert(END, "Encrypted file not found. Please encrypt some text first.")
BUFFER_SIZE = 64 * 1024
PASSWORD = "foopassword"
if __name__ == "__main__":
    root = Tk()
    app = AESApp(root)
    root.mainloop()