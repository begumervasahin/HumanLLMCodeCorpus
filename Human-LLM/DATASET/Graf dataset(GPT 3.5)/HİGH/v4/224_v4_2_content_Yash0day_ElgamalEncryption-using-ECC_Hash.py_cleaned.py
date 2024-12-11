def fonk1(ch):
    b1 = ord(ch) + 100
    return b1
def fonk2(ascii_val):
    b2 = int(ascii_val) - 100
    return b2
def fonk3(msg):
    b3 = ''
    for char in msg:
        b3 += str(fonk1(char))
    return b3
def fonk4(new_ascii_string):
    b4 = ''
    a1 = 0
    while a1 < len(new_ascii_string):
        b5 = new_ascii_string[a1:a1+3]
        b4 += chr(fonk2(b5))
        a1 += 3
    return b4