
b1 = {}
b2 = []
b3 = []
b4 = {}
b5 = {}
b6 = []
b7 = set()
def fonk1():
    b8 = {
        "Vertex 1": 15,
        "Vertex 2": 15,
        "Distance": 10,
        "Cumulative Distance": 10
    }
    print("******************************************************************************")
    for header, width in b8.items():
        print(header.ljust(width, ' '), b9 = '\t')
    print("\n******************************************************************************")
    for edge in b2:
        vertex1, vertex2, weight, b10 = edge
        print(vertex1.ljust(b8["Vertex 1"], ' '), b9 = '\t')
        print(vertex2.ljust(b8["Vertex 2"], ' '), b9 = '\t')
        print(str(weight).ljust(b8["Distance"], ' '), b9 = '\t')
        print(str(b10).ljust(b8["Cumulative Distance"], ' '))
b1 = {
    ('A', 'B'): 5,
    ('B', 'C'): 3,
    ('C', 'D'): 7,
    ('D', 'A'): 2,
    ('A', 'C'): 1
}
b2 = [('A', 'B', 5, 5), ('A', 'C', 1, 1), ('C', 'D', 7, 8)]
fonk1()