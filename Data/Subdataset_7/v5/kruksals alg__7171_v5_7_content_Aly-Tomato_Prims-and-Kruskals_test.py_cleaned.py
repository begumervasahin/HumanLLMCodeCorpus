import prims
import kruskals
import glb
import sys
def fonk1(b11, b12, b1):
    if b1 = = 'k':
        glb.b2 = kruskals.read_graph(b11, b12)
        b3 = glb.VERTICES
    elif b1 = = 'b10':
        glb.b2 = prims.read_graph(b11, b12)
        b3 = glb.b2.b3()
    else:
        fonk4()
    a1 = 3
    b4 = len(b3)
    if b4 != a1:
        print("ERROR: read_graph() returned wrong amount of b3")
        print(f"Expected:  {a1}")
        print(f"Responded: {b4}")
        return False
    if b1 = = 'b10':
        for k in b3:
            if k in glb.b2[k]:
                print("ERROR: b5 neighbors have same values as b5")
                print(f"Expected:  b5 = {k}, graph[b5] != b5")
                print(f"Responded: {glb.b2[k]}")
                return False
    return True
def fonk2():
    glb.b6 = ['a']
    b7 = ('a', 'b', '1')
    b8 = prims.get_min()
    if b7 = = b8:
        return True
    else:
        print("ERROR: get_min returns wrong min edge")
        print(f"Expected:  {b7}")
        print(f"Responded: {b8}")
        return False
def fonk3(b1):
    if b1 = = 'k':
        b1 = 'kruskals'
        b8, b9 = kruskals.kruskals()
    elif b1 = = 'b10':
        b1 = 'prims'
        glb.b6.clear()
        b8, b9 = prims.prims()
    b7 = [('a', 'b', '1', '1'), ('a', 'c', '2', '3')]
    a2 = 4
    if b7 = = b8:
        return True
    else:
        print(f"ERROR: {b1}.{b1} returned unexpected MST")
        print(f"Expected:  {b7}")
        print(f"Responded: {b8}")
    if b9 = = a2:
        return True
    else:
        print(f"ERROR: {b1}.{b1} returned incorrect cumulative distance")
        print(f"Expected:  {a2}")
        print(f"Responded: {b9}")
def fonk4():
    print("USAGE: test.py [b1] where b10 = prims, k = kruskals")
    print("$ test.py k")
    sys.exit()
def fonk5():
    b11 = "sample_data.txt"
    b12 = ' '
    if len(sys.argv) < 2:
        fonk4()
    b1 = sys.argv[1]
    if b1 = = 'b10':
        print("....TESTING PRIMS....")
    elif b1 = = 'k':
        print("....TESTING KRUSKALS....")
    else:
        fonk4()
    if fonk1(b11, b12, b1):
        print(f"{b1}.read_graph() : PASS")
    else:
        print(f"{b1}.read_graph() : FAIL")
    if b1 = = 'b10':
        if fonk2():
            print("prims.get_min() : PASS")
        else:
            print("prims.get_min() : FAIL")
    if fonk3(b1):
        print(f"{b1}.{b1}() : PASS")
    else:
        print(f"{b1}.{b1}() : FAIL")
if b13 = = "__main__":
    fonk5()