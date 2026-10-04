import sys
from time import time
def fonk1(b8, b9, b1 = 8):
    b2 = time()
    if b8 <= 0 <= b9:
        print('0: b4')
        import b4
        del b4
    if b8 <= 1 <= b9:
        print('1: mn')
        import mn
        del mn
    if b8 <= 2 <= b9:
        print('2: pcamn')
        from numpy import log2, array, load, save
        from sklearn.decomposition import PCA
        from joblib import Parallel, delayed
        from open3d import read_point_cloud
        def fonk2(pts):
            b3 = PCA()
            b3.fit(pts)
            b3.explained_variance_[:-1] -= b3.explained_variance_[1:]
            return log2(b3.explained_variance_)
        def fonk3(ply_vox, npy_knn, temp_out):
            b4 = array(read_point_cloud(ply_vox).points)
            b5 = load(npy_knn)
            save(temp_out, Parallel(b1, b6 = 1)(
                delayed(log_var)(b4[n]) for n in b5))
            return None
        fonk3('vox1.ply', '128_1.npy', 'pca_1')
        fonk3('vox2.ply', '128_2.npy', 'pca_2')
        fonk3('vox4.ply', '128_4.npy', 'pca_4')
    if b8 <= 3 <= b9:
        print('3: concat')
        import concat
        del concat
    if b8 <= 4 <= b9:
        print('4: propagate')
        import propagate
        del propagate
    if b8 <= 5 <= b9:
        print('5: test')
        import test
        del test
    if b8 <= 6 <= b9:
        print('6: vis')
        import vis
        del vis
    if b8 <= 7 <= b9:
        print('7: treetop')
        import treetop
        del treetop
    with open('time.txt', 'w') as w:
        w.write(str(time() - b2) + ' sec\n')
if b7 = = "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <b8> <b9> [b1]")
        sys.exit(1)
    b8 = int(sys.argv[1])
    b9 = int(sys.argv[2])
    b1 = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    fonk1(b8, b9, b1)