import sys
class VariancePlugin:
    def input(self, filename):
        self.filename = filename
    def run(self):
        with open(self.filename, 'r') as file:
            self.bacteria = file.readline().strip().split(',')
            self.bacteria = [bacterium for bacterium in self.bacteria if bacterium != '""']
            self.n = len(self.bacteria)
            self.ADJ = [[] for _ in range(self.n)]
            for line in file:
                contents = line.strip().split(',')
                for j, content in enumerate(contents[1:]):
                    value = float(content)
                    self.ADJ[j].append(value)
    def output(self, filename):
        variances = []
        for i in range(self.n):
            sum_values = sum(self.ADJ[i])
            if self.ADJ[i]:
                average = sum_values / len(self.ADJ[i])
                variance = sum((average - value) ** 2 for value in self.ADJ[i]) / len(self.ADJ[i])
                variances.append((variance, self.bacteria[i]))
        variances.sort(reverse=True)
        with open(filename, 'w') as output_file:
            output_file.write("Element\tVariance\n\n")
            for bacterium, variance in variances:
                output_file.write(f"{bacterium}\t{variance}\n")