import copy
class Node:
    def __init__(self, id, x, y, adjList):
        self.id = id
        self.x = x
        self.y = y
        self.adjList = adjList
def runSollins(trees):
    MSTs = []
    for tree in trees:
        MSTs.append(runSollinsOnTree(tree))
    return MSTs
def runSollinsOnTree(tree):
    subtrees = []
    treeToMst = {}
    mstToTree = {}
    for n in tree:
        t = []
        m = copy.copy(n)
        m.adjList = {}
        treeToMst[n] = m
        mstToTree[m] = n
        t.append(m)
        subtrees.append(t)
    while len(subtrees) != 1:
        subtrees = runPhase(subtrees, tree, treeToMst, mstToTree)
    return subtrees.pop(0)
def runPhase(subtrees, tree, treeToMst, mstToTree):
    for subtree in subtrees:
        child = Node(0, 0, 0, {})
        lowestWeight = -1
        parent = Node(0, 0, 0, {})
        for n in subtree:
            treeNode = mstToTree[n]
            for p in treeNode.adjList:
                temp = treeToMst[p]
                if temp not in subtree and (treeNode.adjList[p] < lowestWeight or lowestWeight == -1):
                    lowestWeight = treeNode.adjList[p]
                    child = temp
                    parent = n
        combineComponents(subtrees, subtree, parent, child, lowestWeight)
    return subtrees
def combineComponents(subtrees, subtree, parent, child, lowestWeight):
    childSubtree = []
    for sub in subtrees:
        if child in sub:
            childSubtree = sub
    parent.adjList[child] = lowestWeight
    child.adjList[parent] = lowestWeight
    for y in subtree:
        childSubtree.append(y)
    subtrees.remove(subtree)
    return subtrees
if __name__ == "__main__":
    tree1 = [Node(1, 0, 0, {2: 10, 3: 15}), Node(2, 0, 0, {1: 10, 3: 5}), Node(3, 0, 0, {1: 15, 2: 5})]
    tree2 = [Node(1, 0, 0, {2: 8, 3: 9}), Node(2, 0, 0, {1: 8, 3: 7}), Node(3, 0, 0, {1: 9, 2: 7})]
    msts = runSollins([tree1, tree2])
    for idx, mst in enumerate(msts):
        print(f"MST {idx+1}: {[(node.id, node.adjList) for node in mst]}")