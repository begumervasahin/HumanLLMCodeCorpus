import random
import string
def main():
    with open("key.dat", mode="w") as f, open("key1.dat", mode="w") as f1:
        for _ in range(1000000):
            b = random.choice(string.ascii_letters)
            f.write(b)
            dec = ord(b)
            b_bin = '{0:08b}'.format(dec)
            f1.write(b_bin)
if __name__ == "__main__":
    main()