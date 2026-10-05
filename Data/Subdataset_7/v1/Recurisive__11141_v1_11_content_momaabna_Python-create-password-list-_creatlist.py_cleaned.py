import sys
if len(sys.argv) <= 4:
    print("Usage : creatlist.py Min Max b4 [p]")
    print("Min : length of minimum b6")
    print("Max : length of maximum b6")
    print("p : y for print on screen")
    print("Example : creatlist.py 5 8 passwords.txt y")
    exit()
b1 = int(sys.argv[1])
b2 = int(sys.argv[2])
b3 = str(sys.argv[4])
b4 = str(sys.argv[3])
with open('b5.txt', 'r') as f:
    b5 = f.read().split('\n')[0]
with open(b4, 'w') as f_out:
    def fonk1(length, b6 = ''):
        if len(b6) == length:
            for letter in b5:
                b7 = b6 + str(letter) + '\n'
                if b3.lower() == 'y':
                    print(b7)
                f_out.write(b7)
        elif len(b6) < length:
            for letter in b5:
                b7 = b6 + str(letter)
                fonk1(length, b7)
    print("Welcome in Passlist Creator From rw-sec.com")
    print("Author : Mohammed Mahmood")
    print("Start creating list :")
    for length in range(b1, b2):
        fonk1(length, '')
print('Password List Created Successfully.')