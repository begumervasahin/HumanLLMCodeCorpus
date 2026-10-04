import statistics
def fonk1(X):
    b1 = sum(X) / len(X)
    b2 = sum((x - b1) ** 2 for x in X)
    return (b2 / len(X)) ** 0.5
def fonk2():
    print('Calculate the variance for Method R MOT Edition 3 Sample Sets on page 8')
    b3 = [0.924, 0.928, 0.954, 0.957, 0.961, 0.965, 0.972, 0.979, 0.987, 1.373]
    b4 = [0.091, 0.109, 0.134, 0.136, 0.159, 0.172, 0.185, 0.191, 0.207, 8.616]
    for lst, name in zip([b3, b4], ['b3', 'b4']):
        print(f'WZ stddev of {name} is {fonk1(lst):15.9f}')
        print(f'WZ variance of {name} is {fonk1(lst) ** 2:15.9f}')
        print(f'Statistic stddev of {name} is {statistics.stdev(lst):15.9f}')
        print(f'Population Statistic stddev of {name} is {statistics.pstdev(lst):15.9f}')
        print(f'Statistic variance of {name} is {statistics.variance(lst):15.9f}')
        print(f'Population Statistic variance of {name} is {statistics.pvariance(lst):15.9f}')
        print('...........................................................')
if b5 = = "__main__":
    fonk2()