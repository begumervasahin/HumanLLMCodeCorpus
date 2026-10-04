import sys
def fonk1():
    b1 = print(b1)
def fonk2(length, current_password, b8, output_file, b7):
    if len(current_password) == length:
        for letter in b8:
            b2 = current_password + letter + '\n'
            if b7:
                print(b2, b3 = '')
            output_file.write(b2)
    else:
        for letter in b8:
            b2 = current_password + letter
            fonk2(length, b2, b8, output_file, b7)
def fonk3():
    if len(sys.argv) <= 4:
        fonk1()
        sys.exit()
    b4 = int(sys.argv[1])
    b5 = int(sys.argv[2])
    b6 = sys.argv[3]
    b7 = len(sys.argv) > 4 and sys.argv[4].lower() == 'y'
    with open('b8.txt', 'r') as f:
        b8 = f.read().strip()
    with open(b6, 'w') as f:
        print("Welcome to Password List Creator")
        print("Author: Mohammed Mahmood")
        print("Start creating list...")
        for length in range(b4, b5 + 1):
            fonk2(length, '', b8, f, b7)
    print("Password List Created Successfully.")
if b9 = = '__main__':
    fonk3()