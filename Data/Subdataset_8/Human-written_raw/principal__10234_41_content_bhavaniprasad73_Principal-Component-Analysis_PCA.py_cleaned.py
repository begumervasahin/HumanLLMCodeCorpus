import numpy.linalg as LA
from scipy import stats
import pandas as pd
import numpy as np
csv = pd.read_csv('C:/Users/ebhavaniprasad/Desktop/magic04.txt', header=None)
print("data structure : ", type(csv))
print("data with labels")
print(csv.head(3))
new_csv = csv[csv.columns[:-1]]
transp = new_csv.T
print("data without class labels")
print(new_csv.head(3))
df = transp
print("transposed data")
print(df)
df["sum"] = df.sum(axis=1)
print(df)
sum = df['sum']
print("the sum ")
print(sum)
df_new = df[df.columns[:-1]]
print(df_new)
n = len(df_new.columns)
print("N = ", len(df_new.columns))
mean = sum / n
m_df = mean.to_frame().T
print("m_df")
print(m_df)
print(type(df_new))
Trans = df_new.T
print(Trans)
print(Trans.shape)
print(m_df.shape)
diff = pd.DataFrame(Trans.values-m_df.values, columns=Trans.columns)
DT = diff.T
print("x-mhu")
print(DT)
DTP = DT.pow(2)
print(DT.pow(2))
DTP["sumsquare"] = DTP.sum(axis=1)
print(DTP)
ss = DTP['sumsquare']
DTP_new = DTP[DTP.columns[:-1]]
print(ss)
print("Variance")
variance = ss/n
print(variance)
sd = variance.pow(1./2)
print("Standard Deviation")
print(sd)
znor = DT.div(sd, axis='index')
print("z-nor")
print(znor)
print("library scipy")
print(stats.zscore(df, axis=1, ddof=1))
print("MEAN USING NUMPY BUILT-IN FUNCTION")
print(np.mean(csv))
print("MANUALLY CALCULATED MEAN")
print(mean)
print("VARIANCE USING NUMPY BUILT-IN FUNCTION", np.var(csv))
print("VARIANCE USING MANUAL CALCULATION", variance)
print("MANUALLY CALCULATED Z-SCORE")
znormal = znor.T
print(znormal)
csv3 = csv
csv5 = new_csv
csv4 = csv3.values
df_zscore = (csv5 - csv5.mean())/csv5.std()
print("Z-SCORE USING LIBRARY FUNCTION")
print(df_zscore)
znormal2 = znormal.copy()
print("Mean of the Z-Score Normalized Dataset")
print(znormal2.values.mean())
print("Standard Deviation of the Z-Score Normalized Dataset")
print(znormal2.values.std(ddof=1))
z_score2 = znor
z_score = znor
z_score["Z- score sum"] = z_score.sum(axis=1)
print('z-score mean')
print(z_score)
z_sum = z_score['Z- score sum']
print("The z-score sum ")
print(z_sum)
z_score_new = z_score[z_score.columns[:-1]]
print(z_score_new)
z_mean = z_sum/n
print('z-mean')
z_mean_df = z_mean.to_frame().T
print(type(z_mean_df))
print(z_mean_df.shape)
print(z_score_new)
z_data = z_score_new.T
diff2 = pd.DataFrame(z_data.values-z_mean_df.values, columns=Trans.columns)
zD = diff2
print('Z-Centered Data')
print(zD)
zDT = zD.T
print(zDT)
zD2 = zD
zDT2 = zDT
matri1 = zD2.values
matri2 = zDT2.values
print(type(matri1), "", matri1.shape)
print(type(matri2), "", matri2.shape)
prod = np.matmul(matri2, matri1)
cov_mat = prod/n
print("covariance matrix shape ", cov_mat.shape)
print("COVARIANCE MATRIX USING MANUAL CALCULATION ")
print(cov_mat)
print(z_data.shape)
z_data2 = z_data
result = z_data2.cov()
print("Dimension of the Covariance matrix : ", result.shape)
print("COVARIANCE MATRIX USING DATA FRAME COV() BUILT-IN FUNCTION ")
print(result)
cov_mat_new = np.copy(cov_mat)
d = cov_mat_new.shape[1]
x = np.random.rand(d, 1)
flag = True
count = 0
while(flag==True):
    y = cov_mat_new.dot(x)
    max_val = np.amax(abs(y))
    n = y / max_val
    p = n-x
    if(count<100):
        count = count + 1
    if(LA.norm(p)<0.000001):
        flag = False
    x = np.copy(n)
