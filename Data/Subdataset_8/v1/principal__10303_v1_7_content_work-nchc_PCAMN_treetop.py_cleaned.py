from open3d import read_point_cloud, write_point_cloud, Vector3dVector
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
cloud = read_point_cloud('tree.ply')
calibrate = read_point_cloud('photo_test.ply')
neigh0 = KNeighborsRegressor(n_neighbors=4, weights='distance', n_jobs=-1)
neigh0.fit(calibrate.points, calibrate.colors)
arr_points = np.array(cloud.points)
arr_colors = np.array(cloud.colors)
arr_normals = np.array(cloud.normals)
arr_filter = arr_normals[:, 0] * (arr_colors[:, 2] > 0.5)
points_other = arr_points[~arr_filter]
colors_other = arr_colors[~arr_filter]
points_abn = arr_points[arr_filter]
neigh1 = KNeighborsRegressor(n_neighbors=1, n_jobs=-1)
neigh1.fit(points_other, colors_other)
colors_abn = (neigh0.predict(points_abn) + neigh1.predict(points_abn)) / 2
cloud.points = Vector3dVector(np.concatenate((points_other, points_abn)))
cloud.colors = Vector3dVector(np.concatenate((colors_other, colors_abn)))
write_point_cloud('corr.ply', cloud)