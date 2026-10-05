from Graph import Graph
def fonk1():
    b1 = Graph.graphreader("graph1.txt")
    b2 = b1.get_node_by_label(1)
    b3 = b1.linkState(b2)
    for element in sorted(b3):
        print("Path from " + str(b2) + " to Node " + str(element) +
              " : Length :" + str(b3[element][0]) + ". Preceding : " + str(b3[element][1]))
        print("From Node: Cost")
        cost, b4 = b3[element]
        print(element, '       :', cost, '(', b4, ')')
def fonk2():
    b1 = Graph.graphreader("simplegraph2.txt")
    b2 = b1.get_node_by_label(14)
    b3 = b1.linkState(b2)
    for element in b3:
        print("Path from " + str(b2) + "  to Node " + str(element) +
              ". Length :" + str(b3[element][0]) + ". Preceding : " + str(b3[element][1]))
        print("From Node: Cost")
        cost, b4 = b3[element]
        print(element, '       :', cost, '(', b4, ')')
if b5 = = "__main__":
    fonk1()
    fonk2()