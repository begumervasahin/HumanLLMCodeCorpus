class StatisticsCalculator:
    def calculate_median(self, data):
        sorted_data = sorted(data)
        data_length = len(sorted_data)
        if data_length % 2 == 0:
            middle_index = data_length
            return (sorted_data[middle_index - 1] + sorted_data[middle_index]) / 2
        else:
            return sorted_data[data_length
    def calculate_mode(self, data):
        frequency_dict = {}
        for item in set(data):
            frequency_dict[item] = data.count(item)
        max_frequency = max(frequency_dict.values())
        if max_frequency <= 1:
            return [0]
        else:
            return [key for key, val in frequency_dict.items() if val == max_frequency]
    def calculate_mean(self, data):
        return sum(data) / len(data)
    def calculate_variance(self, data):
        mean = self.calculate_mean(data)
        return sum((item - mean) ** 2 for item in data) / len(data)
    def calculate_standard_deviation(self, data):
        return (self.calculate_variance(data)) ** 0.5
def main():
    calculator = StatisticsCalculator()
    with open("data.txt", 'r') as file:
        data = [float(line.strip()) for line in file]
    print('Median is %.2f' % (calculator.calculate_median(data)))
    print('Mean is %.2f' % (calculator.calculate_mean(data)))
    print('Mode is ' + (', '.join(map(str, calculator.calculate_mode(data)))))
    print('Variance is %.2f' % (calculator.calculate_variance(data)))
    print('Standard Deviation is %.2f' % (calculator.calculate_standard_deviation(data)))
if __name__ == "__main__":
    main()