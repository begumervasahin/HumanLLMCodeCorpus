import numpy as np
import sys
def process_clusters():
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
                centroid = centroid_sum / len(cluster_indices)
                print(f'{current_cluster}\t{",".join(map(str, cluster_indices))}\t{",".join(map(str, centroid))}')
            current_cluster = cluster_id
            cluster_indices = []
            centroid_sum = np.zeros(len(vector))
        cluster_indices.append(index)
        centroid_sum += vector
    if current_cluster is not None:
        centroid = centroid_sum / len(cluster_indices)
        print(f'{current_cluster}\t{",".join(map(str, cluster_indices))}\t{",".join(map(str, centroid))}')
if __name__ == "__main__":
    process_clusters()