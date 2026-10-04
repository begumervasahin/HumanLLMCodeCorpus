class State:
    def __init__(self, state, parent=None, move=None, depth=0, cost=0, key=None):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost
        self.key = key
        self.map = self._create_map(state)
    def _create_map(self, state):
        return ''.join(str(e) for e in state) if state else ''
    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        return self.map == other.map
    def __lt__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        return self.map < other.map