import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics
import math
from scipy.stats import norm
import matplotlib.patches as mpatches
def fonk1(tsize0,tsize1):
    b1 = [1,0]
    b2 = [0,1]
    b3 = [[1,0.75],[0.75,1] ]
    b4 = [[1,0.75],[0.75,1] ]
    b5 = tsize0
    b6 = tsize1
    b7 = {1: 'r', 2: 'g', 3: 'b',4:'b42',5:'pink',6:'brown'}
    x1,b8 = np.random.multivariate_normal(b1, b3, b5).T
    x2,b9 = np.random.multivariate_normal(b2, b4, b6).T
    x3,b10 = np.random.multivariate_normal(b1, b3, 100).T
    x4,b11 = np.random.multivariate_normal(b2, b4, 100).T
    b12 = np.mean(x1)
    b13 = np.mean(b8)
    b14 = np.std(x1)
    b15 = np.std(b8)
    b16 = np.mean(x2)
    b17 = np.mean(b9)
    b18 = np.std(x2)
    b19 = np.std(b9)
    b20 = {'b41':x1,'b42':b8,'label':np.zeros(len(x1),dtype=int)}
    b21 = pd.DataFrame(data=b20)
    b20 = {'b41':x2,'b42':b9,'label':np.ones(len(x2),dtype=int)}
    b21 = b21.append(pd.DataFrame(data=b20))
    b20 = {'b41':x3,'b42':b10,'actual':np.zeros(len(x3),dtype=int)}
    b22 = pd.DataFrame(data=b20)
    b20 = {'b41':x4,'b42':b11,'actual':np.ones(len(x4),dtype=int)}
    b22 = b22.append(pd.DataFrame(data=b20))
    b23 = b5/(b5+b6)
    b24 = b6/(b5+b6)
    b25 = norm.pdf(b22['b41'],loc=b12,scale=b14)*norm.pdf(b22['b42'],loc=b13,scale=b15)
    b26 = norm.pdf(b22['b41'],loc=b16,scale=b18)*norm.pdf(b22['b42'],loc=b17,scale=b19)
    b27 = b25*b23
    b28 = b26*b24
    b22['b27'] = b27
    b22['b28']=b28
    b22['pred']=b22[["b27", "b28"]].max(b29 = 1)
    b22.loc[b22.pred > b28, 'b30'] = 0
    b22.loc[b22.pred > b27, 'b30'] = 1
    b22.loc[b22.pred > b28, 'b40'] = 'r'
    b22.loc[b22.pred > b27, 'b40'] = 'b'
    b22.loc[np.logical_and(b22.b30 = =0, b22.actual==0),'true_negative']=1
    b22.loc[np.logical_and(b22.b30 = =0, b22.actual==1),'true_negative']=0
    b22.loc[np.logical_and(b22.b30 = =1, b22.actual==1),'true_negative']=0
    b22.loc[np.logical_and(b22.b30 = =1, b22.actual==0),'true_negative']=0
    b22.loc[np.logical_and(b22.b30 = =1, b22.actual==1),'true_positive']=1
    b22.loc[np.logical_and(b22.b30 = =1, b22.actual==0),'true_positive']=0
    b22.loc[np.logical_and(b22.b30 = =0, b22.actual==0),'true_positive']=0
    b22.loc[np.logical_and(b22.b30 = =0, b22.actual==1),'true_positive']=0
    b22.fillna(0)
    b22.loc[np.logical_and(b22.b30 = =0, b22.actual==1),'false_positive']=1
    b22.loc[np.logical_and(b22.b30 = =0, b22.actual==0),'false_positive']=0
    b22.loc[np.logical_and(b22.b30 = =1, b22.actual==0),'false_positive']=0
    b22.loc[np.logical_and(b22.b30 = =1, b22.actual==1),'false_positive']=0
    b22.fillna(0)
    b22.loc[np.logical_and(b22.b30 = =1, b22.actual==0),'false_negative']=1
    b22.loc[np.logical_and(b22.b30 = =0, b22.actual==1),'false_negative']=0
    b22.loc[np.logical_and(b22.b30 = =1, b22.actual==1),'false_negative']=0
    b22.loc[np.logical_and(b22.b30 = =0, b22.actual==0),'false_negative']=0
    b22.fillna(0)
    b31 = b22.true_negative.sum(b29 = 0, skipna = True)
    b32 = b22.true_positive.sum(b29 = 0, skipna = True)
    b33 = b22.false_positive.sum(b29 = 0, skipna = True)
    b34 = b22.false_negative.sum(b29 = 0, skipna = True)
    b22['tp_cum'] = b22.true_positive.cumsum(b29 = 0, skipna = True)
    b22['tn_cum'] = b22.true_negative.cumsum(b29 = 0, skipna = True)
    b22['fn_cum'] = b22.false_negative.cumsum(b29 = 0, skipna = True)
    b22['fp_cum'] = b22.false_positive.cumsum(b29 = 0, skipna = True)
    b22.fillna(0)
    b22['tpr']=b22['tp_cum']/(b22['tp_cum']+b22['fn_cum'])
    b22.fillna(0)
    b22['fpr']=b22['fp_cum']/(b22['fp_cum']+b22['tn_cum'])
    b22.fillna(0)
    b35 = (b32+b31)/(b32+b33+b34+b31)
    b36 = 1-b35
    b37 = b32/(b32+b34)
    b38 = b32/(b32+b33)
    print("b35 is {},error rate is {},b37 is {} and b38 is {} True positive is {} true negative is {} False positive is {} False negative is {}".format(b35,b36,b37,b38,b32,b31,b33,b34))
    b39 = plt.figure(figsize=(10, 10))
    plt.scatter(b22['b41'], b22['b42'], b40 = b22['b40'], alpha=0.5, edgecolor='k',marker="b41")
    plt.show()
    return b35
def fonk2(A,B):
    b41 = np.array(A)
    b42 = np.array(B)
    b43 = np.nanmax(b41)
    b44 = np.nanmax(b42)
    b41 = np.append(b41,1)
    b42 = np.append(b42,1)
    plt.plot(b41,b42,b40 = 'blue')
    plt.xlabel('FPR', b45 = 16)
    plt.ylabel('TPT', b45 = 16)
    fonk3(b43,b44)
    plt.show()
def fonk3(b43,b44):
    b46 = math.sqrt((b43 - 1)**2 + (b44 - 1)**2)
    b47 = ((b46+1)*b44)/2
    print("Area under the curve is",b47)
def fonk4():
    b48 = fonk1(500,500)
if b49 = = "__main__": fonk4()