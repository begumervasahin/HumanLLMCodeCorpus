def find_encryption_key(phi, n):
    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            return e
        e += 1
    return None
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def find_decryption_key(e, phi):
    d = 1
    while True:
        if (d * e) % phi == 1:
            return d
        d += 1
def encrypt_message(message, e, n, letters):
    encrypted_msg = []
    for char in message:
        encrypted_msg.append((letters.index(char)**e) % n)
    return encrypted_msg
def decrypt_message(encrypted_msg, d, n, letters):
    decrypted_msg = []
    for char in encrypted_msg:
        decrypted_msg.append(letters[(char**d) % n])
    return decrypted_msg
print("Enter 2 PRIME numbers for 'p' and 'q'.")
p = int(input("p: "))
q = int(input("q: "))
n = p * q
print("\nn = " + str(n))
phi = (p - 1) * (q - 1)
print("phi = " + str(phi))
e = find_encryption_key(phi, n)
if e is None:
    print("Failed to find encryption key.")
    exit()
print("e = " + str(e))
print("ENCRYPTION KEY= (" + str(e) + ", " + str(n) + ")")
d = find_decryption_key(e, phi)
print("d = " + str(d))
print("DECRYPTION KEY= (" + str(d) + ", " + str(n) + ")")
alphabet = ".abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letters = list(alphabet)
msg = input("\nEnter simple message (letters only): ")
encrypted_msg = encrypt_message(msg, e, n, letters)
print("\nEncrypted message: ")
print(encrypted_msg)
decrypted_msg = decrypt_message(encrypted_msg, d, n, letters)
print("\nDecrypted Message: ")
print(''.join(decrypted_msg))