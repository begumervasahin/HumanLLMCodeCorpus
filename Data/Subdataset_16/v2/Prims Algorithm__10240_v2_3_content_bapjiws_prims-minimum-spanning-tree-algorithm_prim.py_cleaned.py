import heapq
import time
import argparse
def fonk1(filename):
    with open(filename, 'r') as file:
        b1 = [list(map(float, line.split())) for line in file.readlines()]
    return b1
def fonk2(b1):
    b2 = int(min([b11[0] for b11 in b1[1:]] + [b11[1] for b11 in b1[1:]]))
    b3 = int(max([b11[0] for b11 in b1[1:]] + [b11[1] for b11 in b1[1:]]))
    b4 = {k: [(b11[2], b11[0], b11[1]) for b11 in b1[1:] if b11[0] == k or b11[1] == k] for k in range(b2, b3 + 1)}
    return b4
def fonk3(b1):
    b5 = set([b11[0] for b11 in b1[1:]] + [b11[1] for b11 in b1[1:]])
    while True:
        try:
            b6 = int(input("Source node: "))
            if b6 in b5:
                return b6
            else:
                print("No such node, please try again.")
        except ValueError:
            print("Invalid input, please enter a valid node.")
def fonk4(b4, b6, b17):
    b7 = []
    b8 = set()
    b8.add(float(b6))
    b9 = []
    b10 = []
    while len(b8) < b17:
        for item in b4[b6]:
            heapq.heappush(b9, item)
        while True:
            weight, u, b11 = heapq.heappop(b9)
            if (u in b8) != (b11 in b8):
                break
        b4[u].remove((weight, u, b11))
        b4[b11].remove((weight, u, b11))
        b12 = b11 if u in b8 else u
        b8.add(b12)
        b6 = b12
        b10.append((u, b11, weight))
        b7.append(weight)
    return sum(b7), b10
def fonk5():
    b13 = time.process_time()
    b14 = argparse.ArgumentParser(description="Implements Prim's minimum spanning tree algorithm.")
    b14.add_argument("-s", b15 = "Display the structure of the MST", action="store_true")
    b14.add_argument("-t", b15 = "Display execution time", action="store_true")
    b14.add_argument("filename", b15 = "Path to the input file")
    b16 = b14.parse_args()
    b1 = fonk1(b16.filename)
    b17 = int(b1[0][0])
    b4 = fonk2(b1)
    b18 = fonk3(b1)
    mst_cost, b10 = fonk4(b4, b18, b17)
    print(f"The overall cost of the MST: {mst_cost}")
    if b16.s:
        print(f"The structure of the MST: {b10}")
    if b16.t:
        print(f"--- {time.process_time() - b13} seconds ---")
if b19 = = "__main__":
    fonk5()