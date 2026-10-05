class StatisticsCalculator:
    def calculate_median(self, data):
        sorted_data = sorted(data)
        length = len(sorted_data)
        if length % 2 == 0:
            return (sorted_data[length
        else:
            return sorted_data[length
    def calculate_mode(self, data):
        frequency_dict = {}
        for item in set(data):
            frequency_dict[item] = data.count(item)
        max_frequency = max(frequency_dict.values())
        if max_frequency <= 1:
            return [0]
        else:
            return [key for key, value in frequency_dict.items() if value == max_frequency]
    def calculate_mean(self, data):
        return sum(data) / len(data)
    def calculate_variance(self, data):
        mean = self.calculate_mean(data)
        return sum((x - mean) ** 2 for x in data) / len(data)
    def calculate_standard_deviation(self, data):
        variance = self.calculate_variance(data)
        return variance ** 0.5
def main():
    calculator = StatisticsCalculator()
    with open("data.txt", 'r') as file:
        data = [float(line.strip()) for line in file]
    print('Mean: {:.2f}'.format(calculator.calculate_mean(data)))
    print('Median: {:.2f}'.format(calculator.calculate_median(data)))
    print('Mode: {}'.format(', '.join(map(str, calculator.calculate_mode(data)))))
    print('Variance: {:.2f}'.format(calculator.calculate_variance(data)))
    print('Standard Deviation: {:.2f}'.format(calculator.calculate_standard_deviation(data)))
if __name__ == "__main__":
    main()