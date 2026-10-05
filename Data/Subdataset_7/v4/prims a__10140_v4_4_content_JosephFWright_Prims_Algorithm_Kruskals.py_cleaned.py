
def fonk1(edge_file_name, b1 = 0):
    b2 = Weighted_Graph(edge_file_name)
    b3 = ({b2.vertex_set()}, [])
    while not fonk2(b3):
        b4 = fonk3(b2, b3)
        fonk4(b3, b4)
    return b3
def fonk2(b3):
    pass
def fonk3(b2, b3):
    pass
def fonk4(b3, edge):
    pass