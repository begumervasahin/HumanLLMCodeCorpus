def fonk1(ch):
    return ord(ch) + 100
def fonk2(ascii_val):
    return int(ascii_val) - 100
def fonk3(msg):
    return ''.join(str(fonk1(ch)).zfill(3) for ch in msg)
def fonk4(encoded_msg):
    return ''.join(chr(fonk2(encoded_msg[i:i+3])) for i in range(0, len(encoded_msg), 3))
if b1 = = "__main__":
    b2 = "Hello, World!"
    print("Original Message:", b2)
    b3 = fonk3(b2)
    print("Encoded Message:", b3)
    b4 = fonk4(b3)
    print("Decoded Message:", b4)