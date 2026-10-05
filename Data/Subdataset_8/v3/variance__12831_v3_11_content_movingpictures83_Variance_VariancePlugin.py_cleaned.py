class VariancePlugin:
    def __init__(self):
        self.filename = None
        self.bacteria = []
        self.data = []
    def input(self, filename):
        self.filename = filename
    def parse_input(self):
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            self.bacteria = lines[0].strip().split(',')
            self.bacteria = [bacterium for bacterium in self.bacteria if bacterium != '""']
            for line in lines[1:]:
                data_for_bacteria = [float(value) for value in line.strip().split(',')[1:]]
                self.data.append(data_for_bacteria)
    def calculate_variance(self, data):
        mean = sum(data) / len(data)
        variance = sum((mean - value) ** 2 for value in data) / len(data)
        return variance
    def output(self, filename):
        with open(filename, 'w') as file:
            file.write("Element\tVariance\n\n")
            variances = []
            for i in range(len(self.bacteria)):
                if self.data[i]:
                    variance = self.calculate_variance(self.data[i])
                    variances.append((variance, self.bacteria[i]))
            variances.sort(reverse=True)
            for variance, bacterium in variances:
                file.write(f"{bacterium}\t{variance}\n")
if __name__ == "__main__":
    plugin = VariancePlugin()
    plugin.input("data.txt")
    plugin.parse_input()
    plugin.output("output.txt")