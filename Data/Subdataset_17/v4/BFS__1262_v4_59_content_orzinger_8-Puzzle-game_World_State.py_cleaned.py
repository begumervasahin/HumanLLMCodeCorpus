class WorldState:
    def __init__(self, state, operator, parent, depth, f_value):
        self.state = state
        self.operator = operator
        self.parent = parent
        self.depth = depth
        self.f_value = f_value
    def __eq__(self, other):
        return self.state == other.state
    def __lt__(self, other):
        return self.f_value < other.f_value