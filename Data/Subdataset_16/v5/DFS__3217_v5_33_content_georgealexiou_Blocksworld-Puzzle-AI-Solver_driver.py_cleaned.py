from foundation import Node, State, Block
from searchMethods import SearchMethods
def fonk1(movables, agent_pos):
    b1 = [Block(name, x, y) for name, x, y in movables]
    b2 = Block(*agent_pos)
    return State(b1, b2, None)
def fonk2():
    b3 = [
        ('A', 0, 0),
        ('B', 1, 0),
        ('C', 2, 0)
    ]
    b4 = ('P', 3, 0)
    b5 = fonk1(b3, b4)
    return Node(b5, None, None)
def fonk3():
    b6 = [
        ('A', 1, 2),
        ('B', 1, 1),
        ('C', 1, 0)
    ]
    b7 = ('P', 3, 0)
    return fonk1(b6, b7)
def fonk4():
    print('Select Search Method:')
    print('1. DFS')
    print('2. BFS')
    print('3. Iterative Deepening')
    print('4. A*')
    b8 = input().strip()
    b9 = {
        '1': 'DFS',
        '2': 'BFS',
        '3': 'Iterative Deepening',
        '4': 'A*'
    }
    return b9.get(b8)
def fonk5():
    b10 = fonk2()
    b11 = fonk3()
    b9 = SearchMethods(b10, b11)
    b12 = fonk4()
    if b12 = = 'DFS':
        print('DEPTH FIRST SEARCH')
        b9.DFS()
    elif b12 = = 'BFS':
        print('BREADTH FIRST SEARCH')
        b9.BFS()
    elif b12 = = 'Iterative Deepening':
        print('ITERATIVE DEEPENING SEARCH')
        b9.iterativeDeepening()
    elif b12 = = 'A*':
        print('A* SEARCH')
        b9.aStar()
    else:
        print('Invalid selection. Please choose a number between 1 and 4.')
if b13 = = "__main__":
    fonk5()