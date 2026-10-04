import socket
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
def quick_pow_mod(base, exponent, modulus):
    result = 1
    while exponent != 0:
        if exponent & 1:
            result = (result * base) % modulus
        exponent >>= 1
        base = (base * base) % modulus
    return result
def bin_to_str(binary):
    return ''.join(chr(int(binary[i:i+8], 2)) for i in range(0, len(binary), 8))
def main():
    host = "192.168.146.128"
    port = 25535
    addr = (host, port)
    byte_size = 1024
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg = ""
    while msg != "Let's get it started":
        msg = input("Shall we start?\n")
        sock.sendto(msg.encode("utf-8"), addr)
    e = 65537
    data_N, addr = sock.recvfrom(byte_size)
    data_encrypted_aes_key, addr = sock.recvfrom(byte_size)
    data_history_encrypted_wup, addr = sock.recvfrom(byte_size)
    N = int(data_N.decode("utf-8"))
    C = int(data_encrypted_aes_key.decode("utf-8"))
    print(f"I got N: {N}")
    print(f"I got C: {C}")
    current_known = ""
    for b in range(127, -1, -1):
        print("*" * 60)
        print(f"b={b}")
        C_b = (C * quick_pow_mod(2, b * e, N)) % N
        aes_key_b = "0" + current_known + "0" * b
        print(f"Try this key: {aes_key_b}")
        aes_key_b_str = bin_to_str(aes_key_b)
        crypto = AES.new(aes_key_b_str.encode('utf-8'), AES.MODE_ECB)
        encrypted_wup = crypto.encrypt(b"WUP0WUP1WUP2WUP3")
        sock.sendto(str(C_b).encode("utf-8"), addr)
        sock.sendto(b2a_hex(encrypted_wup), addr)
        data_msg, addr = sock.recvfrom(byte_size)
        msg = data_msg.decode("utf-8")
        if msg == "valid":
            current_known = "0" + current_known
        else:
            current_known = "1" + current_known
        print(f"Current known AES key: {current_known}")
    aes_key = bin_to_str(current_known)
    print(f"I guess the AES key is: {aes_key}")
    crypto_aes_key = AES.new(aes_key.encode('utf-8'), AES.MODE_ECB)
    history_decrypted_wup = crypto_aes_key.decrypt(a2b_hex(data_history_encrypted_wup.decode("utf-8"))).decode("utf-8")
    print(f"Decrypted history WUP: {history_decrypted_wup}")
if __name__ == "__main__":
    main()