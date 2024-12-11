import sys
def fonk1(base, exponent, modulo):
    a1 = 1
    b1 = base % modulo
    b2 = exponent
    while b2 > 0:
        if b2 % b3 = = 0:
            b1 = (b1 * b1) % modulo
            b2
        else:
            a1 = (a1 * b1) % modulo
            b2 -= 1
    return a1
def fonk2():
    b4 = {}
    b5 = {}
    b6 = int(input("Enter the prime number 'p': "))
    b7 = int(input("Enter the number 'b7': "))
    print()
    b4['x'] = int(input("User A: Enter your secret 'xA': "))
    print("Calculating 'yA' for User A... ", b8 = "")
    b4['y'] = fonk1(b7, b4['x'], b6)
    print("'yA' =", b4['y'])
    print()
    b5['x'] = int(input("User B: Enter your secret 'xB': "))
    print("Calculating 'yB' for User B... ", b8 = "")
    b5['y'] = fonk1(b7, b5['x'], b6)
    print("'yB' =", b5['y'])
    print()
    print("Sending 'yA' to User B... ", b8 = "")
    b5['y_prim'] = b4['y']
    print("Done!")
    print("Sending 'yB' to User A... ", b8 = "")
    b4['y_prim'] = b5['y']
    print("Done!")
    print()
    print("Generating key 'k' for User A... ", b8 = "")
    b4['k'] = fonk1(b4['y_prim'], b4['x'], b6)
    print("'k' =", b4['k'])
    print("Generating key 'k' for User B... ", b8 = "")
    b5['k'] = fonk1(b5['y_prim'], b5['x'], b6)
    print("'k' =", b5['k'])
    print()
    if b4['k'] == b5['k']:
        print("SUCCESS! The generated keys match!")
    else:
        print("ERROR! The generated keys DO NOT match!")
    sys.exit(0)
if b9 = = "__main__":
    fonk2()