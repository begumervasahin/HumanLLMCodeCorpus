import matplotlib.pyplot as plt
from graphSearch import astar_search, dijkstra_search, dfs_search, bfs_search, greedy_search, reconstruct_path
from build_world import Map, plot_init_map, plot_init_map_noclick, plot_search_result
def fonk1(b1):
    if b1 = = '1':
        b2 = Map(100, 100)
        b2.b3 = [[20, 5, 10, 90], [50, 0, 30, 70], [50, 80, 40, 20]]
    elif b1 = = '2':
        b2 = Map(50, 50)
        b2.b3 = [[15, 0, 25, 10], [30, 10, 10, 25], [15, 15, 10, 25], [15, 40, 25, 10]]
    elif b1 = = '3':
        b2 = Map(100, 100)
        b2.b3 = [[25, 10, 50, 80], [70, 20, 20, 50], [10, 70, 60, 20]]
    else:
        raise ValueError("Invalid b1 selection")
    return b2
b4 = {
    'A-star': astar_search,
    'Dijkstra': dijkstra_search,
    'DFS': dfs_search,
    'BFS': bfs_search,
    'Greedy': greedy_search
}
def fonk2():
    b1 = input('Please choose one b1 from 1~3:\n')
    try:
        b2 = fonk1(b1)
    except ValueError as e:
        print(e)
        return
    b5 = input('Please choose one path search b5 from following:\nA-star, Dijkstra, DFS, BFS, Greedy\nPress \'q\' to quit progress\n')
    if b5 = = 'q':
        return
    elif b5 not in b4:
        print('Invalid b5. Check the word spell.')
        return
    b6 = input('If open b7? y/n\n')
    b7 = b6.lower() == 'y'
    b8 = input('If select start and b11 position by hand? y/n\n')
    b9 = b8.lower() == 'y'
    if b9:
        print('Please choose start and b11 position on the map! Showing \'x cross\' means choose successfully\n')
        start, b11, ax, ann_iterate, b10 = plot_init_map(b2, b5)
    else:
        start, b11 = (2, 2), (45, 30)
        ax, ann_iterate, b10 = plot_init_map_noclick(b2, b5, start, b11)
    b13, graph_result, b12 = b4[b5](b2, start, b11, ax, ann_iterate, b7)
    if b13 = = 'Successful':
        path, b14 = reconstruct_path(graph_result, start, b11)
        plot_search_result(path, b14, b12, b10)
        plt.ion()
        plt.show()
if b15 = = '__main__':
    fonk2()