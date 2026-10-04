import numpy as np
class VariancePlugin:
    def __init__(self):
        self.bacteria_names = []
        self.data_matrix = []
    def input(self, filename):
        self.input_file = filename
    def run(self):
        with open(self.input_file, 'r') as file:
            first_line = file.readline().strip()
            self.bacteria_names = [name for name in first_line.split(',') if name != '\"\"']
            num_bacteria = len(self.bacteria_names)
            self.data_matrix = [[] for _ in range(num_bacteria)]
            for line in file:
                values = line.strip().split(',')
                for index in range(1, len(values)):
                    self.data_matrix[index - 1].append(float(values[index]))
    def output(self, filename):
        variances = []
        for index, values in enumerate(self.data_matrix):
            if values:
                variance = np.var(values)
                variances.append((variance, self.bacteria_names[index]))
        variances.sort(reverse=True)
        with open(filename, 'w') as file:
            file.write("Element\tVariance\n\n")
            for variance, name in variances:
                file.write(f"{name}\t{variance:.6f}\n")
