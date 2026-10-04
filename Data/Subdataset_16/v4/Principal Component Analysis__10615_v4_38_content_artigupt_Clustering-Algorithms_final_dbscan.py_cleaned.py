from cluster import *
from pylab import *
class class1:
    def fonk1(self, b1):
        self.b1 = b1
        self.b2 = set()
        self.b3 = []
        self.b4 = []
        self.a1 = 0
    def fonk2(self, eps, min_pts):
        for point in self.b1:
            if point not in self.b2:
                self.b2.add(point)
                b5 = self.fonk4(point, eps)
                if len(b5) < min_pts:
                    self.b3.append(point)
                else:
                    b6 = f'Cluster{self.a1}'
                    b7 = Cluster(b6)
                    self.a1 += 1
                    self.fonk3(point, b5, b7, eps, min_pts)
    def fonk3(self, point, b5, cluster, eps, min_pts):
        cluster.add_point(point)
        a2 = 0
        while a2 < len(b5):
            b8 = b5[a2]
            if b8 not in self.b2:
                self.b2.add(b8)
                b9 = self.fonk4(b8, eps)
                if len(b9) >= min_pts:
                    b5.extend([n for n in b9 if n not already in b5])
            if not any(c.has(b8) for c in self.b4):
                cluster.add_point(b8)
            a2 += 1
        self.b4.append(cluster)
    def fonk4(self, point, eps):
        return [d for d in self.b1 if self.fonk5(d, point) <= eps]
    def fonk5(self, p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5
b10 = [[1,2], [2,2], [3,4], [5,5], [8,8], [8,7], [25,80]]
b11 = class1(b10)
b11.fonk2(0.3, 10)