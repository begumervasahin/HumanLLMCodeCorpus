import os
from subprocess import run
from sys import executable
import numpy as np
from sklearn.decomposition import PCA
from sklearn.externals.joblib import Parallel, delayed
from open3d import read_point_cloud
def main():
    os.chdir('N:/PATH/TO/WORKING/DIR')
    n_jobs = 8
    def log_variance(points):
        pca = PCA()
        pca.fit(points)
        pca.explained_variance_[:-1] -= pca.explained_variance_[1:]
        return np.log2(pca.explained_variance_)
    def export_pca(ply_file, npy_file, output_file):
        voxel_points = np.array(read_point_cloud(ply_file).points)
        nearest_neighbors = np.load(npy_file)
        pca_results = Parallel(n_jobs=n_jobs, verbose=1)(
            delayed(log_variance)(voxel_points[n]) for n in nearest_neighbors)
        np.save(output_file, pca_results)
    export_pca('vox1.ply', '128_1.npy', 'pca_1.npy')
    export_pca('vox2.ply', '128_2.npy', 'pca_2.npy')
    export_pca('vox4.ply', '128_4.npy', 'pca_4.npy')
    run((executable, 'concat.py'))
    run((executable, 'propagate.py'))
    run((executable, 'test.py'))
    run((executable, 'vis.py'))
    run((executable, 'treetop.py'))
if __name__ == "__main__":
    main()