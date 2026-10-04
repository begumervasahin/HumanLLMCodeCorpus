import random
def confA(algoritmo):
    confA = []
    n = 0
    while n != 100000:
        arreglo = random.sample(range(1000000000, 9999999999), 10)
        confA.append(arreglo)
        n += 1
        print(n)
    archivoCreado = open('confAInicial' + str(algoritmo) + '.txt', 'a')
    for i in confA:
        archivoCreado.write(str(i) + '\n')
    archivoCreado.close()
    return confA
def confB(algoritmo):
    confB = []
    n = 0
    while n != 10000:
        arreglo = random.sample(range(1000000000, 9999999999), 100)
        confB.append(arreglo)
        n += 1
        print(n)
    archivoCreado = open('confBInicial' + str(algoritmo) + '.txt', 'a')
    for i in confB:
        archivoCreado.write(str(i) + '\n')
    archivoCreado.close()
    return confB
def confC(algoritmo):
    confC = []
    n = 0
    while n != 1000:
        arreglo = random.sample(range(1000000000, 9999999999), 1000)
        confC.append(arreglo)
        n += 1
        print(n)
    archivoCreado = open('confCInicial' + str(algoritmo) + '.txt', 'a')
    for i in confC:
        archivoCreado.write(str(i) + '\n')
    archivoCreado.close()
    return confC
def confD(algoritmo):
    confD = []
    n = 0
    while n != 100:
        arreglo = random.sample(range(1000000000, 9999999999), 10000)
        confD.append(arreglo)
        n += 1
        print(n)
    archivoCreado = open('confDInicial' + str(algoritmo) + '.txt', 'a')
    for i in confD:
        archivoCreado.write(str(i) + '\n')
    archivoCreado.close()
    return confD
def confE(algoritmo):
    confE = []
    n = 0
    while n != 10:
        arreglo = random.sample(range(1000000000, 9999999999), 100000)
        confE.append(arreglo)
        n += 1
        print(n)
    archivoCreado = open('confEInicial' + str(algoritmo) + '.txt', 'a')
    for i in confE:
        archivoCreado.write(str(i) + '\n')
    archivoCreado.close()
    return confE
def confF(algoritmo):
    confF = []
    n = 0
    while n != 1:
        arreglo = random.sample(range(1000000000, 9999999999), 1000000)
        confF.append(arreglo)
        n += 1
        print(n)
    archivoCreado = open('confFInicial' + str(algoritmo) + '.txt', 'a')
    for i in confF:
        archivoCreado.write(str(i) + '\n')
    archivoCreado.close()
    return confF