import numpy as np
class VPNode:
    def __init__(self, indices, data):
        if len(indices) == 0:
            self.index = None
            self.radius = None
            self.inside = None
            self.outside = None
            return
        self.index = indices[0]
        remaining_indices = indices[1:]
        if remaining_indices.size > 0:
            distances = self._calculate_distances(data[remaining_indices], data[self.index])
            self.radius = np.median(distances)
            inside_mask = distances < self.radius
            outside_mask = ~inside_mask
            self.inside = VPNode(remaining_indices[inside_mask], data[inside_mask])
            self.outside = VPNode(remaining_indices[outside_mask], data[outside_mask])
        else:
            self.radius = None
            self.inside = None
            self.outside = None
    def _calculate_distances(self, points, center_point):
        return np.sum((points - center_point) ** 2, axis=1)
    def print_tree(self, indent=0):
        if self.index is None:
            return
        print(f"{' ' * (indent * 4)}* (Node {self.index})")
        if self.inside and self.inside.index is not None:
            print(f"{' ' * (indent * 4)}  - Inside {self.index}:")
            self.inside.print_tree(indent + 1)
        if self.outside and self.outside.index is not None:
            print(f"{' ' * (indent * 4)}  - Outside {self.index}:")
            self.outside.print_tree(indent + 1)
    def find_neighbors(self, target_index, neighbors, distances, data):
        if self.index is None:
            return
        dist_to_target = np.sum((data[self.index] - data[target_index]) ** 2)
        max_distance = distances[-1]
        if target_index != self.index and dist_to_target < max_distance:
            distances[-1] = dist_to_target
            neighbors[-1] = self.index
            sorted_order = np.argsort(distances)
            distances[:] = distances[sorted_order]
            neighbors[:] = neighbors[sorted_order]
        if self.radius is None:
            return
        if dist_to_target >= max_distance + self.radius:
            self.outside.find_neighbors(target_index, neighbors, distances, data)
        elif self.radius > max_distance + dist_to_target:
            self.inside.find_neighbors(target_index, neighbors, distances, data)
        else:
            self.inside.find_neighbors(target_index, neighbors, distances, data)
            self.outside.find_neighbors(target_index, neighbors, distances, data)
np.random.seed(42)
data_points = np.random.rand(10, 2)
indices = np.arange(len(data_points))
vp_tree = VPNode(indices, data_points)
vp_tree.print_tree()
k = 3
neighbors = np.full(k, -1)
distances = np.full(k, np.inf)
vp_tree.find_neighbors(0, neighbors, distances, data_points)
print("\n3 Nearest Neighbors of the first point:")
print("Indices:", neighbors)
print("Distances:", distances)