import copy
initial_table = [[[2, 3], [1, 4]], [[4, 5], [6, 0]]]
try_to_maximize_player1 = True
try_to_maximize_player2 = False
depth = 3
path_score_list = []
def initialize_path():
    return " " * depth
def search_game_tree(table, try_to_maximize, current_turn, path):
    for i, subtree in enumerate(table):
        path = path[:current_turn - 1] + str(i + 1) + path[current_turn:]
        print(f"Turn {current_turn}, Path: {path}, Computing {subtree}")
        if isinstance(subtree, list):
            table[i] = search_game_tree(subtree, not try_to_maximize, current_turn + 1, path)
    if try_to_maximize:
        result = max(table)
        action = "max"
    else:
        result = min(table)
        action = "min"
    path = path[:current_turn - 1] + str(table.index(result) + 1) + path[current_turn:]
    path_score_list.append((path, result))
    print(f"Turn {current_turn}, Path: {path}, {action} of {table} is {result}")
    return result
def find_optimal_path(path_list, result, string, index):
    if index < depth - 1:
        next_steps = [path for path, score in path_list if result == score and " " != path[index] and " " == path[index + 1]]
    else:
        next_steps = [path for path, score in path_list if result == score and " " != path[index]]
    string += next_steps[0][index]
    if len(string) == depth:
        return string
    else:
        return find_optimal_path(path_list, result, string, index + 1)
print(f"Game Table: {initial_table}\n")
print("1st Player wants to maximize")
current_path = initialize_path()
result = search_game_tree(initial_table, try_to_maximize_player1, 1, current_path)
current_path = find_optimal_path(path_score_list, result, "", 0)
print(f"Score: {result} (if the 1st Player wants to maximize), Path: {current_path}\n")
print("1st Player wants to minimize")
current_path = initialize_path()
result = search_game_tree(copy.deepcopy(initial_table), try_to_maximize_player2, 1, current_path)
current_path = find_optimal_path(path_score_list, result, "", 0)
print(f"Score: {result} (if the 1st Player wants to minimize), Path: {current_path}")