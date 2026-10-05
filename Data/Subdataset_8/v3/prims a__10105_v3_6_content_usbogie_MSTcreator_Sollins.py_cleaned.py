import copy
class Node:
    def __init__(self, id, x, y, adjList):
        self.id = id
        self.x = x
        self.y = y
        self.adjList = adjList
def runSollins(trees):
    minimumSpanningTrees = []
    for tree in trees:
        minimumSpanningTrees.append(findMinimumSpanningTree(tree))
    return minimumSpanningTrees
def findMinimumSpanningTree(tree):
    subtrees = []
    treeToMST = {}
    MSTToTree = {}
    for node in tree:
        tempTree = []
        copiedNode = copy.copy(node)
        copiedNode.adjList = {}
        treeToMST[node] = copiedNode
        MSTToTree[copiedNode] = node
        tempTree.append(copiedNode)
        subtrees.append(tempTree)
    while len(subtrees) != 1:
        subtrees = mergeSubtrees(subtrees, tree, treeToMST, MSTToTree)
    return subtrees.pop(0)
def mergeSubtrees(subtrees, tree, treeToMST, MSTToTree):
    for subtree in subtrees:
        child = Node(0, 0, 0, {})
        lowestWeight = -1
        parent = Node(0, 0, 0, {})
        for node in subtree:
            treeNode = MSTToTree[node]
            for neighbor in treeNode.adjList:
                tempNode = treeToMST[neighbor]
                if tempNode not in subtree and (treeNode.adjList[neighbor] < lowestWeight or lowestWeight == -1):
                    lowestWeight = treeNode.adjList[neighbor]
                    child = tempNode
                    parent = node
        combineSubtrees(subtrees, subtree, parent, child, lowestWeight)
    return subtrees
def combineSubtrees(subtrees, subtree, parent, child, lowestWeight):
    childSubtree = []
    for sub in subtrees:
        if child in sub:
            childSubtree = sub
    parent.adjList[child] = lowestWeight
    child.adjList[parent] = lowestWeight
    for node in subtree:
        childSubtree.append(node)
    subtrees.remove(subtree)
    return subtrees
if __name__ == "__main__":
    tree1 = [Node(1, 0, 0, {2: 10, 3: 15}), Node(2, 0, 0, {1: 10, 3: 5}), Node(3, 0, 0, {1: 15, 2: 5})]
    tree2 = [Node(1, 0, 0, {2: 8, 3: 9}), Node(2, 0, 0, {1: 8, 3: 7}), Node(3, 0, 0, {1: 9, 2: 7})]
    msts = runSollins([tree1, tree2])
    for idx, mst in enumerate(msts):
        print(f"MST {idx+1}: {[(node.id, node.adjList) for node in mst]}")