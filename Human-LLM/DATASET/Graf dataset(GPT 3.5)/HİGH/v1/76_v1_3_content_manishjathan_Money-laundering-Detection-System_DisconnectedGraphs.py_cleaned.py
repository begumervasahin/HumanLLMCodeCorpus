import drawGraph as dG
def fonk1(b8, b9, sourceNode):
    b1 = []
    b2 = [sourceNode]
    while b2:
        b3 = b2.pop()
        if b3 not in b1:
            b1.append(b3)
        if b3 in b9:
            for val in b9[b3]:
                b2.append(val)
    print("Vertices in Graph")
    b1.sort()
    print(b1)
    return b1
def fonk2(b10):
    print("Source Nodes")
    b4 = [k for k, v in b10.items() if v == 0]
    print(b4)
    return b4
def fonk3(b8, b9, b4):
    b5 = []
    for sourceNode in b4:
        b6 = fonk1(b8, b9, sourceNode)
        b7 = [edge for edge in b8 if edge[0] in b6 and edge[1] in b6]
        b5.append(b7)
    print("New Edge Lists after splitting")
    for i, b7 in enumerate(b5):
        print(b7)
        dG.drawGraph(b7, "Graph" + str(i) + ".png")
    return b5
b8 = [(1,2),(1,3),(2,3),(2,4),(3,4),(3,5),(3,6),(4,5),(4,6),(5,6),(7,8),(8,9),(8,10),(9,10)]
b9 = {1: [2, 3], 2: [3, 4], 3: [4, 5, 6], 4: [5, 6], 5: [6], 7: [8], 8: [9, 10], 9: [10]}
b10 = {1: 0, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 0, 8: 1, 9: 1, 10: 2}
b4 = fonk2(b10)
fonk3(b8, b9, b4)