29. Repository: MEShufengRen/path_search
   File: debug2.py
   URL: https:
   Code Content:
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
    b5 = input('Please choose one path search b5 from following:\n'
                   'A-star  ' 'Dijkstra  ' 'DFS  ' 'BFS  ' 'Greedy\n'
                   'press \'q\' to quit progress\n')
    if b5 is 'q':
        return
    elif b5 not in b3:
        print('Check the word spell\n')
        b5 = input('Please choose one path search b5 from following:\n'
                   'A-star  ' 'Dijkstra  ' 'DFS  ' 'BFS  ' 'Greedy\n'
                   'press \'q\' to quit progress\n')
    b6 = input('If open b6? y/n\n')
    if b6 = = 'y':
        b6 = True
    else:
        b6 = False
    b7 = input('If select start and b9 position by hand? y/n\n')
    if b7 = = 'y':
        print('Please choose start and b9 position on the map! Showing \'x corss\' means choose successfully\n')
        start, b9, ax, ann_iterate, b8 = plot_init_map(b1, b5)
    else:
        start, b9 = (2, 2), (45, 30)
        ax, ann_iterate, b8 = plot_init_map_noclick(b1, b5, start, b9)
    b11, graph_result, b10 = b3[b5](b1, start, b9, ax, ann_iterate, b6)
    if b11 = = 'Successful':
        path, b12 = reconstruct_path(graph_result, start, b9)
        plot_search_result(path, b12, b10, b8)
        plt.ion()
if b13 = = '__main__':
    fonk1()
   README Content:
Implement A-start, Dijstra, BFS,DFS and Greedy-Best-First path search algorithm and utilize the matplotlib with python 3.7.1 to animate the path search process
Details please found in [project report](./Route planning in static network_ShufengRen JiaruiLi.pdf)
