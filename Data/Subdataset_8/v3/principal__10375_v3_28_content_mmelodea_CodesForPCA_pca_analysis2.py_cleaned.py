import numpy as np
import math
from ROOT import *
from project_data import project_data
TRAIN_FILE_PATH = "../Higgs13TeV_train_118_130_ggh.csv"
TEST_FILE_PATH = "../Higgs13TeV_test_118_130_ggh.csv"
def load_data(file_path):
    return np.loadtxt(file_path, delimiter=",")
def count_events(labels):
    signal_count = np.sum(labels == 1)
    background_count = np.sum(labels == 0)
    return signal_count, background_count
def extract_events(X, Y, limit):
    signal_indices = np.where(Y == 1)[0][:limit]
    background_indices = np.where(Y == 0)[0][:limit]
    return X[signal_indices], X[background_indices]
def compute_covariance_matrix(signal_data, background_data):
    num_dimensions = signal_data.shape[1]
    covariance_matrix = np.zeros((num_dimensions, num_dimensions))
    signal_mean = np.mean(signal_data, axis=0)
    background_mean = np.mean(background_data, axis=0)
    for i in range(num_dimensions):
        for j in range(num_dimensions):
            covariance_matrix[i][j] = np.mean(
                (signal_data[:, i] - signal_mean[i]) * (background_data[:, j] - background_mean[j])
            )
    return covariance_matrix
def write_matrix_to_file(matrix, file_path):
    np.savetxt(file_path, matrix, delimiter=",")
def plot_covariance_matrix(matrix, dimension_names, output_file):
    hist = TH2D("fconv_hist", "", 21, 0, 21, 21, 0, 21)
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            hist.SetBinContent(j + 1, matrix.shape[0] - i, matrix[i][j])
        hist.GetXaxis().SetBinLabel(i + 1, dimension_names[i])
        hist.GetYaxis().SetBinLabel(matrix.shape[0] - i, dimension_names[i])
    canvas = TCanvas("cv", "", 10, 10, 2300, 1000)
    hist.Draw("text")
    hist.SetTitle("Full Covariance Matrix")
    gPad.Update()
    canvas.Print(output_file)
X_train = load_data(TRAIN_FILE_PATH)
Y_train = X_train[:, -1]
X_train = X_train[:, :-1]
nevents_train = len(Y_train)
dimensions = X_train.shape[1]
n_covariances = math.factorial(dimensions)
print(f"You have {dimensions} dimensions resulting in {n_covariances} covariance matrices...")
signal_count, background_count = count_events(Y_train)
limit = min(signal_count, background_count)
signal_events, background_events = extract_events(X_train, Y_train, limit)
dimension_names = [
    "l1 p_{T}", "l1", "l2 p_{T}", "l2", "l3 p_{T}", "l3",
    "l4 p_{T}", "l4", "j1 p_{T}", "j1", "j2 p_{T}", "j2", "Njets"
]
covariance_matrix = compute_covariance_matrix(signal_events, background_events)
write_matrix_to_file(covariance_matrix, 'full_covariance_matrix.txt')
gROOT.SetBatch()
gStyle.SetOptStat(0)
gStyle.SetPadLeftMargin(0.14)
gStyle.SetTitleOffset(1.4, "y")
gStyle.SetPaintTextFormat("0.2e")
plot_covariance_matrix(covariance_matrix, dimension_names, "plots/Full_covariance_matrix.png")