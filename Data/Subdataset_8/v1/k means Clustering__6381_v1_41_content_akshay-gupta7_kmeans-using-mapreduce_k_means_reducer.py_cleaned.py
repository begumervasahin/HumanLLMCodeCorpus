import sys
slry = [0.0] * 5
stck = [0.0] * 5
count = [0] * 5
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    centroid_id, salary, stock = map(float, data_mapped)
    slry[int(centroid_id)] += salary
    stck[int(centroid_id)] += stock
    count[int(centroid_id)] += 1
clusters = []
for i in range(len(count)):
    if count[i] != 0:
        centroid_id = i
        mean_salary = slry[i] / count[i]
        mean_stock = stck[i] / count[i]
        clusters.append((centroid_id, mean_salary, mean_stock))
with open("clusters.txt", "w") as file1:
    for cluster in clusters:
        centroid_id, mean_salary, mean_stock = cluster
        file1.write(f"{centroid_id}\t{mean_salary};{mean_stock}\n")