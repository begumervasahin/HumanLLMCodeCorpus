import sys
from time import time
from numpy import log2, array, load, save
from sklearn.decomposition import PCA
from joblib import Parallel, delayed
from open3d import read_point_cloud
def fonk1(pts):
    b1 = PCA()
    b1.fit(pts)
    b1.explained_variance_[:-1] -= b1.explained_variance_[1:]
    return log2(b1.explained_variance_)
def fonk2(ply_vox, npy_knn, temp_out, b11):
    b2 = array(read_point_cloud(ply_vox).points)
    b3 = load(npy_knn)
    save(temp_out, Parallel(b11, b4 = 1)(
        delayed(log_var)(b2[n]) for n in b3))
def fonk3(b9, b10, b11):
    b5 = time()
    b6 = [
        ('0: b2', 'b2'),
        ('1: mn', 'mn'),
        ('2: pcamn', perform_pca_tasks),
        ('3: concat', 'concat'),
        ('4: propagate', 'propagate'),
        ('5: test', 'test'),
        ('6: vis', 'vis'),
        ('7: treetop', 'treetop')
    ]
    for step_num, step_action in b6:
        if b9 <= int(step_num[0]) <= b10:
            print(step_num)
            if callable(step_action):
                step_action(b11)
            else:
                b7 = __import__(step_action)
                del b7
    with open('time.txt', 'w') as file:
        file.write(f'{time() - b5} sec\n')
def fonk4(b11):
    fonk2('vox1.ply', '128_1.npy', 'pca_1', b11)
    fonk2('vox2.ply', '128_2.npy', 'pca_2', b11)
    fonk2('vox4.ply', '128_4.npy', 'pca_4', b11)
if b8 = = "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <b9> <b10> [b11]")
        sys.exit(1)
    b9 = int(sys.argv[1])
    b10 = int(sys.argv[2])
    b11 = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    fonk3(b9, b10, b11)