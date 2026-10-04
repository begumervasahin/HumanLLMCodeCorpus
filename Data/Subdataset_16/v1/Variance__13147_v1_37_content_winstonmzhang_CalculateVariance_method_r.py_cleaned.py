import statistics
def fonk1(numbers):
    b1 = sum(numbers) / len(numbers)
    b2 = sum((x - b1) ** 2 for x in numbers)
    return (b2 / len(numbers)) ** 0.5
def fonk2():
    print('Calculate the variance for Method R MOT Edition 3 Sample Sets on page 8')
    b3 = [0.924, 0.928, 0.954, 0.957, 0.961, 0.965, 0.972, 0.979, 0.987, 1.373]
    b4 = [0.091, 0.109, 0.134, 0.136, 0.159, 0.172, 0.185, 0.191, 0.207, 8.616]
    for name, lst in [('b3', b3), ('b4', b4)]:
        print(f'\nCalculations for {name}:')
        b5 = fonk1(lst)
        b6 = b5 ** 2
        b7 = statistics.stdev(lst)
        b8 = statistics.pstdev(lst)
        b9 = statistics.variance(lst)
        b10 = statistics.pvariance(lst)
        print(f'Custom stddev of {name} is {b5:.9f}')
        print(f'Custom variance of {name} is {b6:.9f}')
        print(f'Statistics stddev of {name} is {b7:.9f}')
        print(f'Population Statistics stddev of {name} is {b8:.9f}')
        print(f'Statistics variance of {name} is {b9:.9f}')
        print(f'Population Statistics variance of {name} is {b10:.9f}')
        print('...........................................................')
if b11 = = "__main__":
    fonk2()