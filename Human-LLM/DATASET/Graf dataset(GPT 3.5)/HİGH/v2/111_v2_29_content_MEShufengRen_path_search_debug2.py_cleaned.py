from graphSearch import *
from build_world import *
b1 = {
    'A-star': astar_search,
    'Dijkstra': dijkstra_search,
    'DFS': dfs_search,
    'BFS': bfs_search,
    'Greedy': greedy_search
}
def fonk1():
    b2 = input('Please choose one b2 from 1~3:\n')
    b3 = input('Please choose one path search b3 from following:\n'
                   'A-star  ' 'Dijkstra  ' 'DFS  ' 'BFS  ' 'Greedy\n'
                   'press \'q\' to quit progress\n')
    if b3 = = 'q':
        return
    elif b3 not in b1:
        print('Check the word spell\n')
        b3 = input('Please choose one path search b3 from following:\n'
                       'A-star  ' 'Dijkstra  ' 'DFS  ' 'BFS  ' 'Greedy\n'
                       'press \'q\' to quit progress\n')
    b4 = input('If open b4? y/n\n')
    b4 = True if b4 == 'y' else False
    b5 = input('If select start and b7 position by hand? y/n\n')
    if b5 = = 'y':
        print('Please choose start and b7 position on the map! Showing \'x corss\' means choose successfully\n')
        start, b7, ax, ann_iterate, b6 = plot_init_map(graph, b3)
    else:
        start, b7 = (2, 2), (45, 30)
        ax, ann_iterate, b6 = plot_init_map_noclick(graph, b3, start, b7)
    b9, graph_result, b8 = b1[b3](graph, start, b7, ax, ann_iterate, b4)
    if b9 = = 'Successful':
        path, b10 = reconstruct_path(graph_result, start, b7)
        plot_search_result(path, b10, b8, b6)
        plt.ion()
if b11 = = '__main__':
    fonk1()