import copy
class Node:
    def __init__(self, id, x, y, adjList):
        self.id = id
        self.x = x
        self.y = y
        self.adjList = adjList
def runPrims(trees):
    MSTs = list()
    for tree in trees:
        MSTs.append(runPrimsOnTree(tree))
    return MSTs
def runPrimsOnTree(tree):
    mstNodes = list()
    treeToMst = dict()
    mstToTree = dict()
    for node in tree:
        m = copy.copy(node)
        m.adjList = {}
        treeToMst[node] = m
        mstToTree[m] = node
    first = treeToMst[list(tree.keys())[0]]
    mstNodes.append(first)
    done = False
    while not done:
        if len(mstNodes) == len(tree):
            done = True
        else:
            mstNodes.append(getNextNode(mstNodes, tree, treeToMst, mstToTree))
    return mstNodes
def getNextNode(mstNodes, tree, treeToMst, mstToTree):
    lowestNode = Node(0, 0, 0, {})
    lowestWeight = -1
    parent = Node(0, 0, 0, {})
    treeChild = Node(0, 0, 0, {})
    for node in mstNodes:
        treeNode = mstToTree[node]
        for child, weight in treeNode.adjList.items():
            if (weight < lowestWeight or lowestWeight == -1) and treeToMst[child] not in mstNodes:
                lowestWeight = weight
                lowestNode = treeToMst[child]
                treeChild = child
                parent = node
    treeParent = mstToTree[parent]
    del treeParent.adjList[treeChild]
    del treeChild.adjList[treeParent]
    parent.adjList[lowestNode] = lowestWeight
    lowestNode.adjList[parent] = lowestWeight
    return lowestNode
if __name__ == "__main__":
    tree1 = {
        Node(1, 0, 0, {Node(2, 0, 0, {}): 5, Node(3, 0, 0, {}): 6}),
        Node(2, 0, 0, {Node(1, 0, 0, {}): 5, Node(3, 0, 0, {}): 1}),
        Node(3, 0, 0, {Node(1, 0, 0, {}): 6, Node(2, 0, 0, {}): 1})
    }
    tree2 = {
        Node(1, 0, 0, {Node(2, 0, 0, {}): 4, Node(3, 0, 0, {}): 1}),
        Node(2, 0, 0, {Node(1, 0, 0, {}): 4, Node(3, 0, 0, {}): 2}),
        Node(3, 0, 0, {Node(1, 0, 0, {}): 1, Node(2, 0, 0, {}): 2})
    }
    trees = [tree1, tree2]
    msts = runPrims(trees)
    for mst in msts:
        print("Minimum Spanning Tree:")
        for node in mst:
            print("Node:", node.id, "Adjacent Nodes:", [(adj_node.id, weight) for adj_node, weight in node.adjList.items()])