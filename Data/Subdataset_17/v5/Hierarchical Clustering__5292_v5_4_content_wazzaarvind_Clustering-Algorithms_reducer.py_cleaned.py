import sys
import numpy as np
def process_clusters():
    def output_cluster(cluster_id, cluster_indices, centroid_sum):
        if cluster_indices:
            centroid = centroid_sum / len(cluster_indices)
            centroid_str = ",".join(map(str, centroid))
            indices_str = ",".join(map(str, cluster_indices))
            print(f'{cluster_id}\t{indices_str}\t{centroid_str}')
    current_cluster = None
    cluster_indices = []
    centroid_sum = None
    for line in sys.stdin:
        line = line.strip()
        cluster_id, index, vector_str = line.split('\t')
        vector = np.array([float(value) for value in vector_str.split(',')])
        cluster_id = int(cluster_id)
        index = int(index)
        if current_cluster is None or current_cluster != cluster_id:
            if current_cluster is not None:
                output_cluster(current_cluster, cluster_indices, centroid_sum)
            current_cluster = cluster_id
            cluster_indices = []
            centroid_sum = np.zeros(len(vector))
        cluster_indices.append(index)
        centroid_sum += vector
    if current_cluster is not None:
        output_cluster(current_cluster, cluster_indices, centroid_sum)
if __name__ == "__main__":
    process_clusters()