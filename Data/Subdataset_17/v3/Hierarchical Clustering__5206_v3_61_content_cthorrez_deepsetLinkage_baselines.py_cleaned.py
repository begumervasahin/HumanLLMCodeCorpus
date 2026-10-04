import numpy as np
from eval_utils import pairwise_f1
def load_ground_truth_clusters(filepath):
    return np.loadtxt(filepath, delimiter='\t', dtype=float)[:, 1]
def generate_predictions(n_samples, n_clusters):
    one_cluster_preds = np.zeros(n_samples)
    n_clusters_preds = np.arange(n_samples)
    random_preds = np.random.randint(low=0, high=n_clusters, size=n_samples)
    return one_cluster_preds, n_clusters_preds, random_preds
def compute_f1_scores(blocks):
    one_cluster_f1s = []
    n_clusters_f1s = []
    random_f1s = []
    for block in blocks:
        gt_clusters = load_ground_truth_clusters(f'data/rexa/{block}/gtClusters.tsv')
        n_samples = len(gt_clusters)
        n_clusters = int(np.max(gt_clusters)) + 1
        one_cluster_preds, n_clusters_preds, random_preds = generate_predictions(n_samples, n_clusters)
        one_cluster_f1s.append(pairwise_f1(gt_clusters, one_cluster_preds))
        n_clusters_f1s.append(pairwise_f1(gt_clusters, n_clusters_preds))
        random_f1s.append(pairwise_f1(gt_clusters, random_preds))
    return (
        np.mean(one_cluster_f1s),
        np.mean(n_clusters_f1s),
        np.mean(random_f1s)
    )
def display_f1_scores(one_cluster_f1, n_clusters_f1, random_f1):
    print(f'One cluster F1: {one_cluster_f1:.4f}')
    print(f'N clusters F1: {n_clusters_f1:.4f}')
    print(f'Random F1: {random_f1:.4f}')
def main():
    blocks = np.array([
        'allen_d', 'moore_a', 'lee_l', 'robinson_h',
        'mcguire_j', 'blum_a', 'jones_s', 'young_s'
    ])
    one_cluster_f1, n_clusters_f1, random_f1 = compute_f1_scores(blocks)
    display_f1_scores(one_cluster_f1, n_clusters_f1, random_f1)
if __name__ == '__main__':
    main()