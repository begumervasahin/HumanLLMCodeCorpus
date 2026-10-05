
WGRAPH = {}
MST = []
Vr = []
PARENT = {}
RANK = {}
EDGES = []
VERTICES = set()
def print_pretty():
    headers = {
        "Vertex 1": 15,
        "Vertex 2": 15,
        "Distance": 10,
        "Cumulative Distance": 10
    }
    print("******************************************************************************")
    for header, width in headers.items():
        print(header.ljust(width, ' '), end='\t')
    print("\n******************************************************************************")
    for edge in MST:
        vertex1, vertex2, weight, cumulative_distance = edge
        print(vertex1.ljust(headers["Vertex 1"], ' '), end='\t')
        print(vertex2.ljust(headers["Vertex 2"], ' '), end='\t')
        print(str(weight).ljust(headers["Distance"], ' '), end='\t')
        print(str(cumulative_distance).ljust(headers["Cumulative Distance"], ' '))
WGRAPH = {
    ('A', 'B'): 5,
    ('B', 'C'): 3,
    ('C', 'D'): 7,
    ('D', 'A'): 2,
    ('A', 'C'): 1
}
MST = [('A', 'B', 5, 5), ('A', 'C', 1, 1), ('C', 'D', 7, 8)]
print_pretty()