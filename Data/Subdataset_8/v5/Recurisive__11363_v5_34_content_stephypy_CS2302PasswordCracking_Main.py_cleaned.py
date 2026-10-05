import hashlib
import time
def hash_with_sha256(string):
    hash_object = hashlib.sha256(string.encode('utf-8'))
    hex_digest = hash_object.hexdigest()
    return hex_digest
def find_password(password):
    with open("password_file.txt") as file:
        for line in file:
            elements = line.strip().split(",")
            hashline = elements[2]
            new_hashline = hash_with_sha256(password + elements[1])
            if new_hashline == hashline:
                print(f"Password found for user {elements[0]}: {password}")
def generate_combinations(size, combination):
    if size == 0:
        find_password(combination)
    else:
        for digit in range(10):
            new_combination = combination + str(digit)
            generate_combinations(size - 1, new_combination)
def hack_passwords(start_length, end_length):
    if not isinstance(start_length, int) or not isinstance(end_length, int) or start_length < 3 or end_length > 7:
        print('Invalid input. Please provide integer values between 3 and 7 for password lengths.')
        return
    for size in range(start_length, end_length + 1):
        generate_combinations(size, '')
def test_hack_passwords():
    start = time.time()
    hack_passwords(3.0, 7.0)
    end = time.time()
    print('Running time for invalid data type:', end - start, 'seconds\n')
    start = time.time()
    hack_passwords(2, 7)
    end = time.time()
    print('Running time for invalid range:', end - start, 'seconds\n')
    start = time.time()
    hack_passwords(3, 8)
    end = time.time()
    print('Running time for invalid range:', end - start, 'seconds\n')
def main():
    start = time.time()
    hack_passwords(3, 7)
    end = time.time()
    print('Running time for normal run: ', end - start, 'seconds\n')
    test_hack_passwords()
if __name__ == "__main__":
    main()