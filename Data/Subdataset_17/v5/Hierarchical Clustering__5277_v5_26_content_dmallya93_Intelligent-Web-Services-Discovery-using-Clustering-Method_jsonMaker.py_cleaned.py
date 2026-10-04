import os
import json
def load_cluster_names(filename="ClusterNames.csv"):
    cluster_names = {}
    with open(filename, "r") as file:
        for line in file:
            fields = line.strip().split(",")
            if len(fields) == 2:
                cluster_id, cluster_name = fields
                cluster_names[cluster_id] = cluster_name
    return cluster_names
def build_json_structure(input_file, cluster_names):
    json_structure = {
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
                    {"name": cluster_names.get(cluster_id, cluster_id), "size": 3000}
                    for cluster_id in cluster_ids
                ]
                json_structure["children"].append({
                    "name": parent_name,
                    "children": children
                })
    return json_structure
def save_json(data, output_file="newjson.json"):
    with open(output_file, "w") as file:
        json.dump(data, file, indent=4)
def main():
    cluster_names = load_cluster_names()
    print("Cluster Names:", cluster_names)
    json_structure = build_json_structure("Hierarchies.csv", cluster_names)
    save_json(json_structure)
if __name__ == "__main__":
    main()