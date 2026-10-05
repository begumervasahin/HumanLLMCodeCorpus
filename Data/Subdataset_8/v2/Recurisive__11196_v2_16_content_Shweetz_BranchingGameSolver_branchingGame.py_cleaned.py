import copy
table_1 = [[[2, 3], [1, 4]], [[4, 5], [6, 0]]]
try_to_maximize_1 = True
table_2 = copy.deepcopy(table_1)
try_to_maximize_2 = False
depth = 3
turn = 1
path_list = []
def init():
    path = ""
    for i in range(depth):
        path += " "
    return path
def search(table, try_to_maximize, current_turn, path):
    for i in range(len(table)):
        path = path[:current_turn - 1] + str(i + 1) + path[current_turn:]
        print("Turn " + str(current_turn) + ", Path: " + str(path) + ", Computing " + str(table[i]))
        if isinstance(table[i], int) is False:
            table[i] = search(table[i], not try_to_maximize, current_turn + 1, path)
    if try_to_maximize:
        result = max(table)
        action = "max"
    else:
        result = min(table)
        action = "min"
    path = path[:current_turn - 1] + str(table.index(result) + 1) + path[current_turn:]
    path_entry = (path, result)
    path_list.append(path_entry)
    print("Turn " + str(current_turn) + ", Path: " + path + ", " + action + " of " + str(table) + " is " + str(result))
    return result
def find_path(path_list, result, string, index):
    if index < depth - 1:
        next_steps = [x for x, y in path_list if result == y and " " != x[index] and " " == x[index + 1]]
    else:
        next_steps = [x for x, y in path_list if result == y and " " != x[index]]
    string += next_steps[0][index]
    if len(string) == depth:
        return string
    else:
        return find_path(path_list, result, string, index + 1)
print("Game Table: " + str(table_1) + "\n")
print("1st Player wants to maximize")
current_path = init()
result = search(table_1, try_to_maximize_1, turn, current_path)
current_path = find_path(path_list, result, "", 0)
print("Score: " + str(result) + " (if the 1st Player wants to maximize), Path: " + current_path + "\n")
print("1st Player wants to minimize")
current_path = init()
result = search(table_2, try_to_maximize_2, turn, current_path)
current_path = find_path(path_list, result, "", 0)
print("Score: " + str(result) + " (if the 1st Player wants to minimize), Path: " + current_path)