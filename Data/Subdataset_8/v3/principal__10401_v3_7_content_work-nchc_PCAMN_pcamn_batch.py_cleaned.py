import os
from subprocess import run
from sys import executable
import numpy as np
from sklearn.decomposition import PCA
from sklearn.externals.joblib import Parallel, delayed
from open3d import read_point_cloud
WORKING_DIRECTORY = 'N:/PATH/TO/WORKING/DIR'
NUM_JOBS = 8
def set_working_directory():
    os.chdir(WORKING_DIRECTORY)
def compute_log_variance(points):
    pca = PCA()
    pca.fit(points)
    pca.explained_variance_[:-1] -= pca.explained_variance_[1:]
    return np.log2(pca.explained_variance_)
def export_pca_results(ply_file, npy_file, output_file):
    voxel_points = np.array(read_point_cloud(ply_file).points)
    nearest_neighbors = np.load(npy_file)
    pca_results = Parallel(n_jobs=NUM_JOBS, verbose=1)(
        delayed(compute_log_variance)(voxel_points[n]) for n in nearest_neighbors)
    np.save(output_file, pca_results)
def run_scripts():
    scripts = ['concat.py', 'propagate.py', 'test.py', 'vis.py', 'treetop.py']
    for script in scripts:
        run((executable, script))
def main():
    set_working_directory()
    export_pca_results('vox1.ply', '128_1.npy', 'pca_1.npy')
    export_pca_results('vox2.ply', '128_2.npy', 'pca_2.npy')
    export_pca_results('vox4.ply', '128_4.npy', 'pca_4.npy')
    run_scripts()
if __name__ == "__main__":
    main()