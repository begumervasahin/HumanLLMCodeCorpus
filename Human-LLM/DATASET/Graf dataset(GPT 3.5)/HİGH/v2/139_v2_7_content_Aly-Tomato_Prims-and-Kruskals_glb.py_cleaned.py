
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
    print(b8.ljust(15, ' '), "\t", b9.ljust(15, ' '), "\t",
          b10.ljust(10, ' '), "\t", b11.ljust(10, ' '))
    print("******************************************************************************")
    for edge in b2:
        vertex1, vertex2, weight, b12 = edge
        print(vertex1.ljust(15, ' '), "\t", vertex2.ljust(15, ' '), "\t",
              str(weight).ljust(10, ' '), "\t", str(b12).ljust(15, ' '))
b1 = {
    ('A', 'B'): 5,
    ('B', 'C'): 3,
    ('C', 'D'): 7,
    ('D', 'A'): 2,
    ('A', 'C'): 1
}
b2 = [('A', 'B', 5, 5), ('A', 'C', 1, 1), ('C', 'D', 7, 8)]
fonk1()