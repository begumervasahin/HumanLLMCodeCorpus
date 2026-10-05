import numpy as np
import math
from ROOT import *
from project_data import project_data
b1 = "../Higgs13TeV_train_118_130_ggh.csv"
b2 = "../Higgs13TeV_test_118_130_ggh.csv"
b3 = np.loadtxt(b1, delimiter=",")
b4 = b3[:, 0:21].astype(float)
b5 = b3[:, 21]
b6 = len(b5)
b7 = len(b4[0])
b8 = math.factorial(b7)
print(f"You have {b7} b7 resulting in {b8} covariance matrices...")
a1 = 0
a2 = 0
for b9 in b5:
    if b9 = = 1:
        a1 += 1
    else:
        a2 += 1
b10 = min(a1, a2)
b11 = np.zeros((b10, b7))
b12 = np.zeros((b10, b7))
a1 = 0
a2 = 0
for i in range(b6):
    if b5[i] == 1 and a1 < b10:
        b11[a1] = b4[i]
        a1 += 1
    elif b5[i] == 0 and a2 < b10:
        b12[a2] = b4[i]
        a2 += 1
b13 = [
    "l1 p_{T}", "l1", "l2 p_{T}", "l2", "l3 p_{T}", "l3",
    "l4 p_{T}", "l4", "j1 p_{T}", "j1", "j2 p_{T}", "j2", "Njets"
]
b14 = np.zeros((b7, b7))
b15 = TH2D("b15", "", 21, 0, 21, 21, 0, 21)
b16 = np.sum(b11, axis=0)
b17 = np.sum(b12, axis=0)
for st_d in range(b7):
    print(f"Analyzing through dimension: {st_d + 1} ...")
    for nd_d in range(b7):
        a3 = 0
        b18 = b16[st_d] / float(b10 - 1)
        for ip in range(b10):
            b19 = b17[nd_d] / float(b10 - 1)
            a3 += (b11[ip][st_d] - b18) * (b12[ip][nd_d] - b19)
        b14[st_d][nd_d] = a3 / float(b10 - 1)
        b15.SetBinContent(nd_d + 1, b7 - st_d, b14[st_d][nd_d])
    b15.GetXaxis().SetBinLabel(st_d + 1, b13[st_d])
    b15.GetYaxis().SetBinLabel(b7 - st_d, b13[st_d])
with open('full_covariance_matrix.txt', 'w') as full_conv_matrix:
    for row in b14:
        b20 = ",".join(map(str, row))
        full_conv_matrix.write(b20 + "\n")
gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetPadLeftMargin(0.14)
gStyle.SetTitleOffset(1.4, "y")
gStyle.SetPaintTextFormat("0.2e")
b21 = TCanvas("b21", "", 10, 10, 2300, 1000)
b15.Draw("text")
b15.SetTitle("Full Covariance Matrix")
gPad.Update()
b21.Print("plots/Full_covariance_matrix.png")