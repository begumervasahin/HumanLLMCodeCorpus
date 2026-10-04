class Edge:
    def __init__(self, vertex1, vertex2, weight, extra=0, selected=False):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight
        self.extra = extra
        self.selected = selected
    def __repr__(self):
        return (
            f"V1: {self.vertex1}  "
            f"V2: {self.vertex2}  "
            f"W: {self.weight}  "
            f"SEL: {self.selected}"
        )