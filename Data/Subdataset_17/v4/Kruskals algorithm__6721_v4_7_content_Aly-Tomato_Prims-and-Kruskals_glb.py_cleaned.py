
WGRAPH = {}
MST = []
Vr = []
PARENT = {}
RANK = {}
EDGES = []
VERTICES = set()
def print_pretty():
    header_v1 = "Vertex 1"
    header_v2 = "Vertex 2"
    header_distance = "Distance"
    header_cumulative = "Cumulative Distance"
    print("******************************************************************************")
    print(f"{header_v1.ljust(15)}\t{header_v2.ljust(15)}\t{header_distance.ljust(10)}\t{header_cumulative.ljust(15)}")
    print("******************************************************************************")
    for edge in MST:
        vertex1, vertex2, distance, cumulative_distance = edge
        print(f"{vertex1.ljust(15)}\t{vertex2.ljust(15)}\t{str(distance).ljust(10)}\t{str(cumulative_distance).ljust(15)}")
