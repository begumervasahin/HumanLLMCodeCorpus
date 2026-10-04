import statistics
def calculate_standard_deviation(X):
    mean = sum(X) / len(X)
    total = sum((x - mean) ** 2 for x in X)
    return (total / len(X)) ** 0.5
def main():
    print('Calculate the variance for Method R MOT Edition 3 Sample Sets on page 8')
    list_A = [0.924, 0.928, 0.954, 0.957, 0.961, 0.965, 0.972, 0.979, 0.987, 1.373]
    list_C = [0.091, 0.109, 0.134, 0.136, 0.159, 0.172, 0.185, 0.191, 0.207, 8.616]
    for lst, name in zip([list_A, list_C], ['list_A', 'list_C']):
        print(f'WZ stddev of {name} is {calculate_standard_deviation(lst):15.9f}')
        print(f'WZ variance of {name} is {calculate_standard_deviation(lst) ** 2:15.9f}')
        print(f'Statistic stddev of {name} is {statistics.stdev(lst):15.9f}')
        print(f'Population Statistic stddev of {name} is {statistics.pstdev(lst):15.9f}')
        print(f'Statistic variance of {name} is {statistics.variance(lst):15.9f}')
        print(f'Population Statistic variance of {name} is {statistics.pvariance(lst):15.9f}')
        print('...........................................................')
if __name__ == "__main__":
    main()