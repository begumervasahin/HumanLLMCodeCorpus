from graphSearch import *
from build_world import *
b1 = Map(50, 50)
b1.b2 = [[15, 0, 25, 10], [30, 10, 10, 25], [15, 15, 10, 25], [15, 40, 25, 10]]
b3 = {
    'A-star': astar_search,
    'Dijkstra': dijkstra_search,
    'DFS': dfs_search,
    'BFS': bfs_search,
    'Greedy': greedy_search
}
def fonk1():
    b4 = input('Please choose one b4 from 1~3:\n')
    b5 = input(
        'Please choose one path search b5 from the following:\n'
        'A-star  Dijkstra  DFS  BFS  Greedy\n'
        'Press \'q\' to quit\n'
    )
    if b5 = = 'q':
        return None, None, None, None
    while b5 not in b3:
        print('Invalid b5. Check the spelling and try again.')
        b5 = input(
            'Please choose one path search b5 from the following:\n'
            'A-star  Dijkstra  DFS  BFS  Greedy\n'
            'Press \'q\' to quit\n'
        )
    b6 = input('Enable b7? (y/n)\n')
    b7 = b6.lower() == 'y'
    b8 = input('Select start and b11 positions manually? (y/n)\n')
    b9 = b8.lower() == 'y'
    return b4, b5, b7, b9
def fonk2():
    b4, b5, b7, b9 = fonk1()
    if b5 is None:
        return
    if b9:
        print('Choose start and b11 positions on the map. A cross means selection successful.')
        start, b11, ax, ann_iterate, b10 = plot_init_map(b1, b5)
    else:
        start, b11 = (2, 2), (45, 30)
        ax, ann_iterate, b10 = plot_init_map_noclick(b1, b5, start, b11)
    b12 = b3[b5]
    b14, graph_result, b13 = b12(b1, start, b11, ax, ann_iterate, b7)
    if b14 = = 'Successful':
        path, b15 = reconstruct_path(graph_result, start, b11)
        plot_search_result(path, b15, b13, b10)
        plt.ion()
if b16 = = '__main__':
    fonk2()