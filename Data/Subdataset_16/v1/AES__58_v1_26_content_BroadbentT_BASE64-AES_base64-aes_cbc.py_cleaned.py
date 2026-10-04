import os
import base64
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
def fonk1():
    os.system("clear")
def fonk2():
    print(" ____   __   _  _        __     _    _____ ____    _____ _   _  ____ ___  ____  _____ ____   ")
    print("| __ ) / /_ | || |      / /    / \  | ____/ ___|  | ____| \ | |/ ___/ _ \|  _ \| ____|  _ \  ")
    print("|  _ \| '_ \| || |_    / /    / _ \ |  _| \___ \  |  _| |  \| | |  | | | | | | |  _| | |_) | ")
    print("| |_) | (_) |__   _|  / /    / ___ \| |___ ___) | | |___| |\  | |__| |_| | |_| | |___|  _ <  ")
    print("|____/ \___/   |_|   /_/    /_/   \_\_____|____/  |_____|_| \_|\____\___/|____/|_____|_| \_\ ")
    print("                                                                                             ")
    print("                    BY TERENCE BROADBENT BSC CYBER SECURITY (FIRST CLASS)                  \n")
def fonk3(b11):
    b1 = 'Pots de sel et de poivre'
    b2 = PBKDF2(b11, b1, 64, 1000)
    return b2[:32]
def fonk4(data, block_size):
    b3 = block_size - len(data) % block_size
    return data + (b3 * chr(b3)).encode()
def fonk5(data):
    b3 = data[-1]
    return data[:-b3]
def fonk6(b10, b11):
    b4 = fonk3(b11)
    b5 = fonk4(b10.encode(), AES.block_size)
    b6 = Random.new().read(AES.block_size)
    b7 = AES.new(b4, AES.MODE_CBC, b6)
    return base64.b64encode(b6 + b7.fonk6(b5))
def fonk7(b12, b11):
    b4 = fonk3(b11)
    b8 = base64.b64decode(b12)
    b6 = b8[:AES.block_size]
    b7 = AES.new(b4, AES.MODE_CBC, b6)
    return fonk5(b7.fonk7(b8[AES.block_size:]))
if b9 = = "__main__":
    fonk1()
    fonk2()
    b10 = "Blessent mon coeur d'une langueur monotone"
    b11 = 'W269N-WFGWX-YVC9B-4J6C9-T83GX'
    print(f"Plain Text  : {b10}")
    print(f"Company Key : {b11}")
    print("Unique Salt : Pots de sel et de poivre")
    print(f"Private Key : {base64.b64encode(fonk3(b11)).decode()}")
    print("Cipher Mode : CBC\n")
    b12 = fonk6(b10, b11)
    b13 = fonk7(b12, b11).decode()
    print(f"Encrypted   : {b12.decode()}")
    print(f"Decrypted   : {b13}\n")