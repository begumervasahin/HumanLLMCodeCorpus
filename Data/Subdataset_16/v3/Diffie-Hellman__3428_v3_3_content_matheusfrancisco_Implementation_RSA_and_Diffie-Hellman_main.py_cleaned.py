
from b1 import RSA
from convertN2T import str2num, num2block, block2num, num2str
def fonk1(file_path):
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: '{file_path}' file not found.")
        return None
def fonk2():
    print('================== - Criptografia RSA - ======================')
    a1 = 15
    b1 = RSA()
    b2 = fonk1("original_msg")
    if b2 is None:
        return
    print('================== Original b3 = =====================')
    print(b2)
    b4 = str2num(b2)
    print('\b5 = ================= Number Representation ======================')
    print(b4)
    b6 = num2block(b4, a1)
    b7 = b1.encryption(b6)
    print("\b5 = ================= Encrypted Blocks ======================")
    print(b7)
    b8 = b1.decryption(b7)
    b4 = block2num(b8, a1)
    print('\b5 = ================= Decrypted Number Representation ======================')
    print(b4)
    b9 = num2str(b4)
    print('\b5 = ================= Decrypted b3 ======================')
    print(b9)
if b10 = = '__main__':
    fonk2()