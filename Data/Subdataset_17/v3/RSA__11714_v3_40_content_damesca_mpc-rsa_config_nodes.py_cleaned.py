import subprocess
import json
def get_docker_container_ip(container_prefix="rsa-docker_node_", network_name="rsa-net", max_iterations=20):
    ips = []
    for i in range(1, max_iterations):
        container_name = f"{container_prefix}{i}"
        try:
            output = subprocess.check_output(
                ["docker", "container", "inspect", container_name],
                stderr=subprocess.STDOUT
            ).decode('utf-8')
            container_info = json.loads(output)[0]
            ip_address = container_info["NetworkSettings"]["Networks"][network_name]["IPAddress"]
            ips.append(ip_address)
        except (subprocess.CalledProcessError, IndexError, json.JSONDecodeError):
            break
    return ips
def write_ips_to_file(filename, ips, prefix=""):
    with open(filename, "w") as file:
        for ip in ips:
            file.write(f"{prefix}{ip}\n")
def build_docker_image(tag, context_dir):
    build_command = ["docker", "build", "-t", tag, context_dir]
    try:
        print(f"\nBuilding Docker image '{tag}'...\n")
        build_output = subprocess.check_output(build_command, stderr=subprocess.STDOUT).decode('utf-8')
        print("[Build Output]:")
        print(build_output)
    except subprocess.CalledProcessError as e:
        print("Error during Docker build:")
        print(e.output.decode('utf-8'))
def run_docker_container(image, network):
    run_command = ["docker", "run", "-it", "--network", network, image]
    try:
        print(f"\nRunning Docker container '{image}'...\n")
        run_output = subprocess.check_output(run_command, stderr=subprocess.STDOUT).decode('utf-8')
        print("[Run Output]:")
        print(run_output)
        print("\nFinished test run\n")
    except subprocess.CalledProcessError as e:
        print("Error during Docker run:")
        print(e.output.decode('utf-8'))
node_ips = get_docker_container_ip()
ca_ips = get_docker_container_ip("rsa-docker_ca_", "rsa-net", 2)
orchestrator_ips = get_docker_container_ip("rsa-docker_orchestrator_", "rsa-net", 2)
print("Node IPs:", node_ips)
print("CA IPs:", ca_ips)
print("Orchestrator IPs:", orchestrator_ips)
write_ips_to_file("./test/ips.txt", node_ips)
write_ips_to_file("./test/ips.txt", ca_ips, prefix="ca: ")
write_ips_to_file("./test/ips.txt", orchestrator_ips, prefix="or: ")
write_ips_to_file("./client/orqIp.txt", orchestrator_ips)
build_docker_image("test", "./test")
run_docker_container("test", "rsa-net")