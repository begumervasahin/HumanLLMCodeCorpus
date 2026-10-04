import copy
tab1 = [[[2, 3], [1, 4]], [[4, 5], [6, 0]]]
tab2 = copy.deepcopy(tab1)
depth = 3
initial_turn = 1
path_list = []
def init_path():
    return " " * depth
def search(tab, try_to_max, turn, path):
    for i in range(len(tab)):
        if not isinstance(tab[i], int):
            path = path[:turn - 1] + str(i + 1) + path[turn:]
            print(f"Turn {turn}, path: {path}, computing {tab[i]}")
            tab[i] = search(tab[i], not try_to_max, turn + 1, path)
    if try_to_max:
        res = max(tab)
        action = "max"
    else:
        res = min(tab)
        action = "min"
    path = path[:turn - 1] + str(tab.index(res) + 1) + path[turn:]
    path_list.append((path, res))
    print(f"Turn {turn}, path: {path}, {action} of {tab} is {res}")
    return res
def find_path(path_list, res, current_path, index):
    if index < depth - 1:
        candidates = [x for x, y in path_list if res == y and " " != x[index] and " " == x[index + 1]]
    else:
        candidates = [x for x, y in path_list if res == y and " " != x[index]]
    current_path += candidates[0][index]
    if len(current_path) == depth:
        return current_path
    return find_path(path_list, res, current_path, index + 1)
def main():
    global path_list
    print(f"Game table: {tab1}\n")
    print("1st player wants to maximize")
    path = init_path()
    res = search(tab1, True, initial_turn, path)
    optimal_path = find_path(path_list, res, "", 0)
    print(f"Score: {res} (if the 1st player wants to maximize), path: {optimal_path}\n")
    path_list = []
    print("1st player wants to minimize")
    path = init_path()
    res = search(tab2, False, initial_turn, path)
    optimal_path = find_path(path_list, res, "", 0)
    print(f"Score: {res} (if the 1st player wants to minimize), path: {optimal_path}")
if __name__ == '__main__':
    main()