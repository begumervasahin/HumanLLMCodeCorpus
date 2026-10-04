class Edge:
    def __init__(self, start, target, weight):
        self._start = start
        self._target = target
        self._weight = weight
    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, value):
        self._weight = value
    @property
    def start(self):
        return self._start
    @start.setter
    def start(self, value):
        self._start = value
    @property
    def target(self):
        return self._target
    @target.setter
    def target(self, value):
        self._target = value
if __name__ == "__main__":
    edge = Edge("A", "B", 5)
    print(f"Start: {edge.start}")
    print(f"Target: {edge.target}")
    print(f"Weight: {edge.weight}")
    edge.start = "C"
    edge.target = "D"
    edge.weight = 10
    print(f"Updated Start: {edge.start}")
    print(f"Updated Target: {edge.target}")
    print(f"Updated Weight: {edge.weight}")
