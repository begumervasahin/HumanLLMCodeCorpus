68. Repository: elados93/AI_Ex1
   File: PuzzleState.py
   URL: https:
   Code Content:
class State(object):
    def __init__(self, board=None, move=None, came_from=None, state=None):
        if state is None:
            self._board = board
            self._move = move
            self.came_from = came_from
        else:
            self._board = state.board
            self._move = state.move
            self.came_from = state.came_from
    def __copy__(self):
        import copy
        copy_board = copy.copy(self._board)
        return State(board=copy_board,move=self._move, came_from=self.came_from)
    def __hash__(self):
        return hash(self._board)
    @property
    def board(self):
        return self._board
    @property
    def move(self):
        return self._move
    def __eq__(self, other):
        return self._board == other.board
class HeuristicState(State):
    def __init__(self, board=None, move=None, came_from=None, state=None):
        if state is None:
            State.__init__(self, board, move, came_from)
        else:
            State.__init__(self,state=state)
        self.h_cost = 0
        self.g_cost = 0
    def __lt__(self, other):
        return self.f_cost < other.f_cost
    @property
    def f_cost(self):
        return self.h_cost + self.g_cost
   README Content:
"Tile Puzzle" solver using I-DFS, BFS and A* algorithms.
Running main.py looking for a file "input.txt".
The input will be:
first line: algorithm: 1 : I-DFS, 2 : BFS, 3 : A*
second line: grid length, (rows and cols are equals)
third line: the grid seperated by '-' e.g: 1-2-3-4-5-6-7-0-8
the output file will be one line contains the operations (L, R, U, D) as the solution,
number of developed nodes and the cost of the solution.
