from time import sleep
import os
def clear():
	os.system("cls" if os.name=="nt" else "clear")
content = input("What is the content? e.g: He, N or D: ").lower().replace(" ", "")
clear()
if(content == "he"):
	clear()
	nozzle = input("How many nozzles?: ")
	if(nozzle == "2"):
		clear()
		print("Engine
		sleep(3)
	elif(nozzle == "3"):
		clear()
		print("Engine
		sleep(3)
	else:
		clear()
		print("I can't understand that")
		sleep(3)
elif(content == "n"):
	clear()
	nozzle = input("How many nozzles?: ")
	if(nozzle == "1"):
		clear()
		print("Engine
		sleep(3)
	elif(nozzle == "2"):
		clear()
		print("Engine
		sleep(3)
	elif(nozzle == "3"):
		clear()
		print("Now it's time for the pressure:")
		print("")
		pressure = input("Type 1 for <, or 2 for >")
		if(pressure == "1"):
			clear()
			print("Engine
			sleep(3)
		elif(pressure == "2"):
			clear()
			print("Engine
			sleep(3)
		else:
			clear()
			print("I can't understand that")
			sleep(3)
	else:
		clear()
		print("I can't understand that")
		sleep(3)
elif(content == "d"):
	clear()
	nozzle = input("How many nozzles?: ")
	if(nozzle == "1"):
		clear()
		print("Engine
		sleep(3)
	elif(nozzle == "2"):
		clear()
		print("Engine
		sleep(3)
	elif(nozzle == "3"):
		clear()
		print("Now it's time for the pressure")
		print("")
		pressure = input("Type 1 for <, or 2 for >")
		if(pressure == "1"):
			clear()
			print("Engine
			sleep(3)
		elif(pressure == "2"):
			clear()
			print("Engine
			sleep(3)
		else:
			clear()
			print("I can't understand that")
			sleep(3)
	else:
		clear()
		print("I can't understand that")
		sleep(3)
else:
	clear()
	print("Something went wrong! Try again")
	sleep(3)
