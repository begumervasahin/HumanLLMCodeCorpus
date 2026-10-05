def fonk1(x, b1, N):
    if b1 = = 0:
        return 1
    b2 = fonk1(x, b1
    if b1 % b3 = = 0:
        return b2 ** b3 % N
    else:
        return (x * b2 ** b3) % N
def fonk2(b5, digits_to_truncate):
    if digits_to_truncate > 0:
        b4 = 10 ** digits_to_truncate
        b5 = b5
    return b5
def fonk3(smaller_size_int, larger_size_int):
    return len(str(larger_size_int)) - len(str(smaller_size_int))
b6 = int(input("Prime for modulus:\n"))
b7 = int(input("Secret exponent:\n"))
b8 = int(input("Generator:\n"))
b9 = fonk1(b8, b7, b6)
print("Generating value for key exchange...")
print("b8^b7 (mod b6) =", b9)
b10 = int(input("Shared key from server:\n"))
b11 = int(input("Truncate of shared value length:\n"))
b12 = fonk1(b10, b7, b6)
b12 = fonk2(b12, b11)
print("Shared value is:", b12)