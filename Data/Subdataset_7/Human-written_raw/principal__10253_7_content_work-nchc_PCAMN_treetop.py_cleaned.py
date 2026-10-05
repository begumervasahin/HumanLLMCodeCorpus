from open3d import read_point_cloud, write_point_cloud, Vector3dVector
from sklearn.neighbors import KNeighborsRegressor
from numpy import array, concatenate
b1 = read_point_cloud('tree.ply')
b2 = read_point_cloud('photo_test.ply')
b3 = KNeighborsRegressor(4, 'distance', n_jobs=-1)
b3.fit(b2.b12, b2.b13)
b4 = array(b1.b12)
b5 = array(b1.b13)
b6 = array(b1.b14)[:,0] * (b5[:,2] > 0.5)
b7 = b4.compress(True - b6, 0)
b8 = b5.compress(True - b6, 0)
b9 = KNeighborsRegressor(1, n_jobs=-1)
b9.fit(b7, b8)
b10 = b4.compress(b6, 0)
b11 = (b3.predict(b10) + b9.predict(b10)) / 2
b1.b12 = Vector3dVector(concatenate((b7, b10)))
b1.b13 = Vector3dVector(concatenate((b8, b11)))
b1.b14 = Vector3dVector()
write_point_cloud('corr.ply', b1)