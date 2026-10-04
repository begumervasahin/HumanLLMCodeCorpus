
from abhishek_sharma_knn_agent import Agent
from abhishek_sharma_knn_graph import Graph
import os
class class1:
    def fonk1(self, b22, b7):
        b1 = Agent()
        b2 = os.listdir(b22)
        b3 = [file_name for file_name in b2 if file_name.endswith("tst.dat")]
        b4 = len(b3)
        b5 = int(round(int(b7) / 2.0))
        b6 = "| File Name" + " " * (36 - len("File Name"))
        for i in range(1, int(b7) + 1, 2):
            b6 += f"| Accuracy (b7 = {i})" + " " * (17 - len(f"Accuracy b19 = {i}"))
        print(b6 + "|")
        b8 = [[0 for _ in range(b5 + 1)] for _ in range(b4)]
        for j in range(b4):
            b9 = os.path.join(b22, b3[j])
            b10 = b9.replace("tst.dat", "tra.dat")
            b11 = f"| {b3[j]}{' ' * (36 - len(b3[j]))} |"
            with open(b9) as test_file:
                for line in test_file:
                    if "@data" in line:
                        for line in test_file:
                            b12 = line.strip().split(",")
                            b13 = b12[-1]
                            b14 = b1.sensor(b7, b10, b12)
                            a1 = 1
                            try:
                                b14 = list(map(float, b14))
                            except ValueError:
                                a1 = 0
                            a2 = 1
                            for item in b14:
                                if a1 = = 0:
                                    if item.strip() == b13.strip():
                                        b8[j][a2] += 1
                                else:
                                    if str(float(item)).strip() == str(float(b13)).strip():
                                        b8[j][a2] += 1
                                a2 += 1
                            b8[j][0] += 1
            b15 = b8[j]
            for n in range(1, len(b15)):
                b16 = "{:.2f}".format((float(b15[n]) / b15[0]) * 100)
                b11 += f"{b16}% ({str(b15[n]).zfill(3)}/{str(b15[0]).zfill(3)}){' ' * (7 - len(b16))}|"
            print(b11)
        b17 = [sum(column) for column in zip(*b8)]
        print("-" * 42)
        print("| Average Accuracies" + " " * (36 - len("Average Accuracies")) + "|")
        print("-" * 42)
        a3 = 1
        for items in range(1, len(b17)):
            b17[items] = (float(b17[items]) / b17[0]) * 100
            b18 = "{:.2f}".format(b17[items])
            print(f"b19 = {a3}: {b18}%")
            a3 += 2
        b20 = Graph()
        b20.plotGraph(b17[1:], b22)
if b21 = = '__main__':
    b22 = input("Enter the b22 name: ")
    b7 = int(input("Enter the value of b7: "))
    b23 = class1()
    b23.fonk1(b22, b7)