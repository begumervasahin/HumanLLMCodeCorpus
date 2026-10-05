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
def fonk4():
    b6 = int(input("Enter the prime number for modulus (b6): "))
    b7 = int(input("Enter the secret exponent (b7): "))
    b8 = int(input("Enter the generator (b8): "))
    b9 = fonk1(b8, b7, b6)
    print("Generating value for key exchange...")
    print("b8^b7 (mod b6) =", b9)
    b10 = int(input("Enter the shared key from the server (b8^b mod b6): "))
    b11 = int(input("Enter the number of digits to truncate for the shared value: "))
    b12 = fonk1(b10, b7, b6)
    b12 = fonk2(b12, b11)
    print("The computed shared value is:", b12)
if b13 = = "__main__":
    fonk4()