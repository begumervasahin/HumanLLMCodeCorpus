import random
import string
def generate_keys(num_keys, key_file, binary_key_file):
    with open(key_file, mode="w") as key_f, open(binary_key_file, mode="w") as bin_key_f:
        for _ in range(num_keys):
            char = random.choice(string.ascii_letters)
            key_f.write(char + "\n")
            binary_representation = f'{ord(char):08b}'
            bin_key_f.write(binary_representation + "\n")
def main():
    num_keys = 1_000_000
    key_file = "key.dat"
    binary_key_file = "key1.dat"
    generate_keys(num_keys, key_file, binary_key_file)
if __name__ == "__main__":
    main()