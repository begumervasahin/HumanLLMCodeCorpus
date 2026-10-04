import sys
hel =
if len(sys.argv) <= 4:
    print(hel)
    exit()
min_length = int(sys.argv[1])
max_length = int(sys.argv[2])
filename = str(sys.argv[3])
print_option = str(sys.argv[4]) if len(sys.argv) > 4 else 'n'
with open('letters.txt', 'r') as ff:
    letters = ff.read().strip()
with open(filename, 'w') as f:
    def create(l, pas):
        if len(pas) == l:
            for lett in letters:
                npas = pas + str(lett) + '\n'
                if print_option.lower() == 'y':
                    print(npas, end='')
                f.write(npas)
        elif len(pas) < l:
            for lett in letters:
                npas = pas + str(lett)
                create(l, npas)
    hello =
    print(hello)
    for i in range(min_length, max_length + 1):
        create(i, '')
print('Password List Created Successfully ..')