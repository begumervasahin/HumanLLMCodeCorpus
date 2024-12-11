from graph_search import *
from build_world import *
b1 = {
    'A-star': astar_search,
    'Dijkstra': dijkstra_search,
    'DFS': dfs_search,
    'BFS': bfs_search,
    'Greedy': greedy_search
}
def fonk1():
    b2 = input('Please choose a scene from 1~3:\n')
    b3 = input('Please choose a path search method from the following:\n'
                                 'A-star  Dijkstra  DFS  BFS  Greedy\n'
                                 'Enter \'q\' to quit:\n')
    if b3 = = 'q':
        return
    while b3 not in b1:
        print('Invalid search method. Please choose a valid method.')
        b3 = input('Please choose a path search method from the following:\n'
                                     'A-star  Dijkstra  DFS  BFS  Greedy\n'
                                     'Enter \'q\' to quit:\n')
    b4 = input('Enable animation? (y/n)\n').lower()
    b5 = b4 == 'y'
    b6 = input('Manually select start and b8 position? (y/n)\n').lower()
    if b6 = = 'y':
        print('Please choose start and b8 positions on the map. Click to select.')
        start, b8, ax, ann_iterate, b7 = plot_init_map(graph, b3)
    else:
        start, b8 = (2, 2), (45, 30)
        ax, ann_iterate, b7 = plot_init_map_noclick(graph, b3, start, b8)
    b10, graph_result, b9 = b1[b3](graph, start, b8, ax, ann_iterate, b5)
    if b10 = = 'Successful':
        path, b11 = reconstruct_path(graph_result, start, b8)
        plot_search_result(path, b11, b9, b7)
        plt.ion()
if b12 = = '__main__':
    fonk1()