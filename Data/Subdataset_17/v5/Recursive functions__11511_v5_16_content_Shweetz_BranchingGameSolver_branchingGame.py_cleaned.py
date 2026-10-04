import copy
tab1 = [[[2, 3], [1, 4]], [[4, 5], [6, 0]]]
tab2 = copy.deepcopy(tab1)
DEPTH = 3
TURN = 1
path_list = []
def init_path():
    return " " * DEPTH
def search(tab, try_to_max, turn, path):
    for i in range(len(tab)):
        if not isinstance(tab[i], int):
            new_path = path[:turn - 1] + str(i + 1) + path[turn:]
            print(f"Turn {turn}, path: {new_path}, computing {tab[i]}")
            tab[i] = search(tab[i], not try_to_max, turn + 1, new_path)
    if try_to_max:
        res = max(tab)
        action = "max"
    else:
        res = min(tab)
        action = "min"
    final_path = path[:turn - 1] + str(tab.index(res) + 1) + path[turn:]
    path_list.append((final_path, res))
    print(f"Turn {turn}, path: {final_path}, {action} of {tab} is {res}")
    return res
def find_path(path_list, res, current_path, i):
    if i < DEPTH - 1:
        candidates = [x for x, y in path_list if res == y and x[i] != " " and x[i + 1] == " "]
    else:
        candidates = [x for x, y in path_list if res == y and x[i] != " "]
    current_path += candidates[0][i]
    if len(current_path) == DEPTH:
        return current_path
    else:
        return find_path(path_list, res, current_path, i + 1)
def main():
    print("Game table:", tab1, "\n")
    print("1st player wants to maximize")
    path = init_path()
    res = search(tab1, True, TURN, path)
    optimal_path = find_path(path_list, res, "", 0)
    print(f"Score: {res} (if the 1st player wants to maximize), path: {optimal_path}\n")
    path_list.clear()
    print("1st player wants to minimize")
    path = init_path()
    res = search(tab2, False, TURN, path)
    optimal_path = find_path(path_list, res, "", 0)
    print(f"Score: {res} (if the 1st player wants to minimize), path: {optimal_path}")
if __name__ == "__main__":
    main()