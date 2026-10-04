def fonk1():
    b1 = ["Vertex 1", "Vertex 2", "Distance", "Cumulative Distance"]
    b2 = "*" * 80
    print(b2)
    print(f"{b1[0].ljust(15)}\t{b1[1].ljust(15)}\t{b1[2].ljust(10)}\t{b1[3].ljust(15)}")
    print(b2)
    a1 = 0
    for vertex1, vertex2, distance in MST:
        a1 += distance
        print(f"{vertex1.ljust(15)}\t{vertex2.ljust(15)}\t{str(distance).ljust(10)}\t{str(a1).ljust(15)}")
