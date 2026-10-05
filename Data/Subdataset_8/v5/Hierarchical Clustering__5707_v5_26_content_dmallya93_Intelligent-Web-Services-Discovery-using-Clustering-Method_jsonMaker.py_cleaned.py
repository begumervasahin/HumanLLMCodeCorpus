import os
import time
cluster_names = {}
def read_cluster_names():
    global cluster_names
    with open("ClusterNames.csv", "r") as file:
        for line in file:
            cluster_id, cluster_name = line.strip().split(",")
            cluster_names[cluster_id] = cluster_name
def make_json():
    with open("Hierarchies.csv", "r") as file:
        json_string = "{\n\"name\": \"Entire Dataset\",\n\"children\": [\n"
        for line in file:
            cluster_id, cluster_data = line.strip().split(",", 1)
            clusters = cluster_data.split()[:-1]
            json_string += "{\n\"name\": \"" + cluster_id + "\",\n"
            json_string += "\"children\": [\n"
            for cluster in clusters:
                json_string += "{\"name\": \"" + cluster_names[cluster] + "\", \"size\": 3000 },\n"
            json_string = json_string[:-2] + "\n]\n},\n"
        json_string = json_string[:-2] + "\n]\n}\n"
    with open("newjson.json", "w") as file:
        file.write(json_string)
read_cluster_names()
make_json()