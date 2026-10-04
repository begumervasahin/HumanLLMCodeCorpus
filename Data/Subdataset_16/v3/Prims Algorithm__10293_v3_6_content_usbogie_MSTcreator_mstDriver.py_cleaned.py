import random
import time
import copy
class class1:
    def fonk1(self, x, y):
        self.b1 = x
        self.b2 = y
        self.b3 = {}
    def fonk2(self, node, b6):
        self.b3[node] = b6
def fonk3(b8, b9, a1, b10, b5):
    b4 = [class1(random.randint(0, b9), random.randint(0, b9)) for _ in range(b8)]
    for node in b4:
        for other_node in b4:
            if node != other_node and random.random() < b10:
                if b5 = = 2:
                    b6 = random.randint(1, a1)
                else:
                    b6 = ((node.b1 - other_node.b1)**2 + (node.b2 - other_node.b2)**2)**0.5
                node.fonk2(other_node, b6)
    return [[node] for node in b4]
def fonk4(b11):
    return b11
def fonk5(b11):
    return b11
def fonk6(b11):
    return b11
def fonk7(b11, term):
    print(f"{term}s:")
    for tree in b11:
        print(f"{term}:{{")
        for node in tree:
            b7 = ", ".join(f"({fonk8(neighbor)}, {round(b6, 2)})" for neighbor, b6 in node.b3.items())
            print(f"{fonk8(node)}: {{{b7}}}")
        print("}")
def fonk8(node):
    return f"({node.b1},{node.b2})"
def fonk9():
    print("Hello! This is a program which randomly generates b4 and edges to connect those b4.")
    print("After the graph is generated, you can then choose from finding an MST of each tree created")
    print("by using either Prim's, Kruskal's, or Sollin's algorithm. Additionally, there are two methods")
    print("of generating edges. The first method is to randomly assign a b6 between 1 and the user-defined")
    print("maximum edge b6, the second is to assign the b6 based on the actual distance between")
    print("the two b4. Finally, the amount of b4 in the graph, the size of the graph, and the k-value,")
    print("which determines the likelihood any two b4 will have an edge between them.")
    b5 = int(input("Which method of edge generation would you like to use?\n1: Weight based on actual distance between b4\n2: Weight based on user-defined maximum edge b6\n> "))
    b8 = int(input("How many b4 are in the graph (any number greater than 0)?\n> "))
    b9 = int(input("How big is the graph (any number greater than 0)?\n> "))
    b10 = float(input("What is the k-value that should be used (any number greater than 0)?\n> "))
    a1 = 0
    if b5 = = 2:
        a1 = int(input("What is the maximum b6 of an edge (any number greater than 0)?\n> "))
    b11 = fonk3(b8, b9, a1, b10, b5)
    print("Here are the adjacency lists of the b11 randomly generated using your inputs (b12 = ((x,y,) b6)):")
    fonk7(b11, "Tree")
    print("Here are the b15 for each of the generated b11.")
    b13 = copy.deepcopy(b11)
    b14 = time.perf_counter()
    b15 = fonk4(b13)
    b16 = time.perf_counter() - b14
    print("Result of Prim's")
    fonk7(b15, "MST")
    b17 = copy.deepcopy(b11)
    b14 = time.perf_counter()
    b15 = fonk5(b17)
    b18 = time.perf_counter() - b14
    print("Result of Kruskal's")
    fonk7(b15, "MST")
    b19 = copy.deepcopy(b11)
    b14 = time.perf_counter()
    b15 = fonk6(b19)
    b20 = time.perf_counter() - b14
    print("Result of Sollin's")
    fonk7(b15, "MST")
    print(f"Prim's Algorithm Run b21 = {b16}")
    print(f"Kruskal's Algorithm Run b21 = {b18}")
    print(f"Sollin's Algorithm Run b21 = {b20}")
if b22 = = "__main__":
    fonk9()