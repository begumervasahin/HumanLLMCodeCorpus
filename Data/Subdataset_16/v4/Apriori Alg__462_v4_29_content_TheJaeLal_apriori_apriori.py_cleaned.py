def fonk1(fname):
    with open(fname, 'r') as file:
        b1 = file.read().split('\n')
    return [line.split(':')[1].split(',') for line in b1 if not (line.startswith('
def fonk2(b4, b8):
    return {b7: count for b7, count in b4.items() if count >= b8}
def fonk3(b11):
    b2 = []
    for i in range(len(b11)):
        for j in range(i + 1, len(b11)):
            b3 = b11[i].union(b11[j])
            b2.append(b3)
    return b2
def fonk4(b2, b6):
    b4 = {}
    for b7 in b2:
        for entry in b6:
            if b7.issubset(entry):
                if b7 in b4:
                    b4[b7] += 1
                else:
                    b4[b7] = 1
    return b4
def fonk5():
    b5 = 'input.dat'
    b6 = fonk1(b5)
    b6 = [frozenset(entry) for entry in b6]
    print("Initial Database:")
    for entry in b6:
        print(entry)
    b4 = {}
    for entry in b6:
        for b7 in entry:
            b7 = frozenset([b7])
            if b7 in b4:
                b4[b7] += 1
            else:
                b4[b7] = 1
    print('\n*** Initial Frequency Count ***')
    for b7, count in b4.items():
        print(b7, ':', count)
    b8 = int(input('Enter Support b9: '))
    print('b9 = ', b8)
    b10 = b4
    while True:
        b11 = fonk2(b4, b8)
        print('\n**** Frequent Items ****')
        for b7 in b11:
            print(b7)
        if len(b11) < 1:
            b11 = b10
            break
        print("\n*** New Iteration ***")
        b2 = fonk3(list(b11.keys()))
        b10 = b11
        b4 = fonk4(b2, b6)
        print('\n*** Frequency Count ***')
        for b7, count in b4.items():
            print(b7, ':', count)
    print('\n***************************************************************')
    print('The most frequently associated items are:')
    for b7 in b11:
        print('{', ', '.join(b7), '}')
    print('\n')
if b12 = = "__main__":
    fonk5()