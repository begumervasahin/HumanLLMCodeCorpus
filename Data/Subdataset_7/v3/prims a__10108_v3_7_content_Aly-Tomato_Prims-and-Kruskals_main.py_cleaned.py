import sys
import kruskals
import prims
import glb
def fonk1():
    print("USAGE: main.py [\"file.txt\"] [algo] where b1 = prims, k = kruskals")
    sys.exit()
def fonk2(file, b5, b2):
    if b2 = = 'b1':
        prims.read_graph(file, b5)
        graph, b3 = prims.prims()
    elif b2 = = 'k':
        kruskals.read_graph(file, b5)
        graph, b3 = kruskals.kruskals()
    else:
        fonk1()
    glb.print_pretty()
    print(f"Total Distance: {b3}")
def fonk3():
    if len(sys.argv) < 3:
        fonk1()
    b4 = sys.argv[1]
    b5 = ' '
    b2 = sys.argv[2]
    fonk2(b4, b5, b2)
if b6 = = "__main__":
    fonk3()