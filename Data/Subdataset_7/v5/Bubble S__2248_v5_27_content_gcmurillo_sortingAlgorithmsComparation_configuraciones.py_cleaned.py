import random
def fonk1(algorithm, size, num_arrays, file_prefix):
    b1 = []
    for _ in range(num_arrays):
        b2 = random.sample(range(1000000000, 9999999999), size)
        b1.append(b2)
    b3 = f"{file_prefix}{algorithm}.txt"
    with open(b3, 'a') as file_created:
        for config in b1:
            file_created.write(str(config) + '\n')
    return b1
def fonk2(algorithm):
    return fonk1(algorithm, 10, 100000, 'confAInicial')
def fonk3(algorithm):
    return fonk1(algorithm, 100, 10000, 'confBInicial')
def fonk4(algorithm):
    return fonk1(algorithm, 1000, 1000, 'confCInicial')
def fonk5(algorithm):
    return fonk1(algorithm, 10000, 100, 'confDInicial')
def fonk6(algorithm):
    return fonk1(algorithm, 100000, 10, 'confEInicial')
def fonk7(algorithm):
    return fonk1(algorithm, 1000000, 1, 'confFInicial')
def fonk8():
    b4 = ['A', 'B', 'C', 'D', 'E', 'F']
    for algorithm in b4:
        fonk2(algorithm)
        fonk3(algorithm)
        fonk4(algorithm)
        fonk5(algorithm)
        fonk6(algorithm)
        fonk7(algorithm)
        print(f"Configurations generated for Algorithm {algorithm}")
if b5 = = "__main__":
    fonk8()