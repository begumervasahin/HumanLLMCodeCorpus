import sys
import kruskals
import prims
import glb
def fonk1():
    print("USAGE: main.py [\"b2.txt\"] [b4] where b1 = prims , k = kruskals")
    sys.exit()
def fonk2():
    if len(sys.argv) < 3:
        fonk1()
    b2 = sys.argv[1]
    b3 = ' '
    b4 = sys.argv[2]
    if(b4 = = 'b1'):
        prims.read_graph(b2, b3)
        graph,b5 = prims.prims()
        glb.print_pretty()
        print(f"Total Distance : {b5}")
    elif(b4 = = 'k'):
        kruskals.read_graph(b2, b3)
        graph,b5 = kruskals.kruskals()
        glb.print_pretty()
        print(f"Total Distance : {b5}")
    else:
        fonk1()
if b6 = = "__main__":
    fonk2()