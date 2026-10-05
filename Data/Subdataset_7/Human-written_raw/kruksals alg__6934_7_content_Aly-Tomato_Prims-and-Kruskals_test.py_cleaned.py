import prims
import kruskals
import glb
import sys
def test_read (b11, b12, b1):
    if(b1 = = 'k'):
        glb.b2 = kruskals.read_graph(b11, b12)
        b3 = glb.VERTICES
    elif(b1 = = 'b10'):
        glb.b2 = prims.read_graph(b11, b12)
        b3 = glb.b2.b3()
    else:
        fonk3()
    a1 = 3
    b4 = len(b3)
    if(b4 != a1):
        print("ERROR:\t read_graph() returned wrong amount of b3")
        print(f"Expected:  {a1}")
        print(f"Responded: {b4}")
        return False
    if(b1 = = 'b10'):
        for k in b3:
            if k in glb.b2[k]:
                print("ERROR:\t b5 neighbors have same values as b5")
                print(f"Expected:  b5 = {k}, graph[b5] != b5")
                print(f"Responded: {glb.b2[k]}")
                return False
    return True
def fonk1():
    glb.b6 = ['a']
    b7 = ('a','b','1')
    b8 = prims.get_min()
    if b7 = = b8:
        return True
    else:
        print("ERROR:\t get_min returns wrong min edge")
        print(f"Expected:  {b7}")
        print(f"Responded: {b8}")
        return False
def fonk2(b1):
    if(b1 = = 'k'):
        b1 = 'kruskals'
        b8,b9 = kruskals.kruskals()
    if(b1 = = 'b10'):
        b1 = 'prims'
        glb.b6.clear()
        b8,b9 = prims.prims()
    b7 = [('a', 'b', '1', '1'), ('a', 'c', '2', '3')]
    a2 = 4
    if(b7 = = b8):
        return True
    else:
        print(f"ERROR:\t {b1}.{b1} returned unexpected MST")
        print(f"Expected:  {b7}")
        print(f"Responded: {b8}")
    if(b9 = = a2):
        return True
    else:
        print(f"ERROR:\t {b1}.{b1} returned incorrect cumulative distance")
        print(f"Expected:  {a2}")
        print(f"Responded: {b9}")
def fonk3():
    print("USAGE: test.py [b1] where b10 = prims , k = kruskals")
    print("$ test.py k")
    sys.exit()
def fonk4():
   b11 = "sample_data.txt"
   b12 = ' '
   if(len(sys.argv) < 2):
       fonk3()
   b1 = sys.argv[1]
   if(b1 = = 'b10'):
       print("....TESTING PRIMS....")
       if test_read(b11,b12,b1):
           print("prims.read_graph() : PASS")
       else:
           print("prims.read_graph() : FAIL")
       if fonk1():
           print("prims.get_min() : PASS")
       else:
           print("prims.get_min() : FAIL")
       if fonk2(b1):
           print("prims.prims() : PASS")
       else:
           print("prims.prims() : FAIL")
   elif(b1 = = 'k'):
       print("....TESTING KRUSKALS....")
       if test_read(b11,b12,b1):
           print("kruskals.read_graph() : PASS")
       else:
           print("kruskals.read_graph() : FAIL")
       if fonk2(b1):
           print("kruskals.kruskals() : PASS")
       else:
           print("kruskals.kruskals() : FAIL")
   else:
       fonk3()
if b13 = = "__main__":
    fonk4()