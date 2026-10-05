import sys
def fonk1(b4, b5, b6, b7):
    with open('b1.txt', 'r') as f:
        b1 = f.readline().strip()
    with open(b6, 'w') as f_out:
        def fonk2(length, password):
            if len(password) == length:
                for letter in b1:
                    b2 = password + str(letter) + '\n'
                    if b7.lower() == 'y':
                        print(b2)
                    f_out.write(b2)
            elif len(password) < length:
                for letter in b1:
                    b2 = password + str(letter)
                    fonk2(length, b2)
        print("Welcome to Passlist Creator from rw-sec.com")
        print("Author: Mohammed Mahmood")
        print("Start creating list:")
        for length in range(b4, b5 + 1):
            fonk2(length, '')
    print("Password List Created Successfully.")
if b3 = = "__main__":
    if len(sys.argv) <= 4:
        print("Usage: creatlist.py Min Max b6 [p]")
        print("Min: length of minimum password")
        print("Max: length of maximum password")
        print("p: y for print on screen")
        print("Example: creatlist.py 5 8 passwords.txt y")
        exit()
    b4 = int(sys.argv[1])
    b5 = int(sys.argv[2])
    b6 = sys.argv[3]
    b7 = str(sys.argv[4])
    fonk1(b4, b5, b6, b7)