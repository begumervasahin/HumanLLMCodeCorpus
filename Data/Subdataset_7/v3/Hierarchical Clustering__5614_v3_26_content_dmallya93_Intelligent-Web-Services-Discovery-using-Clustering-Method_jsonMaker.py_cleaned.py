import os
import time
b1 = {}
def fonk1():
    global b1
    with open("ClusterNames.csv", "r") as file:
        for line in file:
            cluster_id, b2 = line.strip().split(",")
            b1[cluster_id] = b2
def fonk2():
    with open("Hierarchies.csv", "r") as file:
        b3 = "{\n\"name\": \"Entire Dataset\",\n\"children\": [\n"
        for line in file:
            cluster_id, b4 = line.strip().split(",")
            b5 = b4.split()[:-1]
            b3 += "{\n\"name\": \"" + cluster_id + "\",\n"
            b3 += "\"children\": [\n"
            for cluster in b5:
                b3 += "{\"name\": \"" + b1[cluster] + "\", \"size\": 3000 },\n"
            b3 = b3[:-2] + "\n]\n},\n"
        b3 = b3[:-2] + "\n]\n}\n"
    with open("newjson.json", "w") as file:
        file.write(b3)
fonk1()
fonk2()