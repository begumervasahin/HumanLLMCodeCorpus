
import collections
def read_input_file(file_name):
    adj_list = {}
    with open(file_name, "r") as f:
        lines = f.readlines()
        num_players = int(lines[0])
        num_rivals = int(lines[num_players + 1])
        for count, line in enumerate(lines):
            if count > num_players + 2 and count <= num_players + 2 + num_rivals:
                wrestler1, wrestler2 = line.strip().split()
                adj_list.setdefault(wrestler1, []).append(wrestler2)
                adj_list.setdefault(wrestler2, []).append(wrestler1)
    return adj_list, num_players, num_rivals
def bfs(graph, source, baby_faces, heels):
    done_checking = []
    queue = collections.deque([source])
    depth = {source: 0}
    visited = {source}
    while queue:
        vertex = queue.popleft()
        done_checking.append(vertex)
        if depth[vertex] % 2 == 0:
            baby_faces.append(vertex)
        else:
            heels.append(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                depth[neighbor] = depth[vertex] + 1
    return done_checking
def main(file_name):
    adj_list, num_players, num_rivals = read_input_file(file_name)
    baby_faces = []
    heels = []
    first_key = list(adj_list.keys())[0]
    checked = bfs(adj_list, first_key, baby_faces, heels)
    for key in adj_list:
        if key not in checked:
            checked += bfs(adj_list, key, baby_faces, heels)
    num_baby_faces = len(baby_faces)
    num_heels = len(heels)
    if num_baby_faces == num_heels:
        print("Yes, possible")
        print("Baby Faces:", baby_faces)
        print("Heels:", heels)
    else:
        print("Not possible")
if __name__ == "__main__":
    file_name = "wrestler2.txt"
    main(file_name)