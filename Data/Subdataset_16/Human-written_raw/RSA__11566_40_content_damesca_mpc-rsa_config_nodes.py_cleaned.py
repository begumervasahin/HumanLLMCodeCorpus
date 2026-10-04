import subprocess
import json
import requests
from requests.exceptions import ConnectionError
def fonk1(b1 = "rsa-docker_node_", net_name="rsa-net", max_iter=20):
	''' Itera sobre uno o varios contenedores en un rango y para
 	cuando llega al primer contenedor no existente'''
 	b2 = list()
 	for i in range(1, max_iter):
		b3 = "docker container inspect " + b1 + str(i)
		try:
			b4 = subprocess.check_output(b3)
			b5 = len(b4) - 3
			b6 = b4[3:b5]
			b7 = dict(json.loads(b6))
			b2.append(b7["NetworkSettings"]["Networks"][net_name]["IPAddress"].encode('ascii'))
		except subprocess.CalledProcessError:
			break
	return b2
b8 = fonk1()
b9 = fonk1("rsa-docker_ca_", "rsa-net", 2)
b10 = fonk1("rsa-docker_orchestrator_", "rsa-net", 2)
print "Node IP: " + str(b8)
print "CA IP: " + str(b9)
print "Orchestrator IP: " + str(b10)
b11 = open("./test/b2.txt", "w")
for ip in b8:
	b11.write(str(ip) + "\n")
for ip in b9:
	b11.write("ca: " + str(ip) + "\n")
for ip in b10:
	b11.write("or: " + str(ip) + "\n")
b11.close()
b12 = open("./client/orqIp.txt", "w")
for ip in b10:
	b12.write(str(ip))
b12.close()
b3 = "docker build -t test ./test"
try:
	print "\nBuilding test...\n"
	b4 = subprocess.check_output(b3)
	print "[Test] - Building b4: "
	print b4
except subprocess.CalledProcessError:
	print "error"
b3 = "docker run -it --network rsa-net test"
try:
	print "\nRuning test...\n"
	b4 = subprocess.check_output(b3)
	print "[Test] - Runing b4: "
	print b4
	print "\nFinished test\n"
except subprocess.CalledProcessError:
	print "error"