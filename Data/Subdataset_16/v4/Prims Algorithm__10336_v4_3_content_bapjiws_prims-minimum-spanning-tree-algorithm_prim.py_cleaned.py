import heapq
import operator
import time
import argparse
def fonk1(filename):
    with open(filename, 'r') as file:
        b1 = [list(map(float, line.split())) for line in file.readlines()]
    return b1
def fonk2(b1):
    b2 = int(min([v[0] for v in b1[1:]] + [v[1] for v in b1[1:]]))
    b3 = int(max([v[0] for v in b1[1:]] + [v[1] for v in b1[1:]]))
    b4 = {k: [(v[2], v[0], v[1]) for v in b1[1:] if v[0] == k or v[1] == k] for k in range(b2, b3 + 1)}
    return b4
def fonk3(b1):
    while True:
        try:
            b5 = int(input("Source node: "))
            if b5 in [v[0] for v in b1[1:]] + [v[1] for v in b1[1:]]:
                return b5
            else:
                print("No such node, please try again")
        except ValueError:
            print("Invalid input, please enter an integer")
def fonk4(b4, b5, b16):
    b6 = []
    b7 = set()
    b8 = b5
    b7.add(float(b8))
    b9 = []
    b10 = []
    while len(b7) < b16:
        for item in b4[b8]:
            heapq.heappush(b9, item)
        while b9:
            b11 = heapq.heappop(b9)
            if operator.xor(b11[1] in b7, b11[2] in b7):
                break
        else:
            break
        b4[b11[1]].remove(b11)
        b4[b11[2]].remove(b11)
        b8 = b11[1] if b11[1] not in b7 else b11[2]
        b7.add(b8)
        b10.append((b11[1], b11[2], b11[0]))
        b6.append(b11[0])
    return sum(b6), b10
def fonk5():
    b12 = time.process_time()
    b13 = argparse.ArgumentParser(description="Implements Prim's minimum spanning tree algorithm.")
    b13.add_argument("-s", b14 = "the structure of the MST", action="store_true")
    b13.add_argument("-t", b14 = "execution time", action="store_true")
    b13.add_argument("filename", b14 = ".txt file to parse")
    b15 = b13.parse_args()
    b1 = fonk1(b15.filename)
    b16 = int(b1[0][0])
    b4 = fonk2(b1)
    b5 = fonk3(b1)
    total_cost, b10 = fonk4(b4, b5, b16)
    print(f"The overall cost of the MST: {total_cost}")
    if b15.s:
        print(f"The structure of the MST: {b10}")
    if b15.t:
        print(f"--- {time.process_time() - b12} seconds ---")
if b17 = = "__main__":
    fonk5()