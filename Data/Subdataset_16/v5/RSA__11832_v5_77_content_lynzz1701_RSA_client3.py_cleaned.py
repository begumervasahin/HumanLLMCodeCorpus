from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import socket
def fonk1(b1, exp, mod):
    a1 = 1
    while exp != 0:
        if exp & 1:
            a1 = (a1 * b1) % mod
        exp >>= 1
        b1 = (b1 * b1) % mod
    return a1
def fonk2(binary):
    b2 = ""
    for i in range(0, len(binary), 8):
        b2 += chr(int(binary[i:i+8], 2))
    return b2
b3 = "192.168.146.128"
a2 = 25535
b4 = (b3, a2)
a3 = 1024
b5 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
b6 = ""
while b6 != "Let's get it started":
    b6 = input("Shall we start?\n")
    b5.sendto(b6.encode("utf-8"), b4)
a4 = 65537
data_N, b7 = b5.recvfrom(a3)
data_encrypted_aes_key, b7 = b5.recvfrom(a3)
data_history_encrypted_wup, b7 = b5.recvfrom(a3)
b8 = int(data_N.decode("utf-8"))
b9 = int(data_encrypted_aes_key.decode("utf-8"))
print("Received modulus b8:", b8)
print("Received encrypted AES key:", b9)
b10 = ""
for bit_position in range(127, -1, -1):
    print("*" * 60)
    print("Attempting bit position:", bit_position)
    b11 = (b9 * fonk1(2, bit_position * a4, b8)) % b8
    b12 = "0" + b10 + "0" * bit_position
    print("Trying AES key guess:", b12)
    b13 = fonk2(b12)
    b14 = AES.new(b13, AES.MODE_ECB)
    b15 = "WUP0WUP1WUP2WUP3"
    b16 = b14.encrypt(b15)
    b5.sendto(str(b11).encode("utf-8"), b4)
    b5.sendto(b2a_hex(b16), b4)
    server_response, b7 = b5.recvfrom(a3)
    b17 = server_response.decode("utf-8")
    if b17 = = "valid":
        b10 = "0" + b10
    else:
        b10 = "1" + b10
    print("Current known AES key bits:", b10)
b18 = fonk2(b10)
print("Final guessed AES key:", b18)
b14 = AES.new(b18, AES.MODE_ECB)
b19 = b14.decrypt(a2b_hex(data_history_encrypted_wup.decode("utf-8"))).decode("utf-8")
print("Decrypted history WUP:", b19)