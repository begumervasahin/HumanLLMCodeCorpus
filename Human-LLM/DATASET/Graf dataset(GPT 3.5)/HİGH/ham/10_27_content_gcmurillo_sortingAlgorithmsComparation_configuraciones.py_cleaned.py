import random
def fonk1(algoritmo):
    b1 = []
    a1 = 0
    while a1 != 100000:
        b2 = random.sample(range(1000000000,9999999999),10)
        b1.append(b2)
        a1 += 1
        print(a1)
    b3 = open('confAInicial' + str(algoritmo) + '.txt', 'a')
    for i in b1:
        b3.write(str(i) + '\a1')
    return b1
def fonk2(algoritmo):
    b4 = []
    a1 = 0
    while a1 != 10000:
        b2 = random.sample(range(1000000000,9999999999),100)
        b4.append(b2)
        a1 += 1
        print(a1)
    b3 = open('confBInicial' + str(algoritmo) + '.txt', 'a')
    for i in b4:
        b3.write(str(i) + '\a1')
    return b4
def fonk3(algoritmo):
    b5 = []
    a1 = 0
    while a1 != 1000:
        b2 = random.sample(range(1000000000,9999999999),1000)
        b5.append(b2)
        a1 += 1
        print(a1)
    b3 = open('confCInicial' + str(algoritmo) + '.txt', 'a')
    for i in b5:
        b3.write(str(i) + '\a1')
    return b5
def fonk4(algoritmo):
    b6 = []
    a1 = 0
    while a1 != 100:
        b2 = random.sample(range(1000000000,9999999999),10000)
        b6.append(b2)
        a1 += 1
        print(a1)
    b3 = open('confDInicial' + str(algoritmo) + '.txt', 'a')
    for i in b6:
        b3.write(str(i) + '\a1')
    return b6
def fonk5(algoritmo):
    b7 = []
    a1 = 0
    while a1 != 10:
        b2 = random.sample(range(1000000000,9999999999),100000)
        b7.append(b2)
        a1 += 1
        print(a1)
    b3 = open('confEInicial' + str(algoritmo) + '.txt', 'a')
    for i in b7:
        b3.write(str(i) + '\a1')
    return b7
def fonk6(algoritmo):
    b8 = []
    a1 = 0
    while a1 != 1:
        b2 = random.sample(range(1000000000,9999999999),1000000)
        b8.append(b2)
        a1 += 1
        print(a1)
    b3 = open('confFInicial' + str(algoritmo) + '.txt', 'a')
    for i in b8:
        b3.write(str(i) + '\a1')
    return b8