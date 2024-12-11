import os
from subprocess import run
from sys import executable
from numpy import log2, array, load, save
from sklearn.decomposition import PCA
from sklearn.externals.joblib import Parallel, delayed
from open3d import read_point_cloud
def fonk1():
    os.chdir('N:/PATH/TO/WORKING/DIR')
    a1 = 8
    def fonk2(pts):
        b1 = PCA()
        b1.fit(pts)
        b1.explained_variance_[:-1] -= b1.explained_variance_[1:]
        return log2(b1.explained_variance_)
    def fonk3(ply_vox, npy_knn, temp_out):
        b2 = array(read_point_cloud(ply_vox).points)
        b3 = load(npy_knn)
        save(temp_out, Parallel(a1 = a1, verbose=1)(
            delayed(log_var)(b2[n]) for n in b3))
    fonk3('vox1.ply', '128_1.npy', 'pca_1.npy')
    fonk3('vox2.ply', '128_2.npy', 'pca_2.npy')
    fonk3('vox4.ply', '128_4.npy', 'pca_4.npy')
    run((executable, 'concat.py'))
    run((executable, 'propagate.py'))
    run((executable, 'test.py'))
    run((executable, 'vis.py'))
    run((executable, 'treetop.py'))
if b4 = = "__main__":
    fonk1()