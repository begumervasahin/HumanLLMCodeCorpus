from foundation import Node, State, Block
from searchMethods import SearchMethods
def fonk1():
    b1 = [
        Block('A', 0, 0),
        Block('B', 1, 0),
        Block('C', 2, 0)
    ]
    b2 = Block('P', 3, 0)
    b3 = State(b1, b2, None)
    return Node(b3, None, None)
def fonk2():
    b4 = [
        Block('A', 1, 2),
        Block('B', 1, 1),
        Block('C', 1, 0)
    ]
    b5 = Block('P', 3, 0)
    return State(b4, b5, None)
def fonk3():
    print('Select Search Method:')
    print('1. DFS')
    print('2. BFS')
    print('3. Iterative Deepening')
    print('4. A*')
    b6 = input().strip()
    b7 = {
        '1': 'DFS',
        '2': 'BFS',
        '3': 'Iterative Deepening',
        '4': 'A*'
    }
    return b7.get(b6, 'Invalid')
def fonk4():
    b8 = fonk1()
    b9 = fonk2()
    b7 = SearchMethods(b8, b9)
    b10 = fonk3()
    if b10 = = 'DFS':
        print('DEPTH FIRST SEARCH')
        b7.DFS()
    elif b10 = = 'BFS':
        print('BREADTH FIRST SEARCH')
        b7.BFS()
    elif b10 = = 'Iterative Deepening':
        print('ITERATIVE DEEPENING SEARCH')
        b7.iterativeDeepening()
    elif b10 = = 'A*':
        print('A* SEARCH')
        b7.aStar()
    else:
        print('Invalid selection. Please choose a number between 1 and 4.')
if b11 = = "__main__":
    fonk4()