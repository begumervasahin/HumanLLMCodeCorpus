from graph_search import *
from build_world import *
scenes = {
    '1': [[20, 5, 10, 90], [50, 0, 30, 70], [50, 80, 40, 20]],
    '2': [[15, 0, 25, 10], [30, 10, 10, 25], [15, 15, 10, 25], [15, 40, 25, 10]],
    '3': []
}
search_methods = {
    'A-star': astar_search,
    'Dijkstra': dijkstra_search,
    'DFS': dfs_search,
    'BFS': bfs_search,
    'Greedy': greedy_search
}
def main():
    print("Welcome to Path Finding Simulator!")
    while True:
        scene_choice = input('Please choose a scene (1-3): ')
        if scene_choice in scenes:
            break
        else:
            print('Invalid scene choice. Please try again.')
    while True:
        print("Available search methods:")
        print(", ".join(search_methods.keys()))
        search_method = input('Please choose a path search method: ')
        if search_method in search_methods:
            break
        else:
            print('Invalid search method. Please try again.')
    while True:
        animation_choice = input('Would you like to enable animation? (y/n): ')
        if animation_choice.lower() == 'y':
            animation_enabled = True
            break
        elif animation_choice.lower() == 'n':
            animation_enabled = False
            break
        else:
            print('Invalid choice. Please enter y/n.')
    while True:
        manual_selection = input('Would you like to select start and goal positions manually? (y/n): ')
        if manual_selection.lower() == 'y':
            manual_selection_enabled = True
            break
        elif manual_selection.lower() == 'n':
            manual_selection_enabled = False
            break
        else:
            print('Invalid choice. Please enter y/n.')
    graph = Map(50, 50)
    graph.walls = scenes[scene_choice]
    if manual_selection_enabled:
        print('Please select start and goal positions on the map.')
        start, goal, ax, ann_iterate, ann_path = plot_init_map(graph, search_method)
    else:
        start, goal = (2, 2), (45, 30)
        ax, ann_iterate, ann_path = plot_init_map_noclick(graph, search_method, start, goal)
    flag, graph_result, update_ax = search_methods[search_method](graph, start, goal, ax, ann_iterate, animation_enabled)
    if flag == 'Successful':
        path, path_length = reconstruct_path(graph_result, start, goal)
        plot_search_result(path, path_length, update_ax, ann_path)
        plt.ion()
if __name__ == '__main__':
    main()