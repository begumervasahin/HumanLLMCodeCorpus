import os
b1 = {}
def fonk1(b2 = "ClusterNames.csv"):
    global b1
    with open(b2, "r") as file:
        for line in file:
            b3 = line.strip().split(",")
            b1[b3[0]] = b3[1]
def fonk2(b4 = "Hierarchies.csv", output_file="newjson.json"):
    with open(b4, "r") as file:
        b5 = "{\n\"name\": \"Entire Dataset\",\n\"children\": [\n"
        for line in file:
            b3 = line.strip().split(",")
            b6 = b3[1].split()
            b5 += "{\n\"name\": \"" + b3[0] + "\",\n"
            b5 += "\"children\": [\n"
            for i, cluster in enumerate(b6):
                if cluster in b1:
                    b7 = b1[cluster]
                    b5 += f"{{\"name\": \"{b7}\", \"size\": 3000}}"
                    if i != len(b6) - 1:
                        b5 += ",\n"
            b5 += "\n]\n},\n"
        b5 = b5.rstrip(",\n") + "\n]\n}\n"
        with open(output_file, "w") as output:
            output.write(b5)
if b8 = = "__main__":
    fonk1()
    print(b1)
    fonk2()