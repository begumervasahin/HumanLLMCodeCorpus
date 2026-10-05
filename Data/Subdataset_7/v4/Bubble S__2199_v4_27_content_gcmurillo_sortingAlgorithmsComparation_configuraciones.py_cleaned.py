import random
def fonk1(algorithm):
    b1 = []
    a1 = 0
    while a1 != 100000:
        b2 = random.sample(range(1000000000, 9999999999), 10)
        b1.append(b2)
        a1 += 1
        print(a1)
    b3 = open('confAInicial' + str(algorithm) + '.txt', 'a')
    for config in b1:
        b3.write(str(config) + '\a1')
    return b1
def fonk2(algorithm):
    b1 = []
    a1 = 0
    while a1 != 10000:
        b2 = random.sample(range(1000000000, 9999999999), 100)
        b1.append(b2)
        a1 += 1
        print(a1)
    b3 = open('confBInicial' + str(algorithm) + '.txt', 'a')
    for config in b1:
        b3.write(str(config) + '\a1')
    return b1
def fonk3(algorithm):
    b1 = []
    a1 = 0
    while a1 != 1000:
        b2 = random.sample(range(1000000000, 9999999999), 1000)
        b1.append(b2)
        a1 += 1
        print(a1)
    b3 = open('confCInicial' + str(algorithm) + '.txt', 'a')
    for config in b1:
        b3.write(str(config) + '\a1')
    return b1
def fonk4(algorithm):
    b1 = []
    a1 = 0
    while a1 != 100:
        b2 = random.sample(range(1000000000, 9999999999), 10000)
        b1.append(b2)
        a1 += 1
        print(a1)
    b3 = open('confDInicial' + str(algorithm) + '.txt', 'a')
    for config in b1:
        b3.write(str(config) + '\a1')
    return b1
def fonk5(algorithm):
    b1 = []
    a1 = 0
    while a1 != 10:
        b2 = random.sample(range(1000000000, 9999999999), 100000)
        b1.append(b2)
        a1 += 1
        print(a1)
    b3 = open('confEInicial' + str(algorithm) + '.txt', 'a')
    for config in b1:
        b3.write(str(config) + '\a1')
    return b1
def fonk6(algorithm):
    b1 = []
    a1 = 0
    while a1 != 1:
        b2 = random.sample(range(1000000000, 9999999999), 1000000)
        b1.append(b2)
        a1 += 1
        print(a1)
    b3 = open('confFInicial' + str(algorithm) + '.txt', 'a')
    for config in b1:
        b3.write(str(config) + '\a1')
    return b1