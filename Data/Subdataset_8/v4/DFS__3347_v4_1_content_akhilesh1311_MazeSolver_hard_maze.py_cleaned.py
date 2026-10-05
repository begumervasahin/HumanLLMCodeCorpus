import random
import copy
def breadth_first_search(arr, is_path=False):
    path = []
    queue = []
    visited = set()
    queue.append((0, 0))
    visited.add((0, 0))
    parent_node = {}
    while queue:
        cur_i, cur_j = queue.pop(0)
        if arr[cur_i][cur_j] == 'G':
            ans = 0
            while cur_i + cur_j:
                path.append((cur_i, cur_j))
                cur_i, cur_j = parent_node[(cur_i, cur_j)]
                ans += 1
            if is_path:
                for p, q in path:
                    if arr[p][q] in ['O', 'X']:
                        arr[p][q] = ' '
                display_maze(arr)
                return
            else:
                return ans
        for i, j in [(cur_i - 1, cur_j), (cur_i + 1, cur_j), (cur_i, cur_j - 1), (cur_i, cur_j + 1)]:
            if 0 <= i < len(arr) and 0 <= j < len(arr) and arr[i][j] != 'X' and (i, j) not in visited:
                queue.append((i, j))
                parent_node[(i, j)] = (cur_i, cur_j)
                visited.add((i, j))
    return -1
def find_best_maze(maze_list):
    evaluation = []
    for index, maze in enumerate(maze_list):
        nodes_expanded = breadth_first_search(maze)
        evaluation.append((nodes_expanded, random.random(), index))
    evaluation.sort(reverse=True)
    return evaluation[0][-1]
def display_maze(maze):
    for row in maze:
        print(*row, sep=' ')
    print('\n')
if __name__ == '__main__':
    dimension = 15
    obstacle_probability = 0.3
    iterations = 100
    maze = [['X' if random.random() < obstacle_probability else 'O' for _ in range(dimension)] for _ in range(dimension)]
    maze[0][0] = 'S'
    maze[dimension - 1][dimension - 1] = 'G'
    print("Initial maze:")
    display_maze(maze)
    print("Shortest path in initial maze:")
    breadth_first_search(maze, True)
    for i in range(dimension):
        for j in range(dimension):
            if maze[i][j] == ' ':
                maze[i][j] = 'O'
    x, y = random.randint(0, dimension - 1), random.randint(0, dimension - 1)
    for _ in range(iterations):
        maze_list = [maze]
        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if 0 <= i < dimension and 0 <= j < dimension and maze[i][j] in ['O', 'X']:
                new_maze = copy.deepcopy(maze)
                new_maze[i][j] = 'O' if new_maze[i][j] == 'X' else 'X'
                maze_list.append(new_maze)
        index = find_best_maze(maze_list)
        maze = maze_list[index]
        if index:
            x, y = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)][index - 1]
        else:
            x, y = random.randint(0, dimension - 1), random.randint(0, dimension - 1)
    print("Final maze after hill climbing:")
    display_maze(maze)
    print("Shortest path in final maze after hill climbing:")
    breadth_first_search(maze, True)