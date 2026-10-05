class World_State:
    def __init__(self, _state, _operator, _parent, _depth, _f_value):
        self.state = _state
        self.operator = _operator
        self.parent = _parent
        self.depth = _depth
        self.f_value = _f_value
    def __eq__(self, other):
        return self.state == other.state
    def __lt__(self, other):
        return self.f_value < other.f_value