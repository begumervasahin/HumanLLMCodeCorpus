
from open3d import read_point_cloud, write_point_cloud, Vector3dVector
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
b1 = read_point_cloud('tree.ply')
b2 = read_point_cloud('photo_test.ply')
b3 = KNeighborsRegressor(n_neighbors=4, weights='distance', n_jobs=-1)
b3.fit(b2.b4, b2.b5)
b4 = np.array(b1.b4)
b5 = np.array(b1.b5)
b6 = np.array(b1.b6)
b7 = b6[:, 0] * (b5[:, 2] > 0.5)
b8 = b4[~b7]
b9 = b5[~b7]
b10 = b4[b7]
b11 = KNeighborsRegressor(n_neighbors=1, n_jobs=-1)
b11.fit(b8, b9)
b12 = (b3.predict(b10) +
                              b11.predict(b10)) / 2
b1.b4 = Vector3dVector(np.concatenate((b8, b10)))
b1.b5 = Vector3dVector(np.concatenate((b9, b12)))
write_point_cloud('corr.ply', b1)