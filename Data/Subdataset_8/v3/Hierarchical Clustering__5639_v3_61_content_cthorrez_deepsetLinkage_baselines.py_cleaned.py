import numpy as np
from eval_utils import pairwise_f1
def load_ground_truth_clusters(block):
    filepath = 'data/rexa/{}/gtClusters.tsv'.format(block)
    gt_clusters = np.loadtxt(filepath, delimiter='\t', dtype=np.float)[:, 1]
    return gt_clusters
def generate_predictions(gt_clusters):
    n = len(gt_clusters)
    n_clusters = np.max(gt_clusters) + 1
    one_cluster_preds = np.zeros(n)
    n_clusters_preds = np.arange(n)
    random_preds = np.random.randint(low=0, high=n_clusters, size=n)
    return one_cluster_preds, n_clusters_preds, random_preds
def calculate_average_f1_scores(blocks, one_cluster_f1s, n_clusters_f1s, random_f1s):
    print('Average F1 score for one cluster prediction:', np.mean(one_cluster_f1s))
    print('Average F1 score for n clusters prediction:', np.mean(n_clusters_f1s))
    print('Average F1 score for random prediction:', np.mean(random_f1s))
def main():
    blocks = np.array(['allen_d', 'moore_a', 'lee_l', 'robinson_h', 'mcguire_j', 'blum_a', 'jones_s', 'young_s' ])
    one_cluster_f1s = []
    n_clusters_f1s = []
    random_f1s = []
    for block in blocks:
        gt_clusters = load_ground_truth_clusters(block)
        one_cluster_preds, n_clusters_preds, random_preds = generate_predictions(gt_clusters)
        one_cluster_f1s.append(pairwise_f1(gt_clusters, one_cluster_preds))
        n_clusters_f1s.append(pairwise_f1(gt_clusters, n_clusters_preds))
        random_f1s.append(pairwise_f1(gt_clusters, random_preds))
    calculate_average_f1_scores(blocks, one_cluster_f1s, n_clusters_f1s, random_f1s)
if __name__ == '__main__':
    main()