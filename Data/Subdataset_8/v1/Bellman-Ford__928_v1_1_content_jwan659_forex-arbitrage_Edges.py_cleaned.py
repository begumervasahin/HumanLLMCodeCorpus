class Edge:
    def __init__(self, start, target, weight):
        self.start = start
        self.target = target
        self.weight = weight
    def get_weight(self):
        return self.weight
    def set_weight(self, weight):
        self.weight = weight
    def get_start(self):
        return self.start
    def set_start(self, start):
        self.start = start
    def get_target(self):
        return self.target
    def set_target(self, target):
        self.target = target
if __name__ == "__main__":
    edge1 = Edge('A', 'B', 10)
    edge2 = Edge('B', 'C', 5)
    print("Start vertex of edge1:", edge1.get_start())
    print("Target vertex of edge1:", edge1.get_target())
    print("Weight of edge1:", edge1.get_weight())
    edge1.set_weight(15)
    print("Updated weight of edge1:", edge1.get_weight())
    edge1.set_start('X')
    print("Updated start vertex of edge1:", edge1.get_start())
    edge1.set_target('Y')
    print("Updated target vertex of edge1:", edge1.get_target())