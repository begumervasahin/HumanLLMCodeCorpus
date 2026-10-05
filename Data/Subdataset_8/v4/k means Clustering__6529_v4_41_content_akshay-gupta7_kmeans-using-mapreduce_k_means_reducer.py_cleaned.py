import sys
import numpy as np
salary_sum = np.zeros(5, dtype=np.float)
stock_sum = np.zeros(5, dtype=np.float)
cluster_counts = np.zeros(5, dtype=np.int)
for line in sys.stdin:
    centroid_id, salary, stock = map(float, line.strip().split("\t"))
    salary_sum[int(centroid_id)] += salary
    stock_sum[int(centroid_id)] += stock
    cluster_counts[int(centroid_id)] += 1
print("Total Salary:")
print(salary_sum)
print("\nTotal Stock:")
print(stock_sum)
print("\nCluster Counts:")
print(cluster_counts)
clusters = []
for i in range(len(cluster_counts)):
    if cluster_counts[i] != 0:
        centroid_id = i
        avg_salary = salary_sum[i] / cluster_counts[i]
        avg_stock = stock_sum[i] / cluster_counts[i]
        clusters.append((centroid_id, avg_salary, avg_stock))
print("\nClusters:")
for cluster in clusters:
    print(cluster)
with open("clusters.txt", "w+") as file:
    for centroid_id, avg_salary, avg_stock in clusters:
        file.write(f"{centroid_id}\t{avg_salary};{avg_stock}\n")