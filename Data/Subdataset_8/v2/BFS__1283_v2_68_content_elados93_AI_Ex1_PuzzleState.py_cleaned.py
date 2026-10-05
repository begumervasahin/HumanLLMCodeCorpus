class State:
    def __init__(self, board=None, move=None, came_from=None, state=None):
        if state is None:
            self._board = board
            self._move = move
            self.came_from = came_from
        else:
            self._board = state.board
            self._move = state.move
            self.came_from = state.came_from
    def __hash__(self):
        return hash(self._board)
    def __eq__(self, other):
        return self._board == other.board
    @property
    def board(self):
        return self._board
    @property
    def move(self):
        return self._move
class HeuristicState(State):
    def __init__(self, board=None, move=None, came_from=None, state=None):
        if state is None:
            super().__init__(board, move, came_from)
        else:
            super().__init__(state=state)
        self.h_cost = 0
        self.g_cost = 0
    def __lt__(self, other):
        return self.f_cost < other.f_cost
    @property
    def f_cost(self):
        return self.h_cost + self.g_cost
if __name__ == "__main__":
    example_state = State(board=[[1, 2, 3], [4, 5, 6], [7, 0, 8]], move=None, came_from=None)
    print("Board:", example_state.board)
    print("Move:", example_state.move)
    print("Came From:", example_state.came_from)