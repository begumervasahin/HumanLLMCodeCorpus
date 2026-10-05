
from open3d import read_point_cloud, write_point_cloud, Vector3dVector
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
cloud = read_point_cloud('tree.ply')
calibrate = read_point_cloud('photo_test.ply')
calibration_regressor = KNeighborsRegressor(n_neighbors=4, weights='distance', n_jobs=-1)
calibration_regressor.fit(calibrate.points, calibrate.colors)
points = np.array(cloud.points)
colors = np.array(cloud.colors)
normals = np.array(cloud.normals)
is_abnormal = normals[:, 0] * (colors[:, 2] > 0.5)
normal_points = points[~is_abnormal]
normal_colors = colors[~is_abnormal]
abnormal_points = points[is_abnormal]
normal_regressor = KNeighborsRegressor(n_neighbors=1, n_jobs=-1)
normal_regressor.fit(normal_points, normal_colors)
predicted_abnormal_colors = (calibration_regressor.predict(abnormal_points) +
                              normal_regressor.predict(abnormal_points)) / 2
cloud.points = Vector3dVector(np.concatenate((normal_points, abnormal_points)))
cloud.colors = Vector3dVector(np.concatenate((normal_colors, predicted_abnormal_colors)))
write_point_cloud('corr.ply', cloud)