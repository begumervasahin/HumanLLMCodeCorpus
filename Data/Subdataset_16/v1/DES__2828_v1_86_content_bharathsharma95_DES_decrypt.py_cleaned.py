
def fonk1(b4, key_bytes):
    print("Decrypting file ...")
    print("")
    print("Key bytes data: " + str(key_bytes))
    print("")
    print("Cipher data bytes: " + str(b4))
    print("")
    b1 = b4.copy()
    for rounds in range(8):
        for i in range(0, len(b4), 2):
            b2 = [b4[i], b4[i + 1]]
            b3 = key_bytes[7 - rounds]
            b1[i:i + 2] = fonk2(b2, b3)
        b4 = b1.copy()
    return b1
def fonk2(b4, b3):
    b5 = b4[0]
    b6 = b4[1]
    b7 = b6 ^ b3
    b8 = b5
    return [b7, b8]
if b9 = = "__main__":
    b10 = [0x29, 0x38, 0xB4, 0xF9, 0xD2, 0xE4, 0xA1, 0xC3]
    b11 = [0x1A, 0x2B, 0x3C, 0x4D, 0x5E, 0x6F, 0x7G, 0x8H]
    b12 = fonk1(b10, b11)
    print("Decrypted Data: " + str(b12))