import matplotlib.pyplot as plt
from graphSearch import astar_search, dijkstra_search, dfs_search, bfs_search, greedy_search, reconstruct_path
from build_world import Map, plot_init_map, plot_init_map_noclick, plot_search_result
def create_map(scene):
    if scene == '1':
        graph = Map(100, 100)
        graph.walls = [[20, 5, 10, 90], [50, 0, 30, 70], [50, 80, 40, 20]]
    elif scene == '2':
        graph = Map(50, 50)
        graph.walls = [[15, 0, 25, 10], [30, 10, 10, 25], [15, 15, 10, 25], [15, 40, 25, 10]]
    elif scene == '3':
        graph = Map(100, 100)
        graph.walls = [[25, 10, 50, 80], [70, 20, 20, 50], [10, 70, 60, 20]]
    else:
        raise ValueError("Invalid scene selection")
    return graph
search_methods = {
    'A-star': astar_search,
    'Dijkstra': dijkstra_search,
    'DFS': dfs_search,
    'BFS': bfs_search,
    'Greedy': greedy_search
}
def main():
    scene = input('Please choose one scene from 1~3:\n')
    try:
        graph = create_map(scene)
    except ValueError as e:
        print(e)
        return
    method = input('Please choose one path search method from the following:\nA-star, Dijkstra, DFS, BFS, Greedy\nPress \'q\' to quit progress\n')
    if method == 'q':
        return
    elif method not in search_methods:
        print('Invalid method. Check the spelling.')
        return
    animation_input = input('Enable animation? (y/n)\n')
    animation = animation_input.lower() == 'y'
    click_input = input('Select start and goal positions manually? (y/n)\n')
    click = click_input.lower() == 'y'
    if click:
        print('Please choose start and goal positions on the map! A \'x cross\' indicates a successful selection.\n')
        start, goal, ax, ann_iterate, ann_path = plot_init_map(graph, method)
    else:
        start, goal = (2, 2), (45, 30)
        ax, ann_iterate, ann_path = plot_init_map_noclick(graph, method, start, goal)
    search_function = search_methods[method]
    flag, graph_result, update_ax = search_function(graph, start, goal, ax, ann_iterate, animation)
    if flag == 'Successful':
        path, path_length = reconstruct_path(graph_result, start, goal)
        plot_search_result(path, path_length, update_ax, ann_path)
        plt.ion()
        plt.show()
if __name__ == '__main__':
    main()