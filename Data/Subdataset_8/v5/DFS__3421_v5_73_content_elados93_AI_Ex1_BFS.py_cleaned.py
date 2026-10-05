from TilePuzzleLogic import backtracking
class BFS_Search:
    def __init__(self, logic):
        self.logic = logic
    def search(self, initial_state):
        open_list = [initial_state]
        states_visited = 0
        while open_list:
            current_state = open_list.pop(0)
            states_visited += 1
            if self.logic.is_goal_state(current_state):
                path = backtracking(current_state)
                return path, str(states_visited), '0'
            children = self.logic.next_states(current_state)
            open_list.extend(children)
        raise Exception('Puzzle is not solvable!')
if __name__ == "__main__":
    bfs_search = BFS_Search(logic)
    initial_state = ...
    path, states_visited, _ = bfs_search.search(initial_state)
    print("Path:", path)
    print("Number of states visited:", states_visited)