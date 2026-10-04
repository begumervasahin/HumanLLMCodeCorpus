
b1 = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5}
b2 = [[1, 2], [1, 3], [1, 4], [3, 4], [4, 5], [4, 6], [5, 6]]
b3 = [1, 2, 4, 3, 5, 2, 4]
b4 = float("b4")
b5 = [b4] * len(b1)
b6 = [0] * len(b1)
b5[0] = 0
for i in range(len(b1) - 1):
    print("\nIteration:", i + 1)
    print("Resulting Table:")
    for e in range(len(b2)):
        b7 = b1[b2[e][0]]
        b8 = b1[b2[e][1]]
        b9 = b3[e]
        if b5[b7] + b9 < b5[b8]:
            b5[b8] = b5[b7] + b9
            b6[b8] = b2[e][0]
            print("Edge:", b2[e])
            print("Vertices:", b1)
            print("Distances (cost):", b5)
            print("Previous:", b6)
def fonk1(destination):
    if b6[b1[destination]] != 0:
        fonk1(b6[b1[destination]])
    print(destination, b10 = " ")
print("\nList of b1 that make up the shortest path with the least cost:")
fonk1(6)
print()