
weighted_graph = {}
minimum_spanning_tree = []
visited_vertices = []
parent_vertices = {}
vertex_ranks = {}
edges = []
vertices = set()
def print_pretty():
    vertex_1_header = "Vertex 1"
    vertex_2_header = "Vertex 2"
    distance_header = "Distance"
    cumulative_distance_header = "Cumulative Distance"
    print("******************************************************************************")
    print(vertex_1_header.ljust(15, ' '), "\t", vertex_2_header.ljust(15, ' '), "\t",
          distance_header.ljust(10, ' '), "\t", cumulative_distance_header.ljust(10, ' '))
    print("******************************************************************************")
    for edge in minimum_spanning_tree:
        vertex1, vertex2, distance, cumulative_distance = edge
        print(vertex1.ljust(15, ' '), "\t", vertex2.ljust(15, ' '), "\t",
              distance.ljust(10, ' '), "\t", cumulative_distance.ljust(15, ' '))