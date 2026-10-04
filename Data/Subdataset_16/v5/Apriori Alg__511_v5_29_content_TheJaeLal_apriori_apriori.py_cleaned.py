def fonk1(fname):
    with open(fname, 'r') as file:
        b1 = file.read().split('\n')
    return [line.split(':')[1].split(',') for line in b1 if not (line.startswith('
def fonk2(b4, b8):
    return {b5: count for b5, count in b4.items() if count >= b8}
def fonk3(b11):
    b2 = []
    for i in range(len(b11)):
        for j in range(i + 1, len(b11)):
            b3 = b11[i].union(b11[j])
            b2.append(b3)
    return b2
def fonk4(b2, b7):
    b4 = {}
    for b5 in b2:
        for entry in b7:
            if b5.issubset(entry):
                if b5 in b4:
                    b4[b5] += 1
                else:
                    b4[b5] = 1
    return b4
def fonk5(b7):
    b4 = {}
    for entry in b7:
        for b5 in entry:
            b5 = frozenset([b5])
            if b5 in b4:
                b4[b5] += 1
            else:
                b4[b5] = 1
    return b4
def fonk6(b11):
    print('\n**** Frequent Items ****')
    for b5 in b11:
        print(b5)
def fonk7(b4):
    print('\n*** Frequency Count ***')
    for b5, count in b4.items():
        print(b5, ':', count)
def fonk8(b7):
    print("Initial Database:")
    for entry in b7:
        print(entry)
def fonk9():
    b6 = 'input.dat'
    b7 = fonk1(b6)
    b7 = [frozenset(entry) for entry in b7]
    fonk8(b7)
    b4 = fonk5(b7)
    print('\n*** Initial Frequency Count ***')
    fonk7(b4)
    b8 = int(input('Enter Support b9: '))
    print('b9 = ', b8)
    b10 = b4
    while True:
        b11 = fonk2(b4, b8)
        fonk6(b11)
        if len(b11) < 1:
            b11 = b10
            break
        print("\n*** New Iteration ***")
        b2 = fonk3(list(b11.keys()))
        b10 = b11
        b4 = fonk4(b2, b7)
        fonk7(b4)
    print('\n***************************************************************')
    print('The most frequently associated items are:')
    for b5 in b11:
        print('{', ', '.join(b5), '}')
    print('\n')
if b12 = = "__main__":
    fonk9()