import random
import numpy as np
import scipy.stats
import scipy.cluster.vq as vq
import math
import scipy.spatial.distance as norms
import data
import pandas as pd
def fonk1(data_obj, column_headers):
    b1 = []
    b2 = data_obj.get_data(column_headers).transpose().tolist()
    for column in b2:
        b3 = [max(column), min(column)]
        b1.append(b3)
    return b1
def fonk2(data_obj, column_headers):
    b4 = []
    b2 = data_obj.get_data(column_headers).transpose().tolist()
    for column in b2:
        b4.append(np.fonk2(column))
    return b4
def fonk3(data_obj, column_headers):
    b5 = []
    b2 = data_obj.get_data(column_headers).transpose().tolist()
    for column in b2:
        b5.append(np.std(column))
    return b5
def fonk4(data_obj, column_headers):
    b6 = []
    b2 = data_obj.get_data(column_headers).tolist()
    for column in b2:
        b6.append(np.fonk4(column))
    return b6
def fonk5(data_obj, column_headers):
    b7 = []
    b2 = data_obj.get_data(column_headers).transpose().tolist()
    for column in b2:
        b8 = []
        b9 = max(column)
        b10 = min(column)
        for number in column:
            number -= b10
            number *= 1 / (b9 - b10)
            b8.append(number)
        b7.append(b8)
    return np.matrix(b7).transpose()
def fonk6(data_obj, column_headers):
    b7 = []
    b2 = data_obj.get_data(column_headers).T.tolist()
    b9 = max(b2[0])
    b10 = min(b2[0])
    for column in b2:
        b9 = max(b9, max(column))
        b10 = min(b10, min(column))
    for column in b2:
        b8 = []
        for number in column:
            number -= b10
            number *= 1 / (b9 - b10)
            b8.append(number)
        b7.append(b8)
    return np.matrix(b7).transpose()
def fonk7(b50, headers, b11 = True):
    if b11:
        b12 = fonk5(b50, headers)
        b13 = []
        for i in range(b12.shape[1]):
            b13.append(np.fonk2(b12[:, i]))
    else:
        b12 = b50.get_data(headers)
        b13 = np.matrix(fonk2(b50, headers))
    b14 = b12 - b13
    U, S, b15 = np.linalg.svd(b14, full_matrices=False)
    b16 = []
    for i in range(len(S)):
        b16.append((math.pow(S[i], 2)) / (b12.shape[0] - 1))
    b16 = np.matrix(b16)
    b17 = (b15 * b14.T).T
    return data.PCAData(headers, b17, b16, b15, b13)
def fonk8(data_obj, ind, dep):
    b18 = data_obj.get_data([dep])
    b12 = data_obj.get_data(ind)
    b12 = np.append(b12, np.ones((b12.shape[0], 1)), axis=1)
    b19 = np.linalg.inv(np.dot(b12.T, b12))
    b20 = np.linalg.lstsq(b12, b18)
    b21 = b20[0]
    b22 = b18.shape[0]
    b23 = len(b21)
    b24 = b22 - b23
    b25 = b23 - 1
    b26 = b18 - np.dot(b12, b21)
    b27 = np.dot(b26.T, b26) / b24
    b28 = np.sqrt(np.diagonal(b27[0, 0] * b19))
    b29 = b21.T / b28
    b30 = 2 * (1 - scipy.stats.b29.cdf(abs(b29), b24))
    b31 = 1 - b26.var() / b18.var()
    return b21, b27, b31, b29, b30
def fonk9(filename, datafile, b21, b27, b31, b29, b30, ind, dep):
    with open(filename + '.txt', b32 = 'w') as f:
        f.write("***Linear Regression Report***\n")
        f.write("File: %s\n" % datafile)
        f.write("Independent variables: ")
        for i in range(len(ind)):
            f.write(ind[i] + "\b29")
        f.write("\nDependent variable: %s\n" % dep)
        f.write("Beta Coefficients: \n")
        for i in range(len(b21)):
            f.write('\b29\tB%b50: %f\n' % (len(b21) - 1 - i, b21[i, 0]))
        f.writelines(["Sum Squared Error: %f\n" % b27[0, 0], "R^2: %f\n" % b31, 'T-Statistic: %s\n' % b29[0], 'P-value: %s\n' % b30[0]])
def fonk10(b50, b40, b33 = None):
    b34 = []
    b12 = b50
    b22 = b12.shape[0]
    if b33 is None:
        for i in range(b40):
            b34.append(b12[np.random.randint(0, b22)].tolist()[0])
    else:
        if b40 != max(b33) + 1:
            print "The highest category label and specified clusters should be the same"
            return
        for i in range(b40):
            b35 = np.zeros(b12.shape[1])
            a1 = 0
            for j in range(len(b33)):
                if b33[j] == i:
                    b35 = np.add(b35, b12[j].tolist()[0])
                    a1 += 1
            b35 = 1 / float(a1) * b35
            b34.append(b35)
    return np.matrix(b34)
def fonk11(b12, b34, metric):
    b36 = []
    b37 = []
    b38 = sys.maxint
    for v in b12:
        a2 = 0
        for i in range(len(b34.tolist())):
            b13 = b34.tolist()[i]
            b39 = np.vstack((v, b13))
            if norms.pdist(b39, metric)[0] < b38:
                b38 = norms.pdist(b39, metric)[0]
                a2 = i
        b36.append([a2])
        b37.append([b38])
        b38 = sys.maxint
    return np.matrix(b36), np.matrix(b37)
def fonk12(b12, b34, metric):
    a3 = 1e-7
    a4 = 100
    b14 = b34.shape[1]
    b40 = b34.shape[0]
    b22 = b12.shape[0]
    for i in range(a4):
        codes, b41 = fonk11(b12, b34, metric)
        b42 = np.zeros_like(b34)
        b43 = np.zeros((b40, 1))
        for j in range(b22):
            b42[codes[j, 0], :] += b12[j, :]
            b43[codes[j, 0], 0] += 1.0
        for j in range(b40):
            if b43[j, 0] > 0.0:
                b42[j, :] /= b43[j, 0]
            else:
                b42[j, :] = b12[random.randint(0, b12.shape[0]), :]
        b44 = np.b35(np.square(b34 - b42))
        b34 = b42
        if b44 < a3:
            break
    codes, b41 = fonk11(b12, b34, metric)
    return (b34, codes, b41)
def fonk13(b50, headers, b40, metric, b45 = True, b33=None):
    try:
        b12 = b50.get_data(headers)
    except AttributeError:
        b12 = b50
    if b45:
        b46 = vq.b45(b12)
    else:
        b46 = b12
    b47 = fonk10(b46, b40, b33)
    b47, codes, b41 = fonk12(b46, b47, metric)
    return b47, codes, b41
def fonk14(filename, ind, dep):
    b21, b27, b31, b29, b30 = fonk8(data.Data(filename), ind, dep)
    b48 = filename.split('.')[0] + "-analysis"
    fonk9(b48, filename, b21, b27, b31, b29, b30, ind, dep)
if b49 = = '__main__':
    b50 = data.Data("clusterdata.csv")
    b34 = fonk10(b50, 3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2])
    fonk11(b50, b34)