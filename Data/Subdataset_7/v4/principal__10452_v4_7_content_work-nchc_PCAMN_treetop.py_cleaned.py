
from open3d import read_point_cloud, write_point_cloud, Vector3dVector
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
b1 = read_point_cloud('tree.ply')
b2 = read_point_cloud('photo_test.ply')
b3 = KNeighborsRegressor(b12=4, weights='distance', n_jobs=-1)
b3.fit(b2.b13, b2.b14)
b4 = np.array(b1.b13)
b5 = np.array(b1.b14)
b6 = np.array(b1.b15)
b7 = b6[:, 0] * (b5[:, 2] > 0.5)
b8 = b4[~b7]
b9 = b5[~b7]
b10 = b4[b7]
b11 = (b3.predict(b10) +
                   KNeighborsRegressor(b12 = 1, n_jobs=-1).fit(b8, b9).predict(b10)) / 2
b1.b13 = Vector3dVector(np.concatenate((b8, b10)))
b1.b14 = Vector3dVector(np.concatenate((b9, b11)))
b1.b15 = Vector3dVector()
write_point_cloud('corrected_tree.ply', b1)