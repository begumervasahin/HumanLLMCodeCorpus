from TilePuzzleLogic import backtracking
class BFS_Search:
    def __init__(self, logic):
        self._logic = logic
    def search(self, init_state):
        open_list = []
        count = 0
        open_list.append(init_state)
        while len(open_list):
            current = open_list.pop(0)
            count += 1
            if self._logic.is_goal_state(current):
                return backtracking(current), str(count), '0'
            children = self._logic.next_states(current)
            for child in children:
                open_list.append(child)
        raise Exception('Puzzle is not solvable!')
if __name__ == "__main__":
    bfs_search = BFS_Search(logic)
    initial_state = ...
    path, states_visited, _ = bfs_search.search(initial_state)
    print("Path:", path)
    print("Number of states visited:", states_visited)