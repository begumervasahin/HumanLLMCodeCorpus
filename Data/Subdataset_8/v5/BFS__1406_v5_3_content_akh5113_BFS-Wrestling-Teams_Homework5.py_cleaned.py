
import collections
def read_wrestlers(file_name):
    wrestlers = {}
    with open(file_name, "r") as f:
        lines = f.readlines()
        num_players = int(lines[0])
        num_rivalries = int(lines[num_players + 1])
        for line in lines[num_players + 2:]:
            wrestler1, wrestler2 = line.strip().split()
            wrestlers.setdefault(wrestler1, []).append(wrestler2)
            wrestlers.setdefault(wrestler2, []).append(wrestler1)
    return wrestlers
def breadth_first_search(graph, source):
    checked = []
    queue = [source]
    depth = {source: 0}
    visited = [source]
    while queue:
        vertex = queue.pop(0)
        checked.append(vertex)
        if depth[vertex] % 2 == 0:
            baby_faces.append(vertex)
        else:
            heel.append(vertex)
        neighbors = graph[vertex]
        for neighbor in neighbors:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.append(neighbor)
                depth[neighbor] = depth[vertex] + 1
    return checked
file_name = "wrestler2.txt"
adj_list = read_wrestlers(file_name)
key = next(iter(adj_list))
checked = breadth_first_search(adj_list, key)
for key in adj_list:
    if key not in checked:
        key2 = next(iter(adj_list))
        checked2 = breadth_first_search(adj_list, key2)
        checked += checked2
baby_faces = []
heel = []
for key in adj_list:
    if key in checked:
        if checked.index(key) % 2 == 0:
            baby_faces.append(key)
        else:
            heel.append(key)
num_baby_faces = len(baby_faces)
num_heel = len(heel)
if num_baby_faces == num_heel:
    print("Yes, possible")
    print("Baby Faces:", baby_faces)
    print("Heels:", heel)
else:
    print("Not possible")