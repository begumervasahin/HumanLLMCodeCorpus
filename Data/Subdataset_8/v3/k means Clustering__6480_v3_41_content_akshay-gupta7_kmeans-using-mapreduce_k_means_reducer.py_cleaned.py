import sys
NUM_CENTROIDS = 5
total_salary = [0.0] * NUM_CENTROIDS
total_stock = [0.0] * NUM_CENTROIDS
data_count = [0] * NUM_CENTROIDS
for line in sys.stdin:
    centroid_id, salary, stock = map(float, line.strip().split("\t"))
    total_salary[int(centroid_id)] += salary
    total_stock[int(centroid_id)] += stock
    data_count[int(centroid_id)] += 1
clusters = []
for i in range(NUM_CENTROIDS):
    if data_count[i] != 0:
        mean_salary = total_salary[i] / data_count[i]
        mean_stock = total_stock[i] / data_count[i]
        clusters.append((i, mean_salary, mean_stock))
with open("clusters.txt", "w") as file1:
    for centroid_id, mean_salary, mean_stock in clusters:
        file1.write(f"{centroid_id}\t{mean_salary};{mean_stock}\n")