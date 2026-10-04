import sys
def fonk1(b1):
    b1 = b1.strip()
    key_part, b2 = b1.split(',')
    word_part, b3 = key_part.split('=')
    b3 = b3.strip()
    _, b4 = b2.split("&")[3].split("=")
    b5 = int(b4.strip())
    return b3, b5
def fonk2(b12):
    b6 = {}
    b7 = None
    a1 = 0
    for b1 in b12:
        try:
            b3, b5 = fonk1(b1)
        except ValueError:
            continue
        if b7 = = b3:
            a1 += b5
        else:
            if b7 is not None:
                b6[b7] = a1
            b7 = b3
            a1 = b5
    if b7 = = b3:
        b6[b7] = a1
    return b6
def fonk3(b12, b6):
    for b1 in b12:
        b1 = b1.strip()
        key_part, b2 = b1.split(',')
        word_part, b3 = key_part.split('=')
        b3 = b3.strip()
        b8 = b2.split("=")[1].split("&")
        file_name, n, b9 = b8[0], b8[1], b8[2]
        b10 = str(b6[b3])
        print(f"b11 = {b3}&{file_name}, value={n}&{b9}&{b10}")
def fonk4():
    b12 = [b1.strip() for b1 in sys.stdin]
    b6 = fonk2(b12)
    fonk3(b12, b6)
if b13 = = "__main__":
    fonk4()