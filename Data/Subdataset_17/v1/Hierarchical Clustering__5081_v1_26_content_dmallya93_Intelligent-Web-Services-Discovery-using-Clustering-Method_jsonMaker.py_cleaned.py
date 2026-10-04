import os
cluster_names = {}
def read_cluster_names(filename="ClusterNames.csv"):
    global cluster_names
    with open(filename, "r") as file:
        for line in file:
            fields = line.strip().split(",")
            cluster_names[fields[0]] = fields[1]
def make_json(input_file="Hierarchies.csv", output_file="newjson.json"):
    with open(input_file, "r") as file:
        json_string = "{\n\"name\": \"Entire Dataset\",\n\"children\": [\n"
        for line in file:
            fields = line.strip().split(",")
            clusters = fields[1].split()
            json_string += "{\n\"name\": \"" + fields[0] + "\",\n"
            json_string += "\"children\": [\n"
            for i, cluster in enumerate(clusters):
                if cluster in cluster_names:
                    cluster_name = cluster_names[cluster]
                    json_string += f"{{\"name\": \"{cluster_name}\", \"size\": 3000}}"
                    if i != len(clusters) - 1:
                        json_string += ",\n"
            json_string += "\n]\n},\n"
        json_string = json_string.rstrip(",\n") + "\n]\n}\n"
        with open(output_file, "w") as output:
            output.write(json_string)
if __name__ == "__main__":
    read_cluster_names()
    print(cluster_names)
    make_json()