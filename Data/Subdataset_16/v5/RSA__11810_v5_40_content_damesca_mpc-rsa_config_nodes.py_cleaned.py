import subprocess
import json
def fonk1(b1 = "rsa-docker_node_", network_name="rsa-net", max_containers=20):
    b2 = []
    for i in range(1, max_containers + 1):
        b3 = f"{b1}{i}"
        try:
            b4 = subprocess.check_output(f"docker container inspect {b3}", shell=True)
            b5 = json.loads(b4)[0]
            b6 = b5["NetworkSettings"]["Networks"][network_name]["IPAddress"]
            b2.append(b6)
        except subprocess.CalledProcessError:
            break
    return b2
def fonk2(file_path, b2, b7 = ""):
    with open(file_path, "w") as file:
        for ip in b2:
            file.write(f"{b7}{ip}\n")
def fonk3(dockerfile_path, image_tag):
    try:
        print("\nBuilding Docker image...\n")
        b8 = subprocess.check_output(f"docker build -t {image_tag} {dockerfile_path}", shell=True)
        print("[Build] Output:\n", b8.decode())
    except subprocess.CalledProcessError as e:
        print("Error during build:", e)
def fonk4(image_tag, network_name):
    try:
        print("\nRunning Docker container...\n")
        b9 = subprocess.check_output(f"docker run -it --network {network_name} {image_tag}", shell=True)
        print("[Run] Output:\n", b9.decode())
        print("\nFinished running container\n")
    except subprocess.CalledProcessError as e:
        print("Error during run:", e)
b10 = fonk1()
b11 = fonk1("rsa-docker_ca_", "rsa-net", 2)
b12 = fonk1("rsa-docker_orchestrator_", "rsa-net", 2)
print("Node IPs:", b10)
print("CA IPs:", b11)
print("Orchestrator IPs:", b12)
fonk2("./test/b2.txt", b10)
fonk2("./test/b2.txt", b11, b7 = "ca: ")
fonk2("./test/b2.txt", b12, b7 = "or: ")
fonk2("./client/orqIp.txt", b12)
fonk3("./test", "test")
fonk4("test", "rsa-net")