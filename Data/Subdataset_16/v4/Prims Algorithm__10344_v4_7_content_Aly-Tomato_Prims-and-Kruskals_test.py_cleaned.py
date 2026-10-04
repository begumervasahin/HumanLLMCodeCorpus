import prims
import kruskals
import glb
import sys
def fonk1(b12, b13, b1):
    if b1 = = 'k':
        glb.b2 = kruskals.read_graph(b12, b13)
        b3 = glb.VERTICES
    elif b1 = = 'b11':
        glb.b2 = prims.read_graph(b12, b13)
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
    if b1 = = 'b11':
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
        b8, b9 = kruskals.kruskals()
        b10 = 'kruskals'
    elif b1 = = 'b11':
        glb.b6.clear()
        b8, b9 = prims.prims()
        b10 = 'prims'
    else:
        fonk4()
    b7 = [('a', 'b', '1', '1'), ('a', 'c', '2', '3')]
    a2 = 4
    if b7 = = b8 and a2 == b9:
        return True
    else:
        if b7 != b8:
            print(f"ERROR:\t {b10} returned unexpected MST")
            print(f"Expected:  {b7}")
            print(f"Responded: {b8}")
        if a2 != b9:
            print(f"ERROR:\t {b10} returned incorrect cumulative distance")
            print(f"Expected:  {a2}")
            print(f"Responded: {b9}")
        return False
def fonk4():
    print("USAGE: test.py [b1] where b11 = prims , k = kruskals")
    print("$ test.py k")
    sys.exit()
def fonk5():
    b12 = "sample_data.txt"
    b13 = ' '
    if len(sys.argv) < 2:
        fonk4()
    b1 = sys.argv[1]
    if b1 = = 'b11':
        print("....TESTING PRIMS....")
        if fonk1(b12, b13, b1):
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
        if fonk1(b12, b13, b1):
            print("kruskals.read_graph() : PASS")
        else:
            print("kruskals.read_graph() : FAIL")
        if fonk3(b1):
            print("kruskals.kruskals() : PASS")
        else:
            print("kruskals.kruskals() : FAIL")
    else:
        fonk4()
if b14 = = "__main__":
    fonk5()