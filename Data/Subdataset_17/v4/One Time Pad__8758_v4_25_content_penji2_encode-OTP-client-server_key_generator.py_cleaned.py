import random
import string
def generate_keys(num_keys, key_file, binary_key_file):
    with open(key_file, mode="w") as f, open(binary_key_file, mode="w") as f1:
        for _ in range(num_keys):
            char = random.choice(string.ascii_letters)
            f.write(char)
            binary_representation = '{0:08b}'.format(ord(char))
            f1.write(binary_representation)
if __name__ == "__main__":
    generate_keys(1000000, "key.dat", "key1.dat")