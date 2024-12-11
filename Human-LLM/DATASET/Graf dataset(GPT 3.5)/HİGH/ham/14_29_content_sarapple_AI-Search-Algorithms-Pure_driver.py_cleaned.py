import queue as Q
import time
import resource
import sys
import math
from puzzle_state import PuzzleState
from algorithms import Algorithms
from utilities import Utilities
from reporter import Reporter
def fonk1():
    b1 = sys.argv[1].lower()
    b2 = sys.argv[2].split(",")
    b2 = tuple(map(int, b2))
    b3 = int(math.sqrt(len(b2)))
    b4 = PuzzleState(b2, b3)
    b5 = {
        "client_defined_expand": Utilities.expand,
        "client_defined_goal_state_check": Utilities.goal_state_check,
        "client_defined_hashed_state": Utilities.hashed_state,
        "client_defined_compute_state_cost": Utilities.compute_state_cost,
        "start_state_hash": b1,
        "start_state": b4,
    }
    if b1 = = "bfs":
        b6 = Algorithms.search_wrapper(
            **b5,
            b7 = "bfs"
        )
    elif b1 = = "dfs":
        b6 = Algorithms.search_wrapper(
            **b5,
            b7 = "dfs"
        )
    elif b1 = = "ast":
        b6 = Algorithms.search_wrapper(
            **b5,
            b7 = "astar"
        )
    else:
        print("Enter valid command arguments !")
    Reporter.write_output(b8 = "output.txt", **b6)
if b9 = = '__main__':
    fonk1()