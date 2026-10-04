
b1 = {}
b2 = []
b3 = []
b4 = {}
b5 = {}
b6 = []
b7 = set()
def fonk1():
    b8 = "Vertex 1"
    b9 = "Vertex 2"
    b10 = "Distance"
    b11 = "Cumulative Distance"
    print("******************************************************************************")
    print(f"{b8.ljust(15)}\t{b9.ljust(15)}\t{b10.ljust(10)}\t{b11.ljust(15)}")
    print("******************************************************************************")
    for edge in b2:
        vertex1, vertex2, distance, b12 = edge
        print(f"{vertex1.ljust(15)}\t{vertex2.ljust(15)}\t{str(distance).ljust(10)}\t{str(b12).ljust(15)}")
