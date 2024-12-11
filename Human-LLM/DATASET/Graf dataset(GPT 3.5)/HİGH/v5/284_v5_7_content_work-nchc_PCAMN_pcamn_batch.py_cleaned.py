import os
import subprocess
import numpy as np
from sklearn.decomposition import PCA
from sklearn.externals.joblib import Parallel, delayed
from open3d import read_point_cloud
b1 = 'N:/PATH/TO/WORKING/DIR'
os.chdir(b1)
a1 = 8
def fonk1(b4):
    b2 = PCA()
    b2.fit(b4)
    b3 = b2.explained_variance_[:-1] - b2.explained_variance_[1:]
    return np.log2(b3)
def fonk2(ply_file, knn_file, output_file):
    b4 = np.array(read_point_cloud(ply_file).b4)
    b5 = np.load(knn_file)
    Parallel(b6 = a1, verbose=1)(
        delayed(save_pca)(b4[neighbor_indices], output_file.format(i))
        for i, neighbor_indices in enumerate(b5)
    )
def fonk3(b4, output_file):
    b7 = fonk1(b4)
    np.save(output_file, b7)
fonk2('vox1.ply', '128_1.npy', 'pca_{}.npy')
fonk2('vox2.ply', '128_2.npy', 'pca_{}.npy')
fonk2('vox4.ply', '128_4.npy', 'pca_{}.npy')
subprocess.run([executable, 'concat.py'])
subprocess.run([executable, 'propagate.py'])
subprocess.run([executable, 'test.py'])
subprocess.run([executable, 'vis.py'])
subprocess.run([executable, 'treetop.py'])