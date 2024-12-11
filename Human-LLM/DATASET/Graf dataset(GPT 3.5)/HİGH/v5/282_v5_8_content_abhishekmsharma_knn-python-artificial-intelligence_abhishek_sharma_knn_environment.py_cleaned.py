import os
from abhishek_sharma_knn_agent import Agent
from abhishek_sharma_knn_graph import Graph
class class1:
    def fonk1(self):
        self.b1 = Agent()
    def fonk2(self, directory, b14):
        b2 = [file for file in os.listdir(directory) if file.endswith("tst.dat")]
        b3 = len(b2)
        b4 = int(round(int(b14) / 2.0))
        self.fonk4(b14)
        b5 = [[0] * (b4 + 1) for _ in range(b3)]
        for idx, testing_file in enumerate(b2):
            b6 = testing_file.replace("tst.dat", "tra.dat")
            print("| {:<36}".format(testing_file), b7 = "|")
            with open(os.path.join(directory, testing_file)) as test_file:
                for line in test_file:
                    if "@data" in line:
                        for line in test_file:
                            b8 = line.strip().split(",")
                            b9 = b8[-1]
                            b10 = self.b1.sensor(int(b14), b6, b8)
                            self.fonk3(b5[idx], b10, b9)
                self.fonk5(b5[idx])
        self.fonk6(b5)
        self.fonk7(b5, directory)
    def fonk3(self, stats, b10, b9):
        b11 = [float(b13) if isinstance(b13, str) and b13.strip().isdigit() else b13 for b13 in b10]
        stats[0] += 1
        for idx, b13 in enumerate(b11, b12 = 1):
            if b13 = = b9:
                stats[idx] += 1
    def fonk4(self, b14):
        print("| File Name                          ", b7 = "")
        for i in range(1, int(b14) + 1, 2):
            print("| Accuracy (b14 = {})        ".format(i), b7="")
        print("|")
    def fonk5(self, stats):
        for idx, count in enumerate(stats[1:], b12 = 1):
            b15 = (count / stats[0]) * 100 if stats[0] != 0 else 0
            print(" {:.2f}% ({} / {})      |".format(b15, count, stats[0]), b7 = "")
        print()
    def fonk6(self, b5):
        print("-" * 42)
        print("| Average Accuracies                 |")
        print("-" * 42)
        for idx, stats in enumerate(zip(*b5)[1:], b12 = 1):
            b16 = (sum(stats) / b5[0][idx]) * 100 if b5[0][idx] != 0 else 0
            print("| b17 = {:<2}: {:.2f}%".format(idx * 2 - 1, b16))
        print("-" * 42)
    def fonk7(self, b5, directory):
        b18 = Graph()
        b19 = [sum(stats[1:]) / stats[0] * 100 if stats[0] != 0 else 0 for stats in b5]
        b18.fonk7(b19, directory)