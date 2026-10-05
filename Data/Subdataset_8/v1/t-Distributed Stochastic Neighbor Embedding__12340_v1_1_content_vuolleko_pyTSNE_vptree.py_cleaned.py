import numpy as np
class VPnode:
    def __init__(self, inds, data):
        if len(inds) == 0:
            self.ind = None
            self.radius = None
            return
        self.ind = inds[0]
        inds = inds[1:]
        if len(inds) > 0:
            distances = np.sum((data[1:, :] - data[0, :]) ** 2., axis=1)
            data = data[1:, :]
            self.radius = np.median(distances)
            inds_inside = distances < self.radius
            inds_outside = np.invert(inds_inside)
            self.inside = VPnode(inds[inds_inside], data[inds_inside])
            self.outside = VPnode(inds[inds_outside], data[inds_outside])
        else:
            self.radius = None
            self.inside = VPnode([], [])
            self.outside = VPnode([], [])
    def print_node(self, indent=0):
        if self.ind is None:
            return
        indent_str = "    " * indent
        print(indent_str + "* (Node {})".format(self.ind))
        if self.inside.ind is not None:
            print(indent_str + "  - Inside {}:".format(self.ind))
            self.inside.print_node(indent + 1)
        if self.outside.ind is not None:
            print(indent_str + "  - Outside {}:".format(self.ind))
            self.outside.print_node(indent + 1)
    def find_neighbors(self, ind, neighbors, distances, data):
        if self.ind is None:
            return
        dist = np.sum((data[self.ind, :] - data[ind, :]) ** 2.)
        radius_search = distances[-1]
        if ind != self.ind and dist < radius_search:
            distances[-1] = dist
            neighbors[-1] = self.ind
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