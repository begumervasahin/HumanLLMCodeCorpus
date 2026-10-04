
import os
from abhishek_sharma_knn_agent import Agent
from abhishek_sharma_knn_graph import Graph
class class1:
    def fonk1(self, b23, b7):
        b1 = Agent()
        b2 = os.listdir(b23)
        b3 = [file_name for file_name in b2 if file_name.endswith("tst.dat")]
        b4 = len(b3)
        b5 = int(round(int(b7) / 2.0))
        b6 = "| File Name" + " " * (36 - len("File Name"))
        for i in range(1, int(b7) + 1, 2):
            b6 += f"| Accuracy (b7 = {i})" + " " * (17 - len(f"Accuracy (b7={i})"))
        print(b6 + "|")
        b8 = [[0 for _ in range(b5 + 1)] for _ in range(b4)]
        for j, testing_file in enumerate(b3):
            b9 = os.path.join(b23, testing_file)
            b10 = b9.replace("tst.dat", "tra.dat")
            b11 = f"| {testing_file}{' ' * (36 - len(testing_file))} |"
            with open(b9) as test_file:
                for line in test_file:
                    if "@data" in line:
                        for line in test_file:
                            b12 = line.strip().split(",")
                            b13 = b12[-1]
                            b14 = b1.sensor(b7, b10, b12)
                            b15 = all(item.isdigit() for item in b14)
                            for count, item in enumerate(b14, b16 = 1):
                                if b15:
                                    if str(float(item)).strip() == str(float(b13)).strip():
                                        b8[j][count] += 1
                                else:
                                    if item.strip() == b13.strip():
                                        b8[j][count] += 1
                            b8[j][0] += 1
            b17 = b8[j]
            for n in range(1, len(b17)):
                b18 = "{:.2f}".format((float(b17[n]) / b17[0]) * 100)
                b11 += f"{b18}% ({str(b17[n]).zfill(3)}/{str(b17[0]).zfill(3)}){' ' * (7 - len(b18))}|"
            print(b11)
        b19 = [sum(column) for column in zip(*b8)]
        print("-" * 42)
        print(f"| {'Average Accuracies':<36} |")
        print("-" * 42)
        for counter in range(1, len(b19), 2):
            b19[counter] = (float(b19[counter]) / b19[0]) * 100
            b18 = "{:.2f}".format(b19[counter])
            print(f"b20 = {counter}: {b18}%")
        b21 = Graph()
        b21.plotGraph(b19[1:], b23)
if b22 = = '__main__':
    b23 = input("Enter the b23 name: ")
    b7 = int(input("Enter the value of b7: "))
    b24 = class1()
    b24.fonk1(b23, b7)