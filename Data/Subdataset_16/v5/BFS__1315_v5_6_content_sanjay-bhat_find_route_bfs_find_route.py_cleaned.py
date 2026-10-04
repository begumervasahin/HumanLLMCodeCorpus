import romania
import sys
class class1:
    def fonk1(self):
        b1 = sys.argv[1]
        b2 = sys.argv[2]
        b3 = sys.argv[3]
        graph, b4 = romania.Romania().get_data(b1)
        b5 = [False] * b4
        b6 = []
        for i in range(b4):
            if not b5[i]:
                self.fonk2(graph, b2, b5, b6)
        b7 = [float("Inf")] * b4
        b7[list(graph.keys()).index(b2)] = 0.0
        b8 = [None] * b4
        b9 = [None] * b4
        b10 = [0] * b4
        a1 = 0
        while b6:
            b11 = b6.pop()
            for b14, distance in graph[b11]:
                b12 = list(graph.keys()).index(b14)
                b13 = b7[list(graph.keys()).index(b11)] + float(distance)
                if b7[b12] > b13:
                    b7[b12] = b13
                    b8[b12] = b11
                    b9[b12] = b14
                    b10[b12] = float(distance)
                    if b14 = = b3:
                        a1 = b13
        b15 = self.fonk3(b8, b9, b10, b2, b3, a1)
        self.fonk4(b15, a1)
    def fonk2(self, graph, b2, b5, b6):
        b16 = list(graph.keys()).index(b2)
        b5[b16] = True
        for b14, _ in graph[b2]:
            b12 = list(graph.keys()).index(b14)
            if not b5[b12]:
                self.fonk2(graph, b14, b5, b6)
        b6.append(b2)
    def fonk3(self, b8, b9, b10, b2, b3, a1):
        b15 = []
        b17 = a1
        b18 = list(b9).index(b3)
        while b17 != 0:
            b15.append(b8[b18])
            b15.append(b9[b18])
            b15.append(str(b10[b18]))
            b17 = b7[b18] - b10[b18]
            b3 = b8[b18]
            b18 = list(b9).index(b3)
        b15.reverse()
        return b15
    def fonk4(self, b15, a1):
        if a1 = = 0:
            print("distance: infinity\nroute:\nnone\n")
        else:
            print(f"distance: {a1} km\nroute:")
            for i in range(0, len(b15), 3):
                print(f"{b15[i]} to {b15[i + 1]}, {b15[i + 2]} km")
def fonk5():
    b19 = class1()
    b19.fonk1()
if b20 = = "__main__":
    fonk5()