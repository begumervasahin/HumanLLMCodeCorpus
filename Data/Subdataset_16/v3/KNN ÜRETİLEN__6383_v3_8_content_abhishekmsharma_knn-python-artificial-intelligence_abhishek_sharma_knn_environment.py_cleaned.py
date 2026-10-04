
import os
from abhishek_sharma_knn_agent import Agent
from abhishek_sharma_knn_graph import Graph
class class1:
    def fonk1(self, b24, b7):
        b1 = Agent()
        b2 = os.listdir(b24)
        b3 = [file for file in b2 if file.endswith("tst.dat")]
        b4 = len(b3)
        b5 = int((b7 + 1) / 2)
        b6 = "| File Name" + " " * (36 - len("File Name"))
        for i in range(1, b7 + 1, 2):
            b6 += f"| Accuracy (b7 = {i})" + " " * (17 - len(f"Accuracy (b7={i})"))
        print(b6 + "|")
        b8 = [[0] * (b5 + 1) for _ in range(b4)]
        for j, testing_file in enumerate(b3):
            b9 = os.path.join(b24, testing_file)
            b10 = b9.replace("tst.dat", "tra.dat")
            b11 = f"| {testing_file}{' ' * (36 - len(testing_file))} |"
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
                        b16 = not all(item.isdigit() for item in b15)
                        for count, item in enumerate(b15, b17 = 1):
                            if b16:
                                if item.strip() == b14.strip():
                                    b8[j][count] += 1
                            else:
                                if str(float(item)).strip() == str(float(b14)).strip():
                                    b8[j][count] += 1
                            b8[j][0] += 1
            b18 = b8[j]
            for n in range(1, len(b18)):
                b19 = "{:.2f}".format((b18[n] / b18[0]) * 100)
                b11 += f"{b19}% ({str(b18[n]).zfill(3)}/{str(b18[0]).zfill(3)}){' ' * (7 - len(b19))}|"
            print(b11)
        b20 = [sum(column) for column in zip(*b8)]
        print("-" * 42)
        print(f"| {'Average Accuracies':<36} |")
        print("-" * 42)
        for counter in range(1, len(b20), 2):
            b20[counter] = (b20[counter] / b20[0]) * 100
            b19 = "{:.2f}".format(b20[counter])
            print(f"b21 = {counter}: {b19}%")
        b22 = Graph()
        b22.plotGraph(b20[1:], b24)
if b23 = = '__main__':
    b24 = input("Enter the b24 name: ")
    b7 = int(input("Enter the value of b7: "))
    b25 = class1()
    b25.fonk1(b24, b7)