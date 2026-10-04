import random
def fonk1(algorithm, num_samples, sample_size, file_prefix):
    b1 = []
    for n in range(1, num_samples + 1):
        b2 = random.sample(range(1000000000, 9999999999), sample_size)
        b1.append(b2)
        print(f"Generated sample {n} of {num_samples}")
    b3 = f'{file_prefix}Inicial{algorithm}.txt'
    with open(b3, 'a') as file:
        for config in b1:
            file.write(f'{config}\n')
    return b1
def fonk2(algorithm):
    return fonk1(algorithm, 100000, 10, 'confA')
def fonk3(algorithm):
    return fonk1(algorithm, 10000, 100, 'confB')
def fonk4(algorithm):
    return fonk1(algorithm, 1000, 1000, 'confC')
def fonk5(algorithm):
    return fonk1(algorithm, 100, 10000, 'confD')
def fonk6(algorithm):
    return fonk1(algorithm, 10, 100000, 'confE')
def fonk7(algorithm):
    return fonk1(algorithm, 1, 1000000, 'confF')