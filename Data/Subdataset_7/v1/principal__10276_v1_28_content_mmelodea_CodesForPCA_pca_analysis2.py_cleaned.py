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
b8 = math.factorial(b7) / (math.factorial(b7 - 2) * 2)
print("You have %i b7 resulting in %i covariance matrices..." % (b7, b8))
a1 = 0
a2 = 0
for i in range(b6):
    if b5[i] == 1:
        a1 += 1
    else:
        a2 += 1
b9 = min(a1, a2)
b10 = np.zeros((b9, b7))
b11 = np.zeros((b9, b7))
a1 = 0
a2 = 0
for i in range(b6):
    if b5[i] == 1 and a1 < b9:
        b10[a1] = b4[i]
        a1 += 1
    elif b5[i] == 0 and a2 < b9:
        b11[a2] = b4[i]
        a2 += 1
b12 = ["l1 p_{T}", "l1", "l2 p_{T}", "l2", "l3 p_{T}", "l3", "l4 p_{T}", "l4", "j1 p_{T}", "j1", "j2 p_{T}",
             "j2", "Njets"]
b13 = np.zeros((b7, b7))
b14 = TH2D("b14", "", 21, 0, 21, 21, 0, 21)
b15 = np.sum(b10, axis=0)
b16 = np.sum(b11, axis=0)
for st_d in range(b7):
    print("Analyzing through dimension: %i ..." % (st_d + 1))
    for nd_d in range(b7):
        a3 = 0
        b17 = b15[st_d] / float(b9 - 1)
        for ip in range(b9):
            b18 = b16[nd_d] / float(b9 - 1)
            a3 += (b10[ip][st_d] - b17) * (b11[ip][nd_d] - b18)
        b13[st_d][nd_d] = a3 / float(b9 - 1)
        b14.SetBinContent(nd_d + 1, b7 - st_d, b13[st_d][nd_d])
    b14.GetXaxis().SetBinLabel(st_d + 1, b12[st_d])
    b14.GetYaxis().SetBinLabel(b7 - st_d, b12[st_d])
with open('full_covariance_matrix.txt', 'w') as full_conv_matrix:
    for i in range(b7):
        b19 = ",".join(map(str, b13[i]))
        full_conv_matrix.write(b19 + "\n")
gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetPadLeftMargin(0.14)
gStyle.SetTitleOffset(1.4, "y")
gStyle.SetPaintTextFormat("0.2e")
b20 = TCanvas("b20", "", 10, 10, 2300, 1000)
b14.Draw("text")
b14.SetTitle("Full Covariance Matrix")
gPad.Update()
b20.Print("plots/Full_covariance_matrix.png")