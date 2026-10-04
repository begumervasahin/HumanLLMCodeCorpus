def print_pretty():
    headers = ["Vertex 1", "Vertex 2", "Distance", "Cumulative Distance"]
    separator = "*" * 80
    print(separator)
    print(f"{headers[0].ljust(15)}\t{headers[1].ljust(15)}\t{headers[2].ljust(10)}\t{headers[3].ljust(15)}")
    print(separator)
    cumulative_distance = 0
    for vertex1, vertex2, distance in MST:
        cumulative_distance += distance
        print(f"{vertex1.ljust(15)}\t{vertex2.ljust(15)}\t{str(distance).ljust(10)}\t{str(cumulative_distance).ljust(15)}")
