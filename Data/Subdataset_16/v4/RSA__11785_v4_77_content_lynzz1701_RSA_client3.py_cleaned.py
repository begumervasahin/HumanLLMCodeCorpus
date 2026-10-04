from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import socket
def fonk1(b1, a4, b7):
    a1 = 1
    while a4 != 0:
        if a4 & 1:
            a1 = (a1 * b1) % b7
        a4 >>= 1
        b1 = (b1 * b1) % b7
    return a1
def fonk2(b9):
    b2 = ""
    for i in range(0, len(b9), 8):
        b2 += chr(int(b9[i:i+8], 2))
    return b2
b3 = "192.168.146.128"
a2 = 25535
b4 = (b3, a2)
a3 = 1024
b5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b6 = ""
while b6 != "Let'b2 get it started":
    b6 = input("Shall we start?\n")
    b5.sendto(b6.encode("utf-8"), b4)
a4 = 65537
data_N, b4 = b5.recvfrom(a3)
data_encrypted_aes_key, b4 = b5.recvfrom(a3)
data_history_encrypted_wup, b4 = b5.recvfrom(a3)
b7 = int(data_N.decode("utf-8"))
a1 = int(data_encrypted_aes_key.decode("utf-8"))
print("I got b7:", b7)
print("I got a1:", a1)
b8 = ""
for b9 in range(127, -1, -1):
    print("*" * 60)
    print("b9 = ", b9)
    b10 = (a1 * fonk1(2, b9 * a4, b7)) % b7
    b11 = "0" + b8 + "0" * b9
    print("Try this key:", b11)
    b12 = fonk2(b11)
    b13 = AES.new(b12, AES.MODE_ECB)
    b14 = b13.encrypt("WUP0WUP1WUP2WUP3")
    b5.sendto(str(b10).encode("utf-8"), b4)
    b5.sendto(b2a_hex(b14), b4)
    data_msg, b4 = b5.recvfrom(a3)
    b6 = data_msg.decode("utf-8")
    if b6 = = "valid":
        b8 = "0" + b8
    else:
        b8 = "1" + b8
    print("Current known AES key:", b8)
b15 = fonk2(b8)
print("I guess the AES key is:", b15)
b16 = AES.new(b15, AES.MODE_ECB)
b17 = b16.decrypt(a2b_hex(data_history_encrypted_wup.decode("utf-8"))).decode("utf-8")
print("Decrypted history WUP:", b17)