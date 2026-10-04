import random
import string
def fonk1():
    with open("key.dat", b1 = "w") as f, open("key1.dat", b1="w") as f1:
        for _ in range(1000000):
            b2 = random.choice(string.ascii_letters)
            f.write(b2)
            b3 = ord(b2)
            b4 = '{0:08b}'.format(b3)
            f1.write(b4)
if b5 = = "__main__":
    fonk1()