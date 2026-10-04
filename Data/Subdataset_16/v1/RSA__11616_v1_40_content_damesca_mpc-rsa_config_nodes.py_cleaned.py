import subprocess
import json
import os
def fonk1(b1 = "rsa-docker_node_", net_name="rsa-net", max_iter=20):
    '''Iterate over one or more containers in a range and stop at the first non-existent container'''
    b2 = list()
    for i in range(1, max_iter):
        b3 = ["docker", "container", "inspect", b1 + str(i)]
        try:
            b4 = subprocess.check_output(b3, stderr=subprocess.STDOUT).decode('utf-8')
            b5 = json.loads(b4)[0]
            b2.append(b5["NetworkSettings"]["Networks"][net_name]["IPAddress"])
        except (subprocess.CalledProcessError, IndexError, json.JSONDecodeError):
            break
    return b2
b6 = fonk1()
b7 = fonk1("rsa-docker_ca_", "rsa-net", 2)
b8 = fonk1("rsa-docker_orchestrator_", "rsa-net", 2)
print("Node IP: " + str(b6))
print("CA IP: " + str(b7))
print("Orchestrator IP: " + str(b8))
with open("./test/b2.txt", "w") as test_file:
    for ip in b6:
        test_file.write(str(ip) + "\n")
    for ip in b7:
        test_file.write("ca: " + str(ip) + "\n")
    for ip in b8:
        test_file.write("or: " + str(ip) + "\n")
with open("./client/orqIp.txt", "w") as client_file:
    for ip in b8:
        client_file.write(str(ip))
b3 = ["docker", "build", "-t", "test", "./test"]
try:
    print("\nBuilding test...\n")
    b4 = subprocess.check_output(b3, stderr=subprocess.STDOUT).decode('utf-8')
    print("[Test] - Building b4: ")
    print(b4)
except subprocess.CalledProcessError as e:
    print("Error during build: ")
    print(e.b4.decode('utf-8'))
b3 = ["docker", "run", "-it", "--network", "rsa-net", "test"]
try:
    print("\nRunning test...\n")
    b4 = subprocess.check_output(b3, stderr=subprocess.STDOUT).decode('utf-8')
    print("[Test] - Running b4: ")
    print(b4)
    print("\nFinished test\n")
except subprocess.CalledProcessError as e:
    print("Error during run: ")
    print(e.b4.decode('utf-8'))