def fonk1(fname):
    with open(fname, 'r') as file:
        b1 = [
            line.split(':')[1].split(',')
            for line in file
            if not (line.startswith('
        ]
    return b1
def fonk2(b4, b7):
    return [item for item in b4 if b4[item] >= b7]
def fonk3(b10):
    b2 = []
    for i in range(len(b10)):
        for j in range(i + 1, len(b10)):
            b3 = b10[i].union(b10[j])
            if b3 not in b2:
                b2.append(b3)
    return b2
def fonk4(b2, b6):
    b4 = defaultdict(int)
    for item in b2:
        for entry in b6:
            if item.issubset(entry):
                b4[item] += 1
    return b4
def fonk5(b10, message):
    print(f'\n**** {message} ****')
    for item in b10:
        print(f"{item}")
def fonk6():
    b5 = 'input.dat'
    b6 = fonk1(b5)
    b6 = [frozenset(entry) for entry in b6]
    print("Database Transactions:")
    for transaction in b6:
        print(transaction)
    b4 = defaultdict(int)
    for transaction in b6:
        for item in transaction:
            b4[frozenset([item])] += 1
    fonk5(b4.items(), 'Initial Frequency Count')
    b7 = int(input('\nEnter Support b8:\n>>> '))
    print('b8 = ', b7)
    b9 = b4
    while True:
        b10 = fonk2(b4, b7)
        fonk5(b10, 'Frequent Items')
        if not b10:
            b10 = b9
            break
        print("\n*** New Iteration ***")
        b2 = fonk3(b10)
        b9 = b10
        b4 = fonk4(b2, b6)
        fonk5(b4.items(), 'Frequency Count')
    print('\n***************************************************************')
    print('The most frequently associated items are:')
    for item in b10:
        print(f"{{ {', '.join(item)} }}")
    print('\n')
if b11 = = "__main__":
    fonk6()