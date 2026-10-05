class WorldState:
    def __init__(self, state, operator, parent=None, depth=0, f_value=0.0):
        self.state = state
        self.operator = operator
        self.parent = parent
        self.depth = depth
        self.f_value = f_value
    def __eq__(self, other):
        return self.state == other.state
    def __lt__(self, other):
        return self.f_value < other.f_value
if __name__ == "__main__":
    example_state = WorldState("example_state", "example_operator")
    print("State:", example_state.state)
    print("Operator:", example_state.operator)
    print("Parent:", example_state.parent)
    print("Depth:", example_state.depth)
    print("F Value:", example_state.f_value)