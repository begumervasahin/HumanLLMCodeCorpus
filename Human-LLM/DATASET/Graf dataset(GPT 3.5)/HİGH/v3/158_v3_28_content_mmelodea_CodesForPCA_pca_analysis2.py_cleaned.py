import numpy as np
import math
from ROOT import *
from project_data import project_data
b1 = "../Higgs13TeV_train_118_130_ggh.csv"
b2 = "../Higgs13TeV_test_118_130_ggh.csv"
def fonk1(file_path):
    return np.loadtxt(file_path, b3 = ",")
def fonk2(labels):
    b4 = np.sum(labels == 1)
    b5 = np.sum(labels == 0)
    return b4, b5
def fonk3(X, Y, b19):
    b6 = np.where(Y == 1)[0][:b19]
    b7 = np.where(Y == 0)[0][:b19]
    return X[b6], X[b7]
def fonk4(signal_data, background_data):
    b8 = signal_data.shape[1]
    b9 = np.zeros((b8, b8))
    b10 = np.mean(signal_data, axis=0)
    b11 = np.mean(background_data, axis=0)
    for i in range(b8):
        for j in range(b8):
            b9[i][j] = np.mean(
                (signal_data[:, i] - b10[i]) * (background_data[:, j] - b11[j])
            )
    return b9
def fonk5(matrix, file_path):
    np.savetxt(file_path, matrix, b3 = ",")
def fonk6(matrix, b21, output_file):
    b12 = TH2D("fconv_hist", "", 21, 0, 21, 21, 0, 21)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            b12.SetBinContent(j + 1, matrix.shape[0] - i, matrix[i][j])
        b12.GetXaxis().SetBinLabel(i + 1, b21[i])
        b12.GetYaxis().SetBinLabel(matrix.shape[0] - i, b21[i])
    b13 = TCanvas("cv", "", 10, 10, 2300, 1000)
    b12.Draw("text")
    b12.SetTitle("Full Covariance Matrix")
    gPad.Update()
    b13.Print(output_file)
b14 = fonk1(b1)
b15 = b14[:, -1]
b14 = b14[:, :-1]
b16 = len(b15)
b17 = b14.shape[1]
b18 = math.factorial(b17)
print(f"You have {b17} b17 resulting in {b18} covariance matrices...")
b4, b5 = fonk2(b15)
b19 = min(b4, b5)
signal_events, b20 = fonk3(b14, b15, b19)
b21 = [
    "l1 p_{T}", "l1", "l2 p_{T}", "l2", "l3 p_{T}", "l3",
    "l4 p_{T}", "l4", "j1 p_{T}", "j1", "j2 p_{T}", "j2", "Njets"
]
b9 = fonk4(signal_events, b20)
fonk5(b9, 'full_covariance_matrix.txt')
gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetPadLeftMargin(0.14)
gStyle.SetTitleOffset(1.4, "y")
gStyle.SetPaintTextFormat("0.2e")
fonk6(b9, b21, "plots/Full_covariance_matrix.png")