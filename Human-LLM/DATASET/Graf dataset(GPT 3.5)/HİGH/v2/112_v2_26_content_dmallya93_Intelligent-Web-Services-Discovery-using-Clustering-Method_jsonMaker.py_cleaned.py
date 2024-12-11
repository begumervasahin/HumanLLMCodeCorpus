import os
import time
b1 = {}
def fonk1():
    global b1
    with open("ClusterNames.csv", "r") as file:
        for line in file:
            b2 = line.split(",")
            b1[b2[0]] = b2[1].strip()
def fonk2():
    with open("Hierarchies.csv", "r") as file:
        b3 = "{\n\"name\": \"Entire Dataset\",\n\"children\": [\n"
        for line in file:
            b2 = line.split(",")
            b4 = b2[1].split(" ")[:-1]
            b3 += "{\n\"name\": \"" + b2[0] + "\",\n"
            b3 += "\"children\": [\n"
            for cluster in b4:
                b3 += "{\"name\": \"" + b1[cluster] + "\", \"size\": 3000 },\n"
            b3 = b3[:-2] + "\n]\n},\n"
        b3 = b3[:-2] + "\n]\n}\n"
    with open("newjson.json", "w") as file:
        file.write(b3)
fonk1()
fonk2()