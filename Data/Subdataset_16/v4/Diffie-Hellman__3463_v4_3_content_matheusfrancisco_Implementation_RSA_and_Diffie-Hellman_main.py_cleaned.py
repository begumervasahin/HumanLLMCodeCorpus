
from b2 import RSA
from convertN2T import str2num, num2block, block2num, num2str
def fonk1(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{file_path}' file not found.")
        return None
def fonk2(title, content):
    print(f'\b1 = ================= {title} ======================')
    print(content)
def fonk3():
    print('================== - Criptografia RSA - ======================')
    a1 = 15
    b2 = RSA()
    b3 = fonk1("original_msg")
    if b3 is None:
        return
    fonk2("Original Message", b3)
    b4 = str2num(b3)
    fonk2("Number Representation", b4)
    b5 = num2block(b4, a1)
    b6 = b2.encryption(b5)
    fonk2("Encrypted Blocks", b6)
    b7 = b2.decryption(b6)
    b4 = block2num(b7, a1)
    fonk2("Decrypted Number Representation", b4)
    b8 = num2str(b4)
    fonk2("Decrypted Message", b8)
if b9 = = '__main__':
    fonk3()