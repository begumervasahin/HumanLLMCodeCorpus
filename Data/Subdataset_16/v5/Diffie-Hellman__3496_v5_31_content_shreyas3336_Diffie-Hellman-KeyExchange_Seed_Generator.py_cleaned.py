import Seeded_Random_Generator
def fonk1(key):
    b1 = str(key)
    b2 = b1.split(' ')[-1].rstrip('>')
    return int(b2, 16)
def fonk2(b15, b16, b17, b18, b3 = 3336):
    b4 = fonk1(b15)
    b5 = fonk1(b16)
    b6 = fonk1(b17)
    b7 = fonk1(b18)
    b8 = (b6 ^ b4) % b7
    b9 = (b6 ^ b5) % b7
    b10 = (b9 ^ b4) % b7
    b11 = (b8 ^ b5) % b7
    b12 = b10 % 1111 if b10 == b11 else b3
    b13 = Seeded_Random_Generator.reduce(b12)
    print(f"Original b12: {b12}, New b12: {b13}")
    Seeded_Random_Generator.random_generator(b13)
if b14 = = "__main__":
    b15 = "<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x7f8b6c34>"
    b16 = "<cryptography.hazmat.backends.openssl.dh._DHPrivateKey object at 0x7f8b6c35>"
    b17 = "<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x7f8b6c36>"
    b18 = "<cryptography.hazmat.backends.openssl.dh._DHPublicKey object at 0x7f8b6c37>"
    fonk2(b15, b16, b17, b18)