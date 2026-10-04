import hashlib
import time
def fonk1(input_str):
    return hashlib.sha256(input_str.encode('utf-8')).hexdigest()
def fonk2(password):
    try:
        with open("password_file.txt") as file:
            for line in file:
                user, salt, b1 = line.strip().split(",")
                b2 = fonk1(password + salt)
                if b2 = = b1:
                    print(f"{user}: {password}")
    except FileNotFoundError:
        print("Password file not found.")
def fonk3(b3, prefix):
    if b3 = = 0:
        fonk2(prefix)
    else:
        for digit in range(10):
            fonk3(b3 - 1, prefix + str(digit))
def fonk4(b4, b5):
    if not isinstance(b4, int) or not isinstance(b5, int):
        print('Invalid input. Please enter integer values for b4 and b5.')
        return
    if b4 < 3 or b5 > 7:
        print('Invalid range. Please enter a b4 value of at least 3 and an b5 value of at most 7.')
        return
    for b3 in range(b4, b5 + 1):
        fonk3(b3, '')
def fonk5():
    b4 = time.time()
    fonk4(3.0, 7.0)
    b5 = time.time()
    print('Running time for invalid data type:', b5 - b4, 'seconds\n')
    b4 = time.time()
    fonk4(2, 7)
    b5 = time.time()
    print('Running time for invalid range:', b5 - b4, 'seconds\n')
    b4 = time.time()
    fonk4(3, 8)
    b5 = time.time()
    print('Running time for invalid range:', b5 - b4, 'seconds\n')
def fonk6():
    b4 = time.time()
    fonk4(3, 7)
    b5 = time.time()
    print('Running time for normal run:', b5 - b4, 'seconds\n')
    fonk5()
if b6 = = "__main__":
    fonk6()