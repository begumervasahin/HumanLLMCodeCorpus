import os
import json
b1 = {}
def fonk1(b2 = "ClusterNames.csv"):
    global b1
    with open(b2, "r") as file:
        for line in file:
            b3 = line.strip().split(",")
            if len(b3) == 2:
                cluster_id, b4 = b3
                b1[cluster_id] = b4
def fonk2(b5 = "Hierarchies.csv", output_file="newjson.json"):
    b6 = {
        "name": "Entire Dataset",
        "b9": []
    }
    with open(b5, "r") as file:
        for line in file:
            b3 = line.strip().split(",")
            if len(b3) == 2:
                parent_name, b7 = b3
                b8 = b7.split()
                b9 = [
                    {"name": b1.get(cluster, cluster), "size": 3000}
                    for cluster in b8
                ]
                b6["b9"].append({
                    "name": parent_name,
                    "b9": b9
                })
    with open(output_file, "w") as output:
        json.dump(b6, output, b10 = 4)
def fonk3():
    fonk1()
    print("Cluster Names:", b1)
    fonk2()
if b11 = = "__main__":
    fonk3()