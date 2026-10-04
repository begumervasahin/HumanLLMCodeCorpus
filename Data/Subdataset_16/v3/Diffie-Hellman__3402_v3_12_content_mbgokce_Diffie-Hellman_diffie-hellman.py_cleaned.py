import random
from Crypto.Util import number
def fonk1(b1 = 9):
    return number.getPrime(b1, None)
def fonk2(b2 = 5, max_value=200):
    return random.randint(b2, max_value)
def fonk3(b3):
    return random.randint(0, b3 - 1)
def fonk4(b4, private_key, b3):
    return pow(b4, private_key, b3)
def fonk5(public_key, private_key, b3):
    return pow(public_key, private_key, b3)
def fonk6(public_key, b4, b3):
    for possible_private_key in range(b3):
        if fonk4(b4, possible_private_key, b3) == public_key:
            return possible_private_key
    return None
def fonk7():
    b3 = fonk1()
    b4 = fonk2()
    b5 = fonk3(b3)
    b6 = fonk3(b3)
    b7 = fonk4(b4, b5, b3)
    b8 = fonk4(b4, b6, b3)
    print(f"g : {b4}")
    print(f"p : {b3}")
    print(f"Alice's public key: {b7}")
    print(f"Bob's public key: {b8}")
    b9 = fonk5(b8, b5, b3)
    b10 = fonk5(b7, b6, b3)
    if b9 != b10:
        print("Woah! Something is terribly wrong.")
    else:
        print(f"Alice's and Bob's shared secret: {b9}")
    print("\n---Brute force---")
    b11 = fonk6(b7, b4, b3)
    b12 = fonk5(b8, b11, b3)
    print(f"\nFound! Alice's and Bob's shared secret: {b12}")
if b13 = = "__main__":
    fonk7()