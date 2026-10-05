
def Kruskals(edge_file_name,start_vertex = 0):
   G = Weighted_Graph(edge_file_name)
   F = ({G.vertex_set()}, [])
   for