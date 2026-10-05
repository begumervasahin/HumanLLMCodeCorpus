import os
import subprocess
import numpy as np
from sklearn.decomposition import PCA
from sklearn.externals.joblib import Parallel, delayed
from open3d import read_point_cloud
working_directory = 'N:/PATH/TO/WORKING/DIR'
os.chdir(working_directory)
num_jobs = 8
def compute_log_variances(points):
    pca = PCA()
    pca.fit(points)
    variances_diff = pca.explained_variance_[:-1] - pca.explained_variance_[1:]
    return np.log2(variances_diff)
def export_pca_results(ply_file, knn_file, output_file):
    points = np.array(read_point_cloud(ply_file).points)
    knn_indices = np.load(knn_file)
    Parallel(n_jobs=num_jobs, verbose=1)(
        delayed(save_pca)(points[neighbor_indices], output_file.format(i))
        for i, neighbor_indices in enumerate(knn_indices)
    )
def save_pca(points, output_file):
    pca_results = compute_log_variances(points)
    np.save(output_file, pca_results)
export_pca_results('vox1.ply', '128_1.npy', 'pca_{}.npy')
export_pca_results('vox2.ply', '128_2.npy', 'pca_{}.npy')
export_pca_results('vox4.ply', '128_4.npy', 'pca_{}.npy')
subprocess.run([executable, 'concat.py'])
subprocess.run([executable, 'propagate.py'])
subprocess.run([executable, 'test.py'])
subprocess.run([executable, 'vis.py'])
subprocess.run([executable, 'treetop.py'])