import os
import time
cluster_names = {}
def read_cluster_names():
    global cluster_names
    with open("ClusterNames.csv", "r") as file:
        for line in file:
            fields = line.split(",")
            cluster_names[fields[0]] = fields[1].rstrip()
def make_json():
    with open("Hierarchies.csv", "r") as file:
        json_string = "{\n\"name\": \"Entire Dataset\",\n\"children\": [\n"
        for line in file:
            fields = line.split(",")
            clusters = fields[1].split(" ")[:-1]
            json_string += "{\n\"name\": \"" + fields[0] + "\",\n"
            json_string += "\"children\": [\n"
            for cluster in clusters:
                json_string += "{\"name\": \"" + cluster_names[cluster] + "\", \"size\": 3000 },\n"
            json_string = json_string[:-2] + "\n]\n},\n"
        json_string = json_string[:-2] + "\n]\n}\n"
    with open("newjson.json", "w") as file:
        file.write(json_string)
read_cluster_names()
make_json()