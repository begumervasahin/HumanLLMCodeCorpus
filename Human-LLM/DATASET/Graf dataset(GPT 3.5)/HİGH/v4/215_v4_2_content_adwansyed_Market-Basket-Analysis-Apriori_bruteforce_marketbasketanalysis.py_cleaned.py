import time
def fonk1(b10, a1):
    b1 = {}
    with open(b10, 'r') as file:
        b2 = file.readlines()
        for line in b2:
            b3 = sorted(line.split())
            for i in range(len(b3)):
                for j in range(i + 1, len(b3)):
                    for k in range(j + 1, len(b3)):
                        b4 = ','.join([b3[i], b3[j], b3[k]])
                        b1[b4] = b1.get(b4, 0) + 1
        b5 = [(value, b4) for b4, value in b1.b3()
                            if value > len(b2) * a1]
        b5.sort(b6 = True)
        fonk3(b5)
def fonk2(b10, a1):
    b7 = {}
    with open(b10, 'r') as file:
        b2 = file.readlines()
        for line in b2:
            b3 = sorted(line.split())
            for i in range(len(b3)):
                for j in range(i + 1, len(b3)):
                    b4 = ','.join([b3[i], b3[j]])
                    b7[b4] = b7.get(b4, 0) + 1
        b8 = [(value, b4) for b4, value in b7.b3()
                             if value > len(b2) * a1]
        b8.sort(b6 = True)
        fonk3(b8)
def fonk3(frequent_items):
    for idx, (count, b3) in enumerate(frequent_items, 1):
        print(f"{idx}) {b3}: {count}")
if b9 = = "__main__":
    print('------------------------------------------------------------------------')
    print('Running...')
    print('Done!')
    a1 = 0.03
    b10 = 'movies.dat'
    print('------------------------------------------------------------------------')
    print('Running Frequent Doubles...')
    b11 = time.time()
    fonk2(b10, a1)
    b12 = time.time()
    print('Time taken in seconds for frequent doubles:', b12 - b11)
    print('Done!')
    print('------------------------------------------------------------------------')
    print('Running Frequent Triples...')
    b11 = time.time()
    fonk1(b10, a1)
    b12 = time.time()
    print('Time taken in seconds for frequent triples:', b12 - b11)
    print('Done!')