import sys
import numpy as np
def process_input():
    salary_sum = np.zeros(5, dtype=np.float)
    stock_sum = np.zeros(5, dtype=np.float)
    cluster_counts = np.zeros(5, dtype=np.int)
    for line in sys.stdin:
        centroid_id, salary, stock = map(float, line.strip().split("\t"))
        salary_sum[int(centroid_id)] += salary
        stock_sum[int(centroid_id)] += stock
        cluster_counts[int(centroid_id)] += 1
    return salary_sum, stock_sum, cluster_counts
def calculate_clusters(salary_sum, stock_sum, cluster_counts):
    clusters = []
    for i, count in enumerate(cluster_counts):
        if count != 0:
            avg_salary = salary_sum[i] / count
            avg_stock = stock_sum[i] / count
            clusters.append((i, avg_salary, avg_stock))
    return clusters
def print_debug_info(salary_sum, stock_sum, cluster_counts, clusters):
    print("Total Salary:")
    print(salary_sum)
    print("\nTotal Stock:")
    print(stock_sum)
    print("\nCluster Counts:")
    print(cluster_counts)
    print("\nClusters:")
    for cluster in clusters:
        print(cluster)
def write_clusters_to_file(clusters):
    with open("clusters.txt", "w+") as file:
        for centroid_id, avg_salary, avg_stock in clusters:
            file.write(f"{centroid_id}\t{avg_salary};{avg_stock}\n")
def main():
    salary_sum, stock_sum, cluster_counts = process_input()
    clusters = calculate_clusters(salary_sum, stock_sum, cluster_counts)
    print_debug_info(salary_sum, stock_sum, cluster_counts, clusters)
    write_clusters_to_file(clusters)
if __name__ == "__main__":
    main()