
from open3d import read_point_cloud, write_point_cloud, Vector3dVector
from sklearn.neighbors import KNeighborsRegressor
import numpy as np
def read_point_cloud_file(file_path):
    return read_point_cloud(file_path)
def calibrate_model(calibrate_cloud):
    calibrate_neigh = KNeighborsRegressor(n_neighbors=4, weights='distance', n_jobs=-1)
    calibrate_neigh.fit(calibrate_cloud.points, calibrate_cloud.colors)
    return calibrate_neigh
def filter_abnormal_points(tree_points, tree_colors, tree_normals):
    filter_condition = tree_normals[:, 0] * (tree_colors[:, 2] > 0.5)
    filtered_points = tree_points[~filter_condition]
    filtered_colors = tree_colors[~filter_condition]
    abnormal_points = tree_points[filter_condition]
    return filtered_points, filtered_colors, abnormal_points
def predict_abnormal_colors(abnormal_points, filtered_points, filtered_colors, calibrate_neigh):
    abnormal_colors = (calibrate_neigh.predict(abnormal_points) +
                       KNeighborsRegressor(n_neighbors=1, n_jobs=-1).fit(filtered_points, filtered_colors).predict(abnormal_points)) / 2
    return abnormal_colors
def update_point_cloud(tree_cloud, filtered_points, filtered_colors, abnormal_points, abnormal_colors):
    tree_cloud.points = Vector3dVector(np.concatenate((filtered_points, abnormal_points)))
    tree_cloud.colors = Vector3dVector(np.concatenate((filtered_colors, abnormal_colors)))
    tree_cloud.normals = Vector3dVector()
def write_corrected_point_cloud(tree_cloud, output_file_path):
    write_point_cloud(output_file_path, tree_cloud)
def main():
    tree_cloud = read_point_cloud_file('tree.ply')
    calibrate_cloud = read_point_cloud_file('photo_test.ply')
    calibrate_neigh = calibrate_model(calibrate_cloud)
    tree_points = np.array(tree_cloud.points)
    tree_colors = np.array(tree_cloud.colors)
    tree_normals = np.array(tree_cloud.normals)
    filtered_points, filtered_colors, abnormal_points = filter_abnormal_points(tree_points, tree_colors, tree_normals)
    abnormal_colors = predict_abnormal_colors(abnormal_points, filtered_points, filtered_colors, calibrate_neigh)
    update_point_cloud(tree_cloud, filtered_points, filtered_colors, abnormal_points, abnormal_colors)
    write_corrected_point_cloud(tree_cloud, 'corrected_tree.ply')
if __name__ == "__main__":
    main()