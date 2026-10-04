class Group:
    def __init__(self, elements, similarity, index, node):
        self.elements = elements
        self.similarity = similarity
        self.index = index
        self.node = node
    def __str__(self):
        return f"{self.elements} => {self.similarity} ({self.index})"
class Node:
    def __init__(self, value=" ", left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def basic_display(self):
        result = "\n"
        current_level = [self]
        while current_level:
            next_level = []
            for elem in current_level:
                result += str(elem.value) + " "
                if elem.left:
                    next_level.append(elem.left)
                if elem.right:
                    next_level.append(elem.right)
            result += "\n"
            current_level = next_level
        return result
    def __bool__(self):
        return self.value != " "
    def __str__(self):
        current_level = [self]
        result = []
        while current_level:
            result.append(" ".join([str(node.value) for node in current_level]))
            if any(node for node in current_level):
                children = []
                for node in current_level:
                    if node.value != " ":
                        for subnode in (node.left, node.right):
                            children.append(subnode if subnode else Node())
                    else:
                        children.append(node)
                current_level = children
            else:
                break
        return "\n" + "\n".join(result)
rep_matrix = [
    [10, 6, 0, 0, 0, 0, 0, 0, 0],
    [6, 10, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 10, 5, 3, 3, 1, 1, 0],
    [0, 0, 5, 10, 1, 2, 1, 1, 0],
    [0, 0, 3, 1, 10, 4, 1, 2, 0],
    [0, 0, 3, 2, 4, 10, 1, 4, 0],
    [0, 0, 1, 1, 1, 1, 10, 1, 0],
    [0, 0, 1, 1, 2, 4, 1, 10, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 10],
]
print("Representation Matrix:")
for row in rep_matrix:
    print(row)
print()
work_matrix = rep_matrix
for i in range(len(rep_matrix)):
    work_matrix[i][i] = -1
groups = []
for i in range(len(rep_matrix)):
    max_sim = max(work_matrix[i])
    index = work_matrix[i].index(max_sim)
    g = Group([i], max_sim, index, Node([i]))
    groups.append(g)
for _ in range(len(rep_matrix) - 1):
    max_sim = -1
    max_index = [-1, -1]
    for j, group in enumerate(groups):
        if group.similarity > max_sim:
            max_sim = group.similarity
            max_index = [j, group.index]
    print(f"Found max: {max_sim} @{max_index}")
    dest_group_idx = max_index[0]
    source_group_idx = next(j for j, group in enumerate(groups) if max_index[1] in group.elements)
    dest_group = groups[dest_group_idx]
    source_group = groups[source_group_idx]
    for element in source_group.elements:
        for dest_element in dest_group.elements:
            work_matrix[element][dest_element] = -1
            work_matrix[dest_element][element] = -1
    print(f"Merging groups: {dest_group.elements} & {source_group.elements}")
    dest_group.elements += source_group.elements
    dest_group.node = Node(dest_group.elements, dest_group.node, source_group.node)
    groups.remove(source_group)
    for group in groups:
        if group.index in source_group.elements:
            group.index = dest_group_idx
    max_sim = -1
    max_idx = -1
    for element in dest_group.elements:
        for i in range(len(work_matrix)):
            if work_matrix[element][i] > max_sim:
                max_sim = work_matrix[element][i]
                max_idx = i
    dest_group.index = max_idx
    dest_group.similarity = max_sim
print("\nFinal Hierarchical Grouping:")
print(groups[0].node)