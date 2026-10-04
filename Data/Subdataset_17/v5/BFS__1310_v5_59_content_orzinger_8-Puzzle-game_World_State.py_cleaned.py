class WorldState:
    def __init__(self, state, operator=None, parent=None, depth=0, f_value=0.0):
        self.state = state
        self.operator = operator
        self.parent = parent
        self.depth = depth
        self.f_value = f_value
    def __eq__(self, other):
        return self.state == other.state
    def __lt__(self, other):
        return self.f_value < other.f_value
    def __repr__(self):
        return f"WorldState(state={self.state}, operator={self.operator}, depth={self.depth}, f_value={self.f_value})"