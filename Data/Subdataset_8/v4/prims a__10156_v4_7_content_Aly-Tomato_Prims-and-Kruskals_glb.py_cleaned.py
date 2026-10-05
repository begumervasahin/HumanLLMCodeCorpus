
WGRAPH = {}
MST = []
Vr = []
PARENT = {}
RANK = {}
EDGES = []
VERTICES = set()
def print_pretty():
    t1 = "Vertex 1"
    t2 = "Vertex 2"
    tw = "Distance"
    cd = "Cumulative Distance"
    print("******************************************************************************")
    print(t1.ljust(15, ' '), "\t", t2.ljust(15, ' '), "\t", tw.ljust(10, ' '), "\t", cd.ljust(10, ' '))
    print("******************************************************************************")
    for m in MST:
        v1, v2, w, c = m
        print(v1.ljust(15, ' '), "\t", v2.ljust(15, ' '), "\t", w.ljust(10, ' '), "\t", c.ljust(15, ' '))