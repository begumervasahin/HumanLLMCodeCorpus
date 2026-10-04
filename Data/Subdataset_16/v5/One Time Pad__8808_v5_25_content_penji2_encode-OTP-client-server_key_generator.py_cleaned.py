import random
import string
def fonk1(a1, b4, b5):
    with open(b4, b1 = "w") as key_f, open(b5, b1="w") as bin_key_f:
        for _ in range(a1):
            b2 = random.choice(string.ascii_letters)
            key_f.write(b2 + "\n")
            b3 = f'{ord(b2):08b}'
            bin_key_f.write(b3 + "\n")
def fonk2():
    a1 = 1_000_000
    b4 = "key.dat"
    b5 = "key1.dat"
    fonk1(a1, b4, b5)
if b6 = = "__main__":
    fonk2()