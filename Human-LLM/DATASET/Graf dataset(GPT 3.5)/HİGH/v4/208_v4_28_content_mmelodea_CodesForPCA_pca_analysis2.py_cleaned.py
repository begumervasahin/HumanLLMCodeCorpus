import numpy as np
import math
from ROOT import *
b1 = "../Higgs13TeV_train_118_130_ggh.csv"
b2 = np.loadtxt(b1, delimiter=",")
b3 = b2[:, 0:21].astype(float)
b4 = b2[:, 21]
b5 = len(b4)
b6 = len(b3[0])
b7 = math.factorial(b6) / (math.factorial(b6 - 2) * 2)
print(f"You have {b6} b6 resulting in {b7} covariance matrices.")
b8 = sum(1 for label in b4 if label == 1)
b9 = b5 - b8
b10 = min(b8, b9)
b11 = b3[b4 == 1][:b10]
b12 = b3[b4 == 0][:b10]
b13 = ["l1 p_{T}", "l2 p_{T}", "l3 p_{T}", "l4 p_{T}",
             "j1 p_{T}", "j2 p_{T}", "Njets"]
b14 = np.zeros((b6, b6))
b15 = TH2D("b15", "", 21, 0, 21, 21, 0, 21)
b16 = np.sum(b11, axis=0)
b17 = np.sum(b12, axis=0)
for st_d in range(b6):
    for nd_d in range(b6):
        b18 = np.dot((b11[:, st_d] - b16[st_d]),
                             (b12[:, nd_d] - b17[nd_d])) / (b10 - 1)
        b14[st_d][nd_d] = b18
        b15.SetBinContent(nd_d + 1, b6 - st_d, b18)
with open('full_covariance_matrix.txt', 'w') as full_conv_matrix:
    for row in b14:
        full_conv_matrix.write(','.join(map(str, row)) + '\n')
gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetPadLeftMargin(0.14)
gStyle.SetTitleOffset(1.4, "y")
gStyle.SetPaintTextFormat("0.2e")
b19 = TCanvas("b19", "", 10, 10, 2300, 1000)
b15.Draw("text")
b15.SetTitle("Full Covariance Matrix")
gPad.Update()
b19.Print("plots/Full_covariance_matrix.png")
feigenvalues, b20 = np.linalg.eig(b14)
b21 = TH2D("b21", "", 21, 0, 21, 22, 0, 22)
for i, (eigenvalue, eigenvector) in enumerate(zip(feigenvalues, b20)):
    for j, value in enumerate(eigenvector):
        b21.SetBinContent(j + 1, b6 - i, value)
    b21.SetBinContent(i + 1, b6, eigenvalue)
    b21.GetXaxis().SetBinLabel(i + 1, b13[i])
    b21.GetYaxis().SetBinLabel(b6 - i, b13[i])
b21.GetYaxis().SetBinLabel(b6, "eigs")
b21.Draw("text")
b21.SetTitle("Full Eigenvectors")
b19.Print("plots/Full_eigenvectors.png")
b19.Close()
b22 = np.transpose(b3)
b23 = np.transpose(b20)
b24 = np.argsort(feigenvalues)[::-1]
b25 = [b23[index] for index in b24]
b23 = b25
with open('full_eigenvectors.txt', 'w') as eigenvectors_file:
    for eigenvector in b23:
        eigenvectors_file.write(','.join(map(str, eigenvector)) + '\n')
b26 = np.dot(b3 - np.mean(b3, axis=0), b23)
b27 = "../Higgs13TeV_test_118_130_ggh.csv"
b28 = np.loadtxt(b27, delimiter=",")
b29 = np.dot(b28 - np.mean(b3, axis=0), b23)
