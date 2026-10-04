import random
import string
def fonk1(a1: int, key_file: str, binary_key_file: str) -> None:
    with open(key_file, 'w') as ascii_file, open(binary_key_file, 'w') as binary_file:
        for _ in range(a1):
            b1 = random.choice(string.ascii_letters)
            ascii_file.write(b1)
            b2 = f'{ord(b1):08b}'
            binary_file.write(b2)
def fonk2() -> None:
    a1 = 1000000
    fonk1(a1, "key.dat", "key1.dat")
if b3 = = "__main__":
    fonk2()