import random
import time
import copy
class class1:
    def fonk1(self, x, y):
        self.b1 = x
        self.b2 = y
        self.b3 = {}
    def fonk2(self, node, b7):
        self.b3[node] = b7
def fonk3(b10, b11, a1, b12, b9):
    b4 = [class1(random.randint(0, b11), random.randint(0, b11)) for _ in range(b10)]
    b5 = []
    for node in b4:
        b6 = []
        for other_node in b4:
            if node != other_node and random.random() < b12:
                b7 = random.randint(1, a1) if b9 == 2 else ((node.b1 - other_node.b1)**2 + (node.b2 - other_node.b2)**2)**0.5
                node.fonk2(other_node, b7)
        b6.append(node)
        b5.append(b6)
    return b5
def fonk4(b5):
    return b5
def fonk5(b5):
    return b5
def fonk6(b5):
    return b5
def fonk7(b5, term):
    print(f"{term}s:")
    for t in b5:
        print(f"{term}:{{")
        for x in t:
            print(f"{fonk8(x)}: {{", b8 = "")
            for y in x.b3:
                print(f"({fonk8(y)}, {round(x.b3[y], 2)})", b8 = " ")
            print("}")
        print("}")
def fonk8(n):
    return f"({n.b1},{n.b2})"
def fonk9():
    print("Hello! This is a program which randomly generates b4 and edges to connect those b4.")
    print("After the graph is generated, you can then choose from finding an MST of each b6 created")
    print("by using either Prim's, Kruskal's, or Sollin's algorithm. Additionally, there are two methods")
    print("of generating edges. The first method is to randomly assign a b7 between 1 and the user-defined")
    print("maximum edge b7, the second is to assign the b7 based on the actual distance between")
    print("the two b4. Finally, the amount of b4 in the graph, the size of the graph, and the k-value,")
    print("which determines the likelihood any two b4 will have an edge between them.")
    print("Which method of edge generation would you like to use?")
    print("1: Weight based on actual distance between b4")
    print("2: Weight based on user-defined maximum edge b7")
    b9 = int(input('> '))
    print("How many b4 are in the graph (any number greater than 0)?")
    b10 = int(input('> '))
    print("How big is the graph (any number greater than 0)?")
    b11 = int(input('> '))
    print("What is the k-value that should be used (any number greater than 0)?")
    b12 = int(input('> '))
    a1 = 0
    if b9 = = 2:
        print("What is the maximum b7 of an edge (any number greater than 0)?")
        a1 = int(input('> '))
    b5 = fonk3(b10, b11, a1, b12, b9)
    print("Here are the adjacency lists of the b5 randomly generated using your inputs (b13 = ((x,y,) b7)):")
    fonk7(b5, "Tree")
    print("Here are the b16 for each of the generated b5.")
    b14 = copy.deepcopy(b5)
    b15 = time.perf_counter()
    b16 = fonk4(b14)
    b17 = (time.perf_counter() - b15)
    print("Result of Prim's")
    fonk7(b16, "MST")
    b18 = copy.deepcopy(b5)
    b15 = time.perf_counter()
    b16 = fonk5(b18)
    b19 = (time.perf_counter() - b15)
    print("Result of Kruskal's")
    fonk7(b16, "MST")
    b20 = copy.deepcopy(b5)
    b15 = time.perf_counter()
    b16 = fonk6(b20)
    b21 = (time.perf_counter() - b15)
    print("Result of Sollin's")
    fonk7(b16, "MST")
    print(f"Prim's Algorithm Run b22 = {b17}")
    print(f"Kruskal's Algorithm Run b22 = {b19}")
    print(f"Sollin's Algorithm Run b22 = {b21}")
fonk9()