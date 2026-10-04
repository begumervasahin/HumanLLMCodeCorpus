import prims
import kruskals
import glb
import sys
def fonk1(b15, b16, b1):
    if b1 = = 'k':
        glb.b2 = kruskals.read_graph(b15, b16)
        b3 = glb.VERTICES
    elif b1 = = 'b14':
        glb.b2 = prims.read_graph(b15, b16)
        b3 = glb.b2.b3()
    else:
        fonk4()
        return False
    a1 = 3
    b4 = len(b3)
    if b4 != a1:
        print("ERROR:\t read_graph() returned the wrong number of b3")
        print(f"Expected: {a1}")
        print(f"Responded: {b4}")
        return False
    if b1 = = 'b14':
        for key in b3:
            if key in glb.b2[key]:
                print("ERROR:\t b5 neighbors have the same values as b5")
                print(f"Expected: b5 = {key}, graph[b5] != b5")
                print(f"Responded: {glb.b2[key]}")
                return False
    return True
def fonk2():
    glb.b6 = ['a']
    b7 = ('a', 'b', '1')
    b8 = prims.get_min()
    if b7 = = b8:
        return True
    else:
        print("ERROR:\t get_min returns the wrong minimum edge")
        print(f"Expected: {b7}")
        print(f"Responded: {b8}")
        return False
def fonk3(b1):
    if b1 = = 'k':
        b9 = 'kruskals'
        b8, b10 = kruskals.kruskals()
    elif b1 = = 'b14':
        b9 = 'prims'
        glb.b6.clear()
        b8, b10 = prims.prims()
    else:
        fonk4()
        return False
    b11 = [('a', 'b', '1', '1'), ('a', 'c', '2', '3')]
    a2 = 4
    b12 = (b11 == b8)
    if not b12:
        print(f"ERROR:\t {b9}.{b9} returned an unexpected MST")
        print(f"Expected: {b11}")
        print(f"Responded: {b8}")
    b13 = (b10 == a2)
    if not b13:
        print(f"ERROR:\t {b9}.{b9} returned an incorrect cumulative distance")
        print(f"Expected: {a2}")
        print(f"Responded: {b10}")
    return b12 and b13
def fonk4():
    print("USAGE: test.py [b1] where b14 = prims, k = kruskals")
    print("$ test.py k")
    sys.exit()
def fonk5():
    b15 = "sample_data.txt"
    b16 = ' '
    if len(sys.argv) < 2:
        fonk4()
    b1 = sys.argv[1]
    if b1 = = 'b14':
        print("....TESTING PRIMS....")
        if fonk1(b15, b16, b1):
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
        if fonk1(b15, b16, b1):
            print("kruskals.read_graph() : PASS")
        else:
            print("kruskals.read_graph() : FAIL")
        if fonk3(b1):
            print("kruskals.kruskals() : PASS")
        else:
            print("kruskals.kruskals() : FAIL")
    else:
        fonk4()
if b17 = = "__main__":
    fonk5()