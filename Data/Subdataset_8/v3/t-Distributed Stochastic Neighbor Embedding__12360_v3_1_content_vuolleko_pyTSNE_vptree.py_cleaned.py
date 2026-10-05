import numpy as np
class VPnode:
    def __init__(self, indices, data):
        if len(indices) == 0:
            self.index = None
            self.radius = None
            return
        self.index = indices[0]
        remaining_indices = indices[1:]
        if remaining_indices:
            distances = np.sum((data[1:, :] - data[0, :]) ** 2., axis=1)
            data = data[1:, :]
            self.radius = np.median(distances)
            indices_inside = distances < self.radius
            indices_outside = ~indices_inside
            self.inside = VPnode(remaining_indices[indices_inside], data[indices_inside])
            self.outside = VPnode(remaining_indices[indices_outside], data[indices_outside])
        else:
            self.radius = None
            self.inside = VPnode([], [])
            self.outside = VPnode([], [])
    def print_node(self, indent=0):
        if self.index is None:
            return
        indent_str = "    " * indent
        print(indent_str + "* (Node {})".format(self.index))
        if self.inside.index is not None:
            print(indent_str + "  - Inside {}:".format(self.index))
            self.inside.print_node(indent + 1)
        if self.outside.index is not None:
            print(indent_str + "  - Outside {}:".format(self.index))
            self.outside.print_node(indent + 1)
    def find_neighbors(self, point_index, neighbors, distances, data):
        if self.index is None:
            return
        dist = np.sum((data[self.index, :] - data[point_index, :]) ** 2.)
        search_radius = distances[-1]
        if point_index != self.index and dist < search_radius:
            distances[-1] = dist
            neighbors[-1] = self.index
            sorted_indices = np.argsort(distances)
            distances[:] = distances[sorted_indices]
            neighbors[:] = neighbors[sorted_indices]
        if self.radius is None:
            return
        if dist >= search_radius + self.radius:
            self.outside.find_neighbors(point_index, neighbors, distances, data)
        elif self.radius > search_radius + dist:
            self.inside.find_neighbors(point_index, neighbors, distances, data)
        else:
            self.inside.find_neighbors(point_index, neighbors, distances, data)
            self.outside.find_neighbors(point_index, neighbors, distances, data)
        return neighbors