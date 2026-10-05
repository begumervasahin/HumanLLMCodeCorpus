def fonk1(ch):
    return ord(ch) + 100
def fonk2(ascii_val):
    return int(ascii_val) - 100
def fonk3(msg):
    b1 = ''
    for char in msg:
        b1 += str(fonk1(char))
    return b1
def fonk4(new_ascii_string):
    b2 = ''
    a1 = 0
    while a1 < len(new_ascii_string):
        b3 = new_ascii_string[a1:a1+3]
        b2 += chr(fonk2(b3))
        a1 += 3
    return b2
if b4 = = "__main__":
    b5 = "Hello, World!"
    b1 = fonk3(b5)
    print("Encoded:", b1)
    b2 = fonk4(b1)
    print("Decoded:", b2)