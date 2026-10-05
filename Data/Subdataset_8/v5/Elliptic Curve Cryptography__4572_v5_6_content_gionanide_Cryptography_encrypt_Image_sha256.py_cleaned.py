from tkinter import *
from tkinter.filedialog import askopenfilename
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
    return first_pass_bytes + second_pass_bytes
def encrypt_image(image_path):
    private_key = []
    key = generate_key_schedule(get_password())
    image = Image.open(image_path, mode='r')
    width, height = image.size
    print('Width:', width, 'Height:', height)
    for y in range(height):
        for x in range(width):
            cc = image.getpixel((x, y))
            private_key.append(cc)
            image.putpixel((x, y), (0, 0, 0))
    image.show()
    image.save('encrypted.jpg')
    with open('key.txt', 'w') as private_file:
        for x in range(len(private_key)):
            for y in range(3):
                private_file.write(str(xor(private_key[x][y], key[x % len(key)])) + '\n')
def decrypt_image(image_path, private_key_path):
    key = generate_key_schedule(get_password())
    private_key = []
    image = Image.open(image_path, mode='r')
    with open(private_key_path) as pk:
        for f in pk.readlines():
            private_key.append(xor(int(f), key[len(private_key) % len(key)]))
    width, height = image.size
    print('Width:', width, 'Height:', height)
    k = 0
    for y in range(height):
        for x in range(width):
            image.putpixel((x, y), (int(private_key[k]), int(private_key[k+1]), int(private_key[k+2])))
            k += 3
    image.show()
    image.save('decrypted.jpg')
def get_password():
    password = input('Enter a password: ')
    return password + '.jpg'
def main():
    root = Tk()
    root.withdraw()
    image_path = askopenfilename(title="Select Image for Encryption/Decryption", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if image_path:
        choice = input('Enter "e" for encryption or "d" for decryption: ')
        if choice == 'e':
            encrypt_image(image_path)
        elif choice == 'd':
            private_key_path = input('Enter the path of the private key file: ')
            decrypt_image(image_path, private_key_path)
        else:
            print('Input Error')
    else:
        print("No image selected.")
if __name__ == "__main__":
    main()