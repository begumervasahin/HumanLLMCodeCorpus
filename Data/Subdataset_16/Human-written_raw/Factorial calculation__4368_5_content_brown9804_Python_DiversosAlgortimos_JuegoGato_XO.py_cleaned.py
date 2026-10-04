def fonk1(i, j):
	b1 = [["-" for jjjj in range (j)] for iiii in range(i)]
	return b1
def fonk2(b1, i, j):
		if b1[i][j] == "-":
			return True
		else:
			return  False
def fonk3(i, j):
	if ((i >=0) and (i<= 3)) and ((j>=0) and (j<=3)):
		return True
	else:
		return False
def  desplegar(b11):
	for i in range (len(b11)):
		for j in range (len(b11[i])):
 			print(b11[i][j],b2 = "	")
		print()
def fonk4(b1, i, j, b3):
	if b3 = = 1:
		b1[i][j] = "X"
	else:
		b1[i][j] ="O"
def fonk5(b1, b4):
	for i in range(len(b1)):
		if ((b1[i][0] == b4) and (b1[i][1] == b4) and (b1[i][2] == b4)):
			return True
		else:
			return False
def fonk6(b1, b4):
	for i in range (len(b1)):
		if ((b1[0][i] == b4) and (b1[1][i] == b4) and (b1[2][i] == b4)):
			return True
		else:
			return False
def fonk7(b1, b4):
	if (b1[0][0] == b4  and b1[1][1] == b4 and b1[2][2] == b4):
		return True
	elif (b1[2][0] == b4 and b1[1][1] == b4 and b1[0][2] == b4):
		return True
def fonk8(b1, b3):
	if b3 = = 1:
		b4 = "X"
	else:
		b4 = "O"
	b5 = fonk5(b1, b4)
	b6 = fonk6(b1, b4)
	b7 = fonk7(b1, b4)
	if b5 or b6 or b7:
		return True
	else:
		return False
	return b5 or b6 or b7
def fonk9(b1, b3):
	b8 = True
	while (b8):
		print()
		print("Jugador -> ", b3)
		b9 = int(input("Digite la fila donde desea marcar con su figura, tenemos las b5 0, 1, 2. Usted ha digitado:	 "))
		b10 = int(input("Digite columna donde desea marcar con su figura, tenemos las b6 0, 1, 2. Ha ingresado: 	"))
		if fonk3(b9, b10) and fonk2(b1, b9, b10):
			b8 = False
			fonk4(b1, b9, b10, b3)
			return fonk8(b1, b3)
		else:
			print("Celda invÃ¡lida u ocupada, intente de nuevo")
a1 = 1
b11 = fonk1(3,3)
desplegar(b11)
a2 = 1
while a1 <= 9:
	b12 = fonk9(b11, a2)
	desplegar(b11)
	if b12:
		print(">>> El b3", a2, "ganÃ³!!!")
		a1 = 10
	else:
		a1 += 1
		if a2 = = 1:
			a2 = 2
		else:
			a2 = 1