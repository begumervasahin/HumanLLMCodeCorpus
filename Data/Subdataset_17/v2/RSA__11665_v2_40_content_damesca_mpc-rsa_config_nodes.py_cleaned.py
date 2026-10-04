import subprocess
import json
import os
def get_docker_container_ip(cont_name="rsa-docker_node_", net_name="rsa-net", max_iter=20):
    ips = []
    for i in range(1, max_iter):
        container_name = f"{cont_name}{i}"
        try:
            output = subprocess.check_output(
                ["docker", "container", "inspect", container_name],
                stderr=subprocess.STDOUT
            ).decode('utf-8')
            container_info = json.loads(output)[0]
            ip_address = container_info["NetworkSettings"]["Networks"][net_name]["IPAddress"]
            ips.append(ip_address)
        except (subprocess.CalledProcessError, IndexError, json.JSONDecodeError):
            break
    return ips
node_ips = get_docker_container_ip()
ca_ips = get_docker_container_ip("rsa-docker_ca_", "rsa-net", 2)
orchestrator_ips = get_docker_container_ip("rsa-docker_orchestrator_", "rsa-net", 2)
print("Node IPs:", node_ips)
print("CA IPs:", ca_ips)
print("Orchestrator IPs:", orchestrator_ips)
with open("./test/ips.txt", "w") as test_file:
    for ip in node_ips:
        test_file.write(f"{ip}\n")
    for ip in ca_ips:
        test_file.write(f"ca: {ip}\n")
    for ip in orchestrator_ips:
        test_file.write(f"or: {ip}\n")
with open("./client/orqIp.txt", "w") as client_file:
    for ip in orchestrator_ips:
        client_file.write(ip)
build_command = ["docker", "build", "-t", "test", "./test"]
try:
    print("\nBuilding Docker image 'test'...\n")
    build_output = subprocess.check_output(build_command, stderr=subprocess.STDOUT).decode('utf-8')
    print("[Test] - Build output:")
    print(build_output)
except subprocess.CalledProcessError as e:
    print("Error during Docker build:")
    print(e.output.decode('utf-8'))
run_command = ["docker", "run", "-it", "--network", "rsa-net", "test"]
try:
    print("\nRunning Docker container 'test'...\n")
    run_output = subprocess.check_output(run_command, stderr=subprocess.STDOUT).decode('utf-8')
    print("[Test] - Run output:")
    print(run_output)
    print("\nFinished test run\n")
except subprocess.CalledProcessError as e:
    print("Error during Docker run:")
    print(e.output.decode('utf-8'))