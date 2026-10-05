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
        print("| File Name", " " * (36 - len("File Name")), b6 = "")
        for i in range(1, int(b7) + 1, 2):
            print("| Accuracy (b7 = " + str(i) + ")" + " " * (17 - len("Accuracy b18 = " + str(i))), b6="")
        print("|")
        b8 = [[0 for _ in range(b5 + 1)] for _ in range(b4)]
        for j in range(b4):
            b9 = os.path.join(directory, b3[j])
            b10 = b9.replace("tst.dat", "tra.dat")
            print("|", b3[j], " " * (36 - len(b3[j])), "|", b6 = "")
            with open(b9) as test_file:
                for line in test_file:
                    if "@data" in line:
                        for line in test_file:
                            b11 = line.strip().split(",")
                            b12 = b11[-1]
                            b13 = b1.sensor(b7, b10, b11)
                            a1 = 1
                            try:
                                b13 = list(map(float, b13))
                            except ValueError:
                                a1 = 0
                            a2 = 1
                            for item in b13:
                                if a1 = = 0:
                                    if item.strip() == b12.strip():
                                        b8[j][a2] += 1
                                elif str(float(item)).strip() == str(float(b12)).strip():
                                    b8[j][a2] += 1
                                a2 += 1
                            b8[j][0] += 1
                b14 = b8[j]
            for n in range(1, len(b14)):
                b15 = "{:.2f}%".format((float(b14[n]) / b14[0]) * 100)
                print(b15 + " (" + str(b14[n]).zfill(3) + "/" + str(b14[0]).zfill(3) + ")" + " " * (7 - len(str(b15))), "|", b6 = "")
            print("")
        b16 = [sum(items) for items in zip(*b8)]
        print("-" * (42 - len("-")))
        print("| Average Accuracies", " " * (36 - len("Average Accuracies")), "|")
        print("-" * (42 - len("-")))
        a3 = 1
        for items in range(1, len(b16)):
            b16[items] = (float(b16[items]) / b16[0]) * 100
            b17 = "{:.2f}%".format(b16[items])
            print("b18 = " + str(a3) + ": " + b17)
            a3 += 2
        b19 = Graph()
        b19.plot_graph(b16[1:], directory)