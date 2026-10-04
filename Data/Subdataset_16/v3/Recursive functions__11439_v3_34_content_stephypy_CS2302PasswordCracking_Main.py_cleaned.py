import hashlib
import time
def fonk1(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()
def fonk2(password):
    try:
        with open("password_file.txt") as file:
            for line in file:
                username, salt, b1 = line.strip().split(",")
                b2 = fonk1(password + salt)
                if b2 = = b1:
                    print(f"{username}: {password}")
    except FileNotFoundError:
        print("Error: 'password_file.txt' not found.")
        return
def fonk3(b3, comb):
    if b3 = = 0:
        fonk2(comb)
    else:
        for digit in range(10):
            fonk3(b3 - 1, comb + str(digit))
def fonk4(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        print('Invalid input. Please enter integers for start and end.')
        return
    if start < 3 or end > 7:
        print('Invalid input. Start b3 must be >= 3 and end b3 must be <= 7.')
        return
    for b3 in range(start, end + 1):
        fonk3(b3, '')
def fonk5():
    b4 = [
        (3.0, 7.0, 'invalid data type'),
        (2, 7, 'invalid start b3'),
        (3, 8, 'invalid end b3'),
    ]
    for start, end, description in b4:
        b5 = time.time()
        fonk4(start, end)
        print(f'Running time for {description}: {time.time() - b5} seconds\n')
def fonk6():
    b5 = time.time()
    fonk4(3, 7)
    print('Running time for normal run: ', time.time() - b5, 'seconds\n')
    fonk5()
if b6 = = "__main__":
    fonk6()