import binascii
import argparse
b1 = ord(' ')
def fonk1(filename):
    try:
        with open(filename) as file:
            b2 = [binascii.unhexlify(line.rstrip()) for line in file]
            b3 = [bytearray(b'?' * len(ciphertext)) for ciphertext in b2]
        return b2, b3
    except Exception as e:
        print(f"Failed to read {filename}: {e}")
        raise SystemExit(-1)
def fonk2(b2):
    b4 = max(len(ciphertext) for ciphertext in b2)
    b5 = [[] for _ in range(b4)]
    for ciphertext in b2:
        for index, byte in enumerate(ciphertext):
            b5[index].append(byte)
    return b5
def fonk3(b5):
    b6 = []
    for column in b5:
        b7 = {}
        for byte1 in column:
            for byte2 in column:
                b8 = byte1 ^ byte2
                if b8 >= 65:
                    b7[byte1] = b7.get(byte1, 0) + 1
                    b7[byte2] = b7.get(byte2, 0) + 1
        b9 = max(b7, key=b7.get)
        b6.append(b9)
    return b6
def fonk4(b6):
    return [space ^ b1 for space in b6]
def fonk5(b2, b16):
    b3 = []
    for ciphertext in b2:
        b10 = bytearray(len(ciphertext))
        for index, byte in enumerate(ciphertext):
            b10[index] = byte ^ b16[index]
        b3.append(b10)
    return b3
def fonk6():
    b11 = argparse.ArgumentParser(description="Many-time Pad Cracker")
    b11.add_argument("--filename", b12 = str,
                        b13 = "Name of the file containing the b2 (b14: b2.txt)",
                        b14 = "b2.txt")
    b15 = b11.parse_args()
    b2, b3 = fonk1(b15.filename)
    b5 = fonk2(b2)
    b6 = fonk3(b5)
    b16 = fonk4(b6)
    b3 = fonk5(b2, b16)
    print("\n".join(b10.decode('ascii') for b10 in b3))
if b17 = = "__main__":
    fonk6()