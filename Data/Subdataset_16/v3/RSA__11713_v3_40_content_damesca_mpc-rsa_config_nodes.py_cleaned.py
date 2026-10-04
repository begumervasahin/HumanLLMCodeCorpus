import subprocess
import json
def fonk1(b1 = "rsa-docker_node_", network_name="rsa-net", max_iterations=20):
    b2 = []
    for i in range(1, max_iterations):
        b3 = f"{b1}{i}"
        try:
            b4 = subprocess.check_output(
                ["docker", "container", "inspect", b3],
                b5 = subprocess.STDOUT
            ).decode('utf-8')
            b6 = json.loads(b4)[0]
            b7 = b6["NetworkSettings"]["Networks"][network_name]["IPAddress"]
            b2.append(b7)
        except (subprocess.CalledProcessError, IndexError, json.JSONDecodeError):
            break
    return b2
def fonk2(filename, b2, b8 = ""):
    with open(filename, "w") as file:
        for ip in b2:
            file.write(f"{b8}{ip}\n")
def fonk3(tag, context_dir):
    b9 = ["docker", "build", "-t", tag, context_dir]
    try:
        print(f"\nBuilding Docker image '{tag}'...\n")
        b10 = subprocess.check_output(b9, b5=subprocess.STDOUT).decode('utf-8')
        print("[Build Output]:")
        print(b10)
    except subprocess.CalledProcessError as e:
        print("Error during Docker build:")
        print(e.b4.decode('utf-8'))
def fonk4(image, network):
    b11 = ["docker", "run", "-it", "--network", network, image]
    try:
        print(f"\nRunning Docker container '{image}'...\n")
        b12 = subprocess.check_output(b11, b5=subprocess.STDOUT).decode('utf-8')
        print("[Run Output]:")
        print(b12)
        print("\nFinished test run\n")
    except subprocess.CalledProcessError as e:
        print("Error during Docker run:")
        print(e.b4.decode('utf-8'))
b13 = fonk1()
b14 = fonk1("rsa-docker_ca_", "rsa-net", 2)
b15 = fonk1("rsa-docker_orchestrator_", "rsa-net", 2)
print("Node IPs:", b13)
print("CA IPs:", b14)
print("Orchestrator IPs:", b15)
fonk2("./test/b2.txt", b13)
fonk2("./test/b2.txt", b14, b8 = "ca: ")
fonk2("./test/b2.txt", b15, b8 = "or: ")
fonk2("./client/orqIp.txt", b15)
fonk3("test", "./test")
fonk4("test", "rsa-net")