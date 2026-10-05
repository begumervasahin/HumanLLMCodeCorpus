import copy
initial_table = [[[2, 3], [1, 4]], [[4, 5], [6, 0]]]
try_to_max_player1 = True
try_to_max_player2 = False
depth = 3
turn = 1
path_list = []
def init_path():
    return " " * depth
def search_recursive(table, try_to_max, current_turn, current_path):
    for i, sub_table in enumerate(table):
        if isinstance(sub_table, list):
            current_path = current_path[:current_turn - 1] + str(i + 1) + current_path[current_turn:]
            print(f"turn {current_turn}, path: {current_path}, computing {sub_table}")
            table[i] = search_recursive(sub_table, not try_to_max, current_turn + 1, current_path)
    if try_to_max:
        result = max(table)
        action = "max"
    else:
        result = min(table)
        action = "min"
    current_path = current_path[:current_turn - 1] + str(table.index(result) + 1) + current_path[current_turn:]
    current_tuple = (current_path, result)
    path_list.append(current_tuple)
    print(f"turn {current_turn}, path: {current_path}, {action} of {table} is {result}")
    return result
def find_path(path_list, result, current_str, i):
    if i < depth - 1:
        valid_paths = [path for path, value in path_list if result == value and " " != path[i] and " " == path[i + 1]]
    else:
        valid_paths = [path for path, value in path_list if result == value and " " != path[i]]
    current_str += valid_paths[0][i]
    if len(current_str) == depth:
        return current_str
    else:
        return find_path(path_list, result, current_str, i + 1)
print(f"Game table: {initial_table}\n")
print("1st player wants to maximize")
path = init_path()
result = search_recursive(initial_table, try_to_max_player1, turn, path)
path = find_path(path_list, result, "", 0)
print(f"Score: {result} (if the 1st player wants to maximize), path: {path}\n")
print("1st player wants to minimize")
path = init_path()
result = search_recursive(copy.deepcopy(initial_table), try_to_max_player2, turn, path)
path = find_path(path_list, result, "", 0)
print(f"Score: {result} (if the 1st player wants to minimize), path: {path}")