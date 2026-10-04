import hashlib
from PIL import Image
from tkinter import Tk, filedialog, messagebox
def xor(value, key_hex):
    key = int(key_hex, 16)
    return value ^ key
def key_schedule(password):
    first_hash = hashlib.sha256(password.encode()).hexdigest()
    second_hash = hashlib.sha256(first_hash.encode()).hexdigest()
    first_bytes = [first_hash[i:i+2] for i in range(0, len(first_hash), 2)]
    second_bytes = [second_hash[i:i+2] for i in range(0, len(second_hash), 2)]
    key = first_bytes + second_bytes
    return key
def encrypt(image_path, key):
    image = Image.open(image_path)
    width, height = image.size
    print(f'Image dimensions: Width = {width}, Height = {height}')
    private_key = []
    encrypted_image = Image.new('RGB', (width, height), color='black')
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            private_key.append(pixel)
            encrypted_image.putpixel((x, y), (0, 0, 0))
    encrypted_image.save('encrypted.jpg')
    with open('key.txt', 'w') as key_file:
        index = 0
        for pixel in private_key:
            for value in pixel:
                encrypted_value = xor(value, key[index])
                key_file.write(f'{encrypted_value:02x}\n')
                index = (index + 1) % len(key)
def decrypt(image_path, key_file):
    key = key_schedule("password")
    private_key = []
    with open(key_file) as file:
        for line in file:
            value = int(line.strip(), 16)
            private_key.append(value)
    image = Image.open(image_path)
    width, height = image.size
    print(f'Image dimensions: Width = {width}, Height = {height}')
    decrypted_image = Image.new('RGB', (width, height))
    index = 0
    for y in range(height):
        for x in range(width):
            r, g, b = private_key[index:index+3]
            decrypted_image.putpixel((x, y), (r, g, b))
            index += 3
    decrypted_image.save('decrypted.jpg')
def browse_file():
    root = Tk()
    root.withdraw()
    return filedialog.askopenfilename()
def main():
    action = input('Enter "e" for encryption or "d" for decryption: ').strip().lower()
    if action == 'e':
        image_path = browse_file()
        password = input('Enter a password: ')
        key = key_schedule(password + '.jpg')
        encrypt(image_path, key)
        print('Encryption completed.')
    elif action == 'd':
        image_path = browse_file()
        key_file = input('Enter the key file path: ')
        decrypt(image_path, key_file)
        print('Decryption completed.')
    else:
        print('Invalid input. Please enter "e" or "d".')
if __name__ == "__main__":
    main()