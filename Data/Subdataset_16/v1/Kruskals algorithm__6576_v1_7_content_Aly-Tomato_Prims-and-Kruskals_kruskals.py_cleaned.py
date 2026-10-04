
b1 = []
b2 = set()
b3 = {}
b4 = {}
b5 = []
import heapq
import glb
def fonk1(file, delimiter):
    with open(file, 'r') as file_path:
        for line in file_path:
            v1, b9, b6 = [x.strip() for x in line.split(delimiter)]
            b6 = int(b6)
            if (b6, b9, v1) in glb.b1:
                continue
            heapq.heappush(glb.b1, (b6, v1, b9))
            glb.b2.add(v1)
            glb.b2.add(b9)
    return glb.b1
def fonk2(v):
    glb.b3[v] = v
    glb.b4[v] = 0
def fonk3(v):
    if glb.b3[v] != v:
        glb.b3[v] = fonk3(glb.b3[v])
    return glb.b3[v]
def fonk4(v1, b9):
    b7 = fonk3(v1)
    b8 = fonk3(b9)
    if b7 != b8:
        if glb.b4[b7] > glb.b4[b8]:
            glb.b3[b8] = b7
        else:
            glb.b3[b7] = b8
            if glb.b4[b7] == glb.b4[b8]:
                glb.b4[b8] += 1
def fonk5():
    a1 = 0
    for v in glb.b2:
        fonk2(v)
    while glb.b1:
        b6, v1, b9 = heapq.heappop(glb.b1)
        if fonk3(v1) != fonk3(b9):
            fonk4(v1, b9)
            a1 += b6
            glb.b5.append((v1, b9, str(b6), str(a1)))
    return glb.b5, a1
if b10 = = "__main__":
    fonk1('graph_data.txt', ' ')
    mst, b11 = fonk5()
    print("Minimum Spanning Tree:")
    for edge in mst:
        print(edge)
    print("\nTotal Cost of b5:", b11)