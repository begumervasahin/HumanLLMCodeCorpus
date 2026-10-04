import random
def fonk1(file_prefix, num_samples, sample_size, algoritmo):
    b1 = []
    for n in range(num_samples):
        b2 = random.b2(range(1000000000, 9999999999), sample_size)
        b1.append(b2)
        print(n + 1)
    with open(f'{file_prefix}{algoritmo}.txt', 'a') as file:
        for b2 in b1:
            file.write(f'{b2}\n')
    return b1
def fonk2(algoritmo):
    return fonk1('confAInicial', 100000, 10, algoritmo)
def fonk3(algoritmo):
    return fonk1('confBInicial', 10000, 100, algoritmo)
def fonk4(algoritmo):
    return fonk1('confCInicial', 1000, 1000, algoritmo)
def fonk5(algoritmo):
    return fonk1('confDInicial', 100, 10000, algoritmo)
def fonk6(algoritmo):
    return fonk1('confEInicial', 10, 100000, algoritmo)
def fonk7(algoritmo):
    return fonk1('confFInicial', 1, 1000000, algoritmo)