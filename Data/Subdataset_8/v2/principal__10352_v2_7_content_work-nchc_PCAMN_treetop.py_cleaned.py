
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
filter_condition = normals[:, 0] * (colors[:, 2] > 0.5)
filtered_points = points[~filter_condition]
filtered_colors = colors[~filter_condition]
abnormal_points = points[filter_condition]
abnormal_regressor = KNeighborsRegressor(n_neighbors=1, n_jobs=-1)
abnormal_regressor.fit(filtered_points, filtered_colors)
predicted_abnormal_colors = (calibration_regressor.predict(abnormal_points) +
                              abnormal_regressor.predict(abnormal_points)) / 2
cloud.points = Vector3dVector(np.concatenate((filtered_points, abnormal_points)))
cloud.colors = Vector3dVector(np.concatenate((filtered_colors, predicted_abnormal_colors)))
write_point_cloud('corr.ply', cloud)