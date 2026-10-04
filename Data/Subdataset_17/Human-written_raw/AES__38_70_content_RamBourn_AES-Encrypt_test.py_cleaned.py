from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from tkinter import *
import tkinter.filedialog as filedialog
def file_open():
    filename=filedialog.askopenfilename()
    file_in.insert(INSERT,filename)
    if filename:
        f=open(filename,'r')
        input_in.insert(INSERT,f.read())
def add_to_16(text):
    if len(text.encode('utf-8')) % 16:
        add = 16 - (len(text.encode('utf-8')) % 16)
    else:
        add = 0
    text = text + ('\0' * add)
    return text.encode('utf-8')
def encrypt():
    key = key_in.get().encode('utf-8')
    key_file=open('key.txt','w+')
    key_file.write(str(key))
    key_file.close()
    mode = AES.MODE_CBC
    iv = b'qqqqqqqqqqqqqqqq'
    text=str(input_in.get('0.0',END)).strip('\n')
    text = add_to_16(text)
    cryptos = AES.new(key, mode, iv)
    cipher_text = cryptos.encrypt(text)
    encrypt_out.insert(INSERT,b2a_hex(cipher_text))
    encrypted_file=open('encrypted.txt','w+')
    encrypted_file.write(str(b2a_hex(cipher_text)))
def decrypt():
    key = key_in.get().encode('utf-8')
    iv = b'qqqqqqqqqqqqqqqq'
    mode = AES.MODE_CBC
    cryptos = AES.new(key, mode, iv)
    text=str(encrypt_out.get('0.0',END)).strip('\n')
    plain_text = cryptos.decrypt(a2b_hex(text))
    decrypt_out.insert(INSERT,bytes.decode(plain_text).rstrip('\0'))
win=Tk()
win.title('AES-Encrypt')
key_lb=Label(win,text='Key')
input_lb=Label(win,text='Input')
encrypt_lb=Label(win,text='Encrypted')
decrypt_lb=Label(win,text='Decrypted')
file_bt=Button(win,text='Open',command=file_open)
encrypt_bt=Button(win,text='Encrypt',command=encrypt)
decrypt_bt=Button(win,text='Decrypt',command=decrypt)
input_in=Text(win,height=10)
file_in=Text(win,height=1)
key_in=Entry(win)
encrypt_out=Text(win,height=15)
decrypt_out=Text(win,height=15)
file_bt.grid(row=0,column=0)
file_in.grid(row=0,column=1)
key_lb.grid(row=1,column=0)
key_in.grid(row=1,column=1,sticky=E+W)
input_lb.grid(row=2,column=0,sticky=N)
input_in.grid(row=2,column=1)
encrypt_bt.grid(row=3,column=0,sticky=N)
encrypt_out.grid(row=3,column=1)
decrypt_bt.grid(row=4,column=0,sticky=N)
decrypt_out.grid(row=4,column=1)
win.mainloop()