import os
from subprocess import run
from sys import executable
import numpy as np
from sklearn.decomposition import PCA
from sklearn.externals.joblib import Parallel, delayed
from open3d import read_point_cloud
def fonk1():
    os.chdir('N:/PATH/TO/WORKING/DIR')
    a1 = 8
    def fonk2(points):
        b1 = PCA()
        b1.fit(points)
        b1.explained_variance_[:-1] -= b1.explained_variance_[1:]
        return np.log2(b1.explained_variance_)
    def fonk3(ply_file, npy_file, output_file):
        b2 = np.array(read_point_cloud(ply_file).points)
        b3 = np.load(npy_file)
        b4 = Parallel(a1=a1, verbose=1)(
            delayed(log_variance)(b2[n]) for n in b3)
        np.save(output_file, b4)
    fonk3('vox1.ply', '128_1.npy', 'pca_1.npy')
    fonk3('vox2.ply', '128_2.npy', 'pca_2.npy')
    fonk3('vox4.ply', '128_4.npy', 'pca_4.npy')
    run((executable, 'concat.py'))
    run((executable, 'propagate.py'))
    run((executable, 'test.py'))
    run((executable, 'vis.py'))
    run((executable, 'treetop.py'))
if b5 = = "__main__":
    fonk1()