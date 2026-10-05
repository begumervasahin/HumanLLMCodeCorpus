import Queue
cityList = []
adjList = {}
problem = None
currentSearchOption = 1
class Node:
    def __init__(self, state, parent, actions, path_cost):
        self.STATE = state
        self.PATH_COST = path_cost
        self.ACTIONS = actions
        self.PARENT = parent
def getGraphNode(state):
    for node in cityList:
        if node.STATE == state:
            return node
    return None
'''
    Common Method for BFS and DFS based on the imput given by the user the queue insertion and deletion would be different
'''
def read_graph():
    try:
        with open('input_data.txt', 'r') as flobj:
            inputData = flobj.read().split('\n')
            for i in inputData:
                data = i.split(',')
                nodes = []
                if len(data) < 2:
                    break
                node1 = getGraphNode(data[0])
                if node1 == None:
                    node1 = Node(data[0], None, 'Move to', 0)
                    cityList.append(node1)
                node2 = getGraphNode(data[1])
                if node2 == None:
                    node2 = Node(data[1], data[0], 'Move to', data[2])
                    cityList.append(node2)
                if data[0] in adjList:
                    nodes = adjList[node1.STATE]
                    nodes.append(node2)
                else:
                    nodes = [node2]
                    adjList[node1.STATE] = nodes
                if data[1] in adjList:
                    nodes = adjList[node2.STATE]
                    nodes.append(node1)
                else:
                    nodes = [node1]
                    adjList[node2.STATE] = nodes
    except Exception, e:
        print e
class Problem:
    def __init__(self, source, destination):
        self.Source = source
        self.Destination = destination
    def GoalTest(self, NodeState):
        return self.Destination == NodeState
    def ExpandNodes(self, action, state):
        childnodes = adjList[state]
        return childnodes
def POP(frontier):
    nodeState = frontier.get()
    node = getGraphNode(nodeState)
    return node
def getSolution(sList):
    solution = []
    key = problem.Destination
    solution.append(key)
    while key in sList.keys():
        key = sList[key]
        solution.append(key)
    solution.reverse()
    return solution
def checkQueue(frontier, nodeState):
    result = False
    if currentSearchOption == 1:
        newFrontier = Queue.Queue()
    else:
        newFrontier = Queue.LifoQueue()
    while not frontier.empty():
        n1 = frontier.get()
        if n1 == nodeState:
            result = True
        newFrontier.put(n1)
    return newFrontier, result
def printSolution(solution):
    for nodeState in solution:
        node = getGraphNode(nodeState)
        if node is not None:
            print node.STATE + ' ' + str(node.PATH_COST) + ' ' + node.ACTIONS
def Graph_Search():
    solution = {}
    node = getGraphNode(problem.Source)
    if problem.GoalTest(node.STATE):
        return node.STATE
    frontier = InitalizeFrontier(node.STATE)
    explored = []
    while frontier.qsize() > 0:
        node = POP(frontier)
        explored.append(node.STATE)
        childnodes = problem.ExpandNodes(node.ACTIONS, node.STATE)
        for child in childnodes:
            frontier, result = checkQueue(frontier, child.STATE)
            if child.STATE not in explored and result == False:
                if problem.GoalTest(child.STATE):
                    solution[child.STATE] = node.STATE
                    return getSolution(solution)
                frontier = UpdateFrontier(frontier, child.STATE)
                solution[child.STATE] = node.STATE
def InitalizeFrontier(nodeName):
    if currentSearchOption == 1:
        temp = Queue.Queue()
    else:
        temp = Queue.LifoQueue()
    temp.put(nodeName)
    return temp
def UpdateFrontier(frontier, nodeState):
    frontier.put(nodeState)
    return frontier
if __name__ == "__main__":
    read_graph()
    Source = raw_input("Enter the Source Node: ")
    Destination = raw_input("Enter the Destination Node: ")
    currentSearchOption = int(raw_input("Enter 1. for BFS \nEnter 2. for DFS: "))
    problem = Problem(Source, Destination)
    solution = Graph_Search()
    printSolution(solution)