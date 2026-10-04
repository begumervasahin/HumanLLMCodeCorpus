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
    edge = Edge("A", "B", 5)
    print("Start:", edge.get_start())
    print("Target:", edge.get_target())
    print("Weight:", edge.get_weight())
    edge.set_start("C")
    edge.set_target("D")
    edge.set_weight(10)
    print("Updated Start:", edge.get_start())
    print("Updated Target:", edge.get_target())
    print("Updated Weight:", edge.get_weight())
