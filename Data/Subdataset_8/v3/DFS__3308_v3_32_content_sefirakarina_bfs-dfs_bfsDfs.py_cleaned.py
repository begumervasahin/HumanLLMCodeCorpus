data = [50, 17, 72, 12, 23, 54, 76, 9, 14, 19, 0, 0, 67]
def dfs(data, target, index):
    if index <= len(data):
        current_value = data[index - 1]
        if current_value != 0:
            print("Checking", current_value)
        if current_value == target:
            return index
        left_child_index = dfs(data, target, index * 2)
        if left_child_index != -1:
            return left_child_index
        right_child_index = dfs(data, target, (index * 2) + 1)
        if right_child_index != -1:
            return right_child_index
        return -1
    else:
        return -1
def bfs(data, target, index):
    if index <= len(data):
        queue = []
        temp = index
        for _ in range(index):
            queue.append(data[temp - 1])
            if len(data) > temp:
                temp += 1
        for _ in range(index):
            print("Checking", queue[_])
            if queue[_] == target:
                print("Yay,", target, "is found")
                return index
        print("Change row")
        for _ in range(index):
            queue.pop()
        next_row_index = bfs(data, target, index * 2)
        if next_row_index != -1:
            return next_row_index
        return -1
    else:
        return -1
print("DFS:")
result_dfs = dfs(data, 72, 1)
if result_dfs != -1:
    print("Value found at index:", result_dfs)
else:
    print("Value not found")
print("\nBFS:")
result_bfs = bfs(data, 72, 1)
if result_bfs != -1:
    print("Value found at index:", result_bfs)
else:
    print("Value not found")