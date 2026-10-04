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
def fonk2(ply_vox, npy_knn, temp_out, b4):
    b2 = array(read_point_cloud(ply_vox).points)
    b3 = load(npy_knn)
    save(temp_out, Parallel(b4 = b4, verbose=1)(
        delayed(log_var)(b2[n]) for n in b3))
    return None
def fonk3():
    b5 = int(input('b5: '))
    b6 = int(input('b6: '))
    b4 = input('b4: ')
    if not b4:
        b4 = 8
    else:
        b4 = int(b4)
    b7 = time()
    if b5 <= 0 <= b6:
        print('0: b2')
        import b2
        del b2
    if b5 <= 1 <= b6:
        print('1: mn')
        import mn
        del mn
    if b5 <= 2 <= b6:
        print('2: pcamn')
        fonk2('vox1.ply', '128_1.npy', 'pca_1.npy', b4)
        fonk2('vox2.ply', '128_2.npy', 'pca_2.npy', b4)
        fonk2('vox4.ply', '128_4.npy', 'pca_4.npy', b4)
    if b5 <= 3 <= b6:
        print('3: concat')
        import concat
        del concat
    if b5 <= 4 <= b6:
        print('4: propagate')
        import propagate
        del propagate
    if b5 <= 5 <= b6:
        print('5: test')
        import test
        del test
    if b5 <= 6 <= b6:
        print('6: vis')
        import vis
        del vis
    if b5 <= 7 <= b6:
        print('7: treetop')
        import treetop
        del treetop
    with open('time.txt', 'w') as w:
        w.write(f"{time() - b7} sec\n")
if b8 = = "__main__":
    fonk3()