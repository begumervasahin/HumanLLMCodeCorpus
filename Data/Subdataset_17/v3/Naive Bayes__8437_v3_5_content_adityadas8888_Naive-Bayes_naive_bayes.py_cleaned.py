import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import norm
def generate_data(mean, cov, size):
    x, y = np.random.multivariate_normal(mean, cov, size).T
    return x, y
def calculate_metrics(dtest):
    tn = np.sum((dtest['predicted'] == 0) & (dtest['actual'] == 0))
    tp = np.sum((dtest['predicted'] == 1) & (dtest['actual'] == 1))
    fp = np.sum((dtest['predicted'] == 0) & (dtest['actual'] == 1))
    fn = np.sum((dtest['predicted'] == 1) & (dtest['actual'] == 0))
    accuracy = (tp + tn) / (tp + fp + fn + tn)
    error_rate = 1 - accuracy
    recall = tp / (tp + fn)
    precision = tp / (tp + fp)
    return accuracy, error_rate, recall, precision, tp, tn, fp, fn
def naive_bayes(tsize0, tsize1):
    mean1, mean2 = [1, 0], [0, 1]
    cov = [[1, 0.75], [0.75, 1]]
    x1, y1 = generate_data(mean1, cov, tsize0)
    x2, y2 = generate_data(mean2, cov, tsize1)
    x3, y3 = generate_data(mean1, cov, 100)
    x4, y4 = generate_data(mean2, cov, 100)
    meanx0, meany0, stdx0, stdy0 = np.mean(x1), np.mean(y1), np.std(x1), np.std(y1)
    meanx1, meany1, stdx1, stdy1 = np.mean(x2), np.mean(y2), np.std(x2), np.std(y2)
    dtrain = pd.DataFrame({'x': np.concatenate((x1, x2)), 'y': np.concatenate((y1, y2)), 'label': np.concatenate((np.zeros(len(x1)), np.ones(len(x2))))})
    dtest = pd.DataFrame({'x': np.concatenate((x3, x4)), 'y': np.concatenate((y3, y4)), 'actual': np.concatenate((np.zeros(len(x3)), np.ones(len(x4))))})
    prob0, prob1 = tsize0 / (tsize0 + tsize1), tsize1 / (tsize0 + tsize1)
    label0 = norm.pdf(dtest['x'], loc=meanx0, scale=stdx0) * norm.pdf(dtest['y'], loc=meany0, scale=stdy0)
    label1 = norm.pdf(dtest['x'], loc=meanx1, scale=stdx1) * norm.pdf(dtest['y'], loc=meany1, scale=stdy1)
    post0, post1 = label0 * prob0, label1 * prob1
    dtest['post0'], dtest['post1'] = post0, post1
    dtest['predicted'] = np.where(post0 > post1, 0, 1)
    dtest['color'] = np.where(post0 > post1, 'r', 'b')
    accuracy, error_rate, recall, precision, tp, tn, fp, fn = calculate_metrics(dtest)
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
    x, y = np.append(A, 1), np.append(B, 1)
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