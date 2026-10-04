from foundation import Node, State, Block
from searchMethods import SearchMethods
def create_state(movables, agent_pos):
    blocks = [Block(name, x, y) for name, x, y in movables]
    agent = Block(*agent_pos)
    return State(blocks, agent, None)
def create_initial_state():
    start_movables = [
        ('A', 0, 0),
        ('B', 1, 0),
        ('C', 2, 0)
    ]
    start_agent_pos = ('P', 3, 0)
    start_state = create_state(start_movables, start_agent_pos)
    return Node(start_state, None, None)
def create_final_state():
    fin_movables = [
        ('A', 1, 2),
        ('B', 1, 1),
        ('C', 1, 0)
    ]
    fin_agent_pos = ('P', 3, 0)
    return create_state(fin_movables, fin_agent_pos)
def select_search_method():
    print('Select Search Method:')
    print('1. DFS')
    print('2. BFS')
    print('3. Iterative Deepening')
    print('4. A*')
    choice = input().strip()
    search_methods = {
        '1': 'DFS',
        '2': 'BFS',
        '3': 'Iterative Deepening',
        '4': 'A*'
    }
    return search_methods.get(choice)
def main():
    start_node = create_initial_state()
    fin_state = create_final_state()
    search_methods = SearchMethods(start_node, fin_state)
    selected_method = select_search_method()
    if selected_method == 'DFS':
        print('DEPTH FIRST SEARCH')
        search_methods.DFS()
    elif selected_method == 'BFS':
        print('BREADTH FIRST SEARCH')
        search_methods.BFS()
    elif selected_method == 'Iterative Deepening':
        print('ITERATIVE DEEPENING SEARCH')
        search_methods.iterativeDeepening()
    elif selected_method == 'A*':
        print('A* SEARCH')
        search_methods.aStar()
    else:
        print('Invalid selection. Please choose a number between 1 and 4.')
if __name__ == "__main__":
    main()