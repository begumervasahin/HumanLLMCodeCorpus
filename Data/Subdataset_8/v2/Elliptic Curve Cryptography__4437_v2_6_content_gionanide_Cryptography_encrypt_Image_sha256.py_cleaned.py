from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox as tkMessageBox
import os
from PIL import Image
import hashlib
def xor(a, b):
    return a ^ int(b, 16)
def generate_key_schedule(password):
    first_pass = hashlib.sha256(password.encode()).hexdigest()
    second_pass = hashlib.sha256(first_pass.encode()).hexdigest()
    first_pass_bytes = [int(first_pass[i:i+2], 16) for i in range(0, len(first_pass), 2)]
    second_pass_bytes = [int(second_pass[i:i+2], 16) for i in range(0, len(second_pass), 2)]
    key = first_pass_bytes + second_pass_bytes
    return key
def encrypt_image(image_path, password):
    key = generate_key_schedule(password)
    image = Image.open(image_path, mode='r')
    width, height = image.size
    private_key = [image.getpixel((x, y)) for y in range(height) for x in range(width)]
    for y in range(height):
        for x in range(width):
            image.putpixel((x, y), (0, 0, 0))
    image.show()
    image.save('encrypted.jpg')
    with open('key.txt', 'w') as private_key_file:
        for pixel in private_key:
            for val in pixel:
                private_key_file.write(str(xor(val, key.pop(0))))
                private_key_file.write('\n')
def decrypt_image(image_path, private_key_path, password):
    key = generate_key_schedule(password)
    private_key = []
    with open(private_key_path) as pk:
        for f in pk.readlines():
            private_key.append(xor(int(f), key.pop(0)))
    image = Image.open(image_path, mode='r')
    width, height = image.size
    k = 0
    for y in range(height):
        for x in range(width):
            image.putpixel((x, y), (int(private_key[k]), int(private_key[k+1]), int(private_key[k+2])))
            k += 3
    image.show()
    image.save('decrypted.jpg')
def main():
    image_path = input('Enter the path of the image file: ')
    password = input('Enter the password: ')
    choice = input('Enter "e" for encryption or "d" for decryption: ')
    if choice == 'e':
        encrypt_image(image_path, password)
    elif choice == 'd':
        private_key_path = input('Enter the path of the private key file: ')
        decrypt_image(image_path, private_key_path, password)
    else:
        print('Input Error')
if __name__ == "__main__":
    main()