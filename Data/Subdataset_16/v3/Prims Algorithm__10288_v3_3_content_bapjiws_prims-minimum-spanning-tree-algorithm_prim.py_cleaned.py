import heapq
import time
import argparse
def fonk1(filename):
    with open(filename, 'r') as file:
        b1 = [list(map(float, line.split())) for line in file.readlines()]
    return b1
def fonk2(b1):
    b2 = [(b9[2], b9[0], b9[1]) for b9 in b1[1:]]
    b3 = set(b9[0] for b9 in b1[1:]) | set(b9[1] for b9 in b1[1:])
    b4 = {b9: [] for b9 in b3}
    for weight, u, b9 in b2:
        b4[u].append((weight, u, b9))
        b4[b9].append((weight, u, b9))
    return b4
def fonk3(valid_nodes):
    while True:
        try:
            b5 = int(input("Source node: "))
            if b5 in valid_nodes:
                return b5
            else:
                print("No such node, please try again.")
        except ValueError:
            print("Invalid input, please enter a valid node.")
def fonk4(b4, b5, b15):
    b6 = []
    b3 = {b5}
    b7 = []
    b8 = []
    while len(b3) < b15:
        for item in b4[b5]:
            heapq.heappush(b7, item)
        while True:
            weight, u, b9 = heapq.heappop(b7)
            if (u in b3) != (b9 in b3):
                break
        b10 = b9 if u in b3 else u
        b3.add(b10)
        b5 = b10
        b8.append((u, b9, weight))
        b6.append(weight)
    return sum(b6), b8
def fonk5():
    b11 = time.process_time()
    b12 = argparse.ArgumentParser(description="Implements Prim's minimum spanning tree algorithm.")
    b12.add_argument("-s", b13 = "Display the structure of the MST", action="store_true")
    b12.add_argument("-t", b13 = "Display execution time", action="store_true")
    b12.add_argument("filename", b13 = "Path to the input file")
    b14 = b12.parse_args()
    b1 = fonk1(b14.filename)
    b15 = int(b1[0][0])
    b4 = fonk2(b1)
    b16 = fonk3(b4.keys())
    mst_cost, b8 = fonk4(b4, b16, b15)
    print(f"The overall cost of the MST: {mst_cost}")
    if b14.s:
        print(f"The structure of the MST: {b8}")
    if b14.t:
        print(f"--- {time.process_time() - b11} seconds ---")
if b17 = = "__main__":
    fonk5()