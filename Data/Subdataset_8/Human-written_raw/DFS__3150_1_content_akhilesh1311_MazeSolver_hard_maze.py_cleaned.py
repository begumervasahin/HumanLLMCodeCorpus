import random
import copy
import sys
def bfs(arr, is_path = False):
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
						arr[p][q] = '
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
	ans_arr = []
	for index, maze in enumerate(maze_list):
		nodes_expanded = bfs(maze)
		ans_arr.append((nodes_expanded, random.random(), index))
	ans_arr.sort(reverse = True)
	return ans_arr[0][-1]
def display_maze(maze):
	for row in maze:
		print(*row, sep = ' ')
	print('\n\n')
if __name__ == '__main__':
	dim, p, iters = 15, 0.3, 100
	maze = []
	for i in range(dim):
		tmp = []
		for j in range(dim):
			tmp.append('X' if random.random() < p else 'O')
		maze.append(tmp)
	maze[0][0] = 'S'
	maze[dim - 1][dim - 1] = 'G'
	print("Displaying maze from part-1: ")
	display_maze(maze)
	print("Displaying maze from part-1 with the shortest path: ")
	bfs(maze, True)
	for i in range(dim):
		for j in range(dim):
			if maze[i][j] == '
				maze[i][j] = 'O'
	x, y = random.randint(0, dim - 1), random.randint(0, dim - 1)
	for _ in range(iters):
		maze_list = [maze]
		for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
			if 0 <= i < dim and 0 <= j < dim and maze[i][j] in ['O', 'X']:
				arr = copy.deepcopy(maze)
				arr[i][j] = 'O' if arr[i][j] == 'X' else 'X'
				maze_list.append(arr)
		index = find_best_maze(maze_list)
		maze = maze_list[index]
		if index:
			x, y = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)][index - 1]
		else:
			x, y = random.randint(0, dim - 1), random.randint(0, dim - 1)
	print("Displaying maze after hill climbing: ")
	display_maze(maze)
	print("Displaying maze with the shortest path after hill climbing: ")
	bfs(maze, True)