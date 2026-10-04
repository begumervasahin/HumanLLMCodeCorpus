import random
import string
def fonk1(num_keys, key_file, binary_key_file):
    with open(key_file, b1 = "w") as f, open(binary_key_file, b1="w") as f1:
        for _ in range(num_keys):
            b2 = random.choice(string.ascii_letters)
            f.write(b2)
            b3 = '{0:08b}'.format(ord(b2))
            f1.write(b3)
if b4 = = "__main__":
    fonk1(1000000, "key.dat", "key1.dat")