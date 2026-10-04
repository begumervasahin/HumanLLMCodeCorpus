import sys
def fonk1(b8):
    key_value_part, b1 = b8.split(',')
    key_part, b2 = key_value_part.split('=')
    b2 = b2.strip()
    b3 = b1.split("&")
    b4 = b3[3].strip()
    return b2, b4
def fonk2(b17):
    b5 = None
    a1 = 0
    b6 = {}
    b7 = []
    for b8 in b17:
        b8 = b8.strip()
        b7.append(b8)
        b2, b4 = fonk1(b8)
        try:
            b4 = int(b4)
        except ValueError:
            continue
        if b5 = = b2:
            a1 += b4
        else:
            if b5:
                b6[b5] = a1
            a1 = b4
            b5 = b2
    if b5 = = b2:
        b6[b5] = a1
    return b6, b7
def fonk3(b6, b7):
    b9 = []
    for b8 in b7:
        b8 = b8.strip()
        key_value_part, b1 = b8.split(',')
        key_part, b2 = key_value_part.split('=')
        b2 = b2.strip()
        file_name_part, b10 = b1.split("=")
        b3 = b10.split("&")
        b11 = b3[0]
        b12 = b3[1]
        b13 = b3[2]
        b14 = str(b6[b2])
        b15 = f"key={b2}&{b11}, value={b12}&{b13}&{b14}"
        b9.append(b15)
    return b9
if b16 = = "__main__":
    b17 = [
        "b18 = value1, value2&value3&value4&5",
        "b19 = value2, value5&value6&value7&10",
        "b18 = value1, value2&value3&value4&15"
    ]
    b6, b7 = fonk2(b17)
    b9 = fonk3(b6, b7)
    for b8 in b9:
        print(b8)