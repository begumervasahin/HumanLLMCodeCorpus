def fonk1(fname):
    with open(fname, 'r') as file:
        b1 = file.read().split('\n')
        b1 = [line.split(':')[1].split(',') for line in b1 if not (line.startswith('
    return b1
def fonk2(b4, b9):
    return [b8 for b8 in b4 if b4[b8] >= b9]
def fonk3(b11):
    b2 = []
    for i in range(len(b11)):
        for j in range(i + 1, len(b11)):
            b3 = b11[i].union(b11[j])
            b2.append(b3)
    return b2
def fonk4(b2, b7):
    b4 = {}
    for b8 in b2:
        for entry in b7:
            if b8.issubset(entry):
                if b8 in b4:
                    b4[b8] += 1
                else:
                    b4[b8] = 1
    return b4
if b5 = = "__main__":
    b6 = 'input.dat'
    b7 = fonk1(b6)
    b7 = [frozenset(entry) for entry in b7]
    for d in b7:
        print(d)
    b4 = {}
    for entry in b7:
        for b8 in entry:
            b8 = frozenset([b8])
            if b8 in b4:
                b4[b8] += 1
            else:
                b4[b8] = 1
    print('***Initial Frequency Count***')
    for b8 in b4:
        print(b8, ':', b4[b8])
    b9 = int(input('Enter Support Threshold:\n>>> '))
    print('b9 = ', b9)
    b10 = b4
    while True:
        b11 = fonk2(b4, b9)
        print('\n****Frequent Items****')
        for f in b11:
            print(f)
        if len(b11) < 1:
            b11 = b10
            break
        print("\n***New Iteration***")
        b2 = fonk3(b11)
        b10 = b11
        b4 = fonk4(b2, b7)
        print('\n***Frequency Count***')
        for b8 in b4:
            print(b8, ':', b4[b8])
    print('\n***************************************************************')
    print('The most frequently associated items are:')
    for b8 in b11:
        print('{', ', '.join(b8), '}')
    print('\n')