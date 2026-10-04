from graphSearch import *
from build_world import *
graph = Map(50, 50)
graph.walls = [[15, 0, 25, 10], [30, 10, 10, 25], [15, 15, 10, 25], [15, 40, 25, 10]]
search_methods = {
    'A-star': astar_search,
    'Dijkstra': dijkstra_search,
    'DFS': dfs_search,
    'BFS': bfs_search,
    'Greedy': greedy_search
}
def get_user_input():
    scene = input('Please choose one scene from 1~3:\n')
    method = input(
        'Please choose one path search method from the following:\n'
        'A-star  Dijkstra  DFS  BFS  Greedy\n'
        'Press \'q\' to quit\n'
    )
    if method == 'q':
        return None, None, None, None
    while method not in search_methods:
        print('Invalid method. Check the spelling and try again.')
        method = input(
            'Please choose one path search method from the following:\n'
            'A-star  Dijkstra  DFS  BFS  Greedy\n'
            'Press \'q\' to quit\n'
        )
    animation_input = input('Enable animation? (y/n)\n')
    animation = animation_input.lower() == 'y'
    click_input = input('Select start and goal positions manually? (y/n)\n')
    click = click_input.lower() == 'y'
    return scene, method, animation, click
def main():
    scene, method, animation, click = get_user_input()
    if method is None:
        return
    if click:
        print('Choose start and goal positions on the map. A cross means selection successful.')
        start, goal, ax, ann_iterate, ann_path = plot_init_map(graph, method)
    else:
        start, goal = (2, 2), (45, 30)
        ax, ann_iterate, ann_path = plot_init_map_noclick(graph, method, start, goal)
    search_function = search_methods[method]
    success, graph_result, update_ax = search_function(graph, start, goal, ax, ann_iterate, animation)
    if success == 'Successful':
        path, path_length = reconstruct_path(graph_result, start, goal)
        plot_search_result(path, path_length, update_ax, ann_path)
        plt.ion()
if __name__ == '__main__':
    main()