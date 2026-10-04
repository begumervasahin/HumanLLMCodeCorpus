def fonk1(fname):
    with open(fname, 'r') as file:
        b1 = file.read().split('\n')
        b1 = [line.split(':')[1].split(',') for line in b1 if not (line.startswith('
    return b1
def fonk2(b4, b9):
    return [b8 for b8 in b4 if b4[b8] >= b9]
def fonk3(b12):
    b2 = []
    for i in range(len(b12)):
        for j in range(i + 1, len(b12)):
            b3 = b12[i].union(b12[j])
            if b3 not in b2:
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
    print("Database Transactions:")
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
    print('\n*** Initial Frequency Count ***')
    for b8, count in b4.items():
        print(f"{b8}: {count}")
    b9 = int(input('\nEnter Support b10:\n>>> '))
    print('b10 = ', b9)
    b11 = b4
    while True:
        b12 = fonk2(b4, b9)
        print('\n**** Frequent Items ****')
        for f in b12:
            print(f)
        if not b12:
            b12 = b11
            break
        print("\n*** New Iteration ***")
        b2 = fonk3(b12)
        b11 = b12
        b4 = fonk4(b2, b7)
        print('\n*** Frequency Count ***')
        for b8, count in b4.items():
            print(f"{b8}: {count}")
    print('\n***************************************************************')
    print('The most frequently associated items are:')
    for b8 in b12:
        print(f"{{ {', '.join(b8)} }}")
    print('\n')