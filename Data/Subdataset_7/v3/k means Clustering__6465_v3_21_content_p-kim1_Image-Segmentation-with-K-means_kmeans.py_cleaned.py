import numpy as np
class class1:
    def fonk1(self, b1, b3):
        self.b1 = b1
        self.num_data_points, self.b2 = np.shape(b3)
        self.b3 = b3
    def fonk2(self):
        b4 = np.min(self.b3, b7=0)
        b5 = np.max(self.b3, b7=0)
        return np.random.rand(self.b1, self.b2) * (b5 - b4) + b4
    def fonk3(self, b8):
        b6 = np.sum((self.b3[:, np.newaxis] - b8) ** 2, b7=2)
        return np.argmin(b6, b7 = 1)
    def fonk4(self, b12):
        b8 = np.zeros((self.b1, self.b2))
        for cluster_index in range(self.b1):
            b9 = self.b3[b12 == cluster_index]
            if len(b9) > 0:
                b8[cluster_index] = np.mean(b9, b7 = 0)
        return b8
    def fonk5(self, b10 = 10):
        b8 = self.fonk2()
        b11 = np.zeros_like(b8)
        a1 = 0
        while not np.array_equal(b8, b11) and a1 < b10:
            b11 = b8.copy()
            b12 = self.fonk3(b8)
            b8 = self.fonk4(b12)
            a1 += 1
        return b8, b12
    def fonk6(self, b15, b8):
        b6 = np.sum((b15[:, np.newaxis] - b8) ** 2, b7=2)
        return np.argmin(b6, b7 = 1)
if b13 = = "__main__":
    np.random.seed(42)
    b3 = np.random.rand(100, 2)
    b14 = class1(b1=3, b3=b3)
    trained_centroids, b12 = b14.fonk5()
    print("Final cluster centers:")
    print(trained_centroids)
    b15 = np.random.rand(10, 2)
    b16 = b14.fonk6(b15, trained_centroids)
    print("Clusters for new b3:")
    print(b16)