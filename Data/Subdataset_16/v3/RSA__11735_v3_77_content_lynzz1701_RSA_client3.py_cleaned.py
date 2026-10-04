import socket
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
def fonk1(b1, exponent, modulus):
    a1 = 1
    while exponent:
        if exponent & 1:
            a1 = (a1 * b1) % modulus
        exponent >>= 1
        b1 = (b1 * b1) % modulus
    return a1
def fonk2(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
def fonk3(b13, b12, b16, a3, b15):
    b2 = ""
    for b3 in range(127, -1, -1):
        print("*" * 60)
        print(f"b3 = {b3}")
        b4 = (b16 * fonk1(2, b3 * a3, b15)) % b15
        b5 = "0" + b2 + "0" * b3
        print(f"Trying key: {b5}")
        b6 = fonk2(b5)
        b7 = AES.new(b6.encode('utf-8'), AES.MODE_ECB)
        b8 = b7.encrypt(b3"WUP0WUP1WUP2WUP3")
        b13.sendto(str(b4).encode("utf-8"), b12)
        b13.sendto(b2a_hex(b8), b12)
        data_msg, b9 = b13.recvfrom(1024)
        b10 = data_msg.decode("utf-8")
        if b10 = = "valid":
            b2 = "0" + b2
        else:
            b2 = "1" + b2
        print(f"Current known AES key: {b2}")
    return fonk2(b2)
def fonk4():
    b11 = "192.168.146.128"
    a2 = 25535
    b12 = (b11, a2)
    b13 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        b14 = input("Shall we start?\n")
        b13.sendto(b14.encode("utf-8"), b12)
        if b14 = = "Let's get it started":
            break
    a3 = 65537
    data_N, b9 = b13.recvfrom(1024)
    data_encrypted_aes_key, b9 = b13.recvfrom(1024)
    data_history_encrypted_wup, b9 = b13.recvfrom(1024)
    b15 = int(data_N.decode("utf-8"))
    b16 = int(data_encrypted_aes_key.decode("utf-8"))
    print(f"I got b15: {b15}")
    print(f"I got b16: {b16}")
    b17 = fonk3(b13, b12, b16, a3, b15)
    print(f"I guess the AES key is: {b17}")
    b18 = AES.new(b17.encode('utf-8'), AES.MODE_ECB)
    b19 = b18.decrypt(a2b_hex(data_history_encrypted_wup.decode("utf-8"))).decode("utf-8")
    print(f"Decrypted history WUP: {b19}")
if b20 = = "__main__":
    fonk4()