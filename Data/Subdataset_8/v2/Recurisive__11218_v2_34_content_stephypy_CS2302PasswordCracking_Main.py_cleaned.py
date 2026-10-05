import hashlib
import time
def hash_with_sha256(string):
    hash_object = hashlib.sha256(string.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig
def find_password(password):
    with open("password_file.txt") as file:
        for line in file:
            elements = line.split(",")
            stored_hash = elements[2].replace('\n', '')
            new_hash = hash_with_sha256(password + str(elements[1]))
            if new_hash == stored_hash:
                print(elements[0] + ': ' + password)
def generate_combinations(size, combination):
    if size == 0:
        find_password(combination)
    else:
        for digit in range(0, 10):
            new_combination = combination + str(digit)
            generate_combinations(size - 1, new_combination)
def crack_passwords(start_size, end_size):
    if not isinstance(start_size, int) or not isinstance(end_size, int):
        print('Invalid input. Please provide integer values.')
        return
    if start_size < 3 or end_size > 7:
        print('Invalid input. Password length must be between 3 and 7.')
        return
    for size in range(start_size, end_size + 1):
        generate_combinations(size, '')
def test_cases():
    start = time.time()
    crack_passwords(3.0, 7.0)
    end = time.time()
    print('Running time for invalid data type:', end - start, 'seconds\n')
    start = time.time()
    crack_passwords(2, 7)
    end = time.time()
    print('Running time for valid range:', end - start, 'seconds\n')
    start = time.time()
    crack_passwords(3, 8)
    end = time.time()
    print('Running time for invalid range:', end - start, 'seconds\n')
def main():
    start = time.time()
    crack_passwords(3, 7)
    end = time.time()
    print('Running time for normal run: ', end - start, 'seconds\n')
    test_cases()
if __name__ == "__main__":
    main()