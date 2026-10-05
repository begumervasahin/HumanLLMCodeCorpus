import sys
class VariancePlugin:
    def input(self, filename):
        self.myfile = filename
    def run(self):
        with open(self.myfile, 'r') as filestuff:
            firstline = filestuff.readline()
            self.bacteria = firstline.strip().split(',')
            if '\"\"' in self.bacteria:
                self.bacteria.remove('\"\"')
            self.n = len(self.bacteria)
            self.ADJ = [[] for _ in range(self.n)]
            for line in filestuff:
                contents = line.strip().split(',')
                for j in range(len(contents) - 1):
                    value = float(contents[j + 1])
                    self.ADJ[j].append(value)
    def output(self, filename):
        with open(filename, 'w') as filestuff2:
            filestuff2.write("Element\tVariance\n\n")
            variances = []
            for i in range(self.n):
                if len(self.ADJ[i]) != 0:
                    mean = sum(self.ADJ[i]) / len(self.ADJ[i])
                    variance = sum((mean - x) ** 2 for x in self.ADJ[i]) / len(self.ADJ[i])
                    variances.append((variance, self.bacteria[i]))
            variances.sort(reverse=True)
            for variance, element in variances:
                filestuff2.write(f"{element}\t{variance}\n")
if __name__ == "__main__":
    plugin = VariancePlugin()
    plugin.input("data.txt")
    plugin.run()
    plugin.output("output.txt")
