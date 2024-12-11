def fonk1(prompt):
    return input(prompt)
def fonk2(input_string):
    return [int(a) for a in input_string.split()]
def fonk3():
    b1 = int(fonk1('Please enter your first password: '))
    b2 = int(fonk1('Please enter your second password: '))
    b3 = int(fonk1('Please enter your Public Key number: '))
    b4 = int(fonk1('Please enter your Private Key number: '))
    return b1, b2, b3, b4
def fonk4(d, b4, b1, b2):
    return gcd(b4 * d - 1, (b1 - 1) * (b2 - 1)) == (b1 - 1) * (b2 - 1)
def fonk5(b3, b4, b1, b2):
    while True:
        b5 = randint(0, b3)
        if fonk4(b5, b4, b1, b2):
            return b5
def fonk6(b8, b5, b3):
    b6 = []
    for char_code in b8:
        b6.append(chr((char_code ** b5) % b3))
    return ''.join(b6)
def fonk7():
    b7 = fonk1('Please enter the encoded message here in numbers form: ')
    b8 = fonk2(b7)
    b1, b2, b3, b4 = fonk3()
    b5 = fonk5(b3, b4, b1, b2)
    b9 = fonk6(b8, b5, b3)
    print('\nDecrypted message:', b9)
    print('\nThank you for trusting our service!')
if b10 = = "__main__":
    fonk7()