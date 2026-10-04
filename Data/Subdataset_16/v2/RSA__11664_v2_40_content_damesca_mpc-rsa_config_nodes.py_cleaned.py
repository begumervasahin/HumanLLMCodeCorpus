import subprocess
import json
import os
def fonk1(b1 = "rsa-docker_node_", net_name="rsa-net", max_iter=20):
    b2 = []
    for i in range(1, max_iter):
        b3 = f"{b1}{i}"
        try:
            b4 = subprocess.check_output(
                ["docker", "container", "inspect", b3],
                b5 = subprocess.STDOUT
            ).decode('utf-8')
            b6 = json.loads(b4)[0]
            b7 = b6["NetworkSettings"]["Networks"][net_name]["IPAddress"]
            b2.append(b7)
        except (subprocess.CalledProcessError, IndexError, json.JSONDecodeError):
            break
    return b2
b8 = fonk1()
b9 = fonk1("rsa-docker_ca_", "rsa-net", 2)
b10 = fonk1("rsa-docker_orchestrator_", "rsa-net", 2)
print("Node IPs:", b8)
print("CA IPs:", b9)
print("Orchestrator IPs:", b10)
with open("./test/b2.txt", "w") as test_file:
    for ip in b8:
        test_file.write(f"{ip}\n")
    for ip in b9:
        test_file.write(f"ca: {ip}\n")
    for ip in b10:
        test_file.write(f"or: {ip}\n")
with open("./client/orqIp.txt", "w") as client_file:
    for ip in b10:
        client_file.write(ip)
b11 = ["docker", "build", "-t", "test", "./test"]
try:
    print("\nBuilding Docker image 'test'...\n")
    b12 = subprocess.check_output(b11, b5=subprocess.STDOUT).decode('utf-8')
    print("[Test] - Build b4:")
    print(b12)
except subprocess.CalledProcessError as e:
    print("Error during Docker build:")
    print(e.b4.decode('utf-8'))
b13 = ["docker", "run", "-it", "--network", "rsa-net", "test"]
try:
    print("\nRunning Docker container 'test'...\n")
    b14 = subprocess.check_output(b13, b5=subprocess.STDOUT).decode('utf-8')
    print("[Test] - Run b4:")
    print(b14)
    print("\nFinished test run\n")
except subprocess.CalledProcessError as e:
    print("Error during Docker run:")
    print(e.b4.decode('utf-8'))