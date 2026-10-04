import random
import string
b1 = open("key.dat",mode="w")
b2 = open("key1.dat",mode="w")
for a in range(0,1000000):
    b3 = random.choice(string.ascii_letters)
    b1.write(b3)
    b4 = ord(b3)
    b3 = '{0:08b}'.format(b4)
    b2.write(b3)
b1.close()
b2.close()