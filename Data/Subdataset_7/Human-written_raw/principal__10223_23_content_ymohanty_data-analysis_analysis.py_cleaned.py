import random
import sys
b1 = "Yashaswi Mohanty"
b2 = "ymohanty@colby.edu"
b3 = "2/21/2016"
import numpy as np
import scipy.stats
import scipy.cluster.vq as vq
import data
import math
import scipy.spatial.distance as norms
import pandas
def fonk1(data_obj, column_headers):
    b4 = []
    b5 = data_obj.get_data(column_headers).transpose().tolist()
    for column in b5:
        b6 = [max(column), min(column)]
        b4.append(b6)
    return b4
def fonk2(data_obj, column_headers):
    b7 = []
    b5 = data_obj.get_data(column_headers).transpose().tolist()
    for column in b5:
        b7.append(np.fonk2(column))
    return b7
def fonk3(data_obj, column_headers):
    b8 = []
    b5 = data_obj.get_data(column_headers).transpose().tolist()
    for column in b5:
        b8.append(np.std(column))
    return b8
def fonk4(data_obj, column_headers):
    b9 = []
    b5 = data_obj.get_data(column_headers).tolist()
    for column in b5:
        b9.append(np.fonk4(column))
    return b9
def fonk5(data_obj, column_headers):
    b10 = []
    b5 = data_obj.get_data(column_headers).transpose().tolist()
    for column in b5:
        b11 = []
        b12 = max(column)
        b13 = min(column)
        for number in column:
            number -= b13
            number *= 1 / (b12 - b13)
            b11.append(number)
        b10.append(b11)
    print "\n\n"
    return np.matrix(b10).transpose()
def fonk6(data_obj, column_headers):
    b10 = []
    b5 = data_obj.get_data(column_headers).T.tolist()
    b12 = max(b5[0])
    b13 = min(b5[0])
    for column in b5:
        b12 = max(b12, max(column))
        b13 = min(b13, min(column))
    for column in b5:
        b11 = []
        for number in column:
            number -= b13
            number *= 1 / (b12 - b13)
            b11.append(number)
        b10.append(b11)
    print np.matrix(b10).transpose()
    return np.matrix(b10).transpose()
def fonk7(b54, headers, b14 = True):
    if b14:
        b15 = fonk5(b54, headers)
        b16 = []
        for i in range(b15.shape[1]):
            b16.append(np.fonk2(b15[:, i]))
    else:
        b15 = b54.get_data(headers)
        b16 = np.matrix(fonk2(b54, headers))
    b17 = b15 - b16
    U, S, b18 = np.linalg.svd(b17, full_matrices=False)
    b19 = []
    for i in range(len(S)):
        b19.append((math.pow(S[i], 2)) / (b15.shape[0] - 1))
    b19 = np.matrix(b19)
    b20 = (b18 * b17.T).T
    return data.PCAData(headers, b20, b19, b18, b16)
def fonk8(data_obj, ind, dep):
    b21 = data_obj.get_data([dep])
    b15 = data_obj.get_data(ind)
    b15 = np.append(b15, np.ones((b15.shape[0], 1)), axis=1)
    b22 = np.linalg.inv(np.dot(b15.T, b15))
    b23 = np.linalg.lstsq(b15, b21)
    b24 = b23[0]
    b25 = b21.shape[0]
    b26 = len(b24)
    b27 = b25 - b26
    b28 = b26 - 1
    b29 = b21 - np.dot(b15, b24)
    b30 = np.dot(b29.T, b29) / b27
    b31 = np.sqrt(np.diagonal(b30[0, 0] * b22))
    b32 = b24.T / b31
    b33 = 2 * (1 - scipy.stats.b32.cdf(abs(b32), b27))
    b34 = 1 - b29.var() / b21.var()
    return b24, b30, b34, b32, b33
