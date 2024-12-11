def fonk1(table, b14):
    return [b14[i - 1] for i in table]
def fonk2(arr, n):
    return arr[n:] + arr[:n]
def fonk3(b1):
    b1 = fonk1(PC_1, b1)
    b2 = []
    for shift in SHIFT:
        b4, b3 = b1[:28], b1[28:]
        b4 = fonk2(b4, shift)
        b3 = fonk2(b3, shift)
        b1 = b4 + b3
        b2.append(fonk1(PC_2, b1))
    return b2
def fonk4(b14):
    return fonk1(IP_table, b14)
def fonk5(b14):
    return fonk1(IP_re_table, b14)
def fonk6(b14):
    return fonk1(E, b14)
def fonk7(b14):
    return fonk1(P, b14)
def fonk8(b14):
    b5 = []
    for i in range(0, len(b14), 6):
        b6 = b14[i:i + 6]
        b7 = int(b6[0] + b6[-1], 2)
        b8 = int(b6[1:-1], 2)
        b9 = bin(S[i
        b5.extend(b9)
    return b5
def fonk9(b14, b1):
    b10 = fonk6(b14)
    b11 = [str(int(a) ^ int(b)) for a, b in zip(b10, b1)]
    b12 = fonk8(''.join(b11))
    b13 = fonk7(b12)
    return b13
def fonk10(b14, b2):
    b14 = fonk4(b14)
    left, b15 = b14[:32], b14[32:]
    for subkey in b2:
        left, b15 = b15, fonk9(b15, subkey)
    b16 = fonk5(b15 + left)
    return b16
b1 = '0001001100110100010101110111100110011011101111001101111111110001'
b2 = fonk3(b1)
b17 = '0000000100100011010001010110011110001001101010111100110111101111'
b18 = fonk10(b17, b2)
print('Ciphertext:', ''.join(b18))