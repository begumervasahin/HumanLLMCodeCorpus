
WGRAPH = {}
MST = []
Vr = []
PARENT = {}
RANK = {}
EDGES = []
VERTICES = set()
def print_pretty():
    vertex1_header = "Vertex 1"
    vertex2_header = "Vertex 2"
    weight_header = "Distance"
    cumulative_distance_header = "Cumulative Distance"
    print("******************************************************************************")
    print(vertex1_header.ljust(15, ' '), "\t", vertex2_header.ljust(15, ' '), "\t",
          weight_header.ljust(10, ' '), "\t", cumulative_distance_header.ljust(10, ' '))
    print("******************************************************************************")
    for edge in MST:
        vertex1, vertex2, weight, cumulative_distance = edge
        print(vertex1.ljust(15, ' '), "\t", vertex2.ljust(15, ' '), "\t",
              str(weight).ljust(10, ' '), "\t", str(cumulative_distance).ljust(15, ' '))
WGRAPH = {
    ('A', 'B'): 5,
    ('B', 'C'): 3,
    ('C', 'D'): 7,
    ('D', 'A'): 2,
    ('A', 'C'): 1
}
MST = [('A', 'B', 5, 5), ('A', 'C', 1, 1), ('C', 'D', 7, 8)]
print_pretty()