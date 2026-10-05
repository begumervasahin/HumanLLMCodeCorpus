class State:
    def __init__(self, board=None, move=None, came_from=None, state=None):
        if state is None:
            self.board = board
            self.move = move
            self.came_from = came_from
        else:
            self.board = state.board
            self.move = state.move
            self.came_from = state.came_from
    def __hash__(self):
        return hash(tuple(self.board))
    def __eq__(self, other):
        return self.board == other.board
class HeuristicState(State):
    def __init__(self, board=None, move=None, came_from=None, state=None):
        super().__init__(board, move, came_from) if state is None else super().__init__(state=state)
        self.h_cost = 0
        self.g_cost = 0
    def __lt__(self, other):
        return self.f_cost < other.f_cost
    @property
    def f_cost(self):
        return self.h_cost + self.g_cost