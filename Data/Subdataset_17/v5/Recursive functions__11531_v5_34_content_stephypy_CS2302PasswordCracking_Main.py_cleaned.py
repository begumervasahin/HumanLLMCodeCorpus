import hashlib
import time
def hash_with_sha256(input_str):
    return hashlib.sha256(input_str.encode('utf-8')).hexdigest()
def find_password(password):
    try:
        with open("password_file.txt") as file:
            for line in file:
                user, salt, stored_hash = line.strip().split(",")
                computed_hash = hash_with_sha256(password + salt)
                if computed_hash == stored_hash:
                    print(f"{user}: {password}")
    except FileNotFoundError:
        print("Password file not found.")
def generate_combinations(size, prefix):
    if size == 0:
        find_password(prefix)
    else:
        for digit in range(10):
            generate_combinations(size - 1, prefix + str(digit))
def hack_file(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        print('Invalid input. Please enter integer values for start and end.')
        return
    if start < 3 or end > 7:
        print('Invalid range. Please enter a start value of at least 3 and an end value of at most 7.')
        return
    for size in range(start, end + 1):
        generate_combinations(size, '')
def test_cases():
    start = time.time()
    hack_file(3.0, 7.0)
    end = time.time()
    print('Running time for invalid data type:', end - start, 'seconds\n')
    start = time.time()
    hack_file(2, 7)
    end = time.time()
    print('Running time for invalid range:', end - start, 'seconds\n')
    start = time.time()
    hack_file(3, 8)
    end = time.time()
    print('Running time for invalid range:', end - start, 'seconds\n')
def main():
    start = time.time()
    hack_file(3, 7)
    end = time.time()
    print('Running time for normal run:', end - start, 'seconds\n')
    test_cases()
if __name__ == "__main__":
    main()