import os
import numpy as np
import matplotlib.pyplot as plt
from utils import projection_algorithms, plt_styles
b1 = "run_model/"
b2 = ["linear", "rf10"]
b3 = {"linear": "Ordinary Linear Regression", "rf10": "Random Forest"}
b4 = [10, 100, 500, 1000, 2000]
b5 = {"RP": "RP", "PCA": "PCA", "SPCA": "SPCA", "SSPCA": "SSPCA"}
def fonk1(model_name, b10):
    plt.figure()
    for projection_name in projection_algorithms:
        plt.semilogx(b4, b10[1:], plt_styles[projection_name], b6 = b5[projection_name], mew=0)
    print(f"Raw data performance with {model_name}: {b10[0]}")
    if model_name != "linear":
        plt.plot([10, 2000], [b10[0], b10[0]], "--", b7 = "gray", b6="raw")
    plt.legend(b8 = 0)
    plt.title(b3[model_name])
    plt.xticks(b4, b4)
    plt.xlim(8, 2500)
    plt.ylabel("RMSE")
    plt.xlabel("k")
    plt.savefig(f"{model_name}.pdf", b9 = "tight")
for model_name in b2:
    b10 = np.loadtxt(os.path.join(b1, f"{model_name}__{{}}.txt"))
    fonk1(model_name, b10)