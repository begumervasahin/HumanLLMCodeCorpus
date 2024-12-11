import sys
import math
from puzzle_state import PuzzleState
from algorithms import Algorithms
from utilities import Utilities
from reporter import Reporter
def fonk1():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <b1> <b3>")
        return
    b1 = sys.argv[1].lower()
    b2 = sys.argv[2].split(",")
    b3 = tuple(map(int, b2))
    b4 = int(math.sqrt(len(b3)))
    b5 = PuzzleState(b3, b4)
    b6 = {
        "client_defined_expand": Utilities.expand,
        "client_defined_goal_state_check": Utilities.goal_state_check,
        "client_defined_hashed_state": Utilities.hashed_state,
        "client_defined_compute_state_cost": Utilities.compute_state_cost,
        "start_state_hash": b1,
        "start_state": b5,
    }
    b7 = ""
    if b1 = = "bfs":
        b7 = "bfs"
    elif b1 = = "dfs":
        b7 = "dfs"
    elif b1 = = "ast":
        b7 = "astar"
    else:
        print("Invalid search method! Available options: bfs, dfs, ast")
        return
    b8 = Algorithms.search_wrapper(**b6, b7=b7)
    Reporter.write_output(b9 = "output.txt", **b8)
if b10 = = '__main__':
    fonk1()