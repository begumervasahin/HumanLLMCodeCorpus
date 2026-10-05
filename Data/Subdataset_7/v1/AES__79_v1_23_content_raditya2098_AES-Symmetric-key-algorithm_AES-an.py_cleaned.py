
b1 = [
]
def fonk1(input_string):
    b2 = [hex(ord(char)) for char in input_string]
    b3 = [hex(b1[int(hex_val[2:], 16)]) for hex_val in b2]
    b4 = ''.join([chr(int(hex_val, 16)) for hex_val in b3])
    return b4
def fonk2():
    b5 = 'Thats my Kung Fu'
    print(f"Key length: {len(b5.encode('utf-8'))}")
    b6 = 'Two One Nine Two'
    print(f"Original message: {b6}")
    print(f"Message length: {len(b6.encode('utf-8'))}")
    b7 = fonk1(b6)
    print(f"S-box substituted message: {b7}")
if b8 = = "__main__":
    fonk2()