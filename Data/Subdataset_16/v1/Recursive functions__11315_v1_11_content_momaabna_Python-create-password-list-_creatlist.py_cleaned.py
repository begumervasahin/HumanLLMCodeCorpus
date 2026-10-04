import sys
b1 = if len(sys.argv) <= 4:
    print(b1)
    exit()
b2 = int(sys.argv[1])
b3 = int(sys.argv[2])
b4 = str(sys.argv[3])
b5 = str(sys.argv[4]) if len(sys.argv) > 4 else 'n'
with open('b6.txt', 'r') as ff:
    b6 = ff.read().strip()
with open(b4, 'w') as f:
    def fonk1(l, pas):
        if len(pas) == l:
            for lett in b6:
                b7 = pas + str(lett) + '\n'
                if b5.lower() == 'y':
                    print(b7, b8 = '')
                f.write(b7)
        elif len(pas) < l:
            for lett in b6:
                b7 = pas + str(lett)
                fonk1(l, b7)
    b9 = print(b9)
    for i in range(b2, b3 + 1):
        fonk1(i, '')
print('Password List Created Successfully ..')