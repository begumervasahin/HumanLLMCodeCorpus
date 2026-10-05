import random
def confA(algorithm):
    configurations = []
    n = 0
    while n != 100000:
        array = random.sample(range(1000000000, 9999999999), 10)
        configurations.append(array)
        n += 1
        print(n)
    file_created = open('confAInicial' + str(algorithm) + '.txt', 'a')
    for config in configurations:
        file_created.write(str(config) + '\n')
    return configurations
def confB(algorithm):
    configurations = []
    n = 0
    while n != 10000:
        array = random.sample(range(1000000000, 9999999999), 100)
        configurations.append(array)
        n += 1
        print(n)
    file_created = open('confBInicial' + str(algorithm) + '.txt', 'a')
    for config in configurations:
        file_created.write(str(config) + '\n')
    return configurations
def confC(algorithm):
    configurations = []
    n = 0
    while n != 1000:
        array = random.sample(range(1000000000, 9999999999), 1000)
        configurations.append(array)
        n += 1
        print(n)
    file_created = open('confCInicial' + str(algorithm) + '.txt', 'a')
    for config in configurations:
        file_created.write(str(config) + '\n')
    return configurations
def confD(algorithm):
    configurations = []
    n = 0
    while n != 100:
        array = random.sample(range(1000000000, 9999999999), 10000)
        configurations.append(array)
        n += 1
        print(n)
    file_created = open('confDInicial' + str(algorithm) + '.txt', 'a')
    for config in configurations:
        file_created.write(str(config) + '\n')
    return configurations
def confE(algorithm):
    configurations = []
    n = 0
    while n != 10:
        array = random.sample(range(1000000000, 9999999999), 100000)
        configurations.append(array)
        n += 1
        print(n)
    file_created = open('confEInicial' + str(algorithm) + '.txt', 'a')
    for config in configurations:
        file_created.write(str(config) + '\n')
    return configurations
def confF(algorithm):
    configurations = []
    n = 0
    while n != 1:
        array = random.sample(range(1000000000, 9999999999), 1000000)
        configurations.append(array)
        n += 1
        print(n)
    file_created = open('confFInicial' + str(algorithm) + '.txt', 'a')
    for config in configurations:
        file_created.write(str(config) + '\n')
    return configurations