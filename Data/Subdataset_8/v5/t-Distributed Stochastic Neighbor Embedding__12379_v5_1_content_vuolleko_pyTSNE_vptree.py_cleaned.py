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
    def find_neighbors(self, ind, neighbors, distances, data):
        if self.index is None:
            return
        dist = np.sum((data[self.index, :] - data[ind, :]) ** 2.)
        radius_search = distances[-1]
        if ind != self.index and dist < radius_search:
            distances[-1] = dist
            neighbors[-1] = self.index
            ind_sort = np.argsort(distances)
            distances[:] = distances[ind_sort]
            neighbors[:] = neighbors[ind_sort]
        if self.radius is None:
            return
        if dist >= radius_search + self.radius:
            self.outside.find_neighbors(ind, neighbors, distances, data)
        elif self.radius > radius_search + dist:
            self.inside.find_neighbors(ind, neighbors, distances, data)
        else:
            self.inside.find_neighbors(ind, neighbors, distances, data)
            self.outside.find_neighbors(ind, neighbors, distances, data)
        return neighbors