import hashlib
import time
def fonk1(s):
    b1 = hashlib.sha256(s.encode('utf-8'))
    return b1.hexdigest()
def fonk2(password):
    try:
        with open("password_file.txt") as file:
            for line in file:
                username, salt, b2 = line.strip().split(",")
                b3 = fonk1(password + salt)
                if b3 = = b2:
                    print(f"{username}: {password}")
    except FileNotFoundError:
        print("Error: 'password_file.txt' not found.")
        return
def fonk3(b4, comb):
    if b4 = = 0:
        fonk2(comb)
    else:
        for digit in range(10):
            fonk3(b4 - 1, comb + str(digit))
def fonk4(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        print('Invalid input. Please enter integers for start and end.')
        return
    if start < 3 or end > 7:
        print('Invalid input. Start b4 must be >= 3 and end b4 must be <= 7.')
        return
    for b4 in range(start, end + 1):
        fonk3(b4, '')
def fonk5():
    b5 = time.time()
    fonk4(3.0, 7.0)
    print('Running time for invalid data type:', time.time() - b5, 'seconds\n')
    b5 = time.time()
    fonk4(2, 7)
    print('Running time for invalid start b4:', time.time() - b5, 'seconds\n')
    b5 = time.time()
    fonk4(3, 8)
    print('Running time for invalid end b4:', time.time() - b5, 'seconds\n')
def fonk6():
    b5 = time.time()
    fonk4(3, 7)
    print('Running time for normal run: ', time.time() - b5, 'seconds\n')
    fonk5()
if b6 = = "__main__":
    fonk6()