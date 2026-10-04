import subprocess
import json
import requests
from requests.exceptions import ConnectionError
def fonk1(b1 = "rsa-docker_node_", net_name="rsa-net", max_iter=20):
    b2 = []
    for i in range(1, max_iter):
        try:
            b3 = subprocess.check_output(f"docker container inspect {b1}{i}")
            b4 = json.loads(b3)[0]
            b5 = b4["NetworkSettings"]["Networks"][net_name]["IPAddress"]
            b2.append(b5)
        except subprocess.CalledProcessError:
            break
    return b2
b6 = fonk1()
b7 = fonk1("rsa-docker_ca_", "rsa-net", 2)
b8 = fonk1("rsa-docker_orchestrator_", "rsa-net", 2)
print("Node IPs:", b6)
print("CA IPs:", b7)
print("Orchestrator IPs:", b8)
with open("./test/b2.txt", "w") as test_file:
    for ip in b6:
        test_file.write(f"{ip}\n")
    for ip in b7:
        test_file.write(f"ca: {ip}\n")
    for ip in b8:
        test_file.write(f"or: {ip}\n")
with open("./client/orqIp.txt", "w") as client_file:
    for ip in b8:
        client_file.write(ip)
try:
    print("\nBuilding test Docker image...\n")
    b9 = subprocess.check_output("docker build -t test ./test", shell=True)
    print("[Test] - Build b3:\n", b9.decode())
except subprocess.CalledProcessError as e:
    print("Error during build:", e)
try:
    print("\nRunning test Docker container...\n")
    b10 = subprocess.check_output("docker run -it --network rsa-net test", shell=True)
    print("[Test] - Run b3:\n", b10.decode())
    print("\nFinished test\n")
except subprocess.CalledProcessError as e:
    print("Error during run:", e)