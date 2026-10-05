import sys
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage.color import rgb2gray
import skimage.filters as filt
from numpy import linalg as LA
from sklearn.preprocessing import StandardScaler
def EM_algorithm(Y, initial_Ps, initial_p, initial_q):
    max_iterations = 20
    num_samples = len(Y)
    mu0 = (initial_Ps*(1-initial_p))/((initial_Ps*(1-initial_p)) + (1-initial_Ps)*(1-initial_q))
    mu1 = (initial_Ps*initial_p)/((initial_Ps*initial_p) + (1-initial_Ps)*initial_q)
    mean_mu = np.mean([mu0 if y == 0 else mu1 for y in Y])
    print("\nInitial parameters:")
    print("Pie(0)=", initial_Ps)
    print("p(0)=", initial_p)
    print("q(0)=", initial_q)
    print("\nmu(1) for Y=0:", mu0)
    print("mu(1) for Y=1:", mu1)
    print("Initial mean mu=", mean_mu)
    for iteration in range(1, max_iterations + 1):
        Ps_sum = sum(mu0 if y == 0 else mu1 for y in Y)
        Ps = Ps_sum / 10
        p_num = sum(mu1 for y in Y if y == 1)
        p_den = sum(mu1 if y == 1 else mu0 for y in Y)
        p = p_num / p_den
        q_num = sum(1-mu1 for y in Y if y == 1)
        q_den = sum(1-mu1 if y == 1 else 1-mu0 for y in Y)
        q = q_num / q_den
        mu0 = (Ps*(1-p))/((Ps*(1-p)) + (1-Ps)*(1-q))
        mu1 = (Ps*p)/((Ps*p) + (1-Ps)*q)
        mean_mu = np.mean([mu0 if y == 0 else mu1 for y in Y])
        print("\nIteration:", iteration)
        print("Pie({})=".format(iteration), Ps)
        print("p({})=".format(iteration), p)
        print("q({})=".format(iteration), q)
        print("mu({}) for Y=0:".format(iteration), mu0)
        print("mu({}) for Y=1:".format(iteration), mu1)
        print("Mean mu({})=".format(iteration), mean_mu)
def process_image(in_fname, debug=False):
    x_in = np.array(Image.open(in_fname))
    x_gray = 1.0 - rgb2gray(x_in)
    if debug:
        plt.figure(1)
        plt.imshow(x_gray)
        plt.title('original grayscale image')
        plt.show()
    thresh = filt.threshold_minimum(x_gray)
    fg = x_gray > thresh
    if debug:
        plt.figure(2)
        plt.imshow(fg)
        plt.title('binarized image')
        plt.show()
    nz_r, nz_c = fg.nonzero()
    n_r, n_c = fg.shape
    l, r = max(0, min(nz_c)-1), min(n_c-1, max(nz_c)+1)+1
    t, b = max(0, min(nz_r)-1), min(n_r-1, max(nz_r)+1)+1
    win = fg[t:b, l:r]
    if debug:
        plt.figure(3)
        plt.imshow(win)
        plt.title('windowed image')
        plt.show()
    max_dim = max(win.shape)
    new_r = int(round(win.shape[0]/max_dim*48))
    new_c = int(round(win.shape[1]/max_dim*48))
    win_img = Image.fromarray(win.astype(np.uint8)*255)
    resize_img = win_img.resize((new_c, new_r))
    resize_win = np.array(resize_img).astype(bool)
    out_win = np.zeros((resize_win.shape[0]+2, resize_win.shape[1]+2), dtype=bool)
    out_win[1:-1, 1:-1] = resize_win
    if debug:
        plt.figure(4)
        plt.imshow(out_win, cmap='Greys')
        plt.title('resized windowed image')
        plt.show()
    return out_win
if __name__ == '__main__':
    X = np.array([(2,3,3,4,5,7), (2,4,5,5,6,8)])
    sc = StandardScaler()
    X_std = sc.fit_transform(X.T)
    X_std = X_std.T
    cov_X = np.cov(X_std)
    w, v = LA.eig(X.T@X)
    w1, v1 = LA.eig(X@X.T)
    w2, v2 = LA.eig(cov_X)
    eigen_pairs = [(np.abs(w2[i]), v2[:,i]) for i in range(len(w2))]
    eigen_pairs.sort(reverse=True)
    PM = eigen_pairs[0][1][:, np.newaxis]
    X_pca = X_std.T.dot(PM)
    X_pca = X_pca.T
    print ("*****PCA*******\n")
    print ("Question 1")
    print ("\nEigen values of X.T@X are:")
    print (w)
    print ("\n")
    print ("Question 2\n")
    print ("Eigenvalues of X@X.T are:")
    print (w1)
    print ("\n")
    print ("Eigenvectors of X@X.T are:")
    print (v1)
    print ("\n")
    print ("Question 4\n")
    print('Shape of transformed data:\n', X_pca.shape)
    print('\nTransformed data after dimension reduction:\n', X_pca)
    print ("\n*****EM*******")
    Y = np.array([1, 1, 0, 1, 0, 0, 1, 0, 1, 1])
    EM_algorithm(Y, initial_Ps=0.4, initial_p=0.6, initial_q=0.7)
    print("\n\n")
    EM_algorithm(Y, initial_Ps=0.5, initial_p=0.5, initial_q=0.5)