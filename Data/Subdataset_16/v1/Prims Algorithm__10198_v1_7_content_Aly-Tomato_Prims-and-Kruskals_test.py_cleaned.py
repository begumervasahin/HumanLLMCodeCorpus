import prims
import kruskals
import glb
import sys
def fonk1(b14, b15, b1):
    if b1 = = 'k':
        glb.b2 = kruskals.read_graph(b14, b15)
        b3 = glb.VERTICES
    elif b1 = = 'b13':
        glb.b2 = prims.read_graph(b14, b15)
        b3 = glb.b2.b3()
    else:
        fonk4()
    a1 = 3
    b4 = len(b3)
    if b4 != a1:
        print("ERROR:\t read_graph() returned wrong amount of b3")
        print(f"Expected:  {a1}")
        print(f"Responded: {b4}")
        return False
    if b1 = = 'b13':
        for k in b3:
            if k in glb.b2[k]:
                print("ERROR:\t b5 neighbors have same values as b5")
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
        print("ERROR:\t get_min returns wrong min edge")
        print(f"Expected:  {b7}")
        print(f"Responded: {b8}")
        return False
def fonk3(b1):
    if b1 = = 'k':
        b9 = 'kruskals'
        b8, b10 = kruskals.kruskals()
    elif b1 = = 'b13':
        b9 = 'prims'
        glb.b6.clear()
        b8, b10 = prims.prims()
    else:
        fonk4()
    b7 = [('a', 'b', '1', '1'), ('a', 'c', '2', '3')]
    a2 = 4
    if b7 = = b8:
        b11 = True
    else:
        print(f"ERROR:\t {b9}.{b9} returned unexpected MST")
        print(f"Expected:  {b7}")
        print(f"Responded: {b8}")
        b11 = False
    if b10 = = a2:
        b12 = True
    else:
        print(f"ERROR:\t {b9}.{b9} returned incorrect cumulative distance")
        print(f"Expected:  {a2}")
        print(f"Responded: {b10}")
        b12 = False
    return b11 and b12
def fonk4():
    print("USAGE: test.py [b1] where b13 = prims , k = kruskals")
    print("$ test.py k")
    sys.exit()
def fonk5():
    b14 = "sample_data.txt"
    b15 = ' '
    if len(sys.argv) < 2:
        fonk4()
    b1 = sys.argv[1]
    if b1 = = 'b13':
        print("....TESTING PRIMS....")
        if fonk1(b14, b15, b1):
            print("prims.read_graph() : PASS")
        else:
            print("prims.read_graph() : FAIL")
        if fonk2():
            print("prims.get_min() : PASS")
        else:
            print("prims.get_min() : FAIL")
        if fonk3(b1):
            print("prims.prims() : PASS")
        else:
            print("prims.prims() : FAIL")
    elif b1 = = 'k':
        print("....TESTING KRUSKALS....")
        if fonk1(b14, b15, b1):
            print("kruskals.read_graph() : PASS")
        else:
            print("kruskals.read_graph() : FAIL")
        if fonk3(b1):
            print("kruskals.kruskals() : PASS")
        else:
            print("kruskals.kruskals() : FAIL")
    else:
        fonk4()
if b16 = = "__main__":
    fonk5()