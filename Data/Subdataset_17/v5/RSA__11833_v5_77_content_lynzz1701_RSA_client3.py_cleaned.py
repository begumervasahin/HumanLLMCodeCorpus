from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
import socket
def modular_exponentiation(base, exp, mod):
    result = 1
    while exp != 0:
        if exp & 1:
            result = (result * base) % mod
        exp >>= 1
        base = (base * base) % mod
    return result
def binary_to_string(binary):
    ascii_str = ""
    for i in range(0, len(binary), 8):
        ascii_str += chr(int(binary[i:i+8], 2))
    return ascii_str
HOST = "192.168.146.128"
PORT = 25535
ADDR = (HOST, PORT)
BUFFER_SIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
msg = ""
while msg != "Let's get it started":
    msg = input("Shall we start?\n")
    sock.sendto(msg.encode("utf-8"), ADDR)
RSA_EXPONENT = 65537
data_N, addr = sock.recvfrom(BUFFER_SIZE)
data_encrypted_aes_key, addr = sock.recvfrom(BUFFER_SIZE)
data_history_encrypted_wup, addr = sock.recvfrom(BUFFER_SIZE)
N = int(data_N.decode("utf-8"))
encrypted_aes_key = int(data_encrypted_aes_key.decode("utf-8"))
print("Received modulus N:", N)
print("Received encrypted AES key:", encrypted_aes_key)
current_known_bits = ""
for bit_position in range(127, -1, -1):
    print("*" * 60)
    print("Attempting bit position:", bit_position)
    modified_ciphertext = (encrypted_aes_key * modular_exponentiation(2, bit_position * RSA_EXPONENT, N)) % N
    aes_key_guess = "0" + current_known_bits + "0" * bit_position
    print("Trying AES key guess:", aes_key_guess)
    aes_key_str = binary_to_string(aes_key_guess)
    aes_cipher = AES.new(aes_key_str, AES.MODE_ECB)
    known_plaintext = "WUP0WUP1WUP2WUP3"
    encrypted_known_plaintext = aes_cipher.encrypt(known_plaintext)
    sock.sendto(str(modified_ciphertext).encode("utf-8"), ADDR)
    sock.sendto(b2a_hex(encrypted_known_plaintext), ADDR)
    server_response, addr = sock.recvfrom(BUFFER_SIZE)
    response_msg = server_response.decode("utf-8")
    if response_msg == "valid":
        current_known_bits = "0" + current_known_bits
    else:
        current_known_bits = "1" + current_known_bits
    print("Current known AES key bits:", current_known_bits)
final_aes_key = binary_to_string(current_known_bits)
print("Final guessed AES key:", final_aes_key)
aes_cipher = AES.new(final_aes_key, AES.MODE_ECB)
history_wup_decrypted = aes_cipher.decrypt(a2b_hex(data_history_encrypted_wup.decode("utf-8"))).decode("utf-8")
print("Decrypted history WUP:", history_wup_decrypted)