print("Iterations took for convergence : ", count)
norm_eigen = LA.norm(n)
unit_vect = n/norm_eigen
print("\n THE DOMINANT EIGEN VALUE FOR COVARIANCE MATRIX USING MANUAL CALCULATION")
print(max_val)
print("\n THE DOMINANT EIGEN VECTOR FOR COVARIANCE MATRIX USING MANUAL CALCULATION")
print(unit_vect)
print("\n The length of the Final Eigen Vector : ", LA.norm(unit_vect))
EValue, EVector = LA.eig(cov_mat_new)
print("\n EIGEN VALUES FOR COVARIANCE MATRIX USING BUILT-IN LIBRARY FUNCTION ")
print(EValue)
print("\n EIGEN VECTOR FOR COVARIANCE MATRIX USING BUILT-IN LIBRARY FUNCTION ")
print(EVector)
pos = EValue.argsort()[::-1]
EValue1 = EValue[pos]
EVector1 = EVector[:, pos]
print("Sorted Eigenvalues and respective Eigenvectors")
print("\n Before sorting the Eigenvalue")
print(EValue)
print("\n After sorting the Eigenvalue")
print(EValue1)
print("\n Before sorting the Eigenvector")
print(EVector)
print("\n After sorting the Eigenvector")
print(EVector1)
dom = 2
print("\n First Two Dominant Eigenvectors of Covariance Matrix")
dom_evect = EVector1[:, :dom]
print(dom_evect)
print(dom_evect.shape)
print(type(dom_evect))
zscore_copy = z_score_new.copy(deep=True)
print("zscore copy")
print(zscore_copy)
zscore_copy_transp = zscore_copy.T
zee_data = zscore_copy_transp.values
print(zee_data.shape)
proj_data = zee_data.dot(dom_evect)
print("data structure : ", type(proj_data), " shape : ", proj_data.shape)
print("\n projection of data points spanned by 2-dominant eigenvector")
print(proj_data)
eigen_2 = EValue1[0:dom]
esum = eigen_2.sum()
print("\n THE VARIANCE OF DATA POINTS ON PROJECTED SUBSPACE : ", esum)
V = EVector.copy()
print("edt")
print(V.shape)
W = V.T
print(W.shape)
L = np.diagflat(EValue)
print(L)
c1 = L.dot(W)
C = V.dot(c1)
print("\n COVARIANCE MATRIX IN EIGEN-DECOMPOSITION FORM UVUT")
print(C)
print("\n COVARIANCE MATRIX ")
print(cov_mat_new)
D = z_score_new.copy(deep=True)
def PCA(D, threshold):
    D2 = D.T
    print(D2)
    D3 = D2.values
    D4 = D.values
    N = D3.shape[0]
    sigma1 = D4.dot(D3)
    sigma2 = sigma1 / N
    print(sigma2.shape)
    eigenval, eigenvect = LA.eig(sigma2)
    indexes = eigenval.argsort()[::-1]
    eigenval1 = eigenval[indexes]
    eigenvect1 = eigenvect[:, indexes]
    print("Unsorted eigenvalues ", eigenval)
    print("Dominant eigenvalues ", eigenval1)
    total_variance = eigenval.sum()
    print("Total Variance ", total_variance)
    S = len(eigenval1)
    print("S", S)
    eig_count = 0
    flag2 = True
    for ele in range(S):
        percentage = [(i / total_variance) * 100 for i in eigenval1]
        position = np.cumsum(percentage)
        if (position[ele] >= threshold):
            break
            flag2 = False
            ele
        eig_count = eig_count + 1
    eig_count2 = eig_count + 1
    print("The number of eigevectors that preserves the variance of %d" %threshold, "% is",  eig_count2)
    print("eigen vector ", eigenvect1)
    eigenvect1_copy = eigenvect1.copy()
    eig_transpose = eigenvect1_copy.T
    Ur = eig_transpose[0:eig_count2, :]
    Ur2 = Ur.T
    a1 = z_score_new.copy()
    a2 = a1.T
    a3 = a2.values
    Reduced_data2 = a3.dot(Ur2)
    m = 10
    Ten_datapoint = Reduced_data2[0:m, :]
    print('COORDINATES OF THE FIRST TEN DATA POINTS')
    return Ten_datapoint, eigenval1, eig_count2, Reduced_data2
alpha = 95
Reduced_data, eigenvalue1, eigencount3, Reduced_data3 = PCA(D, alpha)
print(Reduced_data)
covariances5 = np.cov(Reduced_data3, bias=True, rowvar=False)
print("\n The Covariance Matrix of the Projected data points\n ")
print(covariances5)
Trace_covariance = np.trace(covariances5)
print(Trace_covariance)
princ_evalue = eigenvalue1[0:eigencount3, ]
sum_principal = princ_evalue.sum()
print("COVARIANCE OF THE PROJECTED DATA POINTS : ", Trace_covariance)
print("SUM OF THE EIGENVALUES CORRESPONDING TO THE PRINCIPAL VECTORS ON WHICH DATA IS PROJECTED : ", sum_principal)