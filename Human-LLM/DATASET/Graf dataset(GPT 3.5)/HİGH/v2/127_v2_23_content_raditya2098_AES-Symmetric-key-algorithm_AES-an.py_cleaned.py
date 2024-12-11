
b1 = [
]
def fonk1(input_string):
    b2 = []
    for char in input_string:
        b3 = hex(ord(char))
        b4 = b3[2:]
        b5 = hex(b1[int(b4, 16)])
        b2.append(b5)
    b6 = ''.join(chr(int(hex_val, 16)) for hex_val in b2)
    return b6
def fonk2():
    b7 = 'Thats my Kung Fu'
    print(f"Length of the b7: {len(b7)} bytes")
    b8 = 'Two One Nine Two'
    print(f"Original message: {b8}")
    print(f"Length of the message: {len(b8)} bytes")
    b9 = fonk1(b8)
    print(f"Message after S-box substitution: {b9}")
if b10 = = "__main__":
    fonk2()