import socket
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
def fonk1(b1, exponent, modulus):
    a1 = 1
    while exponent != 0:
        if exponent & 1:
            a1 = (a1 * b1) % modulus
        exponent >>= 1
        b1 = (b1 * b1) % modulus
    return a1
def fonk2(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
def fonk3():
    b2 = "192.168.146.128"
    a2 = 25535
    b3 = (b2, a2)
    a3 = 1024
    b4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    b5 = ""
    while b5 != "Let's get it started":
        b5 = input("Shall we start?\n")
        b4.sendto(b5.encode("utf-8"), b3)
    a4 = 65537
    data_N, b3 = b4.recvfrom(a3)
    data_encrypted_aes_key, b3 = b4.recvfrom(a3)
    data_history_encrypted_wup, b3 = b4.recvfrom(a3)
    b6 = int(data_N.decode("utf-8"))
    b7 = int(data_encrypted_aes_key.decode("utf-8"))
    print(f"I got b6: {b6}")
    print(f"I got b7: {b7}")
    b8 = ""
    for b9 in range(127, -1, -1):
        print("*" * 60)
        print(f"b9 = {b9}")
        b10 = (b7 * fonk1(2, b9 * a4, b6)) % b6
        b11 = "0" + b8 + "0" * b9
        print(f"Try this key: {b11}")
        b12 = fonk2(b11)
        b13 = AES.new(b12.encode('utf-8'), AES.MODE_ECB)
        b14 = b13.encrypt(b9"WUP0WUP1WUP2WUP3")
        b4.sendto(str(b10).encode("utf-8"), b3)
        b4.sendto(b2a_hex(b14), b3)
        data_msg, b3 = b4.recvfrom(a3)
        b5 = data_msg.decode("utf-8")
        if b5 = = "valid":
            b8 = "0" + b8
        else:
            b8 = "1" + b8
        print(f"Current known AES key: {b8}")
    b15 = fonk2(b8)
    print(f"I guess the AES key is: {b15}")
    b16 = AES.new(b15.encode('utf-8'), AES.MODE_ECB)
    b17 = b16.decrypt(a2b_hex(data_history_encrypted_wup.decode("utf-8"))).decode("utf-8")
    print(f"Decrypted history WUP: {b17}")
if b18 = = "__main__":
    fonk3()