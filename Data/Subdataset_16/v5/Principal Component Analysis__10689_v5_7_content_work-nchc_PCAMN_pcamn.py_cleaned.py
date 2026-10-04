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
def fonk2(ply_vox, npy_knn, temp_out, b8):
    b2 = array(read_point_cloud(ply_vox).points)
    b3 = load(npy_knn)
    b4 = Parallel(b8=b8, verbose=1)(
        delayed(log_var)(b2[n]) for n in b3
    )
    save(temp_out, b4)
def fonk3(module_name):
    b5 = __import__(module_name)
    del b5
def fonk4():
    b6 = int(input('b6: '))
    b7 = int(input('b7: '))
    b8 = input('b8: ')
    b8 = int(b8) if b8 else 8
    b9 = time()
    b10 = [
        ('0: b2', 'b2'),
        ('1: mn', 'mn'),
        ('2: pcamn', export_pca, [
            ('vox1.ply', '128_1.npy', 'pca_1.npy', b8),
            ('vox2.ply', '128_2.npy', 'pca_2.npy', b8),
            ('vox4.ply', '128_4.npy', 'pca_4.npy', b8)
        ]),
        ('3: concat', 'concat'),
        ('4: propagate', 'propagate'),
        ('5: test', 'test'),
        ('6: vis', 'vis'),
        ('7: treetop', 'treetop')
    ]
    for step_name, module_or_func, *args in b10:
        b11 = int(step_name.split(':')[0])
        if b6 <= b11 <= b7:
            print(step_name)
            if isinstance(module_or_func, str):
                fonk3(module_or_func)
            else:
                for arg in args[0]:
                    module_or_func(*arg)
    b12 = time() - b9
    with open('time.txt', 'w') as w:
        w.write(f"{b12:.2f} sec\n")
if b13 = = "__main__":
    fonk4()