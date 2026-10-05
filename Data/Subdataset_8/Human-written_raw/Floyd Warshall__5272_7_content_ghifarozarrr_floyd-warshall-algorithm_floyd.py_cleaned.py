import numpy as np
def floyd(graph, node, nextt):
    for k in range(node):
        for i in range(node):
            for j in range(node):
                if graph[i][j] > (graph[i][k] + graph[k][j]):
                    graph[i][j] = graph[i][k] + graph[k][j]
                    nextt[i][j] = nextt[i][k]
    return graph
def path(nextt, source, destination):
   path = [source]
   while source != destination:
       source = nextt[source][destination]
       path.append(source)
   return path
def main():
    node = int(input("N node : "))
    dist_list, nextt = 0, 0
    dist_list = np.zeros(shape=(node,node),dtype=np.int)
    nextt = np.zeros(shape=(node,node),dtype=np.int)
    for i in range(node):
        for j in range(node):
            c = input("Distance from node %d to node %d: " %(i,j))
            if i == j:
                c = 0
            if c == "-":
                c = 9999
            else:
                c = int(c)
            dist_list[i][j] = c
            nextt[i][j] = j
    print("\nIteration 0\n",dist_list)
    new_dist = floyd(dist_list, node, nextt)
    print("\n")
    for i in range(node):
        for j in range(node):
            if i < j:
                print ("Node",i,"and node",j,"are connected through nodes = ",
                           path(nextt, i, j),", total distance =", new_dist[i][j])
main()