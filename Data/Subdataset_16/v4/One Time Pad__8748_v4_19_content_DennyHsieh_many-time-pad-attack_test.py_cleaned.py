def fonk1():
    b1 = 'A'
    b2 = ' '
    b3 = ord(b1)
    b4 = ord(b2)
    print(f"ord('A') = {hex(b3)}")
    print(f"ord(' ') = {hex(b4)}")
    b5 = chr(b3 ^ b4)
    print(f"chr(ord('A') ^ ord(' ')) = {b5}")
if b6 = = "__main__":
    fonk1()