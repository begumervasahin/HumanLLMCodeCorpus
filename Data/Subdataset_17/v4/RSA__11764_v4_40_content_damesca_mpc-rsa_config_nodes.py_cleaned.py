import subprocess
import json
import requests
from requests.exceptions import ConnectionError
def get_docker_container_ip(cont_name="rsa-docker_node_", net_name="rsa-net", max_iter=20):
    ips = []
    for i in range(1, max_iter):
        try:
            output = subprocess.check_output(f"docker container inspect {cont_name}{i}")
            container_info = json.loads(output)[0]
            ip_address = container_info["NetworkSettings"]["Networks"][net_name]["IPAddress"]
            ips.append(ip_address)
        except subprocess.CalledProcessError:
            break
    return ips
node_ip = get_docker_container_ip()
ca_ip = get_docker_container_ip("rsa-docker_ca_", "rsa-net", 2)
orchestrator_ip = get_docker_container_ip("rsa-docker_orchestrator_", "rsa-net", 2)
print("Node IPs:", node_ip)
print("CA IPs:", ca_ip)
print("Orchestrator IPs:", orchestrator_ip)
with open("./test/ips.txt", "w") as test_file:
    for ip in node_ip:
        test_file.write(f"{ip}\n")
    for ip in ca_ip:
        test_file.write(f"ca: {ip}\n")
    for ip in orchestrator_ip:
        test_file.write(f"or: {ip}\n")
with open("./client/orqIp.txt", "w") as client_file:
    for ip in orchestrator_ip:
        client_file.write(ip)
try:
    print("\nBuilding test Docker image...\n")
    build_output = subprocess.check_output("docker build -t test ./test", shell=True)
    print("[Test] - Build output:\n", build_output.decode())
except subprocess.CalledProcessError as e:
    print("Error during build:", e)
try:
    print("\nRunning test Docker container...\n")
    run_output = subprocess.check_output("docker run -it --network rsa-net test", shell=True)
    print("[Test] - Run output:\n", run_output.decode())
    print("\nFinished test\n")
except subprocess.CalledProcessError as e:
    print("Error during run:", e)