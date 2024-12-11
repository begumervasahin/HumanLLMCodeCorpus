import numpy as np
import math
from ROOT import *
def fonk1(file_path):
    b1 = np.loadtxt(file_path, delimiter=",")
    b2 = b1[:, :21].astype(float)
    b3 = b1[:, 21]
    return b2, b3
def fonk2(b2, b3):
    b4 = b2[b3 == 1]
    b5 = b2[b3 == 0]
    return b4, b5
def fonk3(b4, b5):
    b6 = np.sum(b4, axis=0)
    b7 = np.sum(b5, axis=0)
    b8 = min(len(b4), len(b5))
    b9 = np.zeros((len(b4[0]), len(b4[0])))
    for i in range(len(b4[0])):
        for j in range(len(b4[0])):
            b10 = np.dot((b4[:, i] - b6[i]), (b5[:, j] - b7[j])) / (b8 - 1)
            b9[i][j] = b10
    return b9
def fonk4(matrix, file_path):
    with open(file_path, 'w') as file:
        for row in matrix:
            file.write(','.join(map(str, row)) + '\n')
def fonk5(matrix, title, file_path):
    gROOT.SetBatch()
    gStyle.SetOptStat(0)
    gStyle.SetPadLeftMargin(0.14)
    gStyle.SetTitleOffset(1.4, "y")
    gStyle.SetPaintTextFormat("0.2e")
    b11 = TH2D("", "", 21, 0, 21, 21, 0, 21)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            b11.SetBinContent(j + 1, len(matrix) - i, matrix[i][j])
    b11.Draw("text")
    b11.SetTitle(title)
    gPad.Update()
    b12 = TCanvas("b12", "", 10, 10, 2300, 1000)
    b12.Print(file_path)
def fonk6(b9):
    eigenvalues, b13 = np.linalg.eig(b9)
    return eigenvalues, b13
def fonk7(eigenvalues, b13, b17, file_path):
    b11 = TH2D("", "", 21, 0, 21, 22, 0, 22)
    for i, (value, vector) in enumerate(zip(eigenvalues, b13)):
        for j, component in enumerate(vector):
            b11.SetBinContent(j + 1, len(eigenvalues) - i, component)
        b11.SetBinContent(i + 1, len(eigenvalues), value)
        b11.GetXaxis().SetBinLabel(i + 1, b17[i])
        b11.GetYaxis().SetBinLabel(len(eigenvalues) - i, b17[i])
    b11.GetYaxis().SetBinLabel(len(eigenvalues), "eigs")
    b11.Draw("text")
    b11.SetTitle("Full Eigenvectors")
    b12 = TCanvas("b12", "", 10, 10, 2300, 1000)
    b12.Print(file_path)
b14 = "../Higgs13TeV_train_118_130_ggh.csv"
X_train, b15 = fonk1(b14)
b16 = len(X_train[0])
b17 = ["l1 p_{T}", "l2 p_{T}", "l3 p_{T}", "l4 p_{T}", "j1 p_{T}", "j2 p_{T}", "Njets"]
b4, b5 = fonk2(X_train, b15)
b9 = fonk3(b4, b5)
b18 = math.factorial(b16) / (math.factorial(b16 - 2) * 2)
print(f"You have {b16} b16 resulting in {b18} covariance matrices.")
fonk4(b9, 'full_covariance_matrix.txt')
fonk5(b9, "Full Covariance Matrix", "plots/Full_covariance_matrix.png")
eigenvalues, b13 = fonk6(b9)
fonk7(eigenvalues, b13, b17, "plots/Full_eigenvectors.png")
b19 = np.transpose(b13)
b20 = np.argsort(eigenvalues)[::-1]
b21 = [b19[index] for index in b20]
with open('full_eigenvectors.txt', 'w') as file:
    for vector in b21:
        file.write(','.join(map(str, vector)) + '\n')
b22 = np.dot(X_train - np.mean(X_train, axis=0), b21)
b23 = "../Higgs13TeV_test_118_130_ggh.csv"
b24 = np.loadtxt(b23, delimiter=",")
b25 = np.dot(b24 - np.mean(X_train, axis=0), b21)
