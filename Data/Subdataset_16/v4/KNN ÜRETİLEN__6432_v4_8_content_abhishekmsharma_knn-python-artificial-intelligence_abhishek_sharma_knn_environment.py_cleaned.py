
import os
from abhishek_sharma_knn_agent import Agent
from abhishek_sharma_knn_graph import Graph
class class1:
    def fonk1(self, directory, b7):
        b1 = Agent()
        b2 = os.listdir(directory)
        b3 = [file_name for file_name in b2 if file_name.endswith("tst.dat")]
        b4 = len(b3)
        b5 = int(round(int(b7) / 2.0))
        b6 = "| File Name" + " " * (36 - len("File Name"))
        for i in range(1, int(b7) + 1, 2):
            b6 += "| Accuracy (b7 = " + str(i) + ")" + " " * (17 - len("Accuracy (b7=" + str(i) + ")"))
        print(b6 + "|")
        b8 = [[0 for _ in range(b5 + 1)] for _ in range(b4)]
        for j, testing_file in enumerate(b3):
            b9 = os.path.join(directory, testing_file)
            b10 = b9.replace("tst.dat", "tra.dat")
            print("|", b3[j], " " * (36 - len(b3[j])), "|", b11 = '')
            with open(b9) as test_file:
                b12 = False
                for line in test_file:
                    if "@data" in line:
                        b12 = True
                        continue
                    if b12:
                        b13 = line.strip().split(",")
                        b14 = b13[-1]
                        b15 = b1.sensor(b7, b10, b13)
                        a1 = 1
                        try:
                            b15 = list(map(float, b15))
                        except ValueError:
                            a1 = 0
                        a2 = 1
                        for item in b15:
                            if a1 = = 0:
                                if item.strip() == b14.strip():
                                    b8[j][a2] += 1
                            elif str(float(item)).strip() == str(float(b14)).strip():
                                b8[j][a2] += 1
                            a2 += 1
                        b8[j][0] += 1
            b16 = b8[j]
            for n in range(1, len(b16)):
                b17 = (float(b16[n]) / b16[0]) * 100
                b18 = f"{b17:.2f}% ({b16[n]:03}/{b16[0]:03})"
                print(b18 + " " * (27 - len(b18)) + "|", b11 = '')
            print("")
        b19 = [sum(stats) for stats in zip(*b8)]
        print("-" * 42)
        print("| Average Accuracies" + " " * (36 - len("Average Accuracies")) + "|")
        print("-" * 42)
        for i in range(1, len(b19)):
            b20 = (float(b19[i]) / b19[0]) * 100
            print(f"b21 = {i*2-1}: {b20:.2f}%")
        b22 = Graph()
        b22.plotGraph(b19[1:], directory)