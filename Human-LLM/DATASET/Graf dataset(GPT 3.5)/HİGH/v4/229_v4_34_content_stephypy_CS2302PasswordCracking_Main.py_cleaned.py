import hashlib
import time
def fonk1(string):
    b1 = hashlib.sha256(string.encode('utf-8'))
    b2 = b1.hexdigest()
    return b2
def fonk2(password):
    with open("password_file.txt") as file:
        for line in file:
            b3 = line.split(",")
            b4 = b3[2].replace('\n', '')
            b5 = fonk1(password + str(b3[1]))
            if b5 = = b4:
                print(b3[0] + ': ' + password)
def fonk3(b6, combination):
    if b6 = = 0:
        fonk2(combination)
    else:
        for digit in range(0, 10):
            b7 = combination + str(digit)
            fonk3(b6 - 1, b7)
def fonk4(b8, b9):
    if not isinstance(b8, int) or not isinstance(b9, int):
        print('Invalid input. Please try again')
        return
    if b8 < 3 or b9 > 7:
        print('Invalid input. Please try again')
        return
    for b6 in range(b8, b9 + 1):
        fonk3(b6, '')
def fonk5():
    b8 = time.time()
    fonk4(3.0, 7.0)
    b9 = time.time()
    print('Running time for invalid data type:', b9 - b8, 'seconds\n')
    b8 = time.time()
    fonk4(2, 7)
    b9 = time.time()
    print('Running time for invalid range:', b9 - b8, 'seconds\n')
    b8 = time.time()
    fonk4(3, 8)
    b9 = time.time()
    print('Running time for invalid range:', b9 - b8, 'seconds\n')
def fonk6():
    b8 = time.time()
    fonk4(3, 7)
    b9 = time.time()
    print('Running time for normal run: ', b9 - b8, 'seconds\n')
    fonk5()
if b10 = = "__main__":
    fonk6()