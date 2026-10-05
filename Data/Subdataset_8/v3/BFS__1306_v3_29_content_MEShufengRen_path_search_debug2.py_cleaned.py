from graph_search import *
from build_world import *
SEARCH_METHODS = {
    'A-star': astar_search,
    'Dijkstra': dijkstra_search,
    'DFS': dfs_search,
    'BFS': bfs_search,
    'Greedy': greedy_search
}
def main():
    scene_choice = input('Please choose a scene from 1~3:\n')
    search_method_choice = input('Please choose a path search method from the following:\n'
                                 'A-star  Dijkstra  DFS  BFS  Greedy\n'
                                 'Enter \'q\' to quit:\n')
    if search_method_choice == 'q':
        return
    while search_method_choice not in SEARCH_METHODS:
        print('Invalid search method. Please choose a valid method.')
        search_method_choice = input('Please choose a path search method from the following:\n'
                                     'A-star  Dijkstra  DFS  BFS  Greedy\n'
                                     'Enter \'q\' to quit:\n')
    animation_choice = input('Enable animation? (y/n)\n').lower()
    enable_animation = animation_choice == 'y'
    manual_selection = input('Manually select start and goal position? (y/n)\n').lower()
    if manual_selection == 'y':
        print('Please choose start and goal positions on the map. Click to select.')
        start, goal, ax, ann_iterate, ann_path = plot_init_map(graph, search_method_choice)
    else:
        start, goal = (2, 2), (45, 30)
        ax, ann_iterate, ann_path = plot_init_map_noclick(graph, search_method_choice, start, goal)
    flag, graph_result, update_ax = SEARCH_METHODS[search_method_choice](graph, start, goal, ax, ann_iterate, enable_animation)
    if flag == 'Successful':
        path, path_length = reconstruct_path(graph_result, start, goal)
        plot_search_result(path, path_length, update_ax, ann_path)
        plt.ion()
if __name__ == '__main__':
    main()