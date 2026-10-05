import numpy as np
import math
from ROOT import *
from project_data import project_data
train_file = "../Higgs13TeV_train_118_130_ggh.csv"
test_file = "../Higgs13TeV_test_118_130_ggh.csv"
reader = np.loadtxt(train_file, delimiter=",")
X_train = reader[:, 0:21].astype(float)
Y_train = reader[:, 21]
nevents_train = len(Y_train)
dimensions = len(X_train[0])
n_covariances = math.factorial(dimensions)
print(f"You have {dimensions} dimensions resulting in {n_covariances} covariance matrices...")
ns = 0
nb = 0
for label in Y_train:
    if label == 1:
        ns += 1
    else:
        nb += 1
limit = min(ns, nb)
sX_train = np.zeros((limit, dimensions))
bX_train = np.zeros((limit, dimensions))
ns = 0
nb = 0
for i in range(nevents_train):
    if Y_train[i] == 1 and ns < limit:
        sX_train[ns] = X_train[i]
        ns += 1
    elif Y_train[i] == 0 and nb < limit:
        bX_train[nb] = X_train[i]
        nb += 1
dim_names = [
    "l1 p_{T}", "l1", "l2 p_{T}", "l2", "l3 p_{T}", "l3",
    "l4 p_{T}", "l4", "j1 p_{T}", "j1", "j2 p_{T}", "j2", "Njets"
]
fconv_matrix = np.zeros((dimensions, dimensions))
fconv_hist = TH2D("fconv_hist", "", 21, 0, 21, 21, 0, 21)
svals_sum = np.sum(sX_train, axis=0)
bvals_sum = np.sum(bX_train, axis=0)
for st_d in range(dimensions):
    print(f"Analyzing through dimension: {st_d + 1} ...")
    for nd_d in range(dimensions):
        fcovariance = 0
        d1_mean = svals_sum[st_d] / float(limit - 1)
        for ip in range(limit):
            d2_mean = bvals_sum[nd_d] / float(limit - 1)
            fcovariance += (sX_train[ip][st_d] - d1_mean) * (bX_train[ip][nd_d] - d2_mean)
        fconv_matrix[st_d][nd_d] = fcovariance / float(limit - 1)
        fconv_hist.SetBinContent(nd_d + 1, dimensions - st_d, fconv_matrix[st_d][nd_d])
    fconv_hist.GetXaxis().SetBinLabel(st_d + 1, dim_names[st_d])
    fconv_hist.GetYaxis().SetBinLabel(dimensions - st_d, dim_names[st_d])
with open('full_covariance_matrix.txt', 'w') as full_conv_matrix:
    for row in fconv_matrix:
        text1 = ",".join(map(str, row))
        full_conv_matrix.write(text1 + "\n")
gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetPadLeftMargin(0.14)
gStyle.SetTitleOffset(1.4, "y")
gStyle.SetPaintTextFormat("0.2e")
cv = TCanvas("cv", "", 10, 10, 2300, 1000)
fconv_hist.Draw("text")
fconv_hist.SetTitle("Full Covariance Matrix")
gPad.Update()
cv.Print("plots/Full_covariance_matrix.png")