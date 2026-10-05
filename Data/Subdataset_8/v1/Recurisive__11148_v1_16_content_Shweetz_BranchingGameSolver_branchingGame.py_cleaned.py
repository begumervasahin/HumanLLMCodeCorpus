import copy
tab1 = [[[2, 3], [1, 4]], [[4, 5], [6, 0]]]
tryToMax1 = True
tab2 = copy.deepcopy(tab1)
tryToMax2 = False
depth = 3
turn = 1
pathList = []
def init():
    path = ""
    for i in range(depth):
        path += " "
    return path
def search(tab, tryToMax, turn, path):
    for i in range(len(tab)):
        if isinstance(tab[i], int) is False:
            path = path[:turn - 1] + str(i + 1) + path[turn:]
            print("turn " + str(turn) + ", path: " + str(path) + ", computing " + str(tab[i]))
            tab[i] = search(tab[i], not tryToMax, turn + 1, path)
    if tryToMax:
        res = max(tab)
        action = "max"
    else:
        res = min(tab)
        action = "min"
    path = path[:turn - 1] + str(tab.index(res) + 1) + path[turn:]
    t = (path, res)
    pathList.append(t)
    print("turn " + str(turn) + ", path: " + path + ", " + action + " of " + str(tab) + " is " + str(res))
    return res
def findPath(pathList, res, string, i):
    if i < depth - 1:
        x = [x for x, y in pathList if res == y and " " != x[i] and " " == x[i + 1]]
    else:
        x = [x for x, y in pathList if res == y and " " != x[i]]
    string += x[0][i]
    if len(string) == depth:
        return string
    else:
        return findPath(pathList, res, string, i + 1)
    return "error"
print("Game table: " + str(tab1) + "\n")
print("1st player wants to maximize")
path = init()
res = search(tab1, tryToMax1, turn, path)
path = findPath(pathList, res, "", 0)
print("Score: " + str(res) + " (if the 1st player wants to maximize), path: " + path + "\n")
print("1st player wants to minimize")
path = init()
res = search(tab2, tryToMax2, turn, path)
path = findPath(pathList, res, "", 0)
print("Score: " + str(res) + " (if the 1st player wants to minimize), path: " + path)