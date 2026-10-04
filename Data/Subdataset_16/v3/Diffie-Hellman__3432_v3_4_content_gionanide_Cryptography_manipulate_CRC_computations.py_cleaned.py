import itertools
def fonk1(num_bits):
    b1 = itertools.product('01', repeat=num_bits)
    return [''.join(combination) for combination in b1]
def fonk2(message, divisor):
    b2 = message + '0' * (len(divisor) - 1)
    b3 = list(b2)
    b4 = list(divisor)
    for i in range(len(b2) - len(divisor) + 1):
        if b3[i] == '1':
            for j in range(len(divisor)):
                b3[i + j] = str(int(b3[i + j]) ^ int(b4[j]))
    return ''.join(b3[-(len(divisor) - 1):])
def fonk3(message, divisor, b5 = None):
    b6 = fonk2(message, divisor)
    b7 = fonk1(len(divisor))
    if b5 is None:
        b5 = fonk1(len(message) - len(divisor))
    b8 = []
    for prefix in b5:
        for candidate in b7:
            b9 = prefix + candidate
            if fonk2(b9, divisor) == b6:
                b8.append(b9)
    return b8
if b10 = = "__main__":
    b11 = "11010110"
    b12 = "10011"
    b13 = ["111"]
    b14 = fonk3(b11, b12, b13)
    print("Collisions found:")
    for collision in b14:
        print(collision)