import os
import json
cluster_names = {}
def read_cluster_names(filename="ClusterNames.csv"):
    global cluster_names
    with open(filename, "r") as file:
        for line in file:
            fields = line.strip().split(",")
            if len(fields) == 2:
                cluster_id, cluster_name = fields
                cluster_names[cluster_id] = cluster_name
def generate_json(input_file="Hierarchies.csv", output_file="newjson.json"):
    json_data = {
        "name": "Entire Dataset",
        "children": []
    }
    with open(input_file, "r") as file:
        for line in file:
            fields = line.strip().split(",")
            if len(fields) == 2:
                parent_name, clusters_str = fields
                cluster_ids = clusters_str.split()
                children = [
                    {"name": cluster_names.get(cluster, cluster), "size": 3000}
                    for cluster in cluster_ids
                ]
                json_data["children"].append({
                    "name": parent_name,
                    "children": children
                })
    with open(output_file, "w") as output:
        json.dump(json_data, output, indent=4)
def main():
    read_cluster_names()
    print("Cluster Names:", cluster_names)
    generate_json()
if __name__ == "__main__":
    main()