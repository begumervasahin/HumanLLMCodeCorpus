import statistics
def calculate_standard_deviation(numbers):
    mean = sum(numbers) / len(numbers)
    variance_sum = sum((x - mean) ** 2 for x in numbers)
    return (variance_sum / len(numbers)) ** 0.5
def display_statistics(name, data):
    custom_std_dev = calculate_standard_deviation(data)
    custom_variance = custom_std_dev ** 2
    sample_std_dev = statistics.stdev(data)
    population_std_dev = statistics.pstdev(data)
    sample_variance = statistics.variance(data)
    population_variance = statistics.pvariance(data)
    print(f'\nCalculations for {name}:')
    print(f'Custom standard deviation of {name} is {custom_std_dev:.9f}')
    print(f'Custom variance of {name} is {custom_variance:.9f}')
    print(f'Statistics standard deviation of {name} is {sample_std_dev:.9f}')
    print(f'Population statistics standard deviation of {name} is {population_std_dev:.9f}')
    print(f'Statistics variance of {name} is {sample_variance:.9f}')
    print(f'Population statistics variance of {name} is {population_variance:.9f}')
    print('...........................................................')
def main():
    print('Calculate the variance for Method R MOT Edition 3 Sample Sets on page 8')
    list_A = [0.924, 0.928, 0.954, 0.957, 0.961, 0.965, 0.972, 0.979, 0.987, 1.373]
    list_C = [0.091, 0.109, 0.134, 0.136, 0.159, 0.172, 0.185, 0.191, 0.207, 8.616]
    display_statistics('list_A', list_A)
    display_statistics('list_C', list_C)
if __name__ == "__main__":
    main()