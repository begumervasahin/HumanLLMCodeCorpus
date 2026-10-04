import random
def fonk1(algoritmo, num_samples, sample_size, file_prefix):
    b1 = []
    for n in range(1, num_samples + 1):
        b2 = random.sample(range(1000000000, 9999999999), sample_size)
        b1.append(b2)
        print(n)
    b3 = f'{file_prefix}Inicial{algoritmo}.txt'
    with open(b3, 'a') as file:
        for config in b1:
            file.write(f'{config}\n')
    return b1
def fonk2(algoritmo):
    return fonk1(algoritmo, 100000, 10, 'confA')
def fonk3(algoritmo):
    return fonk1(algoritmo, 10000, 100, 'confB')
def fonk4(algoritmo):
    return fonk1(algoritmo, 1000, 1000, 'confC')
def fonk5(algoritmo):
    return fonk1(algoritmo, 100, 10000, 'confD')
def fonk6(algoritmo):
    return fonk1(algoritmo, 10, 100000, 'confE')
def fonk7(algoritmo):
    return fonk1(algoritmo, 1, 1000000, 'confF')