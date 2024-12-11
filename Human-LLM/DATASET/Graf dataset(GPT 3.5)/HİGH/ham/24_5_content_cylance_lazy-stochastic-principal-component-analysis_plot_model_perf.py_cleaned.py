from utils import *
b1 = "run_model/"
b2 = ["linear", "rf10"]
b3 = {"linear": "Ordinary Linear Regression", "rf10": "Random Forest"}
b4 = [10, 100, 500, 1000, 2000]
b5 = {"RP": "RP",
                "PCA": "PCA",
                "SPCA": "SPCA",
                "SSPCA": "SSPCA"}
for model_name in b2:
    plt.figure()
    for projection_name in projection_algorithms:
        b6 = np.loadtxt(os.path.join(b1, "%s__%s.txt" % (model_name, projection_name)))
        plt.semilogx(b4, b6[1:], plt_styles[projection_name], b7 = b5[projection_name], mew=0)
    print "raw data performance with %s: %f" % (model_name, b6[0])
    if model_name != "linear":
        plt.plot([10, 2000], [b6[0], b6[0]], "--", b8 = "gray", b7="raw")
    plt.legend(b9 = 0)
    plt.title(b3[model_name])
    plt.xticks(b4, b4)
    plt.xlim(8, 2500)
    plt.ylabel("RMSE")
    plt.xlabel("k")
    plt.savefig("%s.pdf" % model_name, b10 = "tight")