import statistics
def fonk1(numbers):
    b1 = sum(numbers) / len(numbers)
    b2 = sum((x - b1) ** 2 for x in numbers)
    return (b2 / len(numbers)) ** 0.5
def fonk2(name, data):
    b3 = fonk1(data)
    b4 = b3 ** 2
    b5 = statistics.stdev(data)
    b6 = statistics.pstdev(data)
    b7 = statistics.variance(data)
    b8 = statistics.pvariance(data)
    print(f'\nCalculations for {name}:')
    print(f'Custom standard deviation of {name} is {b3:.9f}')
    print(f'Custom variance of {name} is {b4:.9f}')
    print(f'Statistics standard deviation of {name} is {b5:.9f}')
    print(f'Population statistics standard deviation of {name} is {b6:.9f}')
    print(f'Statistics variance of {name} is {b7:.9f}')
    print(f'Population statistics variance of {name} is {b8:.9f}')
    print('...........................................................')
def fonk3():
    print('Calculate the variance for Method R MOT Edition 3 Sample Sets on page 8')
    b9 = [0.924, 0.928, 0.954, 0.957, 0.961, 0.965, 0.972, 0.979, 0.987, 1.373]
    b10 = [0.091, 0.109, 0.134, 0.136, 0.159, 0.172, 0.185, 0.191, 0.207, 8.616]
    fonk2('b9', b9)
    fonk2('b10', b10)
if b11 = = "__main__":
    fonk3()