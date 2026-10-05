class Group:
    def __init__(self, elements, similarity, index, node):
        self.elements = elements
        self.similarity = similarity
        self.index = index
        self.node = node
    def __str__(self):
        return f"Elements: {self.elements}, Similarity: {self.similarity}, Index: {self.index}"
class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def basic_display(self):
        result = "\n"
        current_level = [self]
        while current_level:
            next_level = []
            for element in current_level:
                result += str(element.value) + " " if element.value is not None else ""
                if element.left:
                    next_level.append(element.left)
                if element.right:
                    next_level.append(element.right)
            result += "\n"
            current_level = next_level
        return result
    def __bool__(self):
        return self.value is not None
    def __str__(self):
        current_level = [self]
        output = []
        while current_level:
            output.append(" ".join([str(node.value) if node.value is not None else "" for node in current_level]))
            if any(node for node in current_level):
                children = []
                for node in current_level:
                    if node.value is not None:
                        for sub_node in (node.left, node.right):
                            children.append(sub_node if sub_node else Node())
                    else:
                        children.append(node)
                current_level = children
            else:
                break
        return "\n" + "\n".join(output)
representation_matrix = [
    [10, 6, 0, 0, 0, 0, 0, 0, 0],
    [6, 10, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 10, 5, 3, 3, 1, 1, 0],
    [0, 0, 5, 10, 1, 2, 1, 1, 0],
    [0, 0, 3, 1, 10, 4, 1, 2, 0],
    [0, 0, 3, 2, 4, 10, 1, 4, 0],
    [0, 0, 1, 1, 1, 1, 10, 1, 0],
    [0, 0, 1, 1, 2, 4, 1, 10, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 10]
]
print("Representation Matrix:")
for row in representation_matrix:
    print(row)
print()
working_matrix = [[-1 if i == j else representation_matrix[i][j] for j in range(len(representation_matrix))]
                  for i in range(len(representation_matrix))]
groups = []
for i in range(len(representation_matrix)):
    max_similarity = max(working_matrix[i])
    max_index = working_matrix[i].index(max_similarity)
    group = Group([i], max_similarity, max_index, Node(i))
    groups.append(group)
for _ in range(len(representation_matrix) - 1):
    max_similarity = -1
    max_index = [-1, -1]
    for j, gr in enumerate(groups):
        if max_similarity < gr.similarity:
            max_similarity = gr.similarity
            max_index = [j, gr.index]
    print("Found max:", max_similarity, "@", max_index)
    group_index = [max_index[0], -1]
    for j, group in enumerate(groups):
        if max_index[1] in group.elements:
            group_index[1] = j
    destination_group = groups[group_index[0]]
    source_group = groups[group_index[1]]
    for element in source_group.elements:
        for element2 in destination_group.elements:
            working_matrix[element][element2] = -1
            working_matrix[element2][element] = -1
    display_elements = destination_group.elements
    destination_group.elements += source_group.elements
    destination_group.node = Node(destination_group.elements, destination_group.node, source_group.node)
    groups.remove(source_group)
    for group in groups:
        if group.index in source_group.elements:
            group.index = max_index[0]
    max_similarity = -1
    max_index = -1
    for e in destination_group.elements:
        for i in range(len(working_matrix)):
            if working_matrix[e][i] > max_similarity:
                max_similarity = working_matrix[e][i]
                max_index = i
    destination_group.index = max_index
    destination_group.similarity = max_similarity
    print("Merged", group_index, ":", display_elements, "&", source_group.elements)
print(groups[0].node)