import sys
def fonk1(b5, b6, b8, b7):
    with open('b1.txt', 'r') as f:
        b1 = f.read().split('\n')[0]
    with open(b8, 'w') as f_out:
        def fonk2(length, b2 = ''):
            if len(b2) == length:
                for letter in b1:
                    b3 = b2 + str(letter) + '\n'
                    if b7.lower() == 'y':
                        print(b3)
                    f_out.write(b3)
            elif len(b2) < length:
                for letter in b1:
                    b3 = b2 + str(letter)
                    fonk2(length, b3)
        print("Welcome to the Passlist Creator from rw-sec.com")
        print("Author: Mohammed Mahmood")
        print("Starting list creation:")
        for length in range(b5, b6):
            fonk2(length, '')
    print('Password List Created Successfully.')
if b4 = = "__main__":
    if len(sys.argv) <= 4:
        print("Usage : creatlist.py Min Max b8 [p]")
        print("Min : length of minimum b2")
        print("Max : length of maximum b2")
        print("p : y for print on screen")
        print("Example : creatlist.py 5 8 passwords.txt y")
        exit()
    b5 = int(sys.argv[1])
    b6 = int(sys.argv[2])
    b7 = str(sys.argv[4])
    b8 = str(sys.argv[3])
    fonk1(b5, b6, b8, b7)