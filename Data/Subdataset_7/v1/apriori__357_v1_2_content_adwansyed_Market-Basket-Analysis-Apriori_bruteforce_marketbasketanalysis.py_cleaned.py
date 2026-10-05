import time
def fonk1(dataset, tHold):
    with open(dataset, 'r') as myFile:
        b1 = myFile.readlines()
        b2 = {}
        for line in b1:
            b3 = sorted(line.split())
            for i in range(len(b3)):
                for j in range(i + 1, len(b3)):
                    for k in range(j + 1, len(b3)):
                        b4 = ','.join([b3[i], b3[j], b3[k]])
                        b2[b4] = b2.get(b4, 0) + 1
        b5 = [(value, b4) for b4, value in b2.b3() if value > len(b1) * tHold]
        b5.sort(b6 = True)
        for idx, (count, b3) in enumerate(b5, 1):
            print(idx, ')', b3, ':', count)
def fonk2(dataset, tHold):
    with open(dataset, 'r') as myFile:
        b1 = myFile.readlines()
        b7 = {}
        for line in b1:
            b3 = sorted(line.split())
            for i in range(len(b3)):
                for j in range(i + 1, len(b3)):
                    b4 = ','.join([b3[i], b3[j]])
                    b7[b4] = b7.get(b4, 0) + 1
        b5 = [(value, b4) for b4, value in b7.b3() if value > len(b1) * tHold]
        b5.sort(b6 = True)
        for idx, (count, b3) in enumerate(b5, 1):
            print(idx, ')', b3, ':', count)
if b8 = = "__main__":
    print('------------------------------------------------------------------------')
    print('Running...')
    print('Done!')
    a1 = 0.03
    print('------------------------------------------------------------------------')
    print('Running Frequent Doubles...')
    b9 = time.time()
    fonk2('movies.dat', a1)
    b10 = time.time()
    print('Time taken in seconds for frequent doubles:', b10 - b9)
    print('Done!')
    print('------------------------------------------------------------------------')
    print('Running Frequent Triples...')
    b9 = time.time()
    fonk1('movies.dat', a1)
    b10 = time.time()
    print('Time taken in seconds for frequent triples:', b10 - b9)
    print('Done!')