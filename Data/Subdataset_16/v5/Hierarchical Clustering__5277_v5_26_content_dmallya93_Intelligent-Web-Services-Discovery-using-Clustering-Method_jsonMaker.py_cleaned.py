import os
import json
def fonk1(b1 = "ClusterNames.csv"):
    b2 = {}
    with open(b1, "r") as file:
        for line in file:
            b3 = line.strip().split(",")
            if len(b3) == 2:
                cluster_id, b4 = b3
                b2[cluster_id] = b4
    return b2
def fonk2(input_file, b2):
    b5 = {
        "name": "Entire Dataset",
        "b8": []
    }
    with open(input_file, "r") as file:
        for line in file:
            b3 = line.strip().split(",")
            if len(b3) == 2:
                parent_name, b6 = b3
                b7 = b6.split()
                b8 = [
                    {"name": b2.get(cluster_id, cluster_id), "size": 3000}
                    for cluster_id in b7
                ]
                b5["b8"].append({
                    "name": parent_name,
                    "b8": b8
                })
    return b5
def fonk3(data, b9 = "newjson.json"):
    with open(b9, "w") as file:
        json.dump(data, file, b10 = 4)
def fonk4():
    b2 = fonk1()
    print("Cluster Names:", b2)
    b5 = fonk2("Hierarchies.csv", b2)
    fonk3(b5)
if b11 = = "__main__":
    fonk4()