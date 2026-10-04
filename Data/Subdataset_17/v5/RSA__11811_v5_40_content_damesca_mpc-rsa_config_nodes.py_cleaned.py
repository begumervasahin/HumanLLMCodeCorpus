import subprocess
import json
def get_docker_container_ip(container_base_name="rsa-docker_node_", network_name="rsa-net", max_containers=20):
    ips = []
    for i in range(1, max_containers + 1):
        container_name = f"{container_base_name}{i}"
        try:
            output = subprocess.check_output(f"docker container inspect {container_name}", shell=True)
            container_info = json.loads(output)[0]
            ip_address = container_info["NetworkSettings"]["Networks"][network_name]["IPAddress"]
            ips.append(ip_address)
        except subprocess.CalledProcessError:
            break
    return ips
def write_ips_to_file(file_path, ips, prefix=""):
    with open(file_path, "w") as file:
        for ip in ips:
            file.write(f"{prefix}{ip}\n")
def build_docker_image(dockerfile_path, image_tag):
    try:
        print("\nBuilding Docker image...\n")
        build_output = subprocess.check_output(f"docker build -t {image_tag} {dockerfile_path}", shell=True)
        print("[Build] Output:\n", build_output.decode())
    except subprocess.CalledProcessError as e:
        print("Error during build:", e)
def run_docker_container(image_tag, network_name):
    try:
        print("\nRunning Docker container...\n")
        run_output = subprocess.check_output(f"docker run -it --network {network_name} {image_tag}", shell=True)
        print("[Run] Output:\n", run_output.decode())
        print("\nFinished running container\n")
    except subprocess.CalledProcessError as e:
        print("Error during run:", e)
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
build_docker_image("./test", "test")
run_docker_container("test", "rsa-net")