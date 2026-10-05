class World_State:
    def __init__(self, _state, _operate, _parent, _depth, _f_value):
        self.state = _state
        self.operator = _operate
        self.parent = _parent
        self.depth = _depth
        self.f_value = _f_value
    def __eq__(self, other):
        return self.state == other.state
    def __lt__(self, other):
        return self.f_value < other.f_value
if __name__ == "__main__":
    example_state = World_State("example_state", "example_operator", None, 0, 0)
    print("State:", example_state.state)
    print("Operator:", example_state.operator)
    print("Parent:", example_state.parent)
    print("Depth:", example_state.depth)
    print("F Value:", example_state.f_value)