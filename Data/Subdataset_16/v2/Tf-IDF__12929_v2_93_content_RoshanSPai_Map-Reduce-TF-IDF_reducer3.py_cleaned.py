import sys
def fonk1(b17):
    b1 = None
    a1 = 0
    b2 = {}
    b3 = []
    for b4 in b17:
        b4 = b4.strip()
        b3.append(b4)
        key_value_part, b5 = b4.split(',')
        key_part, b6 = key_value_part.split('=')
        b6 = b6.strip()
        b7 = b5.split("&")
        b8 = b7[3].strip()
        try:
            b8 = int(b8)
        except ValueError:
            continue
        if b1 = = b6:
            a1 += b8
        else:
            if b1:
                b2[b1] = a1
            a1 = b8
            b1 = b6
    if b1 = = b6:
        b2[b1] = a1
    return b2, b3
def fonk2(b2, b3):
    b9 = []
    for b4 in b3:
        b4 = b4.strip()
        key_value_part, b5 = b4.split(',')
        key_part, b6 = key_value_part.split('=')
        b6 = b6.strip()
        file_name_part, b10 = b5.split("=")
        b7 = b10.split("&")
        b11 = b7[0]
        b12 = b7[1]
        b13 = b7[2]
        b14 = str(b2[b6])
        b15 = f"key={b6}&{b11}, value={b12}&{b13}&{b14}"
        b9.append(b15)
    return b9
if b16 = = "__main__":
    b17 = [
        "b18 = value1, value2&value3&value4&5",
        "b19 = value2, value5&value6&value7&10",
        "b18 = value1, value2&value3&value4&15"
    ]
    b2, b3 = fonk1(b17)
    b9 = fonk2(b2, b3)
    for b4 in b9:
        print(b4)