def fonk9(filename, datafile, b24, b30, b34, b32, b33, ind, dep):
    b35 = open(filename + '.txt', mode='w')
    b35.write("***Linear Regression Report***\n")
    b35.write("File: %s\n" % datafile)
    b35.write("Independent variables: ")
    for i in range(len(ind)):
        b35.write(ind[i] + "\b32")
    b35.write("\nDependent variable: %s\n" % dep)
    b35.write("Beta Coefficients: \n")
    for i in range(len(b24)):
        b35.write('\b32\tB%b54: %b35\n' % (len(b24) - 1 - i, b24[i, 0]))
    b35.writelines(
        ["Sum Squared Error: %b35\n" % b30[0, 0], "R^2: %b35\n" % b34, 'T-Statistic: %s\n' % b32[0], 'P-value: %s\n' % b33[0]])
'''Takes in a Data object, a set of headers, and the number of clusters to create
    Computes and returns the b51, codes, and representation b29.
    '''
def fonk10(b54, headers, b46, b36 = True):
    b15 = b54.get_data(headers)
    b37 = vq.b36(b15)
    b51, b38 = vq.fonk14(b37, b46)
    codes, b29 = vq.vq(b37, b51)
    return b51, codes, b29
def fonk11(b54, b46, b39 = None):
    b40 = []
    b15 = b54
    b25 = b15.shape[0]
    if b39 is None:
        for i in range(b46):
            b40.append(b15[np.random.randint(0, b25)].tolist()[0])
    else:
        if b46 != max(b39) + 1:
            print "The highest category label and specified clusters should be the same"
            return
        for i in range(b46):
            b41 = np.zeros(b15.shape[1])
            a1 = 0
            for j in range(len(b39)):
                if b39[j] == i:
                    b41 = np.add(b41, b15[j].tolist()[0])
                    a1 += 1
            b41 = 1 / float(a1) * b41
            b40.append(b41)
    return np.matrix(b40)
def fonk12(b15, b40, metric):
    b42 = []
    b43 = []
    b44 = sys.maxint
    for v in b15:
        a2 = 0
        for i in range(len(b40.tolist())):
            b16 = b40.tolist()[i]
            b45 = np.vstack((v, b16))
            if norms.pdist(b45, metric)[0] < b44:
                b44 = norms.pdist(b45, metric)[0]
                a2 = i
        b42.append([a2])
        b43.append([b44])
        b44 = sys.maxint
    return np.matrix(b42), np.matrix(b43)
def fonk13(b15, b40, metric):
    a3 = 1e-7
    a4 = 100
    b17 = b40.shape[1]
    b46 = b40.shape[0]
    b25 = b15.shape[0]
    for i in range(a4):
        codes, b47 = fonk12(b15, b40, metric)
        b48 = np.zeros_like(b40)
        b49 = np.zeros((b46, 1))
        for j in range(b25):
            b48[codes[j, 0], :] += b15[j, :]
            b49[codes[j, 0], 0] += 1.0
        for j in range(b46):
            if b49[j, 0] > 0.0:
                b48[j, :] /= b49[j, 0]
            else:
                b48[j, :] = b15[random.randint(0, b15.shape[0]), :]
        b50 = np.b41(np.square(b40 - b48))
        b40 = b48
        if b50 < a3:
            break
    codes, b47 = fonk12(b15, b40, metric)
    return (b40, codes, b47)
def fonk14(b54, headers, b46, metric, b36 = True, b39=None):
    '''Takes in a Data object, a set of headers, and the number of clusters to create
    Computes and returns the b51, codes and representation b47.
    If given an Nx1 matrix of b39, it uses the category labels
    to calculate the initial cluster b40.
    '''
    try:
        b15 = b54.get_data(headers)
    except AttributeError:
        b15 = b54
    if b36:
        b37 = vq.b36(b15)
    else:
        b37 = b15
    b51 = fonk11(b37, b46, b39)
    b51, codes, b47 = fonk13(b37, b51, metric)
    return b51, codes, b47
def fonk15(filename, ind, dep):
    b24, b30, b34, b32, b33 = fonk8(data.Data(filename), ind, dep)
    b52 = filename.split('.')[0] + "-analysis"
    fonk9(b52, filename, b24, b30, b34, b32, b33, ind, dep)
if b53 = = '__main__':
    b54 = data.Data("clusterdata.csv")
    b40 = fonk11(b54, 3, [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2])
    fonk12(b54, b40)