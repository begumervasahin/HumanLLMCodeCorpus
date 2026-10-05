
from open3d import read_point_cloud, write_point_cloud, Vector3dVector
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
tree_cloud = read_point_cloud('tree.ply')
calibrate_cloud = read_point_cloud('photo_test.ply')
calibrate_neigh = KNeighborsRegressor(n_neighbors=4, weights='distance', n_jobs=-1)
calibrate_neigh.fit(calibrate_cloud.points, calibrate_cloud.colors)
tree_points = np.array(tree_cloud.points)
tree_colors = np.array(tree_cloud.colors)
tree_normals = np.array(tree_cloud.normals)
filter_condition = tree_normals[:, 0] * (tree_colors[:, 2] > 0.5)
filtered_points = tree_points[~filter_condition]
filtered_colors = tree_colors[~filter_condition]
abnormal_points = tree_points[filter_condition]
abnormal_colors = (calibrate_neigh.predict(abnormal_points) +
                   KNeighborsRegressor(n_neighbors=1, n_jobs=-1).fit(filtered_points, filtered_colors).predict(abnormal_points)) / 2
tree_cloud.points = Vector3dVector(np.concatenate((filtered_points, abnormal_points)))
tree_cloud.colors = Vector3dVector(np.concatenate((filtered_colors, abnormal_colors)))
tree_cloud.normals = Vector3dVector()
write_point_cloud('corrected_tree.ply', tree_cloud)