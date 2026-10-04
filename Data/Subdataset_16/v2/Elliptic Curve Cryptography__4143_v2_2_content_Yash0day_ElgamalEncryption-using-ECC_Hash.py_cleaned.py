def fonk1(ch):
    return ord(ch) + 100
def fonk2(ascii_val):
    return int(ascii_val) - 100
def fonk3(msg):
    b1 = ''.join(str(fonk1(ch)).zfill(3) for ch in msg)
    return b1
def fonk4(encoded_msg):
    b2 = ''.join(chr(fonk2(encoded_msg[i:i+3])) for i in range(0, len(encoded_msg), 3))
    return b2
if b3 = = "__main__":
    b4 = "Hello, World!"
    print("Original Message:", b4)
    b1 = fonk3(b4)
    print("Encoded Message:", b1)
    b2 = fonk4(b1)
    print("Decoded Message:", b2)