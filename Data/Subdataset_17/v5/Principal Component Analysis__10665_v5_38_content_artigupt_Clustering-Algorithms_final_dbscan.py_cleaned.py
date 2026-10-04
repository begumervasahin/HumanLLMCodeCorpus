from cluster import *
from pylab import *
class DBScanner:
    def __init__(self, dataset):
        self.dataset = dataset
        self.visited = set()
        self.noise = []
        self.clusters = []
        self.cluster_count = 0
    def dbscan(self, eps, min_pts):
        for point in self.dataset:
            if point not in self.visited:
                self.visited.add(point)
                neighbour_points = self._region_query(point, eps)
                if len(neighbour_points) < min_pts:
                    self.noise.append(point)
                else:
                    new_cluster = Cluster(f'Cluster{self.cluster_count}')
                    self.cluster_count += 1
                    self._expand_cluster(point, neighbour_points, new_cluster, eps, min_pts)
    def _expand_cluster(self, point, neighbour_points, cluster, eps, min_pts):
        cluster.add_point(point)
        i = 0
        while i < len(neighbour_points):
            p = neighbour_points[i]
            if p not in self.visited:
                self.visited.add(p)
                new_neighbours = self._region_query(p, eps)
                if len(new_neighbours) >= min_pts:
                    neighbour_points.extend([n for n in new_neighbours if n not in neighbour_points])
            if not any(c.has(p) for c in self.clusters):
                cluster.add_point(p)
            i += 1
        self.clusters.append(cluster)
    def _region_query(self, point, eps):
        return [d for d in self.dataset if self._euclidean_distance(d, point) <= eps]
    def _euclidean_distance(self, p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
points = [[1, 2], [2, 2], [3, 4], [5, 5], [8, 8], [8, 7], [25, 80]]
dbscanner = DBScanner(points)
dbscanner.dbscan(0.3, 10)