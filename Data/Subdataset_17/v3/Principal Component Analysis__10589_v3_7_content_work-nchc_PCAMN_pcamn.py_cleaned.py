import sys
from time import time
from numpy import log2, array, load, save
from sklearn.decomposition import PCA
from joblib import Parallel, delayed
from open3d import read_point_cloud
def log_var(pts):
    pca = PCA()
    pca.fit(pts)
    pca.explained_variance_[:-1] -= pca.explained_variance_[1:]
    return log2(pca.explained_variance_)
def export_pca(ply_vox, npy_knn, temp_out, n_jobs):
    vox = array(read_point_cloud(ply_vox).points)
    knn = load(npy_knn)
    save(temp_out, Parallel(n_jobs, verbose=1)(
        delayed(log_var)(vox[n]) for n in knn))
def main(begin, end, n_jobs):
    start_time = time()
    steps = [
        ('0: vox', 'vox'),
        ('1: mn', 'mn'),
        ('2: pcamn', perform_pca_tasks),
        ('3: concat', 'concat'),
        ('4: propagate', 'propagate'),
        ('5: test', 'test'),
        ('6: vis', 'vis'),
        ('7: treetop', 'treetop')
    ]
    for step_num, step_action in steps:
        if begin <= int(step_num[0]) <= end:
            print(step_num)
            if callable(step_action):
                step_action(n_jobs)
            else:
                module = __import__(step_action)
                del module
    with open('time.txt', 'w') as file:
        file.write(f'{time() - start_time} sec\n')
def perform_pca_tasks(n_jobs):
    export_pca('vox1.ply', '128_1.npy', 'pca_1', n_jobs)
    export_pca('vox2.ply', '128_2.npy', 'pca_2', n_jobs)
    export_pca('vox4.ply', '128_4.npy', 'pca_4', n_jobs)
if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python script.py <begin> <end> [n_jobs]")
        sys.exit(1)
    begin = int(sys.argv[1])
    end = int(sys.argv[2])
    n_jobs = int(sys.argv[3]) if len(sys.argv) > 3 else 8
    main(begin, end, n_jobs)