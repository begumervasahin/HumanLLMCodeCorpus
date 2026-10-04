import sys
class node(object):
    def __init__ (self, index):
        self.children = []
        self.index = index
        self.discovered = False
    def addChild(self, index):
        self.children.append(index)
class graph(object):
    def __init__ (self, head, nodes):
        self.head = head
        self.nodes = nodes
def read_file(path):
    head = 0
    nodes = []
    with open(path, "r") as file:
        head = int(file.readline())
        index = -1
        node_i = None
        for edge in file.readlines():
            split1 = int(edge.split(',')[0])
            split2 = int(edge.split(',')[1])
            if(index == split1):
                node_i.addChild(split2)
            else:
                if(index != -1):
                    nodes.append(node_i)
                index = split1;
                node_i = node(split1)
                node_i.addChild(split2)
        nodes.append(node_i)
    return graph(head, nodes)