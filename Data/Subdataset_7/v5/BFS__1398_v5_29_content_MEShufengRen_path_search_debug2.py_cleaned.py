from graph_search import *
from build_world import *
b1 = {
    '1': [[20, 5, 10, 90], [50, 0, 30, 70], [50, 80, 40, 20]],
    '2': [[15, 0, 25, 10], [30, 10, 10, 25], [15, 15, 10, 25], [15, 40, 25, 10]],
    '3': []
}
b2 = {
    'A-star': astar_search,
    'Dijkstra': dijkstra_search,
    'DFS': dfs_search,
    'BFS': bfs_search,
    'Greedy': greedy_search
}
def fonk1():
    print("Welcome to Path Finding Simulator!")
    while True:
        b3 = input('Please choose a scene (1-3): ')
        if b3 in b1:
            break
        else:
            print('Invalid scene choice. Please try again.')
    while True:
        print("Available search methods:")
        print(", ".join(b2.keys()))
        b4 = input('Please choose a path search method: ')
        if b4 in b2:
            break
        else:
            print('Invalid search method. Please try again.')
    while True:
        b5 = input('Would you like to enable animation? (y/n): ')
        if b5.lower() == 'y':
            b6 = True
            break
        elif b5.lower() == 'n':
            b6 = False
            break
        else:
            print('Invalid choice. Please enter y/n.')
    while True:
        b7 = input('Would you like to select start and b12 positions manually? (y/n): ')
        if b7.lower() == 'y':
            b8 = True
            break
        elif b7.lower() == 'n':
            b8 = False
            break
        else:
            print('Invalid choice. Please enter y/n.')
    b9 = Map(50, 50)
    b9.b10 = b1[b3]
    if b8:
        print('Please select start and b12 positions on the map.')
        start, b12, ax, ann_iterate, b11 = plot_init_map(b9, b4)
    else:
        start, b12 = (2, 2), (45, 30)
        ax, ann_iterate, b11 = plot_init_map_noclick(b9, b4, start, b12)
    b14, graph_result, b13 = b2[b4](b9, start, b12, ax, ann_iterate, b6)
    if b14 = = 'Successful':
        path, b15 = reconstruct_path(graph_result, start, b12)
        plot_search_result(path, b15, b13, b11)
        plt.ion()
if b16 = = '__main__':
    fonk1()