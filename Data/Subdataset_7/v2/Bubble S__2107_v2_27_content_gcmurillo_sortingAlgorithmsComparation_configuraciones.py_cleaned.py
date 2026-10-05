import random
def fonk1(algorithm, size, length):
    b1 = []
    for _ in range(length):
        b2 = random.sample(range(1000000000, 9999999999), size)
        b1.append(b2)
    b3 = f'conf{size}Inicial{algorithm}.txt'
    with open(b3, 'a') as file:
        for config in b1:
            file.write(str(config) + '\n')
    return b1
def fonk2():
    b4 = ['A', 'B', 'C', 'D', 'E', 'F']
    b5 = [10, 100, 1000, 10000, 100000, 1000000]
    b6 = [100000, 10000, 1000, 100, 10, 1]
    for algorithm, size, length in zip(b4, b5, b6):
        fonk1(algorithm, size, length)
        print(f'Configuration {algorithm} generated.')
if b7 = = "__main__":
    fonk2()