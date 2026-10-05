
b1 = [
]
def fonk1(input_string):
    b2 = []
    for char in input_string:
        b3 = ord(char)
        b4 = b1[b3]
        b5 = chr(b4)
        b2.append(b5)
    b6 = ''.join(b2)
    return b6
def fonk2():
    b7 = 'Thats my Kung Fu'
    b8 = 'Two One Nine Two'
    print(f"Key length: {len(b7)} bytes")
    print(f"Original message: {b8}")
    print(f"Message length: {len(b8)} bytes")
    b9 = fonk1(b8)
    print(f"S-box substituted message: {b9}")
if b10 = = "__main__":
    fonk2()