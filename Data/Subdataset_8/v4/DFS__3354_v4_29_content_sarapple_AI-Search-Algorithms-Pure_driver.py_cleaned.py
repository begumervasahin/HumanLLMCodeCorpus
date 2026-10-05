import sys
import math
from puzzle_state import PuzzleState
from algorithms import Algorithms
from utilities import Utilities
from reporter import Reporter
def main():
    if len(sys.argv) != 3:
        print("Usage: python script_name.py <search_method> <begin_state>")
        return
    search_method = sys.argv[1].lower()
    begin_state_values = sys.argv[2].split(",")
    begin_state = tuple(map(int, begin_state_values))
    size = int(math.sqrt(len(begin_state)))
    hard_state = PuzzleState(begin_state, size)
    search_args = {
        "client_defined_expand": Utilities.expand,
        "client_defined_goal_state_check": Utilities.goal_state_check,
        "client_defined_hashed_state": Utilities.hashed_state,
        "client_defined_compute_state_cost": Utilities.compute_state_cost,
        "start_state_hash": search_method,
        "start_state": hard_state,
    }
    if search_method in ["bfs", "dfs", "ast"]:
        result = Algorithms.search_wrapper(**search_args, search_type=search_method)
        Reporter.write_output(file_name="output.txt", **result)
    else:
        print("Invalid search method! Available options: bfs, dfs, ast")
if __name__ == '__main__':
    main()