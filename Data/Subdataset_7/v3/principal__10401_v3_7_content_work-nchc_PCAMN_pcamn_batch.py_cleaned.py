import os
from subprocess import run
from sys import executable
import numpy as np
from sklearn.decomposition import PCA
from sklearn.externals.joblib import Parallel, delayed
from open3d import read_point_cloud
b1 = 'N:/PATH/TO/WORKING/DIR'
a1 = 8
def fonk1():
    os.chdir(b1)
def fonk2(points):
    b2 = PCA()
    b2.fit(points)
    b2.explained_variance_[:-1] -= b2.explained_variance_[1:]
    return np.log2(b2.explained_variance_)
def fonk3(ply_file, npy_file, output_file):
    b3 = np.array(read_point_cloud(ply_file).points)
    b4 = np.load(npy_file)
    b5 = Parallel(n_jobs=a1, verbose=1)(
        delayed(compute_log_variance)(b3[n]) for n in b4)
    np.save(output_file, b5)
def fonk4():
    b6 = ['concat.py', 'propagate.py', 'test.py', 'vis.py', 'treetop.py']
    for script in b6:
        run((executable, script))
def fonk5():
    fonk1()
    fonk3('vox1.ply', '128_1.npy', 'pca_1.npy')
    fonk3('vox2.ply', '128_2.npy', 'pca_2.npy')
    fonk3('vox4.ply', '128_4.npy', 'pca_4.npy')
    fonk4()
if b7 = = "__main__":
    fonk5()