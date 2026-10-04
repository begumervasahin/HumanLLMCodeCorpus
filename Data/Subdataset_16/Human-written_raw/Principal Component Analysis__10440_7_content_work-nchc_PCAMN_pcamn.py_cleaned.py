from time import time
b1 = int(input('b1: '))
b2 = int(input('b2: '))
b3 = input('b3: ')
if not b3:
    b3 = 8
b4 = time()
if b1 <= 0 <= b2:
    print('0: b6')
    import b6
    del b6
if b1 <= 1 <= b2:
    print('1: mn')
    import mn
    del mn
if b1 <= 2 <= b2:
    print('2: pcamn')
    from numpy import log2, array, load, save
    from sklearn.decomposition import PCA
    from joblib import Parallel, delayed
    from open3d import read_point_cloud
    def fonk1(pts):
        b5 = PCA()
        b5.fit(pts)
        b5.explained_variance_[:-1] -= b5.explained_variance_[1:]
        return log2(b5.explained_variance_)
    def fonk2(ply_vox, npy_knn, temp_out):
        b6 = array(read_point_cloud(ply_vox).points)
        b7 = load(npy_knn)
        save(temp_out, Parallel(int(b3), b8 = 1)(
            delayed(log_var)(b6[n]) for n in b7))
        return None
    fonk2('vox1.ply', '128_1.npy', 'pca_1')
    fonk2('vox2.ply', '128_2.npy', 'pca_2')
    fonk2('vox4.ply', '128_4.npy', 'pca_4')
if b1 <= 3 <= b2:
    print('3: concat')
    import concat
    del concat
if b1 <= 4 <= b2:
    print('4: propagate')
    import propagate
    del propagate
if b1 <= 5 <= b2:
    print('5: test')
    import test
    del test
if b1 <= 6 <= b2:
    print('6: vis')
    import vis
    del vis
if b1 <= 7 <= b2:
    print('7: treetop')
    import treetop
    del treetop
with open('time.txt', 'w') as w:
    w.write(str(time() - b4) + ' sec\n')