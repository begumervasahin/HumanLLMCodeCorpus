
import os
from abhishek_sharma_knn_agent import Agent
from abhishek_sharma_knn_graph import Graph
class class1:
    def fonk1(self, directory, b18):
        b1 = Agent()
        b2 = os.listdir(directory)
        b3 = [file_name for file_name in b2 if file_name.endswith("tst.dat")]
        b4 = len(b3)
        b5 = int(round(int(b18) / 2.0))
        self.fonk2(b18)
        b6 = [[0 for _ in range(b5 + 1)] for _ in range(b4)]
        for j, testing_file in enumerate(b3):
            b7 = os.path.join(directory, testing_file)
            b8 = b7.replace("tst.dat", "tra.dat")
            print("|", testing_file, " " * (36 - len(testing_file)), "|", b9 = '')
            with open(b7) as test_file:
                b10 = False
                for line in test_file:
                    if "@data" in line:
                        b10 = True
                        continue
                    if b10:
                        b11 = line.strip().split(",")
                        b12 = b11[-1]
                        b13 = b1.sensor(b18, b8, b11)
                        b14 = self.fonk3(b13)
                        self.fonk4(b13, b12, b14, b6[j])
            self.fonk5(b6[j])
        self.fonk6(b6)
        b15 = [sum(stats) for stats in zip(*b6)]
        b16 = Graph()
        b16.plotGraph(b15[1:], directory)
    def fonk2(self, b18):
        b17 = "| File Name" + " " * (36 - len("File Name"))
        for i in range(1, int(b18) + 1, 2):
            b17 += "| Accuracy (b18 = " + str(i) + ")" + " " * (17 - len("Accuracy (b18=" + str(i) + ")"))
        print(b17 + "|")
    def fonk3(self, b13):
        try:
            list(map(float, b13))
            return False
        except ValueError:
            return True
    def fonk4(self, b13, b12, b14, stats):
        a1 = 1
        for item in b13:
            if b14:
                if item.strip() == b12.strip():
                    stats[a1] += 1
            elif str(float(item)).strip() == str(float(b12)).strip():
                stats[a1] += 1
            a1 += 1
        stats[0] += 1
    def fonk5(self, stats):
        for n in range(1, len(stats)):
            b19 = (float(stats[n]) / stats[0]) * 100
            b20 = f"{b19:.2f}% ({stats[n]:03}/{stats[0]:03})"
            print(b20 + " " * (27 - len(b20)) + "|", b9 = '')
        print("")
    def fonk6(self, b6):
        b15 = [sum(stats) for stats in zip(*b6)]
        print("-" * 42)
        print("| Average Accuracies" + " " * (36 - len("Average Accuracies")) + "|")
        print("-" * 42)
        for i in range(1, len(b15)):
            b21 = (float(b15[i]) / b15[0]) * 100
            print(f"b22 = {i*2-1}: {b21:.2f}%")