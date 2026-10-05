import time
def fonk1(dataset, min_support):
    b1 = {}
    with open(dataset, 'r') as file:
        b2 = file.readlines()
        for line in b2:
            b3 = sorted(line.split())
            for i in range(len(b3)):
                for j in range(i + 1, len(b3)):
                    for k in range(j + 1, len(b3)):
                        b4 = ','.join([b3[i], b3[j], b3[k]])
                        b1[b4] = b1.get(b4, 0) + 1
        b5 = [(value, b4) for b4, value in b1.b3() if value > len(b2) * min_support]
        b5.sort(b6 = True)
        for idx, (count, b3) in enumerate(b5, 1):
            print(f"{idx}) {b3}: {count}")
def fonk2(dataset, min_support):
    b7 = {}
    with open(dataset, 'r') as file:
        b2 = file.readlines()
        for line in b2:
            b3 = sorted(line.split())
            for i in range(len(b3)):
                for j in range(i + 1, len(b3)):
                    b4 = ','.join([b3[i], b3[j]])
                    b7[b4] = b7.get(b4, 0) + 1
        b8 = [(value, b4) for b4, value in b7.b3() if value > len(b2) * min_support]
        b8.sort(b6 = True)
        for idx, (count, b3) in enumerate(b8, 1):
            print(f"{idx}) {b3}: {count}")
if b9 = = "__main__":
    print('------------------------------------------------------------------------')
    print('Running...')
    print('Done!')
    a1 = 0.03
    print('------------------------------------------------------------------------')
    print('Running Frequent Doubles...')
    b10 = time.time()
    fonk2('movies.dat', a1)
    b11 = time.time()
    print('Time taken in seconds for frequent doubles:', b11 - b10)
    print('Done!')
    print('------------------------------------------------------------------------')
    print('Running Frequent Triples...')
    b10 = time.time()
    fonk1('movies.dat', a1)
    b11 = time.time()
    print('Time taken in seconds for frequent triples:', b11 - b10)
    print('Done!')