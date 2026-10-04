import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
def naive_bayes(tsize0, tsize1):
    mean1, mean2 = [1, 0], [0, 1]
    Sigma1, Sigma2 = [[1, 0.75], [0.75, 1]], [[1, 0.75], [0.75, 1]]
    x1, y1 = np.random.multivariate_normal(mean1, Sigma1, tsize0).T
    x2, y2 = np.random.multivariate_normal(mean2, Sigma2, tsize1).T
    x3, y3 = np.random.multivariate_normal(mean1, Sigma1, 100).T
    x4, y4 = np.random.multivariate_normal(mean2, Sigma2, 100).T
    meanx0, meany0 = np.mean(x1), np.mean(y1)
    stdx0, stdy0 = np.std(x1), np.std(y1)
    meanx1, meany1 = np.mean(x2), np.mean(y2)
    stdx1, stdy1 = np.std(x2), np.std(y2)
    dtrain = pd.DataFrame({
        'x': np.concatenate((x1, x2)),
        'y': np.concatenate((y1, y2)),
        'label': np.concatenate((np.zeros(len(x1)), np.ones(len(x2))))
    })
    dtest = pd.DataFrame({
        'x': np.concatenate((x3, x4)),
        'y': np.concatenate((y3, y4)),
        'actual': np.concatenate((np.zeros(len(x3)), np.ones(len(x4))))
    })
    prob0 = tsize0 / (tsize0 + tsize1)
    prob1 = tsize1 / (tsize0 + tsize1)
    label0 = norm.pdf(dtest['x'], loc=meanx0, scale=stdx0) * norm.pdf(dtest['y'], loc=meany0, scale=stdy0)
    label1 = norm.pdf(dtest['x'], loc=meanx1, scale=stdx1) * norm.pdf(dtest['y'], loc=meany1, scale=stdy1)
    post0 = label0 * prob0
    post1 = label1 * prob1
    dtest['post0'] = post0
    dtest['post1'] = post1
    dtest['predicted'] = np.where(post0 > post1, 0, 1)
    dtest['color'] = np.where(post0 > post1, 'r', 'b')
    tn = np.sum((dtest['predicted'] == 0) & (dtest['actual'] == 0))
    tp = np.sum((dtest['predicted'] == 1) & (dtest['actual'] == 1))
    fp = np.sum((dtest['predicted'] == 0) & (dtest['actual'] == 1))
    fn = np.sum((dtest['predicted'] == 1) & (dtest['actual'] == 0))
    accuracy = (tp + tn) / (tp + fp + fn + tn)
    error_rate = 1 - accuracy
    recall = tp / (tp + fn)
    precision = tp / (tp + fp)
    print(f"Accuracy: {accuracy:.3f}, Error Rate: {error_rate:.3f}, Recall: {recall:.3f}, Precision: {precision:.3f}")
    print(f"True Positive: {tp}, True Negative: {tn}, False Positive: {fp}, False Negative: {fn}")
    plt.figure(figsize=(10, 10))
    plt.scatter(dtest['x'], dtest['y'], color=dtest['color'], alpha=0.5, edgecolor='k', marker="x")
    plt.title('Naive Bayes Classification Results')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()
    return accuracy
def find_roc(A, B):
    x = np.append(A, 1)
    y = np.append(B, 1)
    plt.plot(x, y, color='blue')
    plt.xlabel('FPR', fontsize=16)
    plt.ylabel('TPR', fontsize=16)
    area_curve(x, y)
    plt.title('ROC Curve')
    plt.show()
def area_curve(x, y):
    auc = np.trapz(y, x)
    print(f"Area under the curve is {auc:.3f}")
def main():
    accuracy = naive_bayes(500, 500)
    print("ROC Curve and AUC calculation are not demonstrated here.")
if __name__ == "__main__":
    main()