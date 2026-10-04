import hashlib
import time
def fonk1(input_str):
    b1 = hashlib.sha256(input_str.encode('utf-8'))
    return b1.hexdigest()
def fonk2(password):
    with open("password_file.txt") as f:
        for line in f:
            user, salt, b2 = line.strip().split(",")
            b3 = fonk1(password + salt)
            if b3 = = b2:
                print(f"{user}: {password}")
def fonk3(b4, comb):
    if b4 = = 0:
        fonk2(comb)
    else:
        for digit in range(10):
            b5 = comb + str(digit)
            fonk3(b4 - 1, b5)
def fonk4(b6, b7):
    if not isinstance(b6, int) or not isinstance(b7, int):
        print('Invalid input. Please try again.')
        return
    if b6 < 3 or b7 > 7:
        print('Invalid input. Please try again.')
        return
    for b4 in range(b6, b7 + 1):
        fonk3(b4, '')
def fonk5():
    b6 = time.time()
    fonk4(3.0, 7.0)
    b7 = time.time()
    print('Running time for invalid data type:', b7 - b6, 'seconds\n')
    b6 = time.time()
    fonk4(2, 7)
    b7 = time.time()
    print('Running time for invalid range:', b7 - b6, 'seconds\n')
    b6 = time.time()
    fonk4(3, 8)
    b7 = time.time()
    print('Running time for invalid range:', b7 - b6, 'seconds\n')
def fonk6():
    b6 = time.time()
    fonk4(3, 7)
    b7 = time.time()
    print('Running time for normal run:', b7 - b6, 'seconds\n')
    fonk5()
if b8 = = "__main__":
    fonk6()