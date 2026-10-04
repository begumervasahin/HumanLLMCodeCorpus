import random
import string
def generate_random_keys(num_keys: int, key_file: str, binary_key_file: str) -> None:
    with open(key_file, 'w') as ascii_file, open(binary_key_file, 'w') as binary_file:
        for _ in range(num_keys):
            random_letter = random.choice(string.ascii_letters)
            ascii_file.write(random_letter)
            binary_representation = f'{ord(random_letter):08b}'
            binary_file.write(binary_representation)
def main() -> None:
    num_keys = 1000000
    generate_random_keys(num_keys, "key.dat", "key1.dat")
if __name__ == "__main__":
    main()