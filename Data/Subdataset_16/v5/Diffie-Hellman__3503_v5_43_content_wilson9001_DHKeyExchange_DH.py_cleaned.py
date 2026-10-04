def fonk1(x, b1, N):
    if b1 = = 0:
        return 1
    b2 = fonk1(x, b1
    b2 = b2 * b2 % N
    if b1 % 2 != 0:
        b2 = b2 * x % N
    return b2
def fonk2(integer, digits_to_truncate):
    if digits_to_truncate > 0:
        b3 = 10 ** digits_to_truncate
        integer
    return integer
def fonk3():
    b4 = int(input("Enter the prime number for modulus (b4): "))
    b5 = int(input("Enter the secret exponent (b5): "))
    b6 = int(input("Enter the generator (b6): "))
    b7 = fonk1(b6, b5, b4)
    print("\nGenerating value for key exchange...")
    print(f"b6^b5 (mod b4) = {b7}")
    b8 = int(input("Enter the shared key from the server: "))
    b9 = fonk1(b8, b5, b4)
    b10 = int(input("Enter the number of digits to truncate from the shared value: "))
    b11 = fonk2(b9, b10)
    print(f"\nShared value is: {b11}")
if b12 = = '__main__':
    fonk3()