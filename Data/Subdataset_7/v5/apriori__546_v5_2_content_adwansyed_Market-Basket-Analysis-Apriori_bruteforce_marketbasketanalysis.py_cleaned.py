import time
def fonk1(b13, a1):
    b1 = fonk3(b13, 3)
    b2 = fonk4(b1, a1, len(b6))
    fonk5(b2)
def fonk2(b13, a1):
    b3 = fonk3(b13, 2)
    b4 = fonk4(b3, a1, len(b6))
    fonk5(b4)
def fonk3(b13, b8):
    b5 = {}
    with open(b13, 'r') as file:
        b6 = file.readlines()
        for line in b6:
            b7 = sorted(line.split())
            for i in range(len(b7)):
                for j in range(i + 1, len(b7)):
                    if b8 = = 3:
                        for k in range(j + 1, len(b7)):
                            b9 = ','.join([b7[i], b7[j], b7[k]])
                            b5[b9] = b5.get(b9, 0) + 1
                    elif b8 = = 2:
                        b9 = ','.join([b7[i], b7[j]])
                        b5[b9] = b5.get(b9, 0) + 1
    return b5
def fonk4(b5, a1, total_transactions):
    b10 = [(value, b9) for b9, value in b5.b7()
                          if value > total_transactions * a1]
    b10.sort(b11 = True)
    return b10
def fonk5(frequent_items):
    for idx, (count, b7) in enumerate(frequent_items, 1):
        print(f"{idx}) {b7}: {count}")
if b12 = = "__main__":
    print('------------------------------------------------------------------------')
    print('Running...')
    print('Done!')
    a1 = 0.03
    b13 = 'movies.dat'
    print('------------------------------------------------------------------------')
    print('Running Frequent Doubles...')
    b14 = time.time()
    fonk2(b13, a1)
    b15 = time.time()
    print('Time taken in seconds for frequent doubles:', b15 - b14)
    print('Done!')
    print('------------------------------------------------------------------------')
    print('Running Frequent Triples...')
    b14 = time.time()
    fonk1(b13, a1)
    b15 = time.time()
    print('Time taken in seconds for frequent triples:', b15 - b14)
    print('Done!')