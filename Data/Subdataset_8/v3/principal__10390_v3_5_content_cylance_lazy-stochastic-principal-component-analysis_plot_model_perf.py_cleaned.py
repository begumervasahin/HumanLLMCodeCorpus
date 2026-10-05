import os
import numpy as np
import matplotlib.pyplot as plt
from utils import projection_algorithms, plt_styles
model_path = "run_model/"
model_names = ["linear", "rf10"]
model_titles = {"linear": "Ordinary Linear Regression", "rf10": "Random Forest"}
ks = [10, 100, 500, 1000, 2000]
projection_names = {"RP": "RP", "PCA": "PCA", "SPCA": "SPCA", "SSPCA": "SSPCA"}
def plot_data(model_name, scores):
    plt.figure()
    for projection_name in projection_algorithms:
        plt.semilogx(ks, scores[1:], plt_styles[projection_name], label=projection_names[projection_name], mew=0)
    print(f"Raw data performance with {model_name}: {scores[0]}")
    if model_name != "linear":
        plt.plot([10, 2000], [scores[0], scores[0]], "--", color="gray", label="raw")
    plt.legend(loc=0)
    plt.title(model_titles[model_name])
    plt.xticks(ks, ks)
    plt.xlim(8, 2500)
    plt.ylabel("RMSE")
    plt.xlabel("k")
    plt.savefig(f"{model_name}.pdf", bbox_inches="tight")
for model_name in model_names:
    scores = np.loadtxt(os.path.join(model_path, f"{model_name}__{{}}.txt"))
    plot_data(model_name, scores)