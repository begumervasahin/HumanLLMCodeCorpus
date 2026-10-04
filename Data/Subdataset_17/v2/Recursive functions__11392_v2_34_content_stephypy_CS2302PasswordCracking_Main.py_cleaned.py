import hashlib
import time
def hash_with_sha256(s):
    hash_object = hashlib.sha256(s.encode('utf-8'))
    return hash_object.hexdigest()
def find_password(password):
    try:
        with open("password_file.txt") as file:
            for line in file:
                username, salt, stored_hash = line.strip().split(",")
                computed_hash = hash_with_sha256(password + salt)
                if computed_hash == stored_hash:
                    print(f"{username}: {password}")
    except FileNotFoundError:
        print("Error: 'password_file.txt' not found.")
        return
def get_combination(size, comb):
    if size == 0:
        find_password(comb)
    else:
        for digit in range(10):
            get_combination(size - 1, comb + str(digit))
def hack_file(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        print('Invalid input. Please enter integers for start and end.')
        return
    if start < 3 or end > 7:
        print('Invalid input. Start size must be >= 3 and end size must be <= 7.')
        return
    for size in range(start, end + 1):
        get_combination(size, '')
def test_cases():
    start_time = time.time()
    hack_file(3.0, 7.0)
    print('Running time for invalid data type:', time.time() - start_time, 'seconds\n')
    start_time = time.time()
    hack_file(2, 7)
    print('Running time for invalid start size:', time.time() - start_time, 'seconds\n')
    start_time = time.time()
    hack_file(3, 8)
    print('Running time for invalid end size:', time.time() - start_time, 'seconds\n')
def main():
    start_time = time.time()
    hack_file(3, 7)
    print('Running time for normal run: ', time.time() - start_time, 'seconds\n')
    test_cases()
if __name__ == "__main__":
    